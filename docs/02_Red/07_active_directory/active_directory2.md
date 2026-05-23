---
title: Active Directory2
parent: Red Team
---
<details markdown="1">
<summary># Initial Access</summary>

<details markdown="1">
<summary>RDP</summary>

```bash
xfreerdp3 /u:user /p:pass /v:target
```

Check:
- Local admin?
- Domain joined?
- Saved credentials?

</details>

---

<details markdown="1">
<summary>WinRM</summary>

```bash
evil-winrm -i target -u user -p pass
```

Check:
- Admin rights
- PowerShell history
- AV/EDR

</details>

---

<details markdown="1">
<summary>SMB</summary>

```bash
crackmapexec smb targets.txt -u user -p pass
```

Check:
- Local admin reuse
- Shares
- Writable directories

</details>

---

<details markdown="1">
<summary>MSSQL</summary>

```bash
impacket-mssqlclient domain/user:pass@target
```

Check:
- sysadmin role
- xp_cmdshell
- linked servers

</details>

---

<details markdown="1">
<summary>SSH</summary>

```bash
ssh user@target
```

Check:
- sudo
- history
- keys

</details>

</details>

---

<details markdown="1">
<summary># Local Enumeration</summary>

<details markdown="1">
<summary>Identity</summary>

```powershell
whoami
whoami /priv
whoami /groups
hostname
```

Check:
- SeImpersonatePrivilege
- Backup Operators
- Server Operators
- Remote Management Users

</details>

---

<details markdown="1">
<summary>System Info</summary>

```powershell
systeminfo
Get-ComputerInfo
```

Check:
- OS version
- Missing patches
- AV/EDR

</details>

---

<details markdown="1">
<summary>Users</summary>

```powershell
net user
net localgroup administrators
```

Check:
- Service accounts
- Interesting descriptions
- Disabled accounts

</details>

---

<details markdown="1">
<summary>Network</summary>

```powershell
ipconfig /all
route print
arp -a
netstat -ano
```

Check:
- Internal subnets
- DC location
- Management hosts

</details>

---

<details markdown="1">
<summary>Shares</summary>

```powershell
net share
```

Check:
- Writable shares
- Scripts
- Backups

</details>

---

<details markdown="1">
<summary>Scheduled Tasks</summary>

```powershell
schtasks /query /fo LIST /v
```

Check:
- Stored credentials
- Writable scripts

</details>

---

<details markdown="1">
<summary>Services</summary>

```powershell
Get-Service
```

Check:
- Unquoted paths
- Weak permissions
- Writable binaries

</details>

---

<details markdown="1">
<summary>Filesystem</summary>

Check:
- C:\automation
- C:\backup
- unattended.xml
- scripts
- config files
- KeePass
- SSH keys

</details>

---

<details markdown="1">
<summary>Environment Variables</summary>

```powershell
set
Get-ChildItem env:
```

Check:
- Passwords
- Tokens
- API keys

</details>

---

<details markdown="1">
<summary>PowerShell History</summary>

```powershell
Get-History
type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

Check:
- Password reuse
- Admin commands

</details>

</details>

---

<details markdown="1">
<summary># Local Privilege Escalation</summary>

<details markdown="1">
<summary>SeImpersonatePrivilege → Potato Attacks</summary>

Check:

```powershell
whoami /priv
```

Abuse:
- PrintSpoofer
- GodPotato
- RoguePotato

</details>

---

<details markdown="1">
<summary>AlwaysInstallElevated</summary>

```powershell
reg query HKCU\Software\Policies\Microsoft\Windows\Installer
reg query HKLM\Software\Policies\Microsoft\Windows\Installer
```

</details>

---

<details markdown="1">
<summary>Service Misconfiguration</summary>

Check:
- Writable service binary
- Weak service permissions
- Unquoted path

</details>

---

<details markdown="1">
<summary>Scheduled Task Abuse</summary>

Check:
- Writable task
- Writable script

</details>

---

<details markdown="1">
<summary>DLL Hijacking</summary>

Check:
- Writable directories
- Missing DLLs

</details>

---

<details markdown="1">
<summary>UAC Bypass</summary>

Check:
- Local admin?
- Integrity level

</details>

---

<details markdown="1">
<summary>Kernel Exploit</summary>

Check:
- Old OS
- Missing patches

</details>

</details>

---

<details markdown="1">
<summary># Credential Access</summary>

<details markdown="1">
<summary>SYSTEM → Mimikatz</summary>

```powershell
mimikatz
```

Check:
- logonpasswords
- sekurlsa
- wdigest

</details>

---

<details markdown="1">
<summary>SAM / SYSTEM</summary>

```bash
impacket-secretsdump
```

</details>

---

<details markdown="1">
<summary>LSASS Dump</summary>

Check:
- lsassy
- procdump
- nanodump

</details>

---

<details markdown="1">
<summary>DPAPI</summary>

Check:
- Browser creds
- WiFi creds
- Vault

</details>

---

<details markdown="1">
<summary>Browser Credentials</summary>

Check:
- Chrome
- Edge
- Firefox

</details>

---

<details markdown="1">
<summary>Interesting Files</summary>

Check:
- config files
- passwords.txt
- scripts
- backups

</details>

---

<details markdown="1">
<summary>RDP Saved Credentials</summary>

```cmd
cmdkey /list
```

</details>

---

<details markdown="1">
<summary>PowerShell History</summary>

Check:
- hardcoded creds
- admin activity

</details>

---

<details markdown="1">
<summary>GPP Passwords</summary>

```bash
gpp-decrypt
```

</details>

---

<details markdown="1">
<summary>LAPS</summary>

Check:
- ReadLAPSPassword

</details>

</details>

---

<details markdown="1">
<summary># Domain Enumeration</summary>

<details markdown="1">
<summary>Basic Enumeration</summary>

```powershell
net user /domain
net group /domain
```

</details>

---

<details markdown="1">
<summary>Domain Users</summary>

```bash
impacket-GetADUsers
```

</details>

---

<details markdown="1">
<summary>Domain Computers</summary>

```powershell
Get-ADComputer
```

</details>

---

<details markdown="1">
<summary>Domain Admins</summary>

```powershell
net group "Domain Admins" /domain
```

</details>

---

<details markdown="1">
<summary>SPNs → Kerberoast</summary>

```powershell
Get-NetUser -SPN
```

Check:
- Kerberoastable accounts

</details>

---

<details markdown="1">
<summary>Sessions</summary>

```powershell
Get-NetSession
```

Check:
- Admin sessions

</details>

---

<details markdown="1">
<summary>Shares</summary>

```powershell
Find-DomainShare
```

</details>

---

<details markdown="1">
<summary>ACLs</summary>

Check:
- GenericAll
- GenericWrite
- WriteOwner
- WriteDACL

</details>

---

<details markdown="1">
<summary>Trusts</summary>

```powershell
Get-NetDomainTrust
```

</details>

---

<details markdown="1">
<summary>Delegation</summary>

Check:
- Unconstrained
- Constrained
- RBCD

</details>

---

<details markdown="1">
<summary>ADCS</summary>

Check:
- ESC1
- ESC4
- ESC8

</details>

</details>
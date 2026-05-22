---
title: Active Directory
parent: Red Team
nav_order: 7
has_children: true
---
# Summary

---

# Goal

## DC Administrator or Domain Admins Member

- Obtain Domain Admin privileges
- Abuse Active Directory misconfigurations
- Reuse Kerberos tickets / hashes
- Pivot across domain systems

---

# Attack Flow

1. Initial foothold in Domain PC / Server
2. → Enumeration / Discovery
3. → Identify misconfiguration
4. → ☠ exploit:
5. → Administrator / SYSTEM
6. → Searching for Domain User Information
7. → Domain Pivot / Domain lateral
8. → Privilege Escalation

---
# *Initial Access*
---
<details markdown="1">
<summary>RDP</summary>
## RDP

```zsh
xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /p:BrouhahaTungPerorateBroom2023! /v:192.168.158.75 /dynamic-resolution 
```
- /pth:NTLMHash


</details>

<details markdown="1">
<summary>Win-RM</summary>
## Win-RM

```bash
evil-winrm -i 192.168.121.96 -u Eric.Wallows -p EricLikesRunning800
```

</details>

---
# 最終的な目標のユーザを明確化する

## BloodHoundでDomain Adminsのユーザを検索

👉Check:
- GenericALL
- WriteAble

## ユーザとグループを列挙する
Local

```powershell
net user
```

```powershell
net localgroup
```

Domain

```powershell
net user /domain
```

```powershell
net group /domain
```

```powershell
impacket-GetADUsers -all oscp.exam/r.andrews:BusyofficeWorker890 -dc-ip 172.16.x.200
```

---
# *Enumeration for PrivilegeEscalation*
---

# ユーザ情報の確認

## 権限

```powershell
whoami /priv
```

## Group

```powershell
whoami /groups
```

## powershell history

```powershell
Get-History
```

```powershell
type C:\Users\dave\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

# 環境の確認
## env

```cmd
set
```

```powershell
Get-ChildItem env:
```

👉Check:
- Comment
- Password memo

## Cドライブ直下のファイル/ディレクトリ

👉Check:
- C:\automation
- C:\Windows\Log\task.bat

---
# *Enumeration for  Lateral Movement*
---
## SPNの確認

```zsh
~/Tools/PrivEsc/AD/Enum/PowerSploit/Recon/PowerView.ps1
```

```powershell
Import-Module .\PowerView.ps1
```

```zsh
Get-NetUser -SPN | select samaccountname,serviceprincipalname
```




---
# *Attack*
---



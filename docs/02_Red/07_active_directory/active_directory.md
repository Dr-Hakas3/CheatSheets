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
# Initial Access
---
## RDP

```zsh
xfreerdp3 /u:Eric.Wallows /p:EricLikesRunning800 /v:192.168.121.95 /dynamic-resolution
```

## Win-RM

```bash
evil-winrm -i 192.168.121.96 -u Eric.Wallows -p EricLikesRunning800
```

---
# *Enumeration*
---







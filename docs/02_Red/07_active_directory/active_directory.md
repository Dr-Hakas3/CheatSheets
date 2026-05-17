---
title: Active Directory
parent: Red Team
nav_order: 7
has_children: true
---
# Active Directory

---

# Goal

## Administrator
- Obtain Administrator / SYSTEM privileges
- Bypass UAC
- Dump credentials
- Access protected resources

## Domain Admins

- Obtain Domain Admin privileges
- Abuse Active Directory misconfigurations
- Reuse Kerberos tickets / hashes
- Pivot across domain systems

---

# Attack Flow

1. Initial foothold in Domain PC / Server
2. → Enumeration
3. → Identify misconfiguration
4. → ☠ exploit:
5. → Administrator / SYSTEM
6. → Searching for Domain User Information
7. → Domain Pivot / Domain lateral
8. → Privilege Escalation

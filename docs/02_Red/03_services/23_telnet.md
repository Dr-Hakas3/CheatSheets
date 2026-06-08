---
title: 23 TELNET
parent: Services
grand_parent: Red Team
nav_order: 23
has_children: true
---
# TELNET

---

## Default Port
- 23

---

## Service Info

Telnet is an unencrypted remote login protocol used for command-line access to systems.

It transmits all data, including credentials, in plaintext.

It is commonly found in legacy systems, embedded devices, and poorly secured internal networks.

---
## Common security issues

- No encryption (credentials sent in plaintext)
- Default or weak credentials
- Legacy systems with no security updates
- Credential sniffing on network level
- Hardcoded credentials in embedded devices
- Misconfigured network exposure (internal services exposed externally)

---
# 1. Initial Scan
```zsh
nmap -p 23 --script telnet* <IP>
```

👉 Check:

service availability
banner disclosure
device type hints

---

# 2. Enumeration / Connection Test
```
telnet <IP>
```

👉 Check:

login prompt existence
banner information
response timing differences

---

# 3. Access / Login
```
telnet <IP> 23
```

👉 Try:

default credentials
blank password
device-specific logins

---

---
title: 67,68 DHCP
parent: Services
grand_parent: Red Team
nav_order: 67
---
# DHCP
## Dynamic Host Configuration Protocol
---

## Default Port

- Server: UDP 67
- Client: UDP 68

---

## Service Info



---
## Common security issues



---

## 1. Initial Scan


👉 Check:


---

## 2. Enumeration

👉 Usually limited without credentials


---

## 3. Access / Interaction

### With Credentials


---

### With Hash


---

## 4. Credential Hunting

👉 Credentials usually come from:

* [SMB](smb.md)
* [HTTP](http.md)
* [MSSQL](mssql.md)
* Password attacks → [Password Attacks](../03_initial_access/password_attacks.md)
### File Transfer (Upload / Download)

👉 Primary method: evil-winrm built-in transfer


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
- [ligolo](../04_pivot/ligolo.md)
- [chisel](../04_pivot/chisel.md)
- [ssh-tunnel](../04_pivot/ssh_tunnel.md)

---

👉 If shell obtained:


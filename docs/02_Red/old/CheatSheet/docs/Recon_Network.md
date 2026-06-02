## 1. Host Discovery

```bash
arp-scan -l
```

or

```bash
nmap -sn <NETWORK>
```

---

## 2. Full Port Scan

```bash
nmap -p- --min-rate 1000 -T4 <IP>
```

---

## 3. Service Enumeration

```bash
nmap -p <PORTS> -sC -sV <IP>
```

---

## 4. Quick Triage

| Port      | Service    | Action                              |
| --------- | ---------- | ----------------------------------- |
| 21        | FTP        | [FTP](../services/ftp.md)           |
| 22        | SSH        | [SSH](../services/ssh.md)           |
| 23        |            |                                     |
| 53        | DNS        | [DNS](../services/dns.md)           |
| 80/443    | HTTP/HTTPS | [HTTP/HTTPS](../services/http.md)   |
| 88        | Kerberos   | [Kerberos](../services/kerberos.md) |
| 111/2049  |            |                                     |
| 135       |            |                                     |
| 139/445   | SMB        | [SMB](../services/smb.md)           |
| 389       | LDAP       | [LDAP](../services/ldap.md)         |
| 1433      | MSSQL      | [MSSQL](../services/mssql.md)       |
| 5985/5986 | WinRM      | [WinRM](../services/winrm.md)       |

---

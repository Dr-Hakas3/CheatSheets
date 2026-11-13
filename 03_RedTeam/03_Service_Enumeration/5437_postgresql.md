---
title: 5437 PostgreSQL
parent: Services
grand_parent: Red Team
nav_order: 5437
---
# PostgreSQL


---

## Default Port

- 5437

---

## Service Info



---
## Common security issues

### Default Credential

https://github.com/netbiosX/Default-Credentials/blob/master/PostgreSQL-Default-Password-List.md

![](../../assets/images/Pasted%20image%2020260507101928.png)

---

## 1. Access

```zsh
psql -h 192.168.243.47 -p 5437 -U postgres
```

```zsh
Password for user postgres: 
psql (17.5 (Debian 17.5-1), server 11.7 (Debian 11.7-0+deb10u1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off, ALPN: none)
Type "help" for help.
```

```zsh
postgres=# 
```


---

## 2. Enumeration

👉 Usually limited without credentials

---


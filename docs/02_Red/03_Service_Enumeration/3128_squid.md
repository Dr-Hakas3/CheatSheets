---
title: 3128 Squid
parent: Services
grand_parent: Red Team
nav_order: 3128
---
# Squid
---

## Default Port

- 3128

---

## Service Info



---
## Common security issues



---

## 1. Initial Scan

```bash

```

👉 Check:

* 

---

## 2. Exploit

https://book.hacktricks.wiki/en/network-services-pentesting/3128-pentesting-squid.html

👉 
### Download
https://github.com/aancw/spose

### Usage
```zsh
python3 spose.py --proxy http://192.168.239.189:3128 --target 192.168.239.189 
```

---

## 3. Browser Access

```zsh
curl --proxy http://192.168.228.189:3128 http://192.168.45.199
```

---

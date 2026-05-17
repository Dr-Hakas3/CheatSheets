---
title: 135,136 RPC
parent: Services
grand_parent: Red Team
nav_order: 135
---
# RPC
## Remote Procedure Call


---

## Default Port

- 135

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

## 2. Enumeration

👉 Usually limited without credentials
### enum4linux

```bash
enum4linux target-ip
```
- -v # Verbose mode
- -a Everything
- -U users list
- -u user
- -p password

### If you've managed to obtain credentials, you can pull a full list of users regardless of the RestrictAnonymous option
```zsh
enum4linux -u administrator -p password -U target-ip
```
### Get username from the defaut RID range (500-550, 1000-1050)

```zsh
enum4linux -r target-ip
```

# Get username using a custom RID range

```zsh
enum4linux -R 600-660 target-ip
```

### List groups

```zsh
enum4linux -G target-ip
```

### List shares

```zsh
enum4linux -S target-ip
```

### Perform a dictionary attack, if the server doesn't let you retrieve a share list

```zsh
enum4linux -s shares.txt target-ip
```

### Pulls OS information using smbclient, this can pull the service pack version on some versions of Windows

```zsh
enum4linux -o target-ip
```

### Pull information about printers known to the remove device.

```zsh
enum4linux -i target-ip
```


---

## 3. Access / Interaction

### Anonymous connection (-N=no pass)

```bash
rpcclient -U “” -N <ip>
```

### With Credentials

#### Connection with user

```zsh
rpcclient -U “user” <ip>
```

## Hash Login
```zsh
rpcclient -U 'sub.poseidon\lisa' --pw-nt-hash --password='905ae9b4d957545fb7b9ea0c4333247b' 192.168.133.162
```

---

## 4. Command
### Get information about the DC

```zsh
srvinfo
```

### Get information about objects such as groups (enum*)

```zsh
enumdomains
enumdomgroups
enumalsgroups builtin
```

### Try to get domain password policy

```zsh
getdompwinfo
```

### Try to enumerate different truste domains

```zsh
dsr_enumtrustdom
```

### Get username for a defined user ?

```zsh
getusername
```

### Query user, group etc informations

```zsh
queryuser RID
querygroupmem519
queryaliasmem builtin 0x220
```

### Query info policy

```zsh
lsaquery
```

### Convert SID to names

```zsh
lookupsids SID
```

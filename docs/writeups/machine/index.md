---
title:
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.128.157
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-11 05:59 +0900
Nmap scan report for 192.168.128.157
Host is up (0.092s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 74:ba:20:23:89:92:62:02:9f:e7:3d:3b:83:d4:d9:6c (RSA)
|   256 54:8f:79:55:5a:b0:3a:69:5a:d5:72:39:64:fd:07:4e (ECDSA)
|_  256 7f:5d:10:27:62:ba:75:e9:bc:c8:4f:e2:72:87:d4:e2 (ED25519)
25/tcp  open  smtp        Exim smtpd
| smtp-commands: forward Hello nmap.scanme.org [192.168.45.231], SIZE 52428800, 8BITMIME, PIPELINING, CHUNKING, PRDR, HELP
|_ Commands supported: AUTH HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: Host: FORWARD; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.5-Debian)
|   Computer name: forward
|   NetBIOS computer name: FORWARD\x00
|   Domain name: \x00
|   FQDN: forward
|_  System time: 2026-06-10T17:00:20-04:00
| smb2-time: 
|   date: 2026-06-10T21:00:22
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 1h19m59s, deviation: 2h18m33s, median: 0s

TRACEROUTE (using port 445/tcp)
HOP RTT      ADDRESS
1   91.56 ms 192.168.45.1
2   91.54 ms 192.168.45.254
3   91.83 ms 192.168.251.1
4   91.91 ms 192.168.128.157

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 94.07 seconds

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ smbclient -L //192.168.128.157                                                                   
Password for [WORKGROUP\kali]:

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
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Forward]
└─$ smbclient //192.168.128.157/utils
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Dec 18 17:26:48 2020
  ..                                  D        0  Fri Dec 18 16:48:44 2020
  fox.reg                             N    10634  Fri Dec 18 16:48:44 2020
  TeamViewer_Setup_v7.exe             N  5024832  Fri Dec 18 16:48:44 2020
  mara.reg                            N    10408  Fri Dec 18 16:48:44 2020
  vale.reg                            N    10206  Fri Dec 18 16:48:44 2020
  golemitratigunda.reg                N    10206  Fri Dec 18 16:48:44 2020
  alberobello.reg                     N    10206  Fri Dec 18 16:48:44 2020
  giammy.reg                          N    10312  Fri Dec 18 16:48:44 2020
  README.all                          N      165  Fri Dec 18 16:53:55 2020

                14384136 blocks of size 1024. 11598400 blocks available
```

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Forward/utils]
└─$ smbclient //192.168.128.157/utils
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> prompt off
smb: \> recurse on
smb: \> mget *
getting file \fox.reg of size 10634 as fox.reg (28.1 KiloBytes/sec) (average 28.1 KiloBytes/sec)
getting file \TeamViewer_Setup_v7.exe of size 5024832 as TeamViewer_Setup_v7.exe (3737.3 KiloBytes/sec) (average 2921.8 KiloBytes/sec)
getting file \mara.reg of size 10408 as mara.reg (27.4 KiloBytes/sec) (average 2399.0 KiloBytes/sec)
getting file \vale.reg of size 10206 as vale.reg (27.0 KiloBytes/sec) (average 2037.8 KiloBytes/sec)
getting file \golemitratigunda.reg of size 10206 as golemitratigunda.reg (26.9 KiloBytes/sec) (average 1770.8 KiloBytes/sec)
getting file \alberobello.reg of size 10206 as alberobello.reg (26.9 KiloBytes/sec) (average 1566.8 KiloBytes/sec)
getting file \giammy.reg of size 10312 as giammy.reg (27.1 KiloBytes/sec) (average 1404.9 KiloBytes/sec)
getting file \README.all of size 165 as README.all (0.4 KiloBytes/sec) (average 1271.8 KiloBytes/sec)
smb: \> 

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

```

</details>
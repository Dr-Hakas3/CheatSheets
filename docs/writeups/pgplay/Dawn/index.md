---
title: Dawn
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.123.11                 
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-30 03:56 +0900
Nmap scan report for 192.168.123.11
Host is up (0.095s latency).
Not shown: 65531 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 34.24 seconds

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ sudo nmap -Pn -p80,139,445,3306 -sSCV -A -oN full_tcp-scan.txt --open 192.168.123.11
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-30 03:57 +0900
Nmap scan report for 192.168.123.11
Host is up (0.092s latency).

PORT     STATE SERVICE     VERSION
80/tcp   open  http        Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
3306/tcp open  mysql       MariaDB 5.5.5-10.3.15
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.15-MariaDB-1
|   Thread ID: 14
|   Capabilities flags: 63486
|   Some Capabilities: Speaks41ProtocolNew, SupportsCompression, FoundRows, Support41Auth, Speaks41ProtocolOld, SupportsTransactions, IgnoreSigpipes, IgnoreSpaceBeforeParenthesis, InteractiveClient, LongColumnFlag, DontAllowDatabaseTableColumn, SupportsLoadDataLocal, ODBCClient, ConnectWithDatabase, SupportsMultipleResults, SupportsAuthPlugins, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: i-CH~e_,]m1FP=#3uul=
|_  Auth Plugin Name: mysql_native_password
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.14
Network Distance: 4 hops
Service Info: Host: DAWN

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.5-Debian)
|   Computer name: dawn
|   NetBIOS computer name: DAWN\x00
|   Domain name: dawn
|   FQDN: dawn.dawn
|_  System time: 2026-05-29T14:58:03-04:00
| smb2-time: 
|   date: 2026-05-29T18:58:05
|_  start_date: N/A
|_clock-skew: mean: 1h19m59s, deviation: 2h18m33s, median: 0s

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   92.23 ms 192.168.45.1
2   92.05 ms 192.168.45.254
3   92.26 ms 192.168.251.1
4   91.32 ms 192.168.123.11

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.48 seconds

```

# 80

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ feroxbuster \
-u http://192.168.123.11 \
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt

```

```zsh

```

```zsh

```

```zsh

```

# 445

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ smbmap -H 192.168.123.11

[+] IP: 192.168.123.11:445      Name: 192.168.123.11            Status: NULL Session
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        ITDEPT                                                  READ, WRITE     PLEASE DO NOT REMOVE THIS SHARE. IN CASE YOU ARE NOT AUTHORIZED TO USE THIS SYSTEM LEAVE IMMEADIATELY.
        IPC$                                                    NO ACCESS       IPC Service (Samba 4.9.5-Debian)
[|] Closing connections..                                                                                           [/] Closing connections..                                                                                           [-] Closing connections..                                                                                           [*] Closed 1 connections   
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ smbclient -L //192.168.123.11/                                       
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        ITDEPT          Disk      PLEASE DO NOT REMOVE THIS SHARE. IN CASE YOU ARE NOT AUTHORIZED TO USE THIS SYSTEM LEAVE IMMEADIATELY.
        IPC$            IPC       IPC Service (Samba 4.9.5-Debian)
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            WIN2K3STDVIC
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
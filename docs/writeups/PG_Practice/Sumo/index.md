---
title: Sumo
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
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.189.87                 
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-25 00:11 +0900
Nmap scan report for 192.168.189.87
Host is up (0.082s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 28.75 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ sudo nmap -Pn -p22,80 -sSCV -A -oN full_tcp-scan.txt --open 192.168.189.87
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-25 00:15 +0900
Nmap scan report for 192.168.189.87
Host is up (0.083s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 06:cb:9e:a3:af:f0:10:48:c4:17:93:4a:2c:45:d9:48 (DSA)
|   2048 b7:c5:42:7b:ba:ae:9b:9b:71:90:e7:47:b4:a4:de:5a (RSA)
|_  256 fa:81:cd:00:2d:52:66:0b:70:fc:b8:40:fa:db:18:30 (ECDSA)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 2.6.X|3.X
OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3
OS details: Linux 2.6.32 - 3.10, Linux 2.6.32 - 3.13
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   82.61 ms 192.168.45.1
2   82.43 ms 192.168.45.254
3   82.57 ms 192.168.251.1
4   82.75 ms 192.168.189.87

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.57 seconds
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
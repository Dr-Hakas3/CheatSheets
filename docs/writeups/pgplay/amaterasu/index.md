---
title: Amaterasu
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
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.231.249                
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-20 19:52 +0900
Nmap scan report for 192.168.231.249
Host is up (0.078s latency).
Not shown: 65524 filtered tcp ports (no-response), 7 closed tcp ports (reset)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
21/tcp    open  ftp
25022/tcp open  unknown
33414/tcp open  unknown
40080/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 148.62 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ sudo nmap -Pn -p21,25022,33414,40080 -sSCV -A -oN full_tcp-scan.txt --open 192.168.231.249
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-20 19:55 +0900
Nmap scan report for 192.168.231.249
Host is up (0.079s latency).

PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.45.160
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
25022/tcp open  ssh     OpenSSH 8.6 (protocol 2.0)
| ssh-hostkey: 
|   256 68:c6:05:e8:dc:f2:9a:2a:78:9b:ee:a1:ae:f6:38:1a (ECDSA)
|_  256 e9:89:cc:c2:17:14:f3:bc:62:21:06:4a:5e:71:80:ce (ED25519)
33414/tcp open  http    Werkzeug httpd 2.2.3 (Python 3.9.13)
|_http-server-header: Werkzeug/2.2.3 Python/3.9.13
|_http-title: 404 Not Found
40080/tcp open  http    Apache httpd 2.4.53 ((Fedora))
|_http-title: My test page
|_http-server-header: Apache/2.4.53 (Fedora)
| http-methods: 
|_  Potentially risky methods: TRACE
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running (JUST GUESSING): Linux 4.X|5.X|2.6.X|3.X (97%), MikroTik RouterOS 7.X (97%)
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:6
Aggressive OS guesses: Linux 4.15 - 5.19 (97%), Linux 5.0 - 5.14 (97%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (97%), Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 3.4 - 3.10 (91%), Linux 4.15 (91%), Linux 5.14 - 6.8 (91%), Linux 2.6.32 - 3.10 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Unix

TRACEROUTE (using port 21/tcp)
HOP RTT      ADDRESS
1   80.54 ms 192.168.45.1
2   80.21 ms 192.168.45.254
3   80.37 ms 192.168.251.1
4   80.51 ms 192.168.231.249

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 54.33 seconds
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
---
title: Katana
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
┌──(kali㉿kali)-[~/CTF/OffSec/Katana]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.143.83 --min-rate=5000
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-19 19:28 +0900
Nmap scan report for 192.168.143.83
Host is up (0.089s latency).
Not shown: 65464 closed tcp ports (reset), 65 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
7080/tcp open  empowerid
8088/tcp open  radan-http
8715/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 18.95 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Katana]
└─$ sudo nmap -Pn -p21,22,80,7080,8088,8715 -sSCV -A -oN full_tcp-scan.txt --open 192.168.143.83 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-19 19:33 +0900
Nmap scan report for 192.168.143.83
Host is up (0.088s latency).

PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           vsftpd 3.0.3
22/tcp   open  ssh           OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 89:4f:3a:54:01:f8:dc:b6:6e:e0:78:fc:60:a6:de:35 (RSA)
|   256 dd:ac:cc:4e:43:81:6b:e3:2d:f3:12:a1:3e:4b:a3:22 (ECDSA)
|_  256 cc:e6:25:c0:c6:11:9f:88:f6:c4:26:1e:de:fa:e9:8b (ED25519)
80/tcp   open  http          Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Katana X
7080/tcp open  ssl/empowerid LiteSpeed
|_http-server-header: LiteSpeed
| tls-alpn: 
|   h2
|   spdy/3
|   spdy/2
|_  http/1.1
|_http-title: Did not follow redirect to https://192.168.143.83:7080/
| ssl-cert: Subject: commonName=katana/organizationName=webadmin/countryName=US
| Not valid before: 2020-05-11T13:57:36
|_Not valid after:  2022-05-11T13:57:36
|_ssl-date: TLS randomness does not represent time
8088/tcp open  http          LiteSpeed httpd
|_http-title: Katana X
|_http-server-header: LiteSpeed
8715/tcp open  http          nginx 1.14.2
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Restricted Content
|_http-server-header: nginx/1.14.2
|_http-title: 401 Authorization Required
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   87.87 ms 192.168.45.1
2   87.84 ms 192.168.45.254
3   87.96 ms 192.168.251.1
4   88.06 ms 192.168.143.83

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.43 seconds
```

# FTP

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Katana]
└─$ ftp 192.168.143.83  
Connected to 192.168.143.83.
220 (vsFTPd 3.0.3)
Name (192.168.143.83:kali): anonymous
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> exit
221 Goodbye.
```

# HTTP
## 80

```zsh

```
## 7080

```zsh

```

## 8088

![](../../../assets/images/Pasted%20image%2020260519201238.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Katana]
└─$ gobuster dir \
-u http://192.168.143.83:8088 \
-w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
-x php,txt,bak,zip,old \
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
[+] Url:                     http://192.168.143.83:8088
[+] Method:                  GET
[+] Threads:                 25
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt
[+] Negative Status codes:   403,404
[+] User Agent:              Mozilla/5.0 (Windows; U; Windows NT 5.1; nl) AppleWebKit/522.13.1 (KHTML, like Gecko) Version/3.0.2 Safari/522.13.1
[+] Extensions:              php,txt,bak,zip,old
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
upload.php           (Status: 200) [Size: 1800]
docs                 (Status: 200) [Size: 5472]
protected            (Status: 401) [Size: 1242]
phpinfo.php          (Status: 200) [Size: 50840]
Progress: 373686 / 373686 (100.00%)
===============================================================
Finished
===============================================================
```

```zsh

```

http://192.168.231.83:8088/docs/admin.html

![](../../../assets/images/Pasted%20image%2020260520042614.png)
http://192.168.231.83:8088/upload.php


![](../../../assets/images/Pasted%20image%2020260519204740.png)

http://192.168.231.83:8088/upload.html

![](../../../assets/images/Pasted%20image%2020260520041637.png)

![](../../../assets/images/Pasted%20image%2020260520042212.png)


# 8715

![](../../../assets/images/Pasted%20image%2020260520041832.png)

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
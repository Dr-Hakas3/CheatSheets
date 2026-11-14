---
title: DoubleTake
---
```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 10.129.150.179
[sudo] password for kali:
Starting Nmap 7.991 ( https://nmap.org ) at 2026-11-14 19:22 +0900
Nmap scan report for 10.129.150.179
Host is up (0.26s latency).
Not shown: 65492 closed tcp ports (reset), 41 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 75.87 seconds
```

![[Pasted image 20261114192652.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ nmap -Pn -p22,80 -sVC 10.129.150.179
Starting Nmap 7.991 ( https://nmap.org ) at 2026-11-14 19:27 +0900
Nmap scan report for 10.129.150.179
Host is up (0.26s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 10.6 (protocol 2.0)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
|_http-server-header: nginx/1.24.0 (Ubuntu)
| http-auth:
| HTTP/1.1 401 UNAUTHORIZED\x0D
|_  Basic realm=Zentara
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.54 seconds
```

![[Pasted image 20261114192845.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ whatweb http://10.129.150.179
http://10.129.150.179 [401 Unauthorized] Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][nginx/1.24.0 (Ubuntu)], IP[10.129.150.179], WWW-Authenticate[Zentara][Basic], nginx[1.24.0]
```

![[Pasted image 20261114193013.png]]


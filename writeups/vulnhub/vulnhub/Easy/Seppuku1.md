- **Independent Challenges**
- **Host Discovery**
- └─# nmap -sn --min-rate=20000 192.168.133.0/24

![[Seppuku1 image.png]]

- **1 Target #1 – 192.168.133.170**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─# nmap -p- -Pn --min-rate=20000 192.168.133.170

![[Seppuku1 image 1.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.133.170 | **TCP**: 21,22,80,139,445,7080,7601,8088 |

└─#nmap -p21,22,80,139,445,7080,7601,8088 -sV -sC -A --min-rate=20000 192.168.133.170 -o open-port.txt

![[Seppuku1 image 2.png]]

![[Seppuku1 image 3.png]]

![[Seppuku1 image 4.png]]

OS Linux

Port 21

FTP

vsftpd 3.0.3

![[Seppuku1 image 5.png]]

**I can't anonymous login to ftp.**

**Port 22**

OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)

**Port 80**

**HTTP**

**nginx 1.14.2**

![[Seppuku1 image 6.png]]

**Port 139**

**null session.**

![[Seppuku1 image 7.png]]

**Port 445**

└─# enum4linux 192.168.133.170

![[Seppuku1 image 8.png]]

![[Seppuku1 image 9.png]]

![[Seppuku1 image 10.png]]

![[Seppuku1 image 11.png]]

![[Seppuku1 image 12.png]]

![[Seppuku1 image 13.png]]

**Port 7601**

![[Seppuku1 image 14.png]]

└─# gobuster dir -u http://seppuku:7601 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

![[Seppuku1 image 15.png]]

keys

![[Seppuku1 image 16.png]]

![[Seppuku1 image 17.png]]

**password.lst**

![[Seppuku1 image 18.png]]

**1.2** **Initial Access –**

└─# hydra -L users.txt -P passwd.lst seppuku ssh

![[Seppuku1 image 19.png]]

**eeyoree**

![[Seppuku1 image 20.png]]

![[Seppuku1 image 21.png]]

**Local.txt value:**

**1.3** **Privilege Escalation -**

![[Seppuku1 image 22.png]]

![[Seppuku1 image 23.png]]

![[Seppuku1 image 24.png]]

When I looked it up, I found out that this was a rabbit hole.

**1.4** **Post Exploitation**

![[Seppuku1 image 25.png]]

![[Seppuku1 image 26.png]]

![[Seppuku1 image 27.png]]

![[Seppuku1 image 28.png]]

![[Seppuku1 image 29.png]]

**Proof.txt value:**

![[Seppuku1 image 30.png]]

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
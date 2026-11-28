- **Independent Challenges**
- **1 Target #1 –** 10.10.11.32
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

First, run nmap to inspect all ports.

└─# nmap -p- 10.10.11.32 --min-rate 20000

![[Sightless image.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.32 | **TCP**: 21,22,80 |

I found three ports that opened.

Let's dig deeper into the service.

└─# nmap -p21,22,80 -sV -sC 10.10.11.32 --min-rate 20000

![[Sightless image 1.png]]

Before investigating them one by one, register your IPaddress and domain in the hosts file.

└─# echo "10.10.11.32 sightless.htb" | tee -a /etc/hosts

![[Sightless image 2.png]]

21 FTP

First port is FTP port that service is proFTPD.

└─# ftp sightless.htb

![[Sightless image 3.png]]

Anonymous Login failed.

Vulnavility enumeration.

└─# nmap --script ftp* -p 21 sightless.htb

80 http

![[Sightless image 4.png]]

![[Sightless image 5.png]]

**SQLPad's "Start Now" Button is URL  Link that provide new subdomain.**

**I added the subdomain to hosts.**

└─# echo "10.10.11.32 sqlpad.sightless.htb" | tee -a /etc/hosts

![[Sightless image 6.png]]

**Directory Enumeration.**

└─# gobuster dir -u http://sightless.htb -w /usr/share/wordlists/dirb/common.txt

![[Sightless image 7.png]]

**Browser Access**

![[Sightless image 8.png]]

**I found sqlpad page that can save,view and execute sql query.**

**Subdomain Enumeration.**

└─# gobuster dns -d sightless.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt

![[Sightless image 9.png]]

**Vhost Enumeration.**

└─# gobuster vhost -u http://sightless.htb/ -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt --append-domain -r

**1.2** **Initial Access –**

└─# john shadow -w=/usr/share/wordlists/rockyou.txt

![[Sightless image 10.png]]

insaneclownposse

![[Sightless image 11.png]]

**Local.txt value:**

**1.3** **Privilege Escalation -**

**1.4** **Post Exploitation**

**Proof.txt value:**

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
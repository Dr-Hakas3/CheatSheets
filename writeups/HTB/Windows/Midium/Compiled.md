![[Compiled image.png]]

- **Independent Challenges**
- **1 Target #1 –** 10.10.11.26
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─# nmap -p- --min-rate=10000 10.10.11.26 -o nmap_-p-.txt

![[Compiled image 1.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.26 | **TCP**: 3000,5000,5985 |

└─# nmap -p3000,5000,5985 -sC -sV --min-rate=10000 10.10.11.26 -o nmap_-p3000_5000_5985.txt

![[Compiled image 2.png]]

![[Compiled image 3.png]]

![[Compiled image 4.png]]

![[Compiled image 5.png]]

![[Compiled image 6.png]]

**We found OS Version at Windows XP**

**Port 3000 - Gitea**

└─# feroxbuster -u http://gitea.compiled.htb:3000 -w /usr/share/dirb/wordlists/common.txt -g

![[Compiled image 7.png]]

![[Compiled image 8.png]]

![[Compiled image 9.png]]

![[Compiled image 10.png]]

**Version 1.21.6**

**Create NewAccount**

**gkali:gkaligkali gkali@hoge.com**

![[Compiled image 11.png]]

**Create NewRepogitry**

**View -Source**

![[Compiled image 12.png]]

![[Compiled image 13.png]]

![[Compiled image 14.png]]

**git version 2.45.0**

![[Compiled image 15.png]]

**Port 5000 - Compiled Service Page**

![[Compiled image 16.png]]

**Port 5985**

**1.2** **Initial Access –**

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
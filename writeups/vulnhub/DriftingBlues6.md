- **Independent Challenges**
- **1 Target #1 – 192.168.133.166**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

**Host Discovery**

└─# nmap -sn --min-rate=20000 192.168.133.160-170

![[DriftingBlues6 image.png]]

**Service Enumeration**

└─# nmap -p- --min-rate=20000 192.168.133.166

![[DriftingBlues6 image 1.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.133.166 | **TCP**: 80 |

└─# nmap -p80 -sC -sV -A --min-rate=10000 192.168.133.166

![[DriftingBlues6 image 2.png]]

OS Debian Linux

Port 80

Apache 2.2.22

whatweb result

![[DriftingBlues6 image 3.png]]

Directory Enumeration.

└─# ffuf -c -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://192.168.133.166/FUZZ

![[DriftingBlues6 image 4.png]]

**index**

**db**

**robots**

**spammer**

└─# gobuster dir -u http://192.168.133.166 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip

![[DriftingBlues6 image 5.png]]

**Browser Access**

![[DriftingBlues6 image 6.png]]

**robots.txt**

![[DriftingBlues6 image 7.png]]

![[DriftingBlues6 image 8.png]]

![[DriftingBlues6 image 9.png]]

myspace4

![[DriftingBlues6 image 10.png]]

![[DriftingBlues6 image 11.png]]

![[DriftingBlues6 image 12.png]]

mayer:lionheart

textpattern/textpattern/

![[DriftingBlues6 image 13.png]]

![[DriftingBlues6 image 14.png]]

**mayer's information.**

**Textpattern CMS v4.8.3**

![[DriftingBlues6 image 15.png]]

![[DriftingBlues6 image 16.png]]

![[DriftingBlues6 image 17.png]]

**1.2** **Initial Access –**

I created a reverse shell file named test.php.

![[DriftingBlues6 image 18.png]]

**Upload malicias file.**

![[DriftingBlues6 image 19.png]]

![[DriftingBlues6 image 20.png]]

![[DriftingBlues6 image 21.png]]

![[DriftingBlues6 image 22.png]]

**1.3** **Privilege Escalation -**

![[DriftingBlues6 image 23.png]]

![[DriftingBlues6 image 24.png]]

**1.4** **Post Exploitation**

![[DriftingBlues6 image 25.png]]

![[DriftingBlues6 image 26.png]]

![[DriftingBlues6 image 27.png]]

**Proof.txt value:**

![[DriftingBlues6 image 28.png]]

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
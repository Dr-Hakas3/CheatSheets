- **Independent Challenges**
- **1 Target #1 –** 10.129.47.55
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

![[UnderPass image.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.129.47.55 | **TCP**: 22,80 |

![[UnderPass image 1.png]]

![[UnderPass image 2.png]]

snmpbulkwalk -c public -v2c underpass.htb

![[UnderPass image 3.png]]

steve@underpass.htb

daloradius

![[UnderPass image 4.png]]

![[UnderPass image 5.png]]

**1.2** **Initial Access –**

└─# feroxbuster -u http://underpass.htb/daloradius/ -w /usr/share/dirb/wordlists/big.txt

![[UnderPass image 6.png]]

![[UnderPass image 7.png]]

![[UnderPass image 8.png]]

└─# feroxbuster -u http://underpass.htb/daloradius/app/operators/ -w /usr/share/dirb/wordlists/big.txt -x php

![[UnderPass image 9.png]]

![[UnderPass image 10.png]]

![[UnderPass image 11.png]]

412dd4759978acfcc81deab01b382403:underwaterfriends

![[UnderPass image 12.png]]

![[UnderPass image 13.png]]

**Local.txt value:**64cfe0c6ab7f0cd32c8e2f7a1b98c1cb

![[UnderPass image 14.png]]

**1.3** **Privilege Escalation -**

![[UnderPass image 15.png]]

**1.4** **Post Exploitation**

![[UnderPass image 16.png]]

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
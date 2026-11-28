**Independent Challenges**

- **1 Target #1 – 192.168.11.17**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─# cat nmap-p-.txt

\# Nmap 7.94SVN scan initiated Sun Sep  1 15:04:10 2024 as: nmap -p- --min-rate 10000 -o nmap-p-.txt 192.168.110.146

Nmap scan report for 192.168.110.146

Host is up (0.0026s latency).

Not shown: 65532 closed tcp ports (reset)

PORT   STATE SERVICE

21/tcp open  ftp

22/tcp open  ssh

80/tcp open  http

MAC Address: 00:0C:29:DD:E4:D8 (VMware)

\# Nmap done at Sun Sep  1 15:04:32 2024 -- 1 IP address (1 host up) scanned in 22.22 seconds

![[DevGuru 1 image.png]]

└─# cat nmap-A-p21_22_80.txt

\# Nmap 7.94SVN scan initiated Sun Sep  1 15:05:16 2024 as: nmap -p21,22,80 -A --min-rate 10000 -o nmap-A-p21_22_80.txt 192.168.110.146

Nmap scan report for 192.168.110.146

Host is up (0.00078s latency).

PORT   STATE SERVICE VERSION

21/tcp open  ftp     vsftpd 3.0.2

22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)

\| ssh-hostkey:

\|   1024 12:4e:f8:6e:7b:6c:c6:d8:7c:d8:29:77:d1:0b:eb:72 (DSA)

\|   2048 72:c5:1c:5f:81:7b:dd:1a:fb:2e:59:67:fe:a6:91:2f (RSA)

\|   256 06:77:0f:4b:96:0a:3a:2c:3b:f0:8c:2b:57:b5:97:bc (ECDSA)

\|_  256 28:e8:ed:7c:60:7f:19:6c:e3:24:79:31:ca:ab:5d:2d (ED25519)

80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))

\|_http-server-header: Apache/2.4.7 (Ubuntu)

\|_http-title: DeRPnStiNK

\| http-robots.txt: 2 disallowed entries

\|_/php/ /temporary/

MAC Address: 00:0C:29:DD:E4:D8 (VMware)

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Device type: general purpose

Running: Linux 3.X|4.X

OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4

OS details: Linux 3.2 - 4.9

Network Distance: 1 hop

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE

HOP RTT     ADDRESS

1   0.78 ms 192.168.110.146

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

\# Nmap done at Sun Sep  1 15:05:41 2024 -- 1 IP address (1 host up) scanned in 25.86 seconds

![[DevGuru 1 image 1.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: |

Port 80

└─# whatweb http://devguru.local/

![[DevGuru 1 image 2.png]]

└─# feroxbuster -u http://192.168.11.17 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -g -o feroxbuxter-g.txt

![[DevGuru 1 image 3.png]]

Port 8585

└─# whatweb http://devguru.local:8585/

![[DevGuru 1 image 4.png]]

Gitea Version check.

![[DevGuru 1 image 5.png]]

1.12.5

Browser Access

![[DevGuru 1 image 6.png]]

OCTOBER CMS

Error Message

![[DevGuru 1 image 7.png]]

![[DevGuru 1 image 8.png]]

**1.2** **Initial Access –** **公開すべきでは無****いリポジトリ**

https://github.com/arthaud/git-dumper.git

![[DevGuru 1 image 9.png]]

![[DevGuru 1 image 10.png]]

**解読不可能なため既知のパスワードのハッシュに置き換える**

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
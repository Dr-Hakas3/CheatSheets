- **Independent Challenges**
- **1 Target #1 –**
- **1.1 Initial Access –** 10.10.11.51

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─$ sudo nmap -p- 10.10.11.51 --min-rate 20000

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-01 23:02 JST

Nmap scan report for 10.10.11.51

Host is up (0.26s latency).

Not shown: 65509 filtered tcp ports (no-response)

PORT      STATE SERVICE

53/tcp    open  domain

88/tcp    open  kerberos-sec

135/tcp   open  msrpc

139/tcp   open  netbios-ssn

389/tcp   open  ldap

445/tcp   open  microsoft-ds

464/tcp   open  kpasswd5

593/tcp   open  http-rpc-epmap

636/tcp   open  ldapssl

1433/tcp  open  ms-sql-s

3268/tcp  open  globalcatLDAP

3269/tcp  open  globalcatLDAPssl

5985/tcp  open  wsman

9389/tcp  open  adws

47001/tcp open  winrm

49664/tcp open  unknown

49665/tcp open  unknown

49666/tcp open  unknown

49667/tcp open  unknown

49689/tcp open  unknown

49690/tcp open  unknown

49691/tcp open  unknown

49706/tcp open  unknown

49722/tcp open  unknown

49731/tcp open  unknown

49806/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 17.67 seconds

![[EscapeTwo image.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.51 | **TCP**: 53,88,135,139,389,445,464,593,636,1433,3268,3269,5985,9389 |

└─$ sudo nmap -A 10.10.11.51 --min-rate 20000

Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-01 23:10 JST

Nmap scan report for 10.10.11.51

Host is up (0.38s latency).

Not shown: 987 filtered tcp ports (no-response)

PORT     STATE SERVICE       VERSION

53/tcp   open  domain        Simple DNS Plus

88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-02-01 14:10:38Z)

135/tcp  open  msrpc         Microsoft Windows RPC

139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn

389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)

\|_ssl-date: 2025-02-01T14:12:22+00:00; +1s from scanner time.

\| ssl-cert: Subject: commonName=DC01.sequel.htb

\| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:\<unsupported>, DNS:DC01.sequel.htb

\| Not valid before: 2024-06-08T17:35:00

\|_Not valid after:  2025-06-08T17:35:00

445/tcp  open  microsoft-ds?

464/tcp  open  kpasswd5?

593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0

636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)

\| ssl-cert: Subject: commonName=DC01.sequel.htb

\| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:\<unsupported>, DNS:DC01.sequel.htb

\| Not valid before: 2024-06-08T17:35:00

\|_Not valid after:  2025-06-08T17:35:00

\|_ssl-date: 2025-02-01T14:12:22+00:00; +1s from scanner time.

1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM

\| ms-sql-ntlm-info:

\|   10.10.11.51:1433:

\|     Target_Name: SEQUEL

\|     NetBIOS_Domain_Name: SEQUEL

\|     NetBIOS_Computer_Name: DC01

\|     DNS_Domain_Name: sequel.htb

\|     DNS_Computer_Name: DC01.sequel.htb

\|     DNS_Tree_Name: sequel.htb

\|_    Product_Version: 10.0.17763

\| ms-sql-info:

\|   10.10.11.51:1433:

\|     Version:

\|       name: Microsoft SQL Server 2019 RTM

\|       number: 15.00.2000.00

\|       Product: Microsoft SQL Server 2019

\|       Service pack level: RTM

\|       Post-SP patches applied: false

\|_    TCP port: 1433

\| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback

\| Not valid before: 2025-02-01T03:48:20

\|_Not valid after:  2055-02-01T03:48:20

\|_ssl-date: 2025-02-01T14:12:22+00:00; +1s from scanner time.

3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)

\|_ssl-date: 2025-02-01T14:12:22+00:00; +1s from scanner time.

\| ssl-cert: Subject: commonName=DC01.sequel.htb

\| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:\<unsupported>, DNS:DC01.sequel.htb

\| Not valid before: 2024-06-08T17:35:00

\|_Not valid after:  2025-06-08T17:35:00

3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)

\| ssl-cert: Subject: commonName=DC01.sequel.htb

\| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:\<unsupported>, DNS:DC01.sequel.htb

\| Not valid before: 2024-06-08T17:35:00

\|_Not valid after:  2025-06-08T17:35:00

\|_ssl-date: 2025-02-01T14:12:22+00:00; +1s from scanner time.

5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

\|_http-server-header: Microsoft-HTTPAPI/2.0

\|_http-title: Not Found

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Device type: general purpose

Running (JUST GUESSING): Microsoft Windows 2019|10 (97%)

OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10

Aggressive OS guesses: Windows Server 2019 (97%), Microsoft Windows 10 1903 - 21H1 (91%)

No exact OS matches for host (test conditions non-ideal).

Network Distance: 2 hops

Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:

\| smb2-security-mode:

\|   3:1:1:

\|_    Message signing enabled and required

\| smb2-time:

\|   date: 2025-02-01T14:11:45

\|_  start_date: N/A

TRACEROUTE (using port 53/tcp)

HOP RTT       ADDRESS

1   404.58 ms 10.10.16.1

2   404.74 ms 10.10.11.51

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 126.43 seconds

Adding the domain name to the /etc/hosts file

![[EscapeTwo image 1.png]]

**Investigating each port.**

Port 88

└─$ ~/github/tools/kerbrute_linux_amd64 -d sequel.htb --dc 10.10.11.51 userenum /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt

![[EscapeTwo image 2.png]]

Port 389

![[EscapeTwo image 3.png]]

Port 9389

└─$ sudo nmap -p9389 -sV -sC 10.10.11.51

Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-01 23:21 JST

Nmap scan report for sequel.htb (10.10.11.51)

Host is up (0.20s latency).

PORT     STATE SERVICE VERSION

9389/tcp open  mc-nmf  .NET Message Framing

Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 15.35 seconds

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
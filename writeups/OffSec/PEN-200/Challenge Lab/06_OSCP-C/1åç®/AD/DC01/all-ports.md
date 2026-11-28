┌──(kali㉿kali)-\[~/…/ChallengeLab/OSCP_C/AD/DC01\]

└─$ sudo nmap -Pn -n 10.10.85.152 -sCV -p- --open --min-rate=5000 -oX oscp_c_dc01_tcp-ports.xml

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-09 15:57 JST

Nmap scan report for 10.10.85.152

Host is up (1.6s latency).

Not shown: 65523 filtered tcp ports (no-response)

Some closed ports may be reported as filtered due to --defeat-rst-ratelimit

PORT      STATE SERVICE       VERSION

53/tcp    open  domain        Simple DNS Plus

88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-11-09 06:58:57Z)

135/tcp   open  msrpc         Microsoft Windows RPC

139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn

445/tcp   open  microsoft-ds?

593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0

636/tcp   open  tcpwrapped

3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: oscp.exam0., Site: Default-First-Site-Name)

3269/tcp  open  tcpwrapped

9389/tcp  open  mc-nmf        .NET Message Framing

49669/tcp open  msrpc         Microsoft Windows RPC

49673/tcp open  msrpc         Microsoft Windows RPC

Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:

\| smb2-security-mode:

\|   3:1:1:

\|_    Message signing enabled and required

\| smb2-time:

\|   date: 2025-11-09T06:59:48

\|_  start_date: N/A

\|_nbstat: NetBIOS name: DC01, NetBIOS user: \<unknown>, NetBIOS MAC: 00:50:56:ab:57:ba (VMware)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 189.63 seconds
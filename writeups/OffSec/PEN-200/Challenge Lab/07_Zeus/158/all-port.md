└─$ sudo nmap -p- 192.168.143.158 --min-rate=10000

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-28 14:05 JST

Nmap scan report for 192.168.143.158

Host is up (0.12s latency).

Not shown: 65515 filtered tcp ports (no-response)

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

49666/tcp open  unknown

49673/tcp open  unknown

49674/tcp open  unknown

49677/tcp open  unknown

49696/tcp open  unknown

55289/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 13.77 seconds

![[all-port image 6.png]]
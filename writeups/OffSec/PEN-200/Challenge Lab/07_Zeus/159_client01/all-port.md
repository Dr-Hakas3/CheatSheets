└─$ sudo nmap -p- 192.168.143.159 --min-rate=10000

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-28 12:27 JST

Nmap scan report for 192.168.143.159

Host is up (0.10s latency).

Not shown: 65522 closed tcp ports (reset)

PORT      STATE SERVICE

135/tcp   open  msrpc

139/tcp   open  netbios-ssn

445/tcp   open  microsoft-ds

5040/tcp  open  unknown

5985/tcp  open  wsman

47001/tcp open  winrm

49664/tcp open  unknown

49665/tcp open  unknown

49666/tcp open  unknown

49667/tcp open  unknown

49668/tcp open  unknown

49669/tcp open  unknown

49671/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 13.07 seconds

![[all-port image 7.png]]
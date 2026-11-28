└─$ sudo nmap -p- 192.168.233.143 --min-rate=10000

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-26 14:59 JST

Nmap scan report for 192.168.233.143

Host is up (0.11s latency).

Not shown: 65525 filtered tcp ports (no-response)

PORT     STATE SERVICE

21/tcp   open  ftp

22/tcp   open  ssh

80/tcp   open  http

81/tcp   open  hosts2-ns

443/tcp  open  https

3000/tcp open  ppp

3001/tcp open  nessus

3003/tcp open  cgms

3306/tcp open  mysql

5432/tcp open  postgresql

Nmap done: 1 IP address (1 host up) scanned in 13.70 seconds

![[all-port image 1.png]]
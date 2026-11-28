└─$ sudo nmap -p- 192.168.233.145 --min-rate=10000

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-26 15:22 JST

Nmap scan report for 192.168.233.145

Host is up (0.11s latency).

Not shown: 65528 filtered tcp ports (no-response)

PORT     STATE SERVICE

21/tcp   open  ftp

80/tcp   open  http

135/tcp  open  msrpc

139/tcp  open  netbios-ssn

445/tcp  open  microsoft-ds

1978/tcp open  unisql

3389/tcp open  ms-wbt-server

Nmap done: 1 IP address (1 host up) scanned in 13.76 seconds

![[all-ports image.png]]
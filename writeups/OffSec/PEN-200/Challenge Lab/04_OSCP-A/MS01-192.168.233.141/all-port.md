└─$ sudo nmap -p- 192.168.233.141 --min-rate=10000 -oX 141-p-.xml

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-26 14:19 JST

Warning: 192.168.233.141 giving up on port because retransmission cap hit (10).

Nmap scan report for 192.168.233.141

Host is up (0.11s latency).

Not shown: 65512 closed tcp ports (reset)

PORT      STATE    SERVICE

22/tcp    open     ssh

80/tcp    open     http

81/tcp    open     hosts2-ns

135/tcp   open     msrpc

139/tcp   open     netbios-ssn

445/tcp   open     microsoft-ds

3306/tcp  open     mysql

3307/tcp  open     opsession-prxy

4803/tcp  filtered notateit

5040/tcp  open     unknown

5985/tcp  open     wsman

10032/tcp filtered unknown

47001/tcp open     winrm

49364/tcp filtered unknown

49664/tcp open     unknown

49665/tcp open     unknown

49666/tcp open     unknown

49667/tcp open     unknown

49668/tcp open     unknown

49669/tcp open     unknown

49670/tcp open     unknown

51775/tcp open     unknown

63826/tcp filtered unknown

Nmap done: 1 IP address (1 host up) scanned in 12.15 seconds

![[all-port image.png]]
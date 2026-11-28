\# PortScan

└─$ sudo nmap 10.129.22.244 -p- --min-rate=20000

![[Kobold image.png]]

└─$ sudo nmap kobold.htb -p20,80,443,3552 -sCV --min-rate=20000

![[Kobold image 1.png]]

![[Kobold image 2.png]]

![[Kobold image 3.png]]

\## 443

![[Kobold image 4.png]]

![[Kobold image 5.png]]

\## 3552

![[Kobold image 6.png]]

Arcane v1.13.0

└─$ gobuster vhost -u "https://kobold.htb" -w "/usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt" --append-domain --no-tls-validation

![[Kobold image 7.png]]

mcp.kobold.htb

bin.kobold.htb

\# Exploit

https://sploitus.com/exploit?id=12B0F910-8CC7-5FDB-A55D-2C3510845950

![[Kobold image 8.png]]
┌──(kali㉿kali)-\[~/…/ChallengeLab/OSCP_C/AD/MS01\]

└─$ sudo nmap -Pn -n 10.10.85.154 -sCV -p- --open --min-rate=5000 -oX oscp_c_ms02_tcp-ports.xml

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-09 15:50 JST

Nmap scan report for 10.10.85.154

Host is up (0.49s latency).

Not shown: 65530 filtered tcp ports (no-response)

Some closed ports may be reported as filtered due to --defeat-rst-ratelimit

PORT      STATE SERVICE       VERSION

135/tcp   open  msrpc         Microsoft Windows RPC

139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn

445/tcp   open  microsoft-ds?

49665/tcp open  msrpc         Microsoft Windows RPC

49666/tcp open  msrpc         Microsoft Windows RPC

Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:

\|_nbstat: NetBIOS name: MS02, NetBIOS user: \<unknown>, NetBIOS MAC: 00:50:56:ab:8d:01 (VMware)

\| smb2-time:

\|   date: 2025-11-09T06:52:30

\|_  start_date: N/A

\| smb2-security-mode:

\|   3:1:1:

\|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 130.86 seconds

![[all-ports image 4.png]]
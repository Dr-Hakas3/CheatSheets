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
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.56.22
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-30 10:02 +0900
Nmap scan report for 192.168.56.22
Host is up (0.00082s latency).
Not shown: 62052 closed tcp ports (reset), 3479 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE     VERSION
135/tcp   open  msrpc       Microsoft Windows RPC
139/tcp   open  netbios-ssn Microsoft Windows netbios-ssn
49664/tcp open  msrpc       Microsoft Windows RPC
49665/tcp open  msrpc       Microsoft Windows RPC
MAC Address: 08:00:27:96:75:30 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Microsoft Windows 2019
OS CPE: cpe:/o:microsoft:windows_server_2019
OS details: Microsoft Windows Server 2019
Network Distance: 1 hop
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: ERROR: Script execution failed (use -d to debug)
|_nbstat: NetBIOS name: nil, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:96:75:30 (Oracle VirtualBox virtual NIC)
|_smb2-security-mode: SMB: Couldn't find a NetBIOS name that works for the server. Sorry!

TRACEROUTE
HOP RTT     ADDRESS
1   0.82 ms 192.168.56.22

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 75.87 seconds

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

---

# Initial Access

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
---

# Privilege Escalation

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


<details markdown="1">
<summary>Walkthrough</summary>

```zsh

```

</details>
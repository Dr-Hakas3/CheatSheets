---
title: empire-breakout
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Empire-breakout]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.231.238 --min-rate=5000
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-22 04:00 +0900
Nmap scan report for 192.168.231.238
Host is up (0.089s latency).
Not shown: 64474 closed tcp ports (reset), 1058 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
80/tcp    open  http
10000/tcp open  snet-sensor-mgmt
20000/tcp open  dnp

Nmap done: 1 IP address (1 host up) scanned in 19.54 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Empire-breakout]
└─$ sudo nmap -Pn -p80,10000,20000 -sSCV -A -oN full_tcp-scan.txt --open 192.168.231.238
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-22 04:01 +0900
Nmap scan report for 192.168.231.238
Host is up (0.083s latency).

PORT      STATE SERVICE               VERSION
80/tcp    open  http                  Apache httpd 2.4.51 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.51 (Debian)
10000/tcp open  ssl/snet-sensor-mgmt?
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=*/organizationName=Webmin Webserver on breakout
| Not valid before: 2021-10-19T17:48:40
|_Not valid after:  2026-10-18T17:48:40
20000/tcp open  http                  MiniServ 1.830 (Webmin httpd)
|_http-title: 200 &mdash; Document follows
|_http-server-header: MiniServ/1.830
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   80.06 ms 192.168.45.1
2   79.83 ms 192.168.45.254
3   80.07 ms 192.168.251.1
4   80.11 ms 192.168.231.238

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.45 seconds
```

# HTTP

## 80


![](../../../assets/images/Pasted%20image%2020260522052645.png)

```zsh
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>++++++++++++++++.++++.>>+++++++++++++++++.----.<++++++++++.-----------.>-----------.++++.<<+.>-.--------.++++++++++++++++++++.<------------.>>---------.<<++++++.++++++.
```

## decode

![](../../../assets/images/Pasted%20image%2020260522055131.png)

```zsh
.2uqPEfj3D<P'a-3
```

## 20000

![](../../../assets/images/Pasted%20image%2020260522041329.png)

![](../../../assets/images/Pasted%20image%2020260523044921.png)

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
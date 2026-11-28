└─$ sudo nmap -p21,22,80 -A 192.168.233.144 --min-rate=10000

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-26 15:12 JST

Nmap scan report for 192.168.233.144

Host is up (0.11s latency).

PORT   STATE SERVICE VERSION

21/tcp open  ftp     vsftpd 3.0.5

22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)

\| ssh-hostkey:

\|   256 fb:ea:e1:18:2f:1d:7b:5e:75:96:5a:98:df:3d:17:e4 (ECDSA)

\|_  256 66:f4:54:42:1f:25:16:d7:f3:eb:f7:44:9f:5a:1a:0b (ED25519)

80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))

\|_http-title: Home

\| http-git:

\|   192.168.233.144:80/.git/

\|     Git repository found!

\|     Repository description: Unnamed repository; edit this file 'description' to name the...

\|     Last commit message: Security Update

\|     Remotes:

\|_      https://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@github.com/PWK-Challenge-Lab/dev.git

\|_http-generator: Nicepage 4.21.12, nicepage.com

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Device type: general purpose

Running: Linux 4.X|5.X

OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5

OS details: Linux 4.15 - 5.19, Linux 5.0 - 5.14

Network Distance: 4 hops

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)

HOP RTT       ADDRESS

1   146.29 ms 192.168.45.1

2   146.37 ms 192.168.45.254

3   146.39 ms 192.168.251.1

4   146.48 ms 192.168.233.144

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 14.81 seconds

![[all-port image 2.png]]

└─$ ssh stuart@192.168.233.144

The authenticity of host '192.168.233.144 (192.168.233.144)' can't be established.

ED25519 key fingerprint is SHA256:NQ0P6b7BgHDdEToc64di95hvEzS2pdZ7E02r4ZBkBYM.

This key is not known by any other names.

Are you sure you want to continue connecting (yes/no/\[fingerprint\])? yes

Warning: Permanently added '192.168.233.144' (ED25519) to the list of known hosts.

stuart@192.168.233.144's password:

Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-53-generic x86_64)

\* Documentation:  https://help.ubuntu.com

\* Management:     https://landscape.canonical.com

\* Support:        https://ubuntu.com/advantage

System information as of Wed Aug 27 01:26:57 PM UTC 2025

System load:  0.6396484375       Processes:               205

Usage of /:   41.2% of 18.53GB   Users logged in:         0

Memory usage: 17%                IPv4 address for ens160: 192.168.233.144

Swap usage:   0%

\* Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s

just raised the bar for easy, resilient and secure K8s cluster deployment.

https://ubuntu.com/engage/secure-kubernetes-at-the-edge

0 updates can be applied immediately.

The list of available updates is more than a week old.

To check for new updates run: sudo apt update

Last login: Mon Oct 31 14:48:02 2022 from 192.168.118.5

stuart@oscp:~$ ls

local.txt

stuart@oscp:~$ cat local.txt

477e6b02633c4dc823c73b8a23425ad8

stuart@oscp:~$ ip a

1: lo: \<LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000

link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

inet 127.0.0.1/8 scope host lo

valid_lft forever preferred_lft forever

3: ens160: \<BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000

link/ether 00:50:56:ab:27:00 brd ff:ff:ff:ff:ff:ff

altname enp3s0

inet 192.168.233.144/24 brd 192.168.233.255 scope global ens160

valid_lft forever preferred_lft forever

![[all-port image 3.png]]

![[all-port image 4.png]]

![[all-port image 5.png]]
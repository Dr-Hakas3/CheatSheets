┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Charlie\]

└─$ sudo nmap -Pn -n 192.168.202.157 -sCV -p- --open

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-10 22:32 JST

Nmap scan report for 192.168.202.157

Host is up (0.084s latency).

Not shown: 65531 closed tcp ports (reset)

PORT      STATE SERVICE VERSION

21/tcp    open  ftp     vsftpd 3.0.5

\| ftp-anon: Anonymous FTP login allowed (FTP code 230)

\|_drwxr-xr-x    2 114      120          4096 Nov 02  2022 backup

\| ftp-syst:

\|   STAT:

\| FTP server status:

\|      Connected to ::ffff:192.168.45.186

\|      Logged in as ftp

\|      TYPE: ASCII

\|      No session bandwidth limit

\|      Session timeout in seconds is 300

\|      Control connection is plain text

\|      Data connections will be plain text

\|      At session startup, client count was 1

\|      vsFTPd 3.0.5 - secure, fast, stable

\|_End of status

22/tcp    open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)

\| ssh-hostkey:

\|   256 0e:ad:d7:de:60:2b:49:ef:42:3b:1e:76:9c:77:33:85 (ECDSA)

\|_  256 99:b5:48:fb:77:df:18:b0:1d:ad:e0:92:f3:e1:26:0d (ED25519)

80/tcp    open  http    Apache httpd 2.4.52 ((Ubuntu))

\|_http-server-header: Apache/2.4.52 (Ubuntu)

\|_http-title: Apache2 Ubuntu Default Page: It works

20000/tcp open  http    MiniServ 1.820 (Webmin httpd)

\|_http-title: Site doesn't have a title (text/html; Charset=utf-8).

\|_http-server-header: MiniServ/1.820

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 47.56 seconds

![[all-ports image 5.png]]
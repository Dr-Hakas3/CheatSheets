┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha\]

└─$ sudo nmap -Pn -n 192.168.202.155 -sCV -p- --open -oX pascha_tcp-ports.xml

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-10 23:42 JST

Nmap scan report for 192.168.202.155

Host is up (0.083s latency).

Not shown: 65531 filtered tcp ports (no-response)

Some closed ports may be reported as filtered due to --defeat-rst-ratelimit

PORT      STATE SERVICE VERSION

80/tcp    open  http    Microsoft IIS httpd 10.0

\|_http-title: IIS Windows

\|_http-server-header: Microsoft-IIS/10.0

\| http-methods:

\|_  Potentially risky methods: TRACE

9099/tcp  open  unknown

\| fingerprint-strings:

\|   FourOhFourRequest, GetRequest:

\|     HTTP/1.0 200 OK

\|     Server: Mobile Mouse Server

\|     Content-Type: text/html

\|     Content-Length: 321

\|_    \<HTML>\<HEAD>\<TITLE>Success!\</TITLE>\<meta name="viewport" content="width=device-width,user-scalable=no" />\</HEAD>\<BODY BGCOLOR=#000000>\<br>\<br>\<p style="font:12pt arial,geneva,sans-serif; text-align:center; color:green; font-weight:bold;" >The server running on "OSCP" was able to receive your request.\</p>\</BODY>\</HTML>

9999/tcp  open  abyss?

35913/tcp open  unknown

1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :

SF-Port9099-TCP:V=7.95%I=7%D=11/10%Time=6911FA8F%P=x86_64-pc-linux-gnu%r(G

SF:etRequest,1A2,"HTTP/1\.0\x20200\x20OK\x20\r\nServer:\x20Mobile\x20Mouse

SF:\x20Server\x20\r\nContent-Type:\x20text/html\x20\r\nContent-Length:\x20

SF:321\r\n\r\n\<HTML>\<HEAD>\<TITLE>Success!\</TITLE>\<meta\x20name=\"viewport\

SF:"\x20content=\"width=device-width,user-scalable=no\"\x20/>\</HEAD>\<BODY\

SF:x20BGCOLOR=#000000>\<br>\<br>\<p\x20style=\"font:12pt\x20arial,geneva,sans

SF:-serif;\x20text-align:center;\x20color:green;\x20font-weight:bold;\"\x2

SF:0>The\x20server\x20running\x20on\x20\"OSCP\"\x20was\x20able\x20to\x20re

SF:ceive\x20your\x20request\.\</p>\</BODY>\</HTML>\r\n")%r(FourOhFourRequest,

SF:1A2,"HTTP/1\.0\x20200\x20OK\x20\r\nServer:\x20Mobile\x20Mouse\x20Server

SF:\x20\r\nContent-Type:\x20text/html\x20\r\nContent-Length:\x20321\r\n\r\

SF:n\<HTML>\<HEAD>\<TITLE>Success!\</TITLE>\<meta\x20name=\"viewport\"\x20conte

SF:nt=\"width=device-width,user-scalable=no\"\x20/>\</HEAD>\<BODY\x20BGCOLOR

SF:=#000000>\<br>\<br>\<p\x20style=\"font:12pt\x20arial,geneva,sans-serif;\x2

SF:0text-align:center;\x20color:green;\x20font-weight:bold;\"\x20>The\x20s

SF:erver\x20running\x20on\x20\"OSCP\"\x20was\x20able\x20to\x20receive\x20y

SF:our\x20request\.\</p>\</BODY>\</HTML>\r\n");

Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 351.83 seconds
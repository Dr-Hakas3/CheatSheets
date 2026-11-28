└─# nmap -p- -T4 192.168.133.129

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-17 01:17 JST

Nmap scan report for 192.168.133.129

Host is up (0.0038s latency).

Not shown: 65529 closed tcp ports (reset)

PORT      STATE SERVICE

22/tcp    open  ssh

80/tcp    open  http

111/tcp   open  rpcbind

139/tcp   open  netbios-ssn

443/tcp   open  https

32768/tcp open  filenet-tms

MAC Address: 00:0C:29:8A:57:86 (VMware)

Nmap done: 1 IP address (1 host up) scanned in 27.15 seconds

![[Service Enumration image 8.png]]

└─# nmap -Pn -A -p80 -T4 192.168.133.129

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-17 01:32 JST

Nmap scan report for 192.168.133.129

Host is up (0.0011s latency).

PORT   STATE SERVICE VERSION

80/tcp open  http    Apache httpd 1.3.20 ((Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b)

\| http-methods:

\|_  Potentially risky methods: TRACE

\|_http-title: Test Page for the Apache Web Server on Red Hat Linux

\|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b

MAC Address: 00:0C:29:8A:57:86 (VMware)

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Device type: general purpose

Running: Linux 2.4.X

OS CPE: cpe:/o:linux:linux_kernel:2.4

OS details: Linux 2.4.9 - 2.4.18 (likely embedded)

Network Distance: 1 hop

TRACEROUTE

HOP RTT     ADDRESS

1   1.07 ms 192.168.133.129

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 20.48 seconds

![[Service Enumration image 10.png]]

└─# nikto -h 192.168.133.129

\- Nikto v2.5.0

\---------------------------------------------------------------------------

\+ Target IP:          192.168.133.129

\+ Target Hostname:    192.168.133.129

\+ Target Port:        80

\+ Start Time:         2024-03-17 01:34:41 (GMT9)

\---------------------------------------------------------------------------

\+ Server: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b

\+ /: Server may leak inodes via ETags, header found with file /, inode: 34821, size: 2890, mtime: Thu Sep  6 12:12:46 2001. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418

\+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options

\+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/

\+ /: Apache is vulnerable to XSS via the Expect header. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-3918

\+ mod_ssl/2.8.4 appears to be outdated (current is at least 2.9.6) (may depend on server version).

\+ OpenSSL/0.9.6b appears to be outdated (current is at least 3.0.7). OpenSSL 1.1.1s is current for the 1.x branch and will be supported until Nov 11 2023.

\+ Apache/1.3.20 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.

\+ OPTIONS: Allowed HTTP Methods: GET, HEAD, OPTIONS, TRACE .

\+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing

\+ Apache/1.3.20 - Apache 1.x up 1.2.34 are vulnerable to a remote DoS and possible code execution.

\+ Apache/1.3.20 - Apache 1.3 below 1.3.27 are vulnerable to a local buffer overflow which allows attackers to kill any process on the system.

\+ Apache/1.3.20 - Apache 1.3 below 1.3.29 are vulnerable to overflows in mod_rewrite and mod_cgi.

\+ mod_ssl/2.8.4 - mod_ssl 2.8.7 and lower are vulnerable to a remote buffer overflow which may allow a remote shell.

\+ ///etc/hosts: The server install allows reading of any system file by adding an extra '/' to the URL.

\+ /usage/: Webalizer may be installed. Versions lower than 2.01-09 vulnerable to Cross Site Scripting (XSS). See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0835

\+ /manual/: Directory indexing found.

\+ /manual/: Web server manual found.

\+ /icons/: Directory indexing found.

\+ ERROR: Error limit (20) reached for host, giving up. Last error: error reading HTTP response

\+ Scan terminated: 20 error(s) and 18 item(s) reported on remote host

\+ End Time:           2024-03-17 01:42:02 (GMT9) (441 seconds)

\---------------------------------------------------------------------------

\+ 1 host(s) tested

![[Service Enumration image 11.png]]

└─# gobuster dir -u http://192.168.133.129 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .zip .txt .html

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:                     http://192.168.133.129

\[+\] Method:                  GET

\[+\] Threads:                 10

\[+\] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

\[+\] Negative Status codes:   404

\[+\] User Agent:              gobuster/3.6

\[+\] Extensions:              zip

\[+\] Timeout:                 10s

\===============================================================

Starting gobuster in directory enumeration mode

\===============================================================

/manual               (Status: 301) \[Size: 294\] \[--> http://127.0.0.1/manual/\]

/usage                (Status: 301) \[Size: 293\] \[--> http://127.0.0.1/usage/\]

/mrtg                 (Status: 301) \[Size: 292\] \[--> http://127.0.0.1/mrtg/\]

Progress: 441120 / 441122 (100.00%)

\===============================================================

Finished

\===============================================================

![[Service Enumration image 12.png]]

└─# dirb http://192.168.133.129

\-----------------

DIRB v2.22

By The Dark Raver

\-----------------

START_TIME: Sun Mar 17 01:27:37 2024

URL_BASE: http://192.168.133.129/

WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

\-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://192.168.133.129/ ----

\+ http://192.168.133.129/~operator (CODE:403|SIZE:273)

\+ http://192.168.133.129/~root (CODE:403|SIZE:269)

\+ http://192.168.133.129/cgi-bin/ (CODE:403|SIZE:272)

\+ http://192.168.133.129/index.html (CODE:200|SIZE:2890)

==> DIRECTORY: http://192.168.133.129/manual/

==> DIRECTORY: http://192.168.133.129/mrtg/

==> DIRECTORY: http://192.168.133.129/usage/

---- Entering directory: http://192.168.133.129/manual/ ----

(!) WARNING: Directory IS LISTABLE. No need to scan it.

(Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.133.129/mrtg/ ----

\+ http://192.168.133.129/mrtg/index.html (CODE:200|SIZE:17318)

---- Entering directory: http://192.168.133.129/usage/ ----

\+ http://192.168.133.129/usage/index.html (CODE:200|SIZE:3704)

\-----------------

END_TIME: Sun Mar 17 01:28:23 2024

DOWNLOADED: 13836 - FOUND: 6

![[Service Enumration image 13.png]]

http://192.168.133.129/

![[Service Enumration image 9.png]]

└─# smbclient -L \\192.168.133.129

Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set

Anonymous login successful

Password for \[WORKGROUP\root\]:

Sharename       Type      Comment

---------       ----      -------

IPC$            IPC       IPC Service (Samba Server)

ADMIN$          IPC       IPC Service (Samba Server)

Reconnecting with SMB1 for workgroup listing.

Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set

Anonymous login successful

Server               Comment

---------            -------

KIOPTRIX             Samba Server

Workgroup            Master

---------            -------

MYGROUP              KIOPTRIX

![[Service Enumration image 14.png]]
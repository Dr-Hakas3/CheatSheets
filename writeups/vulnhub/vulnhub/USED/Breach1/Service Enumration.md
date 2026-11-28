└─# nmap -sn -T4 192.168.110.140

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-13 08:44 JST

Nmap scan report for 192.168.110.140

Host is up (0.00078s latency).

MAC Address: 08:00:27:33:B6:63 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 11.22 seconds

![[Service Enumration image.png]]

I run nmap and found all ports open.

http://192.168.110.140

Initech was breached and the board of directors voted to bring in their internal Initech Cyber Consulting, LLP division to assist. Given the high profile nature of the breach and nearly catastrophic losses, there have been many subsequent attempts against the company. Initech has tasked their TOP consultants, led by Bill Lumbergh, CISSP and Peter Gibbons, C|EH, SEC+, NET+, A+ to contain and perform analysis on the breach.

Little did the company realize that the breach was not the work of skilled hackers, but a parting gift from a disgruntled former employee on his way out. The TOP consultants have been hard at work containing the breach. However, their own work ethics and the mess left behind may be the company's downfall.

Initechは侵害され、取締役会は社内のInitech Cyber Consulting, LLP部門に支援を依頼することを決議しました。この侵害の注目度の高さと、ほぼ壊滅的な損失を考えると、その後、同社に対して多くの試みが行われてきました。Initechは、CISSPのBill Lumbergh氏とC|EH、SEC+、NET+、A+のPeter Gibbons氏が率いるTOPコンサルタントに、侵害の封じ込めと分析を依頼しました。

同社は、この侵害が熟練したハッカーの仕業ではなく、不満を抱いた元従業員からの別れの贈り物であることにほとんど気づいていませんでした。TOPのコンサルタントは、侵害の封じ込めに懸命に取り組んできました。しかし、彼ら自身の労働倫理と残された混乱は、会社の没落かもしれません。

└─# gobuster dir -u 192.168.110.140 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x php,html,txt

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:                     http://192.168.110.140

\[+\] Method:                  GET

\[+\] Threads:                 10

\[+\] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt

\[+\] Negative Status codes:   404

\[+\] User Agent:              gobuster/3.6

\[+\] Extensions:              txt,php,html

\[+\] Timeout:                 10s

\===============================================================

Starting gobuster in directory enumeration mode

\===============================================================

/.php                 (Status: 403) \[Size: 286\]

/.html                (Status: 403) \[Size: 287\]

/images               (Status: 301) \[Size: 318\] \[--> http://192.168.110.140/images/\]

/index.html           (Status: 200) \[Size: 1098\]

/breach.html          (Status: 200) \[Size: 284\]

/.php                 (Status: 403) \[Size: 286\]

/.html                (Status: 403) \[Size: 287\]

/server-status        (Status: 403) \[Size: 295\]

Progress: 882240 / 882244 (100.00%)

\===============================================================

Finished

\===============================================================

![[Service Enumration image 1.png]]

└─# nikto -h 192.168.110.140

\- Nikto v2.5.0

\---------------------------------------------------------------------------

\+ Target IP:          192.168.110.140

\+ Target Hostname:    192.168.110.140

\+ Target Port:        80

\+ Start Time:         2024-03-12 16:28:58 (GMT9)

\---------------------------------------------------------------------------

\+ Server: Apache/2.4.7 (Ubuntu)

\+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options

\+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/

\+ No CGI Directories found (use '-C all' to force check all possible dirs)

\+ /images: IP address found in the 'location' header. The IP is "127.0.1.1". See: https://portswigger.net/kb/issues/00600300_private-ip-addresses-disclosed

\+ /images: The web server may reveal its internal or real IP in the Location header via a request to with HTTP/1.0. The value is "127.0.1.1". See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0649

\+ /: Server may leak inodes via ETags, header found with file /, inode: 44a, size: 534a04f49139d, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418

\+ Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.

\+ OPTIONS: Allowed HTTP Methods: OPTIONS, GET, HEAD, POST .

\+ /images/: Directory indexing found.

\+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/

\+ /.gitignore: .gitignore file found. It is possible to grasp the directory structure.

\+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.

\+ 8102 requests: 0 error(s) and 11 item(s) reported on remote host

\+ End Time:           2024-03-12 16:29:36 (GMT9) (38 seconds)

\---------------------------------------------------------------------------

\+ 1 host(s) tested

![[Service Enumration image 2.png]]

Browser Access

![[Service Enumration image 3.png]]

view-source:http://192.168.110.140/

![[Service Enumration image 4.png]]

Y0dkcFltSnZibk02WkdGdGJtbDBabVZsYkNSbmIyOWtkRzlpWldGbllXNW5KSFJo

base64 decode

└─# echo Y0dkcFltSnZibk02WkdGdGJtbDBabVZsYkNSbmIyOWtkRzlpWldGbllXNW5KSFJo | base64 -d | base64 -d

pgibbons:damnitfeel$goodtobeagang$ta

![[Service Enumration image 5.png]]

http://192.168.110.140/initech.html

![[Service Enumration image 6.png]]

http://192.168.110.140/breach.html

![[Service Enumration image 7.png]]
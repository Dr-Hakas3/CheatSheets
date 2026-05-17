| OS | Linux |
| Difficulty | Easy |

# Recon
![](../../../assets/images/Pasted%20image%2020260508154749.png)

![](../../../assets/images/Pasted%20image%2020260508154806.png)

![](../../../assets/images/Pasted%20image%2020260508154813.png)

- 80
- 3306
- 33060

http://192.168.133.194

![](../../../assets/images/Pasted%20image%2020260508154842.png)

## Wappalyxer

![](../../../assets/images/Pasted%20image%2020260508154902.png)

# Initial Access

# Enum Directory
```zsh
feroxbuster -u http://192.168.133.194 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,js -b 403,404
```
![](../../../assets/images/Pasted%20image%2020260508154936.png)
*main.js*

![](../../../assets/images/Pasted%20image%2020260508154942.png)
*/seeddms51x/seeddms-5.1.22/*

# Browser Access
http://192.168.133.194/seeddms51x/seeddms-5.1.22/
Redirect ↓
http://192.168.133.194/seeddms51x/seeddms-5.1.22/out/out.Login.php?referuri=%2Fseeddms51x%2Fseeddms-5.1.22%2Fout%2Fout.ViewFolder.php
![](../../../assets/images/Pasted%20image%2020260508154952.png)

# Enum /seeddms51x/seeddms-5.1.22/ Directory
# Enum /seeddms51x/ Directory
# Enum /seeddms51x/conf/ Directory
```zsh
feroxbuster -u http://192.168.133.194/seeddms51x/conf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,js,xml -b 403,404
```
![](../../../assets/images/Pasted%20image%2020260508155001.png)
http://192.168.133.194/seeddms51x/conf/settings.xml

# Browser Access
![](../../../assets/images/Pasted%20image%2020260508155010.png)
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
![](../../../assets/images/Pasted%20image%2020260508155023.png)

![](../../../assets/images/Pasted%20image%2020260508155030.png)

![](../../../assets/images/Pasted%20image%2020260508155035.png)
- saket
- saurav
- Saket@#$1337

![](../../../assets/images/Pasted%20image%2020260508155042.png)
f9ef2c539bad8a6d2f3432b6d49ab51a

![](../../../assets/images/Pasted%20image%2020260508155049.png)

![](../../../assets/images/Pasted%20image%2020260508155054.png)

```zsh
sudo john --format=Raw-MD5 hash.txt /usr/share/wordlists/rockyou.txt
```
*I can't crack hash.*

# Change admin password.
```zsh
update tblUsers set pwd='21232f297a57a5a743894a0e4a801fc3' where login='admin';
```
![](../../../assets/images/Pasted%20image%2020260508155103.png)


![](../../../assets/images/Pasted%20image%2020260508155112.png)
*Login success.*

---
# ReverseShell
## Upload Reverseshell php file.

![](../../../assets/images/Pasted%20image%2020260508155122.png)

![](../../../assets/images/Pasted%20image%2020260508155128.png)

![](../../../assets/images/Pasted%20image%2020260508155133.png)
*DocumentID=4*

![](../../../assets/images/Pasted%20image%2020260508155139.png)
*Upload File Default Path is  /data/1048576/"document_id"/1.php*

http://192.168.133.194/seeddms51x/data/1048576/4/1.php

![](../../../assets/images/Pasted%20image%2020260508155144.png)


# Privilege Escalation

- id
- uname -ar
- sudo -l
- current directory
- user directory
- which python3
- env
![](../../../assets/images/Pasted%20image%2020260508155952.png)

![](../../../assets/images/Pasted%20image%2020260508160000.png)

## su saket
*Use password in DB.*
![](../../../assets/images/Pasted%20image%2020260508160008.png)

# sudo -l
# sudo su
![](../../../assets/images/Pasted%20image%2020260508160050.png)
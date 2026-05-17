# Portscan
```zsh
nmap -Pn -p80 192.168.11.21 --min-rate=5000 -sVC -A
```
![](../../../../Assets/Images/Pasted%20image%2020260503073220.png)

# Browser Access
http://192.168.11.21
![](../../../../Assets/Images/Pasted%20image%2020260503073400.png)
![](../../../../Assets/Images/Pasted%20image%2020260503073452.png)
- CMS Made Simple 2.2.15
# Enum Directory
```zsh
gobuster dir -u http://192.168.11.21 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip,asp,aspx,xml -b 403,404
```
![](../../../../Assets/Images/Pasted%20image%2020260503075156.png)
- index.php            (Status: 200) [Size: 8358]
- modules              (Status: 301) [Size: 237] [--> http://192.168.11.21/modules/]
- uploads              (Status: 301) [Size: 237] [--> http://192.168.11.21/uploads/]
- doc                  (Status: 301) [Size: 233] [--> http://192.168.11.21/doc/]
- admin                (Status: 301) [Size: 235] [--> http://192.168.11.21/admin/]
![](../../../../Assets/Images/Pasted%20image%2020260503143210.png)
- assets               (Status: 301) [Size: 236] [--> http://192.168.11.21/assets/]
- test.php             (Status: 200) [Size: 80] ![](../../../../Assets/Images/Pasted%20image%2020260503143131.png)
size 80

- lib                  (Status: 301) [Size: 233] [--> http://192.168.11.21/lib/]
- config.php           (Status: 200) [Size: 0]
- robots.txt           (Status: 200) [Size: 79]
![](../../../../Assets/Images/Pasted%20image%2020260503143037.png)
- error.html           (Status: 200) [Size: 80]
- tmp                  (Status: 301) [Size: 233] [--> http://192.168.11.21/tmp/]
- missing.html         (Status: 200) [Size: 168]
![](../../../../Assets/Images/Pasted%20image%2020260503161022.png)
patrick

- phpinfo.php          (Status: 200) [Size: 17]

# fuzzing
```zsh
ffuf -u 'http://192.168.11.21/test.php?FUZZ=test' -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs 80
```
![](../../../../Assets/Images/Pasted%20image%2020260503171153.png)
file

# LFI

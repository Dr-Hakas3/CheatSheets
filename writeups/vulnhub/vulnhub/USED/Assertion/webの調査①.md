・サービスの詳細

nmap -sV -sC -A -O -p80 192.168.0.104

![[webの調査① image 3.png]]

・脆弱性調査

nmap --script vuln -A -p80  192.168.0.104

![[webの調査① image 4.png]]

・脆弱性調査（nikto)

nikto -h 192.168.0.104

![[webの調査① image 5.png]]

・ディレクトリ探索

gobuster dir -u http://192.168.0.104 -w /usr/share/wordlists/dirb/common.txt

![[webの調査① image 6.png]]
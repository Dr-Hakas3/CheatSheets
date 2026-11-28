nmap -p80 -sV -sC -A 192.168.15.133

![[Webの調査 image.png]]

〇脆弱性

nikto -h 192.168.15.133

〇ディレクトリ

feroxbuster -u http://192.168.15.133 -w /usr/share/dirb/wordlists/common.txt -g

![[Webの調査 image 1.png]]

〇ブラウザアクセス

![[Webの調査 image 2.png]]
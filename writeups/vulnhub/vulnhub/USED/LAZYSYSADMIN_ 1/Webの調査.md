nmap -Pn -sV -sC -v -p80 192.168.15.136

![[Webの調査 image 20.png]]

feroxbuster -u http://192.168.15.136 -w /usr/share/wordlists/dirb/big.txt -g -x php,txt

![[Webの調査 image 21.png]]

![[Webの調査 image 22.png]]

![[Webの調査 image 23.png]]

I$8b4f5a97-4757-4157-afe8-9a1a8

/wordpress

![[Webの調査 image 24.png]]

![[Webの調査 image 67.png]]

togie
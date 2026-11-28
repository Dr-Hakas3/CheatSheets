nmap -p80 -Pn -sV -sC -A 192.168.0.109

![[Web(80)の調査 image.png]]

nikto -h 192.168.0.109

特になし

ブラウザ内のキーワードを集める

cewl -w keyword.txt http://192.168.0.109

![[Web(80)の調査 image 1.png]]

ディレクトリの列挙

１　通常

gobuster dir -u http://192.168.0.109:80 -w /usr/share/dirb/wordlists/common.txt -x php,html,txt

![[Web(80)の調査 image 2.png]]

/assets/

![[Web(80)の調査 image 9.png]]

２　キーワード

gobuster dir -u http://192.168.0.109:80 -w keyword.txt -x php,html,txt

![[Web(80)の調査 image 10.png]]

/Matrix/

ブラウザにMatrixと入れてみる

![[Web(80)の調査 image 11.png]]

gzに見せかけたテキストファイルを発見

secret.gzの 中身

![[Web(80)の調査 image 12.png]]

admin:76a2173be6393254e72ffa4d6df1030a

76a2173be6393254e72ffa4d6df1030a

![[Web(80)の調査 image 13.png]]

passwd
nmap -p80 -sC -sC -v 192.168.15.135

![[Web（80）の調査 image.png]]

ディレクトリ列挙

gobuster dir -u http://192.168.15.135 -w /usr/share/wordlists/dirb/common.txt

![[Web（80）の調査 image 1.png]]

feroxbuster -u http://192.168.15.135 -w /usr/share/wordlists/dirb/big.txt -g

ファイル列挙

dirb http://192.168.15.135/ /usr/share/wordlists/dirb/big.txt -X .html,.php,.txt

![[Web（80）の調査 image 2.png]]

nikto -h 192.168.15.135

とくになし

ブラウザアクセス

![[Web（80）の調査 image 3.png]]

![[Web（80）の調査 image 4.png]]

![[Web（80）の調査 image 5.png]]

![[Web（80）の調査 image 6.png]]

curl --head -X OPTIONS http://192.168.15.135/cms/core/admin/pages/

![[Web（80）の調査 image 7.png]]

/search.php

![[Web（80）の調査 image 8.png]]

SQLインジェクション

Burpを利用して通信内容を含むファイルの作成

![[Web（80）の調査 image 9.png]]

sqlmap -r sql.txt --dbs --dbms mysql --threads 10 --level 3

とくに得られず

![[Web（80）の調査 image 10.png]]

a.txt

![[Web（80）の調査 image 11.png]]

/adminer.php

![[Web（80）の調査 image 12.png]]

mantissuser

password@123AS

![[Web（80）の調査 image 13.png]]

table名からユーザを列挙

![[Web（80）の調査 image 14.png]]

![[Web（80）の調査 image 15.png]]

1         administrator	XiBejMub	root@localhost	3492f8fe2cb409e387ddb0521c999c38 	OHysKA8CiRbsM1LW0ZoWIF0gP6EGOwJovGZvGgJfDHkrPmaf2Y7qOVecYBxXDCri

2	tre	Tr3@123456A!	tre@localhost 	64c4685f8da5c2225de7890c1bad0d7f	bp9uP3SY4tyKMFHSytb2RyecV5fPrsvGjb4sLboLkoyodEPn0NbZID9GhRURGAvf
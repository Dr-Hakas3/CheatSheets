〇詳細調査

・バージョン確認

droopescan scan drupal -u http://dc-1

※コマンドがない場合はインストール

apt install python3-pip

pip install droopescan

![[webサービスの調査 image.png]]

![[webサービスの調査 image 1.png]]

バージョンは7.xであることを確認

・robots.txtの確認

すべてDisallow

![[webサービスの調査 image 2.png]]

・ヘッダーでも確認

curl -I http://dc-1

HTTP/1.1 200 OK

Date: Wed, 14 Feb 2024 09:35:55 GMT

Server: Apache/2.2.22 (Debian)

X-Powered-By: PHP/5.4.45-0+deb7u14

Expires: Sun, 19 Nov 1978 05:00:00 GMT

Last-Modified: Wed, 14 Feb 2024 09:35:55 +0000

Cache-Control: no-cache, must-revalidate, post-check=0, pre-check=0

ETag: "1707903355"

Content-Language: en

X-Generator: Drupal 7 (http://drupal.org)

Vary: Accept-Encoding

Content-Type: text/html; charset=utf-8

![[webサービスの調査 image 3.png]]
---
title: Web Sv
parent: Servers
grand_parent: Green Team
---
1. 全体構成

WordPress（WordPress）：

Webサーバ：Nginx or Apache HTTP Server
DB：MariaDB（または MySQL）
PHP：PHP-FPM（推奨）
2. パッケージインストール（Ubuntu/Debian）
Nginx構成（推奨：軽量・高速）

```
sudo apt update
sudo apt install nginx mariadb-server php-fpm php-mysql unzip wget -y
```

2. MariaDB初期設定

```
mysql -u root -p
sudo mysql_secure_installation
```

DB作成：

```
CREATE DATABASE wordpress;
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'localhost';
FLUSH PRIVILEGES;
exit;
```

4. WordPressダウンロード

```
cd /var/www/
sudo wget https://wordpress.org/latest.tar.gz
sudo tar -xvzf latest.tar.gz
sudo mv wordpress /var/www/html/
```

権限：

```
sudo chown -R www-data:www-data /var/www/html/wordpress
sudo chmod -R 755 /var/www/html/wordpress
```

5. Nginx設定

```
sudo vim /etc/nginx/sites-available/wordpress
```

例：

```
server {
    listen 80;
    server_name your-domain-or-ip;

    root /var/www/html/wordpress;
    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
    }
}
```

有効化：

```
sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

6. WordPress設定ファイル

```
cd /var/www/html/wordpress
sudo cp wp-config-sample.php wp-config.php
sudo vim wp-config.php
```

DB情報を書き換え：

```
define('DB_NAME', 'wordpress');
define('DB_USER', 'wpuser');
define('DB_PASSWORD', 'strongpassword');
define('DB_HOST', 'localhost');
```

7. ブラウザアクセス
http://サーバIP

→ 初期セットアップ画面が出れば成功

8. よくあるハマりポイント
① 502 Bad Gateway

→ PHP-FPMソケットが違う

ls /run/php/
② 真っ白画面

→ PHP未インストール or 権限ミス

③ DB接続エラー

→ wp-config.phpの値ミス

自己署名証明書でWordPressをHTTPS化する手順だけを、最短で実務レベルでまとめます（Nginx前提）。

※ブラウザ警告は必ず出ます（これは正常動作）

1. 自己署名証明書の作成

まず証明書と秘密鍵を作成します。

```
sudo mkdir -p /etc/ssl/wordpress
cd /etc/ssl/wordpress
sudo openssl req -x509 -nodes -days 3650 \
-newkey rsa:2048 \
-keyout wordpress.key \
-out wordpress.crt
```
入力項目について

適当でも動きますが：

Country: JP
Common Name: サーバIP or ドメイン（重要）
例：192.168.1.10 or wordpress.local

2. Nginx設定をHTTPS対応に変更

設定ファイル編集：

```
sudo vim /etc/nginx/sites-available/wordpress
```

HTTPS版サーバブロック

```bash
server {
    listen 443 ssl;
    server_name your-domain-or-ip;

    root /var/www/html/wordpress;
    index index.php index.html;

    ssl_certificate     /etc/ssl/wordpress/wordpress.crt;
    ssl_certificate_key /etc/ssl/wordpress/wordpress.key;

    ssl_protocols TLSv1.2 TLSv1.3;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
    }
}
```

HTTP → HTTPSリダイレクト追加（重要）

```
server {
    listen 80;
    server_name your-domain-or-ip;

    return 301 https://$host$request_uri;
}
```

3. 設定確認 & 再起動

```bash
sudo nginx -t
sudo systemctl restart nginx
```

4. アクセス確認
https://サーバIP

ブラウザで：

「保護されていない通信」警告 → OK（自己署名なので正常）
WordPress画面が出れば成功

5. WordPress側でやるべき設定（重要）

WordPressはURLをHTTPからHTTPSに変更しないと壊れます。

wp-config.php に追加
define('FORCE_SSL_ADMIN', true);
管理画面 -> 設定 -> 一般
でURL変更（またはDB）
WordPressアドレス
サイトアドレス

を両方：

https://your-domain-or-ip
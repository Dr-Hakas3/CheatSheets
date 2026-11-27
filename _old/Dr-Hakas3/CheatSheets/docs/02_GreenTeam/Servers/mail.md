---
title: Mail Sv
parent: Servers
grand_parent: Green Team
---
1. パッケージのインストール（Ubuntu Server）

まずは必要なソフトウェアをインストールします。

```
sudo apt update
sudo apt install postfix dovecot-core dovecot-imapd mailutils openssl
```
Postfixインストール時の設定
項目	設定値
General type of mail configuration	Internet Site
System mail name	mail.lab.local（任意のFQDN）
2. 証明書作成
保存ディレクトリ作成
```
sudo mkdir -p /etc/ssl/mail
cd /etc/ssl/mail
```
秘密鍵作成
```
sudo openssl genrsa -out mail.key 4096
```
自己署名証明書作成
```
sudo openssl req -new -x509 \
-key mail.key \
-out mail.crt \
-days 3650
```

```
Country Name (2 letter code) [AU]: JP
State or Province Name (full name) [Some-State]: Tokyo
Locality Name (eg, city) []: Chiyoda
Organization Name (eg, company) [Internet Widgits Pty Ltd]: Lab
Organizational Unit Name (eg, section) []: IT
Common Name (e.g. server FQDN or YOUR name) []: mail.lab.local
Email Address []:
```
Common Name (CN) は

mail.lab.local

（Thunderbirdで接続するサーバ名と合わせるのが望ましいです。）

権限設定
```
sudo chmod 600 /etc/ssl/mail/mail.key
```
3. Postfix設定

編集するファイル
/etc/postfix/main.cf
```
# 追加・変更

myhostname = mail.lab.local
home_mailbox = Maildir/

smtpd_use_tls = yes
smtpd_tls_cert_file = /etc/ssl/mail/mail.crt
smtpd_tls_key_file = /etc/ssl/mail/mail.key

smtpd_sasl_auth_enable = yes
smtpd_sasl_type = dovecot
smtpd_sasl_path = private/auth

# 無効化
# smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
# smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
```

編集するファイル
/etc/postfix/master.cf

```
# submission を有効化

submission inet n - y - - smtpd

# 以下を追加

-o smtpd_tls_security_level=encrypt
-o smtpd_sasl_auth_enable=yes
```

4. Dovecot設定
```
/etc/dovecot/conf.d/10-mail.conf
mail_location = maildir:~/Maildir
/etc/dovecot/conf.d/10-auth.conf
disable_plaintext_auth = yes
auth_mechanisms = plain login
/etc/dovecot/conf.d/10-ssl.conf
ssl = required
ssl_cert = </etc/ssl/mail/mail.crt
ssl_key = </etc/ssl/mail/mail.key
/etc/dovecot/conf.d/10-master.conf
service auth {
    unix_listener /var/spool/postfix/private/auth {
        mode = 0660
        user = postfix
        group = postfix
    }
}
```

4. Maildir作成

例：ユーザー alice

```
sudo -u alice mkdir -p /home/alice/Maildir/{cur,new,tmp}
```
6. サービス再起動

```
sudo systemctl restart postfix
sudo systemctl restart dovecot
```

確認

```
sudo systemctl status postfix
sudo systemctl status dovecot
```

7. Thunderbird（Ubuntu Desktop）
受信（IMAPS）
項目	値
プロトコル	IMAP
サーバ	mail.lab.local またはサーバIP
ポート	993
接続の保護	SSL/TLS
認証方式	通常のパスワード
ユーザー名	Linuxユーザー名
送信（SMTP）
項目	値
サーバ	mail.lab.local またはサーバIP
ポート	587
接続の保護	STARTTLS
認証方式	通常のパスワード
ユーザー名	Linuxユーザー名
8. 動作確認

SMTP（STARTTLS）

```
openssl s_client -connect <サーバIP>:587 -starttls smtp
```

IMAPS

```
openssl s_client -connect <サーバIP>:993
```
この構成で使用するポート
ポート	用途
- 25	SMTP（サーバ間配送用）
- 587	Thunderbirdからの送信（STARTTLS）
- 993	Thunderbirdからの受信（IMAPS）
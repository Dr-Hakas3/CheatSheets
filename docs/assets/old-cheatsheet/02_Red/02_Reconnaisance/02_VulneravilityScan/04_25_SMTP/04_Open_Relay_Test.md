# SMTPオープンリレーのテスト
SMTPサーバーがオープンリレーとして設定されているかをテストする方法です。  
telnetを使用してSMTPサーバーに接続し、リレーの確認
```bash
# telnetを使用してSMTPサーバーに接続し、リレーの確認
telnet smtp.example.com 25
EHLO test.com
MAIL FROM:<test@test.com>
RCPT TO:<victim@example.com>
DATA
Subject: Test
This is a test email.
.
QUIT
```
- **EHLO**: SMTPサーバーに対してエンベロープIDを送信します。
- **MAIL FROM**: 送信者のメールアドレスを指定します。
- **RCPT TO**: 受信者のメールアドレスを指定します。
- **DATA**: メールの内容を送信します。


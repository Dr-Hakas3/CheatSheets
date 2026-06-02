
`swaks`（Swiss Army Knife for SMTP）は、SMTPサーバーに対してメール送信のテストを行うためのツールです。詳細な設定を指定してメールの送信をテストするのに利用します。

```bash
# swaksを使用してメール送信のテスト
# 例1
sudo swaks -t user1@test.com -t user2@test.com --from user3@test.com --server --body @body.txt --header "Test" --suppress-data -ap

# 例2
sudo swaks -t dave.wizard@supermagicorg.com --from test@supermagicorg  -ap --attachach @config.Library---serverver 192.168.214.1--bodyody @body.txt --header "Subject: Problems" --suppress-data
[sudo] password for kali: 
Username: test@supermagicorg.com
Password: test
```
- **-t**: 受信者のメールアドレスを指定します。
- **--from**: 送信者のメールアドレスを指定します。
- **--server**: SMTPサーバーのアドレスを指定します（省略可能）。
- **--body**: メールの本文をファイルから指定します。
- **--header**: メールヘッダーを指定します。
- **--suppress-data**: データ部分の出力を抑制します。
- **-ap**: 認証のためのオプション（必要に応じて）。
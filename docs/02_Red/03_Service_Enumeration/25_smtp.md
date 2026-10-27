---
title: 25,587 SMTP
parent: Services
grand_parent: Red Team
nav_order: 25
---
# SMTP

---

## Default Port

- 25
- 587

---

## Service Info



---
## Common security issues

### セキュリティ上の注意点
- **オープンリレー**: 認証なしで外部メールを中継できるSMTPサーバーはスパムの中継に利用される可能性があります。適切な認証とアクセス制御が必要です。
- **スパム対策**: SPF、DKIM、DMARCなどのメール認証技術を使用して、不正なメール送信を防ぎます。
- **暗号化**: メール通信を暗号化するために、STARTTLSやSSL/TLSを利用します。

---

## 1. Initial Scan

```bash
nmap -p 25 smtp.example.com
```

###  SMTPサービスのバージョン検出

```zsh
nmap -sV -p 25 smtp.example.com
```

### SMTP特有のスクリプトを使用して脆弱性をチェック

```
nmap --script smtp-commands,smtp-vuln-cve2010-4344 -p 25 smtp.example.com
```

👉 Check:

* WinRM service exposed
* HTTP (5985) / HTTPS (5986)

---

## 2. Enumeration

#### メールバナーの収集
SMTPサーバーのバナーからサーバーの情報やバージョンを取得します。

```bash
# telnetを使用してメールサーバーに接続し、バナーを取得
telnet smtp.example.com 25
```

```bash
# ncを使用してメールサーバーに接続し、バナーを取得
nc smtp.example.com 25
```

# smtp-user-enumを使用してユーザー列挙
```bash
smtp-user-enum -M VRFY -U /path/to/userlist.txt -t smtp.example.com
```
- **-M VRFY**: SMTPのVRFYコマンドを使用してユーザーを確認します。
- **-U**: ユーザーリストファイルを指定します。
- **-t**: 対象SMTPサーバーを指定します。



---

# SMTP Enumeration
### Netcat
smtp接続
```bash
nc -nv 192.168.50.8 25
```
```bash
VRFY root
```
```bash
VRFY idontexist
^C
```
### Pythonスクリプト
smtp.py
```python
#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
        print("Usage: vrfy.py <username> <target_ip>")
        sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
ip = sys.argv[2]
connect = s.connect((ip,25))

# Receive the banner
banner = s.recv(1024)

print(banner)

# VRFY a user
user = (sys.argv[1]).encode()
s.send(b'VRFY ' + user + b'\r\n')
result = s.recv(1024)

print(result)

# Close the socket
s.close()
```
```bash
python3 smtp.py root 192.168.50.8
```
### Windowsでのtelnetの使用
Telnetクライアントのインストール
```powershell
dism /online /Enable-FeatureName:TelnetClient
```
Telnet接続
```powershell
telnet 192.168.50.8 25
```

---

## 3. # Hydraを使用したSMTPブルートフォース攻撃
```bash
hydra -l username -P /path/to/passwordlist.txt smtp://smtp.example.com
```
- **-l**: 単一のユーザー名を指定します。
- **-P**: パスワードリストファイルを指定します。

---
## 4. swaks

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

---

## 5. SMTPオープンリレーのテスト
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

---

## 6. Error

### 550 Requested action not taken: mailbox unavailable
指定したメールボックスが利用できないことを示します。
- **原因**: メールアドレスが存在しない、またはメールボックスがいっぱいである可能性があります。
- **対処法**: メールアドレスを確認し、メールボックスの状態を確認します。

### 421 Service not available
SMTPサービスが利用できないことを示します。
- **原因**: SMTPサーバーがダウンしているか、接続が拒否された場合があります。
- **対処法**: サーバーの稼働状況を確認し、設定やファイアウォールの確認を行います。

---

## 7. Lab

対象ネットワーク範囲を検索して、SMTPに応答するシステムを特定します。見つかったら、Netcat経由でポート25への接続を開き、_rootユーザーに対して__VRFY_コマンドを実行します。SMTPサーバーはどのような応答コードを返しますか？  

ホスト探索

```bash
nmap -p25 --open 192.168.122.0/24
```

nc接続

```bash
nc 192.168.122.8 25 -nv
```
(UNKNOWN) [192.168.122.8] 25 (smtp) open

220 mail ESMTP Postfix (Ubuntu)

```bash
VRFY root
```

252 2.0.0 root

```bash
VRFY idontexist
```
550 5.1.1  idontexist: Recipient address rejected: User unknown in local recipient table

---



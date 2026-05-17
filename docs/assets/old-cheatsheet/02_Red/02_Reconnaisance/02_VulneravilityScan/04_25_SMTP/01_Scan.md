# セキュリティ上の注意点
- **オープンリレー**: 認証なしで外部メールを中継できるSMTPサーバーはスパムの中継に利用される可能性があります。適切な認証とアクセス制御が必要です。
- **スパム対策**: SPF、DKIM、DMARCなどのメール認証技術を使用して、不正なメール送信を防ぎます。
- **暗号化**: メール通信を暗号化するために、STARTTLSやSSL/TLSを利用します。

# 偵察

#### Nmapを使用したSMTPサーバーの偵察
SMTPサーバーの詳細情報を取得し、脆弱性を調査するための基本的な手順です。

```bash
# 1. 基本的なポートスキャン
nmap -p 25 smtp.example.com

# 2. SMTPサービスのバージョン検出
nmap -sV -p 25 smtp.example.com

# 3. SMTP特有のスクリプトを使用して脆弱性をチェック
nmap --script smtp-commands,smtp-vuln-cve2010-4344 -p 25 smtp.example.com
```

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


#### Nmapを使用したFTPサーバーの偵察
FTPサーバーの詳細情報を取得し、脆弱性を調査するための基本的な手順です。

```bash
# 1. 基本的なポートスキャン
nmap -p 21 ftp.example.com

# 2. FTPサービスのバージョン検出
nmap -sV -p 21 ftp.example.com

# 3. FTP特有のスクリプトを使用して脆弱性をチェック
nmap --script ftp* -p 21 ftp.example.com
```

#### `nmap`によるFTPバナー収集
FTPサーバーのバナーを収集するための手順です。

```bash
# FTPバナーの収集
nmap -p 21 --script ftp-banner ftp.example.com
```

- **--script ftp-banner**: FTPサーバーのバナーを収集するためのスクリプトです。
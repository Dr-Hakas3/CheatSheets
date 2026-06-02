# SSHサービスのバージョン検出
```bash
nmap -sV -p 22 ssh.example.com
```

# SSH特有のスクリプトを使用して脆弱性をチェック
```
nmap --script ssh-hostkey -p 22 ssh.example.com
```
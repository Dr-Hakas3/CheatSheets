### Lab
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
550 5.1.1 <idontexist>: Recipient address rejected: User unknown in local recipient table
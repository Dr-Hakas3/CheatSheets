Kali Linux で全通信を Tor 経由にする方法
 
目次
- Tor のインストールと起動
- Proxychains の設定
- すべての通信を Tor 経由にする
- 確認方法
---
Tor のインストールと起動  
Tor のインストール
以下のコマンドで Tor をインストールします：

```bash

sudo apt update
sudo apt install tor
```
Tor の起動
Tor サービスを開始し、常時起動するように設定します：

```bash

sudo systemctl start tor
sudo systemctl enable tor
```
Tor サービスが正常に動作しているか確認します：

```bash

sudo systemctl status tor
```
---
Proxychains の設定  
Proxychains のインストール
以下のコマンドで Proxychains をインストールします：

```bash

sudo apt install proxychains
```
設定ファイルの編集
Proxychains の設定ファイルを編集します。デフォルトでは /etc/proxychains.conf にあります。

```bash

sudo nano /etc/proxychains.conf
```
以下の設定を確認または変更してください：

動的チェーンを有効化 ファイル内の以下の行を有効化します（先頭の # を削除）：

plaintext

dynamic_chain
strict_chain が有効な場合はコメントアウトしてください。

プロキシリスト ファイル末尾の [ProxyList] セクションで SOCKS5 プロキシとして Tor を設定します：

plaintext

[ProxyList]
socks5 127.0.0.1 9050
保存してファイルを閉じます。
---
すべての通信を Tor 経由にする
Proxychains を使用してアプリケーションを実行 Proxychains を使って特定のアプリケーションを Tor 経由で通信させます。

例: curl を使用する場合

```bash

proxychains curl http://check.torproject.org
```
すべての通信を Tor にリダイレクト iptables を使用して、すべての通信を Tor ネットワークにリダイレクトします。

```bash

sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t nat -A OUTPUT -m owner --uid-owner $(id -u) -j RETURN
sudo iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-ports 9040
sudo iptables -t nat -A OUTPUT -p tcp --dport 443 -j REDIRECT --to-ports 9040
sudo iptables -t nat -A OUTPUT -p tcp -j REDIRECT --to-ports 9040
sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -j DROP
```
Tor TransPort を有効化 Tor の設定ファイルを編集して TransPort を有効化します。

設定ファイルを開く：

```bash

sudo nano /etc/tor/torrc
```
以下の行を有効化または追加します：

plaintext

TransPort 9040
Tor を再起動します：

```bash

sudo systemctl restart tor
```
---
確認方法
以下のコマンドを実行して、自分の通信が Tor ネットワーク経由になっているか確認します。

Tor ネットワークの確認
```bash
proxychains curl http://check.torproject.org
```
出力が以下のようになれば成功です：

plaintext

Congratulations. This browser is configured to use Tor.
[参考リンク](https://hacklido.com/blog/150-proxychains-tor-kali-linux-complete-guide-to-be-anonymous)

---
title: Linux Command
parent: Linux
grand_parent: General
---
# File操作

<details markdown=1><summary>awk</summary>
- ログ解析などに有用なコマンド
- awkはスペースでフィールドを区切る
- awk '条件 {処理}'

exeのあるファイルを表示
```bash
awk '/exe/  {print $0}'
```


```bash
awk '{print $6}' wordpress.log | sort | uniq -c
```


</details>

<details markdown=1><summary></summary>

</details>


<details markdown=1><summary></summary>

</details>


<details markdown=1><summary></summary>

</details>

<details markdown="1">

<summary>sed</summary>
### sed
####標準入力からバックスラッシュを削除
```bash
echo "User\\Name" | sed 's/User\\//g'
```
このコマンドを実行すると、「UserName」が出力されます。

#### ファイル内の「User」からバックスラッシュを削除
```bash

sed 's/User\\//g' inputfile.txt > outputfile.txt
```
#### awkとの組み合わせ
```bash
 awk '{print $3}' users.txt| sed 's/User\\//g'  > username.txt
```
#### Interface名を全変更
```bash
![image](https://github.com/user-attachments/assets/2f042e29-36ba-49dd-bf95-592a8c8a0e10)
```

# wordlist + !!!
```zsh
sed 's/$/!!!/' rockyou.txt > mask_word.txt
```
![](../../../assets/images/Pasted%20image%2020260502140113.png)
# ABC123 + wordlist
```zsh
sed 's/^/ABC123/' rockyou.txt > word_mask.txt
```
![](../../../assets/images/Pasted%20image%2020260502140333.png)

# ABC123 + wordlist + !!!
```zsh
sed 's/^/ABC123/' rockyou.txt | sed 's/$/!!!/' > rockyou_hybrid.txt
```
![](../../../assets/images/Pasted%20image%2020260502140450.png)
</details>

---

# プロセス解析


<details markdown=1>

 <summary>ps pstree</summary>

# ps

```zsh
ps aux 
```

```zsh
ps f -f
```

---

# pstree
</details>

<details markdown=1>

 <summary></summary>

</details>

---

# 通信解析

<details markdown=1><summary>tcpdump</summary>

tcpdump でパケットをキャプチャし、後で Wireshark で開ける形式（pcap）で保存するには -w オプションを使います。

全トラフィックを保存
```zsh
sudo tcpdump -i eth0 -w capture.pcap
```
- -i eth0 : 監視するインターフェース
- -w capture.pcap : pcap形式で保存

停止は Ctrl+C。

インターフェース確認
```zsh
ip a
```

または

tcpdump -D
特定の通信だけ保存
HTTPのみ
```zsh
sudo tcpdump -i eth0 tcp port 80 -w http.pcap
```
特定IPとの通信
```zsh
sudo tcpdump -i eth0 host 192.168.1.10 -w target.pcap
```
DNSのみ
```zsh
sudo tcpdump -i eth0 udp port 53 -w dns.pcap
```
サイズでローテーション

100MBごとにファイル分割:

```zsh
sudo tcpdump -i eth0 -C 100 -w capture.pcap
```

生成例:

capture.pcap0
capture.pcap1
capture.pcap2
時間でローテーション

1時間ごとに保存:

```zsh
sudo tcpdump -i eth0 -G 3600 -w 'capture-%Y%m%d-%H%M%S.pcap'
```

例:

capture-20260607-060000.pcap
capture-20260607-070000.pcap

### Wiresharkで開く

保存したファイルをそのまま開けます。

```zsh
wireshark capture.pcap
```

または GUI から

File → Open → capture.pcap

OSCPやネットワーク演習でよく使うのは、

```zsh
sudo tcpdump -i tun0 -nn -s0 -w lab.pcap
```

です。

-nn : DNS逆引き・ポート名変換をしない
-s0 : パケットを切り捨てずフル保存
-w : Wireshark用pcap保存

後から Wireshark で詳細解析するなら、この形が定番です。

できます。

ただし、tcpdump は HTTP の「プロトコル解析」まではしないので、基本的には ポート番号で絞り込みます。

HTTPのみ保存（一般的）
```zsh
sudo tcpdump -i eth0 -s0 -w http.pcap 'tcp port 80'
```
HTTP/HTTPS両方
```zsh
sudo tcpdump -i eth0 -s0 -w web.pcap 'tcp port 80 or tcp port 443'
```

ただし HTTPS(443) は暗号化されているので、Wiresharkで見ても中身のHTTPリクエストは読めません。

HTTPリクエストだけをキャプチャ

HTTPメソッドを見て絞ることも可能です。

```zsh
sudo tcpdump -i eth0 -s0 -w get_requests.pcap \
'tcp[((tcp[12] & 0xf0) >> 2):4] = 0x47455420'
```

これは先頭が "GET " のパケットだけ保存します。

代表例:

メソッド	16進数
GET	0x47455420
POST	0x504f5354
HEAD	0x48454144

ただし実務ではあまり使わず、まずポート80を全部保存してWireshark側でフィルタします。

Wireshark側でHTTPだけ表示

キャプチャは全部保存しておいて、

httpやhttp.requestでフィルタする方が解析しやすいです。

例えば OSCP のような演習なら、

```zsh
sudo tcpdump -i tun0 -nn -s0 -w traffic.pcap
```

で全部保存し、後から Wireshark で

http
ftp
smb
dns
ldap
kerberos

などを見分ける方法が一般的です。キャプチャ時に絞りすぎると、後で「実は別プロトコルに重要な情報があった」というケースを見逃すことがあります。

特定のアドレス

はい。host を使えば特定のIPアドレスとの通信だけを保存できます。

特定IPとの通信を保存
```zsh
sudo tcpdump -i eth0 -s0 -w target.pcap host 192.168.1.100
```

送信・受信の両方が対象です。

特定IPのHTTPだけ保存
```zsh
sudo tcpdump -i eth0 -s0 -w http_target.pcap \
'host 192.168.1.100 and tcp port 80'
```
特定IPのHTTPSだけ保存
```zsh
sudo tcpdump -i eth0 -s0 -w https_target.pcap \
'host 192.168.1.100 and tcp port 443'
```
送信のみ
```zsh
sudo tcpdump -i eth0 -s0 -w outbound.pcap \
'src host 192.168.1.100'
```
受信のみ
```zsh
sudo tcpdump -i eth0 -s0 -w inbound.pcap \
'dst host 192.168.1.100'
```
複数IP
```zsh
sudo tcpdump -i eth0 -s0 -w multi.pcap \
'(host 192.168.1.100 or host 192.168.1.200)'
```
CTFやペネトレーションテストでよく使う例

ターゲットが 10.10.10.5 の場合:

```zsh
sudo tcpdump -i tun0 -nn -s0 -w target.pcap host 10.10.10.5
```

これで自分とターゲット間の通信だけが保存され、後で Wireshark で HTTP、SMB、LDAP、Kerberos などを解析できます。

特定の日時の間

tcpdump 自体には「2026-06-07 10:00～10:05だけ取得」のような日時指定オプションはありません。

一般的には以下の方法を使います。

方法1: timeoutで指定秒数だけ取得

5分間だけ取得

```zsh
sudo timeout 300 tcpdump -i eth0 -s0 -w capture.pcap
```

300秒後に自動終了します。

方法2: at と組み合わせる

10:00開始、10:05終了

```zsh
echo "timeout 300 tcpdump -i eth0 -s0 -w capture.pcap" | at 10:00
```

方法3: cronで開始・終了

開始:

0 10 * * * tcpdump -i eth0 -s0 -w /tmp/capture.pcap

終了:

5 10 * * * pkill tcpdump

ただし pkill tcpdump は他の tcpdump も止めるので注意です。

方法4: 後から時間で抽出（おすすめ）

長時間キャプチャしておいて、必要な時間帯だけ切り出します。

まず全体を取得:

```zsh
sudo tcpdump -i eth0 -s0 -w all.pcap
```

その後、Wireshark付属の editcap で切り出し:

```zsh
editcap \
-A "2026-06-07 10:00:00" \
-B "2026-06-07 10:05:00" \
all.pcap \
extract.pcap
```
- -A : 開始時刻
- -B : 終了時刻

もし「特定IPの通信を、10分間だけ保存したい」なら、実務的には次のようにすることが多いです。

```zsh
sudo timeout 600 tcpdump \
-i eth0 \
-nn \
-s0 \
-w target.pcap \
'host 192.168.1.100'
```

これで対象IPとの通信だけを10分間保存できます。

</details>
airmon-ng は、Kali Linuxに含まれる Aircrack-ngスイートの無線LANインターフェース管理ツールです。

主な用途は、無線LANインターフェースを Monitor Mode（モニターモード） に切り替えることです。

OSWPの学習では、非常に重要なコマンドです。

# 1. Monitor Modeとは？

通常の無線LANインターフェースは、Managed Modeで動作します。
モード	動作
Managed Mode	APに接続して通信する通常モード
Monitor Mode	周囲の無線LANフレームを受信・観測するモード

Monitor Modeにすると、アクセスポイントに接続しなくても、受信可能な範囲の802.11フレームをキャプチャできます。

例えば、以下のような解析に使用します。
- APやクライアントの検出
- Beaconフレームの取得
- Probe Requestの取得
- WPA/WPA2ハンドシェイクのキャプチャ
- 無線LAN通信の解析

![[Pasted image 20261117014404.png]]

# 2. 基本的な使い方

① 無線LANインターフェースの確認
```
sudo airmon-ng
```


無線LANインターフェースの一覧を表示します。
② Monitor Modeへの切り替え
```
sudo airmon-ng start wlan0
```


wlan0 をMonitor Modeに切り替えます。

環境によっては、新しいインターフェース名として wlan0mon が作成されます。
③ Monitor Modeの確認
```
iw dev
```


または、
```
iwconfig
```


Monitor Modeになっているか確認できます。
④ Monitor Modeの解除
sudo airmon-ng stop wlan0mon


Monitor Modeを解除します。

環境によっては元の wlan0 に戻ります。
# 3. 重要なオプション
OSWP対策として、以下の4つは覚えておきましょう。
コマンド	役割
airmon-ng	無線インターフェース一覧
airmon-ng check	干渉するプロセスを確認
airmon-ng check kill	干渉するプロセスを停止
airmon-ng start wlan0	Monitor Mode開始
airmon-ng stop wlan0mon	Monitor Mode解除

airmon-ng check
sudo airmon-ng check


Monitor Modeの動作を妨げる可能性があるプロセスを確認します。

代表例：
- NetworkManager
- wpa_supplicant
- dhclient
airmon-ng check kill
sudo airmon-ng check kill


無線LAN操作に干渉するプロセスを停止します。

注意
 NetworkManagerなどを停止するため、Kaliの通常のネットワーク接続にも影響します。作業終了後は必要に応じて再起動してください。
チャンネル指定
sudo airmon-ng start wlan0 6


Monitor Modeへの切り替えと同時に、チャンネル6を指定します。

特定のAPを調査する場合に便利です。
4. OSWPでの基本的な使用フロー
5. 無線インターフェース確認
   iw dev
6. 干渉プロセス確認・停止
   sudo airmon-ng check
   sudo airmon-ng check kill
7. Monitor Mode開始
   sudo airmon-ng start wlan0
8. インターフェース確認
   iw dev
9. 無線LANのスキャン
   sudo airodump-ng wlan0mon
# 10. Monitor Mode解除

```zsh
sudo airmon-ng stop wlan0mon
```

# 11. 今取り組んでいるWiFi Challenge Labとの関係
ここは重要です。

現在の環境では、物理無線LANアダプターだけでなく、mac80211_hwsim によって仮想無線LANインターフェースも作成していますね。

この場合、次のように使い分けます。
ツール	役割
mac80211_hwsim	仮想無線LANデバイスを生成
iw	無線インターフェースの詳細設定・確認
airmon-ng	Monitor Modeへの切り替え
airodump-ng	無線LANのスキャン・キャプチャ
aireplay-ng	無線フレームの送受信・再送
aircrack-ng	キャプチャしたデータの解析・鍵検証

つまり、airmon-ngは無線LAN攻撃そのものを実行するツールではなく、攻撃・解析に必要な無線インターフェースの動作モードを準備するツールです。

参考：
- Aircrack-ng公式：Airmon-ng
- Kali Linux Tools：Aircrack-ng
覚えるポイント： airmon-ng でMonitor Modeを準備し、airodump-ng で周囲の無線LANを観測する。この役割分担を理解しておきましょう。
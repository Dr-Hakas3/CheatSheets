---
title: airodump-ng
---
`airodump-ng` は、**無線LANのアクセスポイント（AP）や接続クライアントを検出・監視し、無線LAN通信をキャプチャするツール**です。

Aircrack-ngスイートに含まれており、OSWP学習では無線LANの偵察（Reconnaissance）や通信解析の基本ツールとして使用します。

## 1. 基本コマンド

```
sudo airodump-ng wlan60
```

|要素|意味|
|---|---|
|`sudo`|root権限で実行|
|`airodump-ng`|無線LANのパケットをキャプチャ・監視するツール|
|`wlan60`|監視対象の無線インターフェース（モニターモード）|

### 主な用途

- 周辺アクセスポイント（AP）の検出
    
- BSSID（APのMACアドレス）の取得
    
- ESSID（Wi-Fiネットワーク名）の取得
    
- チャネル（Channel）の確認
    
- 暗号化方式・認証方式の確認
    
- 接続クライアントの検出
    
- 無線LAN通信のパケットキャプチャ
    

## 2. 実行結果の見方

![[Pasted image 20261123083414.png]]

実行すると、主に2つのテーブルが表示されます。

### 2.1 上段：アクセスポイント情報（AP）

|項目|意味|
|---|---|
|BSSID|APのMACアドレス|
|PWR|受信電波強度|
|Beacons|受信したビーコンフレーム数|
|#Data|受信したデータフレーム数|
|#/s|1秒あたりのデータフレーム数|
|CH|使用チャネル|
|MB|最大通信速度の目安|
|ENC|暗号化方式（WEP / WPA / WPA2 / WPA3など）|
|CIPHER|暗号化アルゴリズム（CCMP / TKIPなど）|
|AUTH|認証方式（PSK / MGTなど）|
|ESSID|Wi-Fiネットワーク名|

**特に重要な項目**

- `BSSID`：対象APの識別
    
- `CH`：対象APが使用しているチャネル
    
- `ENC`：暗号化方式の確認
    
- `ESSID`：ネットワーク名の確認
    

### 2.2 下段：接続クライアント情報（STATION）

|項目|意味|
|---|---|
|STATION|クライアントのMACアドレス|
|PWR|クライアントからの受信電波強度|
|Rate|通信速度|
|Lost|パケットの取りこぼし数|
|Frames|受信フレーム数|
|BSSID|接続先APのMACアドレス|
|Probes|クライアントが探しているネットワーク名|

`STATION` はクライアントのMACアドレスです。

`BSSID` が `not associated` の場合、特定のAPに関連付けられていない状態を示します。

## 3. よく使うオプション

|オプション|意味|
|---|---|
|`-c 6`|チャネル6に固定|
|`-w capture`|キャプチャファイルの保存先・名前を指定|
|`--bssid AA:BB:CC:DD:EE:FF`|特定APに絞り込む|
|`-a`|APのみを対象に表示|
|`--band abg`|対象周波数帯を指定|
|`--manufacturer`|MACアドレスからメーカー情報を表示|
|`--wps`|WPS情報を表示|

### 3.1 チャネルを指定する

```
sudo airodump-ng -c 6 wlan60
```

チャネル6に固定してスキャンします。

### 3.2 キャプチャデータを保存する

```
sudo airodump-ng wlan60 -w ~/wifi/scan
```

以下のようなファイルが生成されます。

|ファイル|内容|
|---|---|
|`.cap`|キャプチャした無線LANパケット|
|`.csv`|AP・クライアントなどの検出情報|
|`.kismet.csv`|Kismet形式の情報|
|`.kismet.netxml`|Kismet NetXML形式の情報|

### 3.3 特定APに絞り込む

```
sudo airodump-ng \
  --bssid AA:BB:CC:DD:EE:FF \
  -c 6 \
  -w capture \
  wlan60
```

指定したBSSIDとチャネルを対象に通信をキャプチャします。

### 3.4 周波数帯を指定する

```
sudo airodump-ng wlan60 --band abg
```

`--band` はIEEE 802.11の規格世代ではなく、スキャン対象の無線周波数帯を指定するオプションです。

|指定文字|対象|主な対応規格|
|---|---|---|
|`a`|5GHz帯|802.11a、n、ac、ax、be|
|`b`|2.4GHz帯|802.11b、n、ax、be|
|`g`|2.4GHz帯|802.11g、n、ax、be|

※ 対応規格は周波数帯の対応関係です。`--band` が規格世代を直接指定するわけではありません。

※ 6GHz帯や60GHz帯は、この `abg` の指定対象には含まれません。

### 3.5 メーカー・WPS情報を表示する

```
sudo airodump-ng wlan60 \
  --manufacturer \
  --wps
```

- `--manufacturer`：MACアドレスのOUIからメーカー情報を表示
    
- `--wps`：WPS（Wi-Fi Protected Setup）に関する情報を表示
    

WPSは無線LANへの接続を簡略化する仕組みです。取得できる情報には、WPS対応状況、バージョン、ロック状態などがあります。

## 4. IEEE 802.11規格一覧

IEEE 802.11は無線LANの通信方式を定めた規格群です。

規格によって、使用する周波数帯、通信速度、変調方式、通信機能などが異なります。

### 4.1 主要な無線LAN規格

|規格|周波数帯|最大理論速度|主な特徴|
|---|---|---|---|
|802.11|2.4GHz|2Mbps|初期規格|
|802.11a|5GHz|54Mbps|OFDM採用|
|802.11b|2.4GHz|11Mbps|DSSS / CCK|
|802.11g|2.4GHz|54Mbps|OFDM採用|
|802.11n|2.4 / 5GHz|600Mbps|MIMO、HT|
|802.11ac|5GHz|約6.9Gbps|VHT、MU-MIMO|
|802.11ax|2.4 / 5 / 6GHz|約9.6Gbps|OFDMA、Wi-Fi 6 / 6E|
|802.11be|2.4 / 5 / 6GHz|約46Gbps|MLO、Wi-Fi 7|

※ 最大理論速度は規格上の理論値であり、実際の通信速度ではありません。

### 4.2 その他の周波数帯・用途に関する規格

|規格|周波数帯|主な特徴|
|---|---|---|
|802.11ad|60GHz|WiGig、高速・短距離通信|
|802.11ay|60GHz帯|802.11adの高速化・拡張|
|802.11ah|1GHz未満|Wi-Fi HaLow、長距離・低消費電力|
|802.11af|TVホワイトスペース|テレビ放送用周波数の空き帯域を利用|
|802.11p|5.9GHz帯など|車車間・路車間通信（ITS）|

### 4.3 セキュリティ・管理機能に関する規格

|規格|名称・機能|概要|
|---|---|---|
|802.11i|Security|WPA2の基礎となる無線LANセキュリティ機能|
|802.11w|Protected Management Frames|管理フレームの保護（PMF）|
|802.11e|QoS|通信品質・優先制御|
|802.11r|Fast BSS Transition|AP間の高速ローミング|
|802.11k|Radio Resource Management|周辺APなどの無線リソース情報|
|802.11v|Wireless Network Management|無線ネットワーク管理|
|802.11s|Mesh Networking|メッシュネットワーク|
|802.11u|Interworking|異種ネットワーク間の接続支援|

## 5. Wi-Fi世代との対応

Wi-Fi Allianceが定めるWi-Fi世代とIEEE 802.11規格の対応関係です。

|Wi-Fi名称|IEEE規格|周波数帯|
|---|---|---|
|Wi-Fi 4|802.11n|2.4 / 5GHz|
|Wi-Fi 5|802.11ac|5GHz|
|Wi-Fi 6|802.11ax|2.4 / 5GHz|
|Wi-Fi 6E|802.11ax|2.4 / 5 / 6GHz|
|Wi-Fi 7|802.11be|2.4 / 5 / 6GHz|

### 周波数帯別の整理

|周波数帯|主なIEEE規格|
|---|---|
|2.4GHz|802.11、b、g、n、ax、be|
|5GHz|802.11a、n、ac、ax、be|
|6GHz|802.11ax、be|
|60GHz|802.11ad、ay|
|1GHz未満|802.11ah|

## 6. 実践的なコマンドの組み合わせ

### 6.1 AP・クライアントの全体スキャン

```
sudo airodump-ng wlan60
```

周辺のAPとクライアントを検出します。

### 6.2 2.4GHz帯・5GHz帯を対象にスキャン

```
sudo airodump-ng wlan60 --band abg
```

### 6.3 メーカー・WPS情報を含めて保存

```
sudo airodump-ng wlan60 \
  -w ~/wifi/scan \
  --manufacturer \
  --wps \
  --band abg
```

2.4GHz帯・5GHz帯を対象にAPやクライアントをスキャンし、メーカー情報やWPS情報を表示しながら、取得データを保存します。

### 6.4 特定APの通信をキャプチャ

```
sudo airodump-ng \
  --bssid AA:BB:CC:DD:EE:FF \
  -c 6 \
  -w capture \
  wlan60
```

対象APのチャネルに固定して通信をキャプチャします。

## 7. 操作中のショートカット

|キー|操作|
|---|---|
|`Ctrl + C`|キャプチャを終了|
|`a`|AP表示のソート切り替え|
|`s`|ソート基準の切り替え|

## 8. OSWP学習での使用フロー

```
① 無線インターフェースの確認
   iw dev
        |
        v
② AP・クライアントの偵察
   sudo airodump-ng wlan60
        |
        v
③ 対象AP・チャネルの特定
   BSSID / CH / ENC / ESSID
        |
        v
④ 対象APに絞り込む
   --bssid / -c
        |
        v
⑤ 必要な通信をキャプチャ
   -w capture
        |
        v
⑥ キャプチャデータを解析
   WPAハンドシェイクなど
```

## 9. 重要ポイント・試験対策

`airodump-ng` は、単にSSIDを調べるツールではありません。

無線LANの電波を受信し、ビーコンフレーム・管理フレーム・制御フレーム・データフレームなどを収集することで、APやクライアントの情報を把握するツールです。

**OSWP学習では、以下を重点的に理解します。**

### airodump-ng の重要項目

1. **BSSID**：対象APの識別
    
2. **CH**：対象APの使用チャネル
    
3. **ENC / AUTH**：暗号化・認証方式
    
4. **STATION**：接続クライアントの識別
    
5. **Probes**：クライアントが探しているネットワーク名
    

### IEEE 802.11 の重要規格

1. **802.11a/b/g**：基本的な無線LAN規格
    
2. **802.11n**：MIMO、HT20、HT40
    
3. **802.11ac**：VHT、チャネル幅
    
4. **802.11ax**：OFDMA、Wi-Fi 6
    
5. **802.11i**：無線LANセキュリティ
    
6. **802.11w**：管理フレーム保護（PMF）
    

これらの知識を基礎として、対象APの特定、暗号化方式の確認、通信キャプチャ、ハンドシェイク解析などに進みます。

※ 規格一覧は主要規格を網羅する構成です。IEEE 802.11の全改訂・全タスクグループを列挙した規格台帳ではありません。
---
title: airodump-ng
---

`sudo airodump-ng wlan60` は、**無線LANの周辺アクセスポイント（AP）や接続クライアントを検出・監視するコマンド**です。

OSWP学習では、無線LANの偵察（Reconnaissance）で使用する基本コマンドです。

## **1. コマンドの構成**

```
sudo airodump-ng wlan60
```

|要素|意味|
|---|---|
|`sudo`|root権限でコマンドを実行|
|`airodump-ng`|無線LANのパケットをキャプチャ・監視するツール|
|`wlan60`|監視対象の無線インターフェース|

### **airodump-ng とは**

Aircrack-ngスイートに含まれるツールです。

主な用途は次のとおりです。

- 周辺の無線LANアクセスポイントの検出
    
- BSSID（APのMACアドレス）の取得
    
- ESSID（Wi-Fiネットワーク名）の取得
    
- チャネル（Channel）の確認
    
- 暗号化方式の確認
    
- 接続クライアントの検出
    
- 無線LAN通信のパケットキャプチャ
    

## **2. 実行結果の見方**

実行すると、主に2つのテーブルが表示されます。

### **上段：アクセスポイント情報**

![[Pasted image 20261115192927.png]]

[Surveying Your Wireless Zone | BackTrack - Testing Wireless Network Security](https://images.openai.com/static-rsc-4/6_OSF8dXm2LlqoTsfu79xPwLb1-JBdWZkh9o8E8lUqDcenJzuCfSt75wQHlbaTpItfG8LJFH1jbA6IG2F-xKX4wD5EQuX6CdOxRdlfASRLYLmUFsT-E7cf8jGYS4HUo1fPz74MywP6npuduBvMb45t9MRoXWAMGBKO6f42l5A-k?purpose=inline)

[subscription.packtpub.com](https://subscription.packtpub.com/book/cloud-and-networking/9781782164067/3/ch03lvl1sec23/working-with-tools?utm_source=chatgpt.com)

|項目|意味|
|---|---|
|BSSID|APのMACアドレス|
|PWR|受信電波強度|
|Beacons|受信したビーコンフレーム数|
|#Data|データフレーム数|
|#/s|1秒あたりのデータフレーム数|
|CH|使用チャネル|
|MB|最大通信速度の目安|
|ENC|暗号化方式|
|CIPHER|暗号化アルゴリズム|
|AUTH|認証方式|
|ESSID|Wi-Fiネットワーク名|

特に重要なのは以下の項目です。

- `BSSID`：攻撃対象となるAPの識別
    
- `CH`：APが使用しているチャネル
    
- `ENC`：WEP / WPA / WPA2 / WPA3など
    
- `ESSID`：ネットワーク名
    

### **下段：接続クライアント情報**

|項目|意味|
|---|---|
|STATION|クライアントのMACアドレス|
|PWR|クライアントの受信電波強度|
|Rate|通信速度|
|Lost|パケットの取りこぼし数|
|Frames|受信フレーム数|
|BSSID|接続先APのMACアドレス|
|Probes|クライアントが探しているネットワーク名|

`STATION` は、無線LANに接続しているクライアントのMACアドレスです。

## **3. よく使うオプション**

|オプション|意味|
|---|---|
|`-c 6`|チャネル6に固定|
|`-w capture`|キャプチャファイル名を指定|
|`--bssid AA:BB:CC:DD:EE:FF`|特定APに絞る|
|`-a`|APのみ表示|
|`--band abg`|対象周波数帯を指定|

例えば、チャネル6の通信をキャプチャする場合：

```
sudo airodump-ng -c 6 wlan60
```

特定のAPを対象にする場合：

```
sudo airodump-ng \
  --bssid AA:BB:CC:DD:EE:FF \
  -c 6 \
  -w capture \
  wlan60
```

`-w` を指定すると、キャプチャデータがファイルとして保存されます。

## **4. OSWP学習での位置付け**

今回のWiFiChallengeLabでは、次のような流れで使います。

**① 無線インターフェースの確認**

`iw dev`

**② AP・クライアントの偵察**

`sudo airodump-ng wlan60`

**③ 対象AP・チャネルの特定**

BSSID / CH / ENC

**④ 必要な通信のキャプチャ・解析**

WPAハンドシェイクなど

## **5. 操作上のショートカット**

実行中は以下の操作ができます。

- `Ctrl + C`：終了
    
- `a`：AP表示のソート切り替え
    
- `s`：ソート基準の切り替え
    

**今回、特に覚えておきたいこと**

`airodump-ng` は、単にWi-FiのSSIDを調べるツールではありません。

無線LANの管理フレーム・制御フレーム・データフレームを受信し、APやクライアントの情報を収集するためのツールです。
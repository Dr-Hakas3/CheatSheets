---
title: wpa_supplicant
---
wpa_supplicant は、Linuxにおいて Wi-Fiクライアント（STA）としてアクセスポイント（AP）に接続するための認証・接続管理デーモン です。

OSWP学習では、特に WPA/WPA2 の認証処理や、取得したパスワードを使ったWi-Fi接続を理解するうえで重要なツールです。
# 1. 基本概要

Wi-Fi Client
 Authentication

項目	内容
- コマンド	wpa_supplicant
- 役割	Wi-Fi認証・接続管理
- 対応規格	WPA、WPA2、WPA3など
- 主な対象	LinuxのWi-Fiクライアント
- 設定ファイル	/etc/wpa_supplicant/wpa_supplicant.conf

通信のイメージ
![[Pasted image 20261115224806.png]]


wpa_supplicant はAPとの認証処理を担当します。

具体的には、WPA2-PSKの場合、パスワードから生成される鍵情報を利用して4-way handshakeを実行します。

# 2. 基本的な使い方
① Wi-Fiインターフェースを指定して起動

```
sudo wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
```


オプション	意味
- -i wlan0	使用するWi-Fiインターフェース
- -c	設定ファイルを指定

② バックグラウンドで起動
```
sudo wpa_supplicant -B -i wlan0 -c config.conf
```

- -B はバックグラウンド実行です。

③ 設定ファイルを使わずに接続
```
sudo wpa_supplicant -i wlan0 -c <(wpa_passphrase "SSID" "PASSWORD")
```


wpa_passphrase はSSIDとパスワードから接続設定を生成します。

※ Bash/Zshのプロセス置換を利用しています。
# 3. 設定ファイルの構造

例：wpa_supplicant.conf

```
ctrl_interface=/var/run/wpa_supplicant
update_config=1
country=JP


network={
    ssid="TestWiFi"
    psk="password123"
}
```



設定	意味
- ctrl_interface	制御インターフェースの設定
- update_config	設定ファイルの更新許可
- country	国・地域コード
- ssid	接続先のSSID
- psk	WPA-PSKのパスワードまたは鍵

# 4. OSWP学習で重要な関連コマンド
コマンド	役割
- wpa_supplicant	Wi-Fi認証・接続
- wpa_passphrase	PSK設定の生成
- wpa_cli	wpa_supplicantの制御
- iw	無線インターフェースの管理
- airmon-ng	モニターモードの管理
- airodump-ng	AP・クライアントの観測
- aireplay-ng	フレーム送信・再送など

# 5. OSWP試験との関係
ここが重要です。

OSWPで扱う無線LAN攻撃では、次のような流れが登場します。
# 1. APの調査
   
   airodump-ng でSSID、BSSID、暗号化方式などを確認
# 2. 認証情報の取得
   
   対象の暗号化方式に応じてハンドシェイクなどを取得
# 3. パスワードの解析
   
   取得した情報からPSKを特定する
# 4. Wi-Fiへの接続
   
   wpa_supplicant にPSKを設定して接続する
# 5. ネットワークへのアクセス
   
   接続後、対象ネットワーク内で次の調査を進める

# 6. 特に覚えておきたいこと
混同しやすいので整理します。
ツール	動作
- airodump-ng	無線通信を受動的に観測する
- aireplay-ng	無線フレームを送信する
- aircrack-ng	キャプチャした情報などから鍵を解析する
- wpa_supplicant	Wi-Fiクライアントとして認証・接続する

重要：wpa_supplicant 自体がパスワードを解析するわけではありません。

取得・解析したパスワードを使って、APに接続するためのツールです。
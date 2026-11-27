---
title: mdk4
tags:
---
mdk4 は、無線LAN（Wi-Fi）のセキュリティテストに使用する IEEE 802.11向けの攻撃・検証ツール です。

Kali Linuxで利用でき、主にWi-Fiネットワークに対するDoS攻撃、認証・接続処理の検証、無線LANの堅牢性評価などに使われます。

# 1. mdk4とは

MDK4 = Murder Death Kill 4

無線LANの管理フレームや制御フレームなどを操作し、アクセスポイント（AP）やクライアント端末の動作を検証するツールです。

代表的な用途は次のとおりです。

用途	内容
- Beacon Flood	大量の偽アクセスポイント情報を送信
- Authentication DoS	認証処理への負荷を検証
- Deauthentication	認証解除フレームを利用した接続妨害
- Probe Response	Probe Requestに対する応答を利用した検証
- EAPOL関連	WPA認証処理に関する検証

# 2. 基本構文

```zsh
sudo mdk4 <interface> <mode> [options]
```


引数	意味
- sudo	管理者権限で実行
- interface	無線LANインターフェース
- mode	実行する攻撃・テストの種類
- options	モード固有の追加設定

例えば、wlan60 を指定する場合、そのインターフェースが無線フレームを送受信できる状態である必要があります。

# 3. 攻撃モード一覧

MDK4の重要な部分です。モードはアルファベット1文字で指定します。

モード	名称	動作
- b	Beacon Flooding	偽APのBeaconを大量送信
- a	Authentication DoS	認証要求を大量送信
- p	SSID Probing	SSIDの探索・隠しSSIDの検証
- d	Deauthentication	接続解除フレームを送信
- m	Michael Countermeasures	TKIPの対策機構を悪用する検証
- e	EAPOL Injection	EAPOL Start / Logoffを送信
- s	IEEE 802.11s	メッシュネットワークへの攻撃
- w	WIDS Confusion	無線侵入検知システムの検証
- f	Packet Fuzzer	不正な802.11パケットの生成
- x	PoC Testing	Wi-Fi実装の脆弱性検証

※ モードやオプションはMDK4のバージョンによって差異があります。

# 4. まず覚えるコマンド

今回のOSWP学習では、まず以下を実行してツールの仕様を確認しましょう。

① インストール確認
```
mdk4 --version
```


② 基本ヘルプ
```
mdk4 --help
```


③ 全モードのヘルプ
```
mdk4 --fullhelp
```


④ 特定モードのヘルプ
```
mdk4 --help b
mdk4 --help p
mdk4 --help d
```


これらは情報表示用で、無線フレームを送信しません。

# 5. OSWP学習における位置付け
ここは重要です。

# Wi-Fiペネトレーションテストの基本的な流れ

```

1. 周辺APの調査
   
   airodump-ng
   
   SSID / BSSID / Channel / Encryptionの確認
2. 通信のキャプチャ
   
   airodump-ng
   
   Beacon、Probe、認証関連フレームなどを観察
3. 脆弱性・設定の検証
   
   mdk4 など
   
   802.11プロトコルの挙動やAPの耐性を検証
4. 認証情報の解析
   
   aircrack-ng など
   
   キャプチャした認証情報を解析
5. 接続・フラグ取得
   
   検証環境のネットワークに接続し、目的のリソースを確認
```

注意点として、MDK4はWi-Fiパスワードを直接解析するツールではありません。主に802.11のフレームを操作するツールです。

また、d や a などには通信妨害を引き起こす機能があります。自分の隔離された検証環境に限定してください。
# 6. 参考資料

- [Kali Linux Tools - MDK4](https://www.kali.org/tools/mdk4/?utm_source=chatgpt.com)
- [Debian MDK4 Manual](https://sources.debian.org/src/mdk4/4.1%2Bgit20200420-2/README.md?utm_source=chatgpt.com)
- [MDK4 Source README](https://sources.debian.org/src/mdk4/4.1%2Bgit20200420-2/README.md?utm_source=chatgpt.com)
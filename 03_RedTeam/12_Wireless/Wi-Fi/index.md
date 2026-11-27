---
title: Wi-Fi
---
# Wi-Fi Security Cheat Sheet

## 無線LAN偵察・状態分析・攻撃選定・検証

- 対象環境：Kali Linux
    
- 対象範囲：IEEE 802.11 / Wi-Fi全般
    
- 用途：学習・許可された検証環境・Wi-Fi Challenge Labs
    
- 方針：コマンドの暗記ではなく、観測結果から攻撃手法を選択できるようにする
    

---

# 1. Wi-Fiテストの基本フロー

Wi-Fiのセキュリティテストは、以下の順序で進める。

```
flowchart TD
    A["1. Reconnaissance<br/>周辺無線環境の偵察"]
    B["2. Enumeration<br/>対象AP・クライアントの状態確認"]
    C["3. Attack Selection<br/>観測結果から攻撃を選定"]
    D["4. Execution<br/>許可された環境で検証"]
    E["5. Validation<br/>結果・影響・成立条件を確認"]
    F["6. Reporting<br/>脆弱性と対策を整理"]

    A --> B --> C --> D --> E --> F
    E -->|"追加情報が必要"| B
```

## 各段階で確認すること

|段階|確認事項|
|---|---|
|偵察|SSID、BSSID、チャンネル、周波数、暗号化方式|
|状態確認|認証方式、EAP方式、PMF、WPS、接続クライアント|
|攻撃選定|どの脆弱性・設定不備が攻撃成立条件を満たすか|
|実行|適切なツール・手法を選択|
|検証|認証突破、通信内容、取得情報、影響範囲|
|報告|成立条件、再現方法、リスク、対策|

重要なのは、**攻撃手法を先に決めないこと**。

例えば、WPA2という情報だけでは攻撃方法は決められない。PSKなのかEnterpriseなのか、PMFが有効なのか、クライアントがどのEAP方式を使用しているのかを確認する必要がある。

---

# 2. Wi-Fiの基礎知識

## 2.1 IEEE 802.11の主要規格

|規格|世代|周波数帯|
|---|---|---|
|802.11a|Wi-Fi 2|5GHz|
|802.11b|Wi-Fi 1|2.4GHz|
|802.11g|Wi-Fi 3|2.4GHz|
|802.11n|Wi-Fi 4|2.4 / 5GHz|
|802.11ac|Wi-Fi 5|5GHz|
|802.11ax|Wi-Fi 6 / 6E|2.4 / 5 / 6GHz|
|802.11be|Wi-Fi 7|2.4 / 5 / 6GHz|

## 2.2 Wi-Fiで登場する識別情報

|用語|説明|
|---|---|
|SSID|無線LANのネットワーク名|
|BSSID|APの無線インターフェースを識別するMACアドレス|
|ESSID|複数APで構成されるネットワークの識別名として使われる表現|
|MAC Address|無線インターフェースのMACアドレス|
|Channel|APが通信に使用するチャンネル|
|Band|2.4GHz / 5GHz / 6GHz|
|RSSI|受信信号強度|
|Beacon|APが定期的に送信する管理フレーム|
|Probe Request|クライアントがネットワークを探索する際に送信するフレーム|
|Probe Response|APがProbe Requestに応答するフレーム|
|Association|クライアントがAPに接続する処理|
|Authentication|802.11における認証処理。暗号化方式の認証とは区別する|

**注意：SSIDとBSSIDは別物。**

- SSID：ネットワーク名
    
- BSSID：AP側の無線インターフェースの識別子
    

同じSSIDを複数のAPが提供する場合、BSSIDはそれぞれ異なる。

---

# 3. 偵察（Reconnaissance）

## 3.1 無線インターフェースの確認

### インターフェース一覧

```
iw dev
```

```
ip link show
```

```
iw list
```

確認事項：

- インターフェース名
    
- PHY
    
- Interface type
    
- 対応周波数帯
    
- 対応チャンネル
    
- Monitor Mode対応状況
    

### インターフェースの状態確認

```
iw dev wlan0 info
```

```
rfkill list
```

### Monitor Modeへの変更

```
sudo ip link set wlan0 down
sudo iw dev wlan0 set type monitor
sudo ip link set wlan0 up
```

確認：

```
iw dev
```

通常モードに戻す場合：

```
sudo ip link set wlan0 down
sudo iw dev wlan0 set type managed
sudo ip link set wlan0 up
```

※NetworkManagerやwpa_supplicantが管理している場合は、状態に応じた調整が必要。安易に関連サービスを停止しない。

## 3.2 チャンネル・周波数の確認

```
iw list
```

```
iw dev wlan0 info
```

チャンネルを指定：

```
sudo iw dev wlan0 set channel 44
```

周波数で指定：

```
sudo iw dev wlan0 set freq 5220
```

※実際に設定できるチャンネルは、無線NIC・ドライバ・規制・地域設定に依存する。

## 3.3 周辺APの検出

### airodump-ng

```
sudo airodump-ng wlan0
```

特定チャンネル：

```
sudo airodump-ng --channel 44 wlan0
```

特定BSSIDを対象にする：

```
sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF \
  --channel 44 wlan0
```

キャプチャ保存：

```
sudo airodump-ng \
  --bssid AA:BB:CC:DD:EE:FF \
  --channel 44 \
  --write wifi_capture \
  wlan0
```

### 確認する情報

|項目|意味|次に確認すること|
|---|---|---|
|BSSID|APの識別子|対象APの特定|
|PWR|受信信号強度|電波状況|
|CH|チャンネル|キャプチャ条件|
|ENC|暗号化方式|セキュリティ方式|
|CIPHER|暗号アルゴリズム|CCMP / TKIPなど|
|AUTH|認証方式|PSK / MGTなど|
|ESSID|ネットワーク名|対象ネットワークの識別|
|STATION|クライアントMAC|接続端末の把握|

## 3.4 パケットキャプチャ

```
sudo tcpdump -i wlan0 -w wifi.pcap
```

Wiresharkで開く：

```
wireshark wifi.pcap
```

表示フィルタ例：

```
wlan
wlan.fc.type == 0
wlan.fc.type == 1
wlan.fc.type == 2
eap
eapol
wlan.bssid == aa:bb:cc:dd:ee:ff
```

802.11フレームの種類：

|Type|分類|代表例|
|---|---|---|
|0|Management|Beacon / Probe / Authentication|
|1|Control|ACK / RTS / CTS|
|2|Data|データ通信|

---

# 4. 対象の状態確認（Enumeration）

攻撃手法を選定する前に、以下を確認する。

## 4.1 暗号化・認証方式

|観測結果|意味|
|---|---|
|WEP|古い暗号化方式|
|WPA-PSK|WPAの事前共有鍵方式|
|WPA2-PSK|WPA2の事前共有鍵方式|
|WPA2-MGT|WPA2 Enterprise系の認証|
|WPA3-SAE|SAEを使用するPersonal方式|
|WPA3-Enterprise|Enterprise方式|
|OWE|オープンネットワークの暗号化|
|Open|暗号化なし|

※airodump-ngの表示名やツールによる表記は異なる。RSN Information ElementやBeaconの情報も確認する。

## 4.2 WPA / RSNの確認項目

|項目|確認内容|
|---|---|
|Authentication|PSK / 802.1X / SAE|
|Pairwise Cipher|CCMP / GCMP / TKIP|
|Group Cipher|グループ通信の暗号|
|AKM|認証・鍵管理方式|
|PMF|Protected Management Frames|
|WPA Version|WPA / WPA2 / WPA3|

## 4.3 PMF（802.11w）

PMFは管理フレームを保護する仕組み。

|設定|意味|
|---|---|
|Disabled|無効|
|Capable|対応可能|
|Required|必須|

確認する理由：

- Deauthentication攻撃への耐性
    
- Disassociation攻撃への耐性
    
- WPA3での必須要件との関係
    

PMFがRequiredなら、保護対象となる管理フレームに対する従来型の偽装攻撃は制約される。

## 4.4 WPS

WPS（Wi-Fi Protected Setup）は、端末を簡単にAPへ接続するための仕組み。

確認：

```
sudo wash -i wlan0
```

確認すること：

- WPS対応の有無
    
- WPSのバージョン
    
- Lock状態
    
- APのBSSID
    
- チャンネル
    

WPSが有効であることだけで脆弱性が確定するわけではない。PIN方式の実装・ロックアウト・設定状況を確認する。

## 4.5 Enterprise / EAP

Enterpriseでは、APとRADIUSサーバーを使用した認証が行われる。

代表的なEAP方式：

|EAP方式|特徴|確認ポイント|
|---|---|---|
|EAP-TLS|クライアント証明書を使用|証明書の管理・検証|
|PEAP-MSCHAPv2|TLSトンネル内でMSCHAPv2|サーバー証明書検証|
|EAP-TTLS|TLSトンネル内で追加認証|内部認証方式|
|EAP-FAST|PACを利用する方式|PAC管理・設定|
|EAP-MD5|チャレンジレスポンス型|相互認証・暗号化の不足|

確認すること：

- 外側EAP方式
    
- 内側認証方式
    
- RADIUSサーバー証明書
    
- クライアント側の証明書検証
    
- ユーザー名の形式
    
- ドメイン情報
    

**重要：EAP-TLSとPEAP-MSCHAPv2では、成立する攻撃の前提が大きく異なる。**

---

# 5. 攻撃選定（Attack Selection）

この章が本チートシートの中心。

観測した状態から、候補となる攻撃を選択する。

## 5.1 認証方式別の攻撃選定

|観測した状態|攻撃候補|成立条件・注意点|
|---|---|---|
|WEP|IV収集・鍵解析|対象通信と十分なIV収集が必要|
|WPA/WPA2-PSK|4-way handshake解析|対象認証交換の取得と候補パスワードが必要|
|WPA/WPA2-PSK|PMKID解析|対象APが取得可能な情報を応答すること|
|WPA2-Enterprise PEAP-MSCHAPv2|Rogue APを用いた認証情報検証|クライアントの接続動作や証明書検証に依存|
|WPA2-Enterprise EAP-TLS|証明書・PKI設定の検証|クライアント証明書の管理や検証設定が焦点|
|WPA3-SAE|SAE実装・設定の検証|PSK方式の一般的なHandshake解析とは異なる|
|Open|通信の盗聴・改ざんリスク検証|暗号化されていない通信が対象|
|OWE|暗号化・接続先検証の確認|認証がないことと暗号化がないことは別|
|WPS有効|WPS設定・実装の検証|PIN方式・ロックアウト等の条件による|
|PMF Disabled|管理フレーム保護の検証|対象フレームやクライアントの挙動による|
|Probe Request|情報漏えいの確認|端末がSSIDを含む要求を送信する場合|
|複数APで同一SSID|ローミング・設定不整合の検証|AP間の設定差異を確認|
|不審な同一SSIDのAP|Evil Twinの検証|クライアントの接続先選択と認証検証に依存|

## 5.2 WPA/WPA2-PSKの場合

確認順序：

```
WPA/WPA2-PSKを確認
        |
        v
対象APのBSSIDを特定
        |
        v
Handshake / PMKID取得可能性を確認
        |
        v
取得できたか？
   |             |
  Yes            No
   |             |
   v             v
候補鍵の検証    取得条件を再評価
   |
   v
パスフレーズ強度を評価
```

重要事項：

- Handshake取得はパスワード解読の成功を意味しない。
    
- オフライン解析は候補パスワードの品質に依存する。
    
- WPA3-SAEをWPA2-PSKと同じ手順で扱わない。
    
- WPA2の設定や実装によって、取得できる情報や攻撃可能性は変わる。
    

## 5.3 Enterpriseの場合

```
802.1X / Enterpriseを確認
        |
        v
EAP方式を特定
        |
        +--------------------+
        |                    |
        v                    v
PEAP / TTLS              EAP-TLS
        |                    |
        v                    v
内部認証方式を確認       証明書・PKIを確認
        |                    |
        v                    v
証明書検証設定を確認     証明書管理・失効確認
        |                    |
        v                    v
認証情報保護を評価       クライアント認証を評価
```

特にPEAP-MSCHAPv2では、サーバー証明書の検証が重要。

証明書を検証しないクライアントは、不正な認証サーバーに接続してしまうリスクがある。

一方、EAP-TLSではクライアント証明書を用いるため、単純なパスワード辞書攻撃とは評価対象が異なる。

## 5.4 攻撃選定時のチェックリスト

- 対象SSID・BSSIDを特定した
    
- 周波数帯・チャンネルを確認した
    
- 暗号化方式を確認した
    
- 認証方式を確認した
    
- AKMを確認した
    
- PMFの設定を確認した
    
- WPSの状態を確認した
    
- クライアントの挙動を確認した
    
- 攻撃の成立条件を確認した
    
- 成立しない条件も確認した
    
- 検証範囲と許可を確認した
    

---

# 6. 攻撃・検証ツール

|ツール|用途|
|---|---|
|iw|無線インターフェース管理|
|airmon-ng|Monitor Mode管理|
|airodump-ng|AP・クライアントの偵察、キャプチャ|
|aireplay-ng|無線フレームの送信・検証|
|aircrack-ng|WEP/WPA系の鍵解析|
|wash|WPS対応APの検出|
|reaver|WPS PINの検証|
|hcxdumptool|無線環境のキャプチャ|
|hcxpcapngtool|キャプチャ形式の変換・解析|
|hashcat|対応するハッシュ形式の解析|
|Wireshark|パケット解析|
|tshark|CLIでのパケット解析|
|hostapd|Linux上でのAP構築|
|hostapd-mana|認証方式等の検証用AP|
|wpa_supplicant|Wi-Fiクライアント接続・認証|
|eaphammer|Enterprise Wi-Fi検証|
|wpa_sycophant|Enterprise認証のリレー検証|
|bettercap|ネットワーク調査・検証|
|Kismet|無線ネットワーク監視・検出|

※ツールの利用可否やオプションはバージョン・ドライバ・無線NICによって異なる。

---

# 7. キャプチャ解析

## 7.1 PCAPの基本確認

```
capinfos wifi.pcap
```

```
tshark -r wifi.pcap
```

EAPOL：

```
tshark -r wifi.pcap -Y eapol
```

EAP：

```
tshark -r wifi.pcap -Y eap
```

Beacon：

```
tshark -r wifi.pcap -Y "wlan.fc.type_subtype == 0x08"
```

Probe Request：

```
tshark -r wifi.pcap -Y "wlan.fc.type_subtype == 0x04"
```

Authentication：

```
tshark -r wifi.pcap -Y "wlan.fc.type_subtype == 0x0b"
```

Association Request：

```
tshark -r wifi.pcap -Y "wlan.fc.type_subtype == 0x00"
```

## 7.2 Wiresharkで注目するプロトコル

|プロトコル|確認目的|
|---|---|
|IEEE 802.11|管理・制御・データフレーム|
|EAP|認証方式|
|EAPOL|802.1X関連通信|
|RADIUS|認証サーバーとの通信|
|DHCP|IPアドレス取得|
|DNS|名前解決|
|ARP|IPとMACの対応|
|TLS|暗号化通信|

---

# 8. クライアント側の調査

APだけでなく、クライアント側の設定・挙動も重要。

## 8.1 Linux

接続状況：

```
iw dev
```

```
nmcli device status
```

```
nmcli connection show
```

接続中のWi-Fi情報：

```
iw dev wlan0 link
```

wpa_supplicantの状態：

```
ps aux | grep wpa_supplicant
```

## 8.2 Windows

無線LANインターフェース：

```
netsh wlan show interfaces
```

保存済みプロファイル：

```
netsh wlan show profiles
```

特定プロファイルの設定：

```
netsh wlan show profile name="SSID"
```

ドライバ情報：

```
netsh wlan show drivers
```

## 8.3 クライアント側の確認事項

- 保存済みSSID
    
- 自動接続設定
    
- 認証方式
    
- EAP方式
    
- サーバー証明書の検証設定
    
- 信頼する認証サーバー名
    
- クライアント証明書
    
- ローミング挙動
    

---

# 9. Wi-Fi特有の攻撃カテゴリ

|カテゴリ|概要|主な確認対象|
|---|---|---|
|Passive Reconnaissance|受動的な無線情報収集|Beacon / Probe|
|WEP Cracking|WEPの暗号化上の問題を検証|IV / WEP鍵|
|WPA Handshake Analysis|PSKの強度を検証|4-way handshake|
|PMKID Analysis|PMKIDを利用した検証|PMKID|
|WPS Assessment|WPSの設定・実装を検証|PIN / Lock|
|Deauthentication|管理フレームによる切断の検証|PMF / クライアント|
|Evil Twin|正規APを装う不正APのリスク検証|SSID / BSSID / 証明書|
|Rogue AP|許可されていないAPの検出・評価|APの設置・認証|
|Enterprise Wi-Fi Assessment|802.1X / EAPの設定評価|RADIUS / EAP|
|Credential Relay|認証情報の中継リスクを検証|EAP / MSCHAPv2|
|Probe Request Analysis|端末情報の漏えいを評価|Probe Request|
|Client-Side Assessment|クライアントの接続設定を評価|プロファイル|
|Roaming Assessment|AP間の移動・認証を評価|802.11r / k / v|
|Wireless DoS|無線通信妨害の耐性を評価|管理フレーム・電波環境|

---

# 10. 防御・検知の観点

攻撃を理解するためには、防御側の観点も押さえる。

|リスク|防御策|
|---|---|
|WEP利用|WPA2-AES以上へ移行|
|弱いPSK|十分に長くランダムなパスフレーズ|
|WPA2 Enterpriseの証明書検証不足|信頼するCA・サーバー名を適切に設定|
|不正AP|WIDS / WIPSによる監視|
|Deauthentication|PMFのRequired化を検討|
|WPSの悪用|不要なら無効化|
|Rogue AP|AP管理・資産管理|
|クライアントの自動接続|接続プロファイルの管理|
|証明書の不適切な管理|PKI・失効・更新管理|
|古い暗号スイート|暗号方式・AKMの見直し|

## 検知で注目する情報

- 同一SSIDで異なるBSSIDが出現
    
- 正規APと異なる暗号化方式
    
- 不自然なチャンネル変更
    
- 不審なDeauthentication / Disassociation
    
- 認証失敗の急増
    
- RADIUS認証ログの異常
    
- WPS関連イベント
    
- 不審なProbe Request
    
- 不正APの設置
    

---

# 11. 実践時の記録テンプレート

Wi-Fi Challenge Labsや検証環境では、次の形式で記録する。

## 対象情報

|項目|値|
|---|---|
|SSID||
|BSSID||
|Channel||
|Frequency||
|Band||
|Encryption||
|Authentication||
|Cipher||
|AKM||
|PMF||
|WPS||
|EAP||

## 状態分析

|確認項目|観測結果|判断|
|---|---|---|
|認証方式|||
|暗号化方式|||
|クライアントの接続状況|||
|証明書検証|||
|PMF|||
|WPS|||

## 攻撃選定

|項目|内容|
|---|---|
|観測した事実||
|想定される弱点||
|攻撃候補||
|選定理由||
|成立条件||
|成立しない条件||
|使用ツール||

## 実行・検証結果

|項目|内容|
|---|---|
|実行コマンド||
|取得した情報||
|結果||
|成功・失敗の理由||
|対策||

---

# 12. 学習・拡張方針

このチートシートはマスターインデックスとして使用し、各技術の詳細は個別ページに分けていく。

推奨するページ構成：

```
WiFi/
├── index.md
├── fundamentals.md
├── reconnaissance.md
├── frame-analysis.md
├── authentication/
│   ├── index.md
│   ├── wep.md
│   ├── wpa-psk.md
│   ├── wpa3-sae.md
│   └── enterprise-eap.md
├── attacks/
│   ├── index.md
│   ├── handshake-analysis.md
│   ├── pmkid.md
│   ├── wps.md
│   ├── deauthentication.md
│   ├── evil-twin.md
│   ├── rogue-ap.md
│   └── roaming.md
├── client/
│   ├── index.md
│   ├── linux.md
│   └── windows.md
├── analysis/
│   ├── wireshark.md
│   ├── eap-analysis.md
│   └── radius-analysis.md
└── detection-defense.md
```

各ページは共通して次の構成にする。

1. 技術概要
    
2. 仕組み・プロトコル
    
3. 偵察方法
    
4. 状態確認方法
    
5. 攻撃が有効になる条件
    
6. 攻撃が成立しない条件
    
7. 攻撃手法の選定
    
8. 実行コマンド
    
9. 成功確認・失敗時の分析
    
10. 防御・検知

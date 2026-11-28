# **コマンド解説**

`hostapd-mana` は、**偽のWi-Fiアクセスポイント（Rogue AP）を構築するためのツール**です。

Kali Linuxに含まれる無線セキュリティ監査ツール群の一つで、通常の `hostapd` をベースに、Wi-Fi認証の検証やクライアントの認証情報取得を想定した機能が追加されています。

特に、WiFi Challenge LabやOSWPの学習では、**Evil Twin攻撃や偽アクセスポイントを利用した認証情報の検証**を理解するうえで重要です。

## **1. hostapd-mana とは**

[Rogue Access Points, a threat to the network](https://images.openai.com/static-rsc-4/zcuHoBtk3WBuE_DBJlKCIZjEoKbArWTKapkmIjIUgP2LIKjVu60HpgJszkVX6q5j0xPlittFCIqTve_CBjLmGoePHmxuT-PFWoTMpFQ_l6as2CR8VbT1FnUOAhuswfakxx1PHgkN-xlHEGfltACFO2pEFlC_GISHo1mZ_7u4TME?purpose=inline)

**hostapd-mana**

偽のアクセスポイントを動作させ、接続してきた無線クライアントとの認証処理を検証するツール。

通常の `hostapd` と比較すると、次のような違いがあります。

| 機能         | hostapd  | hostapd-mana |
| ---------- | -------- | ------------ |
| AP構築       | ○        | ○            |
| WPA/WPA2認証 | ○        | ○            |
| Evil Twin  | 標準機能ではない | 対応           |
| EAP認証の検証   | ○        | 拡張機能あり       |
| 認証情報の収集    | 限定的      | 対応           |

## **2. 主な機能**

| 機能                 | 概要                            |
| ------------------ | ----------------------------- |
| Rogue AP           | 偽アクセスポイントの構築                  |
| Evil Twin          | 正規APになりすましたAPの構築              |
| MANA               | クライアントの認証情報を取得するための拡張機能       |
| Karma              | クライアントのProbe Requestを利用したAP偽装 |
| EAP攻撃              | 802.1X/EAP認証のセキュリティ検証         |
| Credential Capture | 認証時の情報を記録                     |

## **3. MANA / KARMA の違い**

ここは重要なので整理します。

**KARMA**

Probe Requestを利用

クライアントが過去に接続したSSIDなどをProbe Requestで問い合わせると、そのSSIDになりすましたAPが応答する仕組みです。

**MANA**

KARMAの拡張

KARMAの仕組みを拡張し、複数端末のProbe Requestなどを利用して、より柔軟に偽APを構築します。

### **設定ファイルの主要パラメータ**

`hostapd-mana` は通常、設定ファイル（hostapd.conf）を指定して起動します。

| パラメータ          | 意味              |
| -------------- | --------------- |
| `interface`    | 使用する無線インターフェース  |
| `ssid`         | APのSSID         |
| `channel`      | Wi-Fiチャンネル      |
| `hw_mode`      | 無線モード（g/aなど）    |
| `enable_mana`  | MANA機能を有効化      |
| `mana_loud`    | 学習したSSIDを広く広告   |
| `mana_wpe`     | EAP認証情報取得機能を有効化 |
| `mana_outfile` | MANAのログ出力先      |

例えば、基本的な設定例は次のようになります。

```
interface=wlan0
ssid=TestAP
channel=6
hw_mode=g

enable_mana=1
mana_loud=1
```

これは検証用APの基本設定例です。実際の動作には無線アダプタのAPモード対応などが必要です。

[image](https://www.google.com/s2/favicons?domain=https://github-wiki-see.page\&sz=32)

sensepost/hostapd-mana GitHub Wiki+1



## **4. EAP認証とWPE**

OSWP学習で特に理解しておきたい機能です。

`mana_wpe=1` を設定すると、対応するEAP認証方式で認証情報を取得する機能が有効になります。

代表的な対象は以下です。

- PEAP/MSCHAPv2
- PEAP/GTC
- EAP-TTLS
- EAP-MD5

例えば、PEAP/MSCHAPv2では認証時のチャレンジレスポンスを取得し、オフライン解析の対象にできます。

注意点として、これは通常のWPA2-PersonalのWi-Fiパスワード取得とは別の仕組みです。

![[Pasted image 20261117034242.png]]

sensepost/hostapd-mana GitHub Wiki



## **5. 起動方法・オプション**

基本構文：

```
sudo hostapd-mana <設定ファイル>
```

主なオプション：

| オプション | 意味           |
| ----- | ------------ |
| `-h`  | ヘルプ表示        |
| `-d`  | デバッグ情報表示     |
| `-dd` | 詳細なデバッグ情報    |
| `-B`  | バックグラウンド起動   |
| `-t`  | タイムスタンプ表示    |
| `-v`  | バージョン表示      |
| `-i`  | 使用インターフェース指定 |

[image](https://www.google.com/s2/favicons?domain=https://www.kali.org\&sz=32)

Kali Linux Tools

## **6. OSWP学習での位置付け**

今回取り組んでいるWiFi Challenge Labの学習では、次のように整理すると理解しやすいです。

| ツール            | 役割                    |
| -------------- | --------------------- |
| `airmon-ng`    | モニターモードへの切り替え         |
| `airodump-ng`  | AP・クライアントの調査          |
| `aireplay-ng`  | フレーム送信・再送攻撃           |
| `aircrack-ng`  | キャプチャした鍵の解析           |
| `airdecap-ng`  | 暗号化キャプチャの復号           |
| `hostapd-mana` | Rogue AP・Evil Twinの構築 |

**特に覚えておきたいこと：**

- `airodump-ng`：周囲のWi-Fiを調査する
- `hostapd-mana`：偽のWi-Fiアクセスポイントを構築する
- `aircrack-ng`：取得した認証情報を解析する

公式資料：

- [Kali Linux - hostapd-mana](https://www.kali.org/tools/hostapd-mana/?utm_source=chatgpt.com)
- [hostapd-mana GitHub README](https://git.mitgai.net/sensepost/hostapd-mana/blob/mana-2.12/Readme.md?utm_source=chatgpt.com)
- [MANA EAP Options](https://github-wiki-see.page/m/sensepost/hostapd-mana/wiki/MANA-EAP-Options-%28aka-WPE%29?utm_source=chatgpt.com)

次は、**hostapd-manaと通常のhostapdの違いを、Evil Twin攻撃の通信フロー図で理解する**と、OSWPの学習につながります。

--- 

`hostapd` と `hostapd-mana` の違いは、簡単にいうと **通常のWi-Fiアクセスポイントを構築するか、無線セキュリティ検証向けの攻撃機能を追加したアクセスポイントを構築するか** です。

## **1. 機能比較**

| 機能          | hostapd | hostapd-mana |
| ----------- | ------- | ------------ |
| 通常のAP構築     | ○       | ○            |
| WPA/WPA2認証  | ○       | ○            |
| SSID偽装      | ○       | ○            |
| Evil Twin構築 | 設定次第    | 対応           |
| KARMA       | ×       | ○            |
| MANA        | ×       | ○            |
| EAP認証情報の取得  | ×       | ○（WPE機能）     |

## **2. 動作イメージ**

**通常のhostapd**

![[Pasted image 20261117034440.png]]

**hostapd-mana**

![[Pasted image 20261117034418.png]]

## **3. 重要な違いは3つ**

- **KARMA**：クライアントのProbe Requestに応答し、過去に接続したSSIDなどを利用して偽APを構築する。
- **MANA**：KARMAを拡張し、クライアントのProbe Requestに対する応答をより柔軟に行う。
- **WPE**：EAP認証のチャレンジレスポンスなどを取得するための機能。

## **4. OSWP学習での覚え方**

- `hostapd` = Wi-Fi APを作るソフトウェア
- `hostapd-mana` = Wi-Fi APを作る機能に、無線セキュリティ検証用の機能を追加したもの

つまり、`hostapd-mana` は `hostapd` の単なる別名ではなく、攻撃検証向けに拡張された実装です。

**補足：** Evil Twin自体はhostapd-mana専用の攻撃ではありません。通常のhostapdでも設定や周辺環境次第で偽APを構築できます。
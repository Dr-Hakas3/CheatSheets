---
tags:
  - evil-twin
---
# What is the wifi-mobile AP password?

```zsh
sudo airodump-ng wlan60
```

![[Pasted image 20261117015422.png]]

```
F0:9F:C2:71:22:12
```

```zsh
sudo airodump-ng wlan60 -c 6 -w wifi-mobile
```

![[Pasted image 20261117023630.png]]
![[Pasted image 20261117023652.png]]

## Deauthentication Attack

```zsh
sudo aireplay-ng -0 10 -a F0:9F:C2:71:22:12 wlan60
```

![[Pasted image 20261117023731.png]]

```zsh
dpkg -L seclists | grep -i xato
```

![[Pasted image 20261117030250.png]]

```zsh
sudo aircrack-ng wifi-mobile-05.cap -w /usr/share/wordlists/seclists/Passwords/Common-Credentials/xato-net-10-million-passwords-1000000.txt
```

![[Pasted image 20261117030413.png]]
![[Pasted image 20261117030430.png]]

```
starwars1
```

---

# 解説
このチャレンジは、**WPA/WPA2-PSKで保護されたWi-Fiのパスワードを、4-way handshakeのキャプチャとオフライン辞書攻撃によって特定する問題**です。

OSWPでも重要になる基本的な攻撃手法です。

今回は、コマンドの意味だけでなく、なぜこの手順でパスワードが判明するのかを順番に解説します。

# **1. 攻撃の全体像**

まず、今回の攻撃フローを理解しましょう。

## **WPA/WPA2-PSK パスワード解析フロー**

1. **対象APを特定する**

   BSSID、チャンネル、暗号化方式を確認する。

2. **通信をキャプチャする**

   `airodump-ng` で無線通信を取得する。

3. **クライアントの再接続を発生させる**

   `aireplay-ng` でDeauthenticationを送信する。

4. **4-way handshakeを取得する**

   クライアントが再接続するときの認証通信を記録する。

5. **オフライン辞書攻撃**

   `aircrack-ng` で候補パスワードを検証する。

6. Goal

   **パスワードを特定する**

   今回の答えは `starwars1`

# **2. airodump-ng：通信のキャプチャ**

```
sudo airodump-ng wlan0mon -c 6 -w wifi-mobile
```

各オプションを分解します。

| オプション            | 意味                    |
| ---------------- | --------------------- |
| `sudo`           | 管理者権限で実行              |
| `airodump-ng`    | 無線パケットのキャプチャ          |
| `wlan0mon`       | Monitor Modeのインターフェース |
| `-c 6`           | チャンネル6に固定             |
| `-w wifi-mobile` | キャプチャファイルの保存名         |

### **なぜチャンネルを固定する？**

Wi-FiのAPはそれぞれ特定のチャンネルで通信しています。

今回の対象APがチャンネル6で動作しているため、チャンネル6に固定して通信を監視します。

チャンネルを固定することで、対象APとクライアントの通信を継続的にキャプチャできます。

### **-w の意味**

キャプチャした通信はファイルに保存されます。

例えば以下のようになります。

```
wifi-mobile-01.cap
```

このファイルには無線通信のパケットが記録されます。

重要なのは、**この時点ではまだWi-Fiパスワードを取得できていない**ということです。

# **3. aireplay-ng：Deauthentication Attack**

```
aireplay-ng -0 10 -a F0:9F:C2:71:22:12 wlan0mon
```

このコマンドは、対象APに接続しているクライアントを切断させ、再接続を誘発するためのものです。

| オプション         | 意味                            |
| ------------- | ----------------------------- |
| `aireplay-ng` | 無線パケットの送信・再送信などを行うツール         |
| `-0`          | Deauthentication Attack       |
| `10`          | Deauthenticationフレームの送信回数     |
| `-a`          | 対象APのBSSID                    |
| `wlan0mon`    | パケットを送信するMonitor Modeインターフェース |

### **そもそもDeauthenticationとは？**

Wi-Fiには、クライアントとAPの接続を解除するためのDeauthenticationフレームがあります。

通常は、以下のような状況で利用されます。

- クライアントがAPから切断される
- APがクライアントを切断する
- クライアントが別のAPに接続し直す

この仕組みを悪用して、攻撃者が偽のDeauthenticationフレームを送信します。

**Deauthentication Attackのイメージ**

**Wi-Fi AP**

**偽のDeauthenticationフレーム**

攻撃者からクライアントに送信

**Wi-Fiクライアント**

切断 → 再接続

### **なぜ切断させる必要がある？**

ここが今回の重要ポイントです。

WPA/WPA2-PSKでは、クライアントがAPに接続するときに4-way handshakeという認証処理が行われます。

しかし、すでに接続済みのクライアントがいる場合、4-way handshakeは通常の再接続時まで発生しません。

そこでDeauthentication Attackを使います。

1. クライアントを切断させる。
2. クライアントがAPに再接続する。
3. 再接続時に4-way handshakeが発生する。
4. その通信をairodump-ngでキャプチャする。

つまり、**4-way handshakeを取得するために、再接続を強制的に発生させている**わけです。

なお、Deauthenticationフレームは送信回数を指定しているだけで、必ずクライアントが切断される保証はありません。PMF（802.11w）が有効な場合などは攻撃が防がれることもあります。

# **4. 4-way handshakeとは？**

ここはOSWP学習で特に理解しておきたい部分です。

4-way handshakeとは、Wi-FiクライアントとAPが共通の暗号鍵を安全に生成・確認するための4段階の通信です。

![[Pasted image 20261117024525.png]]

簡単に説明すると次のようになります。

| メッセージ     | 内容                    |
| --------- | --------------------- |
| Message 1 | APからクライアントへANonceを送信  |
| Message 2 | クライアントからSNonceとMICを送信 |
| Message 3 | APからGTKなどの情報を送信       |
| Message 4 | クライアントが完了を通知          |

ここで重要なのが次の3つです。

- **PSK**：Wi-Fiに接続するときに使用する事前共有パスワード
- **PMK**：PSKなどから導出されるPairwise Master Key
- **MIC**：メッセージの整合性を検証するための値

WPA2-PSKの場合、PSKとSSIDからPMKが導出されます。

そして4-way handshakeで交換される情報を使って、候補パスワードが正しいかどうかを検証できます。

つまり、パスワードそのものが無線通信に平文で流れているわけではありません。

# **5. aircrack-ng：辞書攻撃**

```
aircrack-ng wifi-mobile-01.cap \
-w /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-1000000.txt
```

ここで取得したhandshakeを使って、パスワードを解析します。

| オプション                                       | 意味                |
| ------------------------------------------- | ----------------- |
| `aircrack-ng`                               | WPA/WPA2などの鍵解析ツール |
| `wifi-mobile-01.cap`                        | キャプチャファイル         |
| `-w`                                        | 辞書ファイルの指定         |
| `xato-net-10-million-passwords-1000000.txt` | パスワード候補のリスト       |

### **オフライン辞書攻撃の仕組み**

例えば辞書に以下の候補が入っているとします。

```
password123
admin123
qwerty123
starwars1
letmein123
```

aircrack-ngは候補を1つずつ検証します。

処理の概念は次のとおりです。

![[Pasted image 20261117024451.png]]

# **Password Found**

ここで重要なのは、**攻撃者はAPに何度も接続を試みているわけではない**ということです。

一度handshakeを取得すれば、その後はキャプチャファイルを使ってローカル環境でパスワード候補を検証できます。

そのため、通常のオンラインログイン試行のようなアカウントロックアウトの仕組みでは防げません。

# **6. airdecap-ngについて**

教材には次の記述があります。

> waiting a few minutes capturing with airodump-ng to be able to decipher the traffic later using airdecap-ng.

ここは少し補足が必要です。

`airdecap-ng` は、取得した暗号化済み無線通信を復号するためのツールです。

例えば、パスワードが判明した後に以下のように使います。

```
airdecap-ng -e "SSID" -p "starwars1" wifi-mobile-01.cap
```

- `-e`：SSID
- `-p`：PSK
- `.cap`：キャプチャファイル

ただし、今回のパスワード解析自体にはairdecap-ngは必須ではありません。

また、通信内容を復号するには、必要な鍵情報や対象通信がキャプチャされている必要があります。

# **7. 今回のチャレンジの重要ポイント**

| ツール           | 役割      | 覚えること            |
| ------------- | ------- | ---------------- |
| `airodump-ng` | 通信キャプチャ | handshake取得      |
| `aireplay-ng` | パケット送信  | Deauthentication |
| `aircrack-ng` | パスワード解析 | 辞書攻撃             |
| `airdecap-ng` | 通信復号    | 暗号化通信の復号         |

**今回の本質は「PSKそのものを盗む」のではなく、「認証時の通信を取得して、オフラインでPSKを推測する」ことです。**

# **8. OSWP試験対策として理解しておくこと**

次の4点を押さえておくとよいです。

1. WPA/WPA2-PSKの4-way handshakeが何のために存在するか。
2. なぜDeauthentication Attackでhandshake取得を促進できるか。
3. handshakeがあれば、なぜオフライン辞書攻撃が可能なのか。
4. なぜ辞書に正解のパスワードがなければ解析できないのか。

特に4番目は重要です。

辞書攻撃は、辞書に含まれている候補を検証するだけです。パスワードが複雑で辞書に存在しなければ、解析できません。

**次に理解するとよいテーマは「WPA2のPMK・PTK・GTKの関係」です。** ここが分かると、4-way handshakeの各メッセージが何をしているのか、暗号学的な仕組みまで理解できるようになります。

---


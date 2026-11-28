airdecap-ng は、無線LANのキャプチャファイル（.cap / .pcap）を復号するツールです。

Aircrack-ngスイートに含まれており、主に Wi-Fi のパケット解析で使用します。

今回取り組んでいる WiFi Challenge Lab のような環境では、airodump-ng で取得したキャプチャファイルから、暗号化された通信を復号して中身を解析する場面で使います。
1. 何をするツールなのか
例えば、WPA2-PSKで保護されたWi-Fi通信をキャプチャした場合を考えます。

![[Pasted image 20261117032004.png]]

重要なのは、airdecap-ng 自体がパスワードを解析するツールではないことです。

すでに取得したパスワードや鍵を使って復号します。
2. 基本構文
airdecap-ng [オプション] <captureファイル>


代表的なオプションは以下のとおりです。
オプション	意味
-e	ESSID（Wi-FiのSSID）を指定
-p	WPA/WPA2のパスフレーズを指定
-k	WPA/WPA2のPMKを指定
-w	WEPキーを指定

3. WPA/WPA2の復号
今回のWiFi Challenge Labで重要になる使い方です。
airdecap-ng -e "TargetSSID" -p "password123" capture.cap


引数	意味
-e	対象SSIDを指定
-p	Wi-Fiのパスフレーズを指定
capture.cap	入力するキャプチャファイル

例えば、SSIDが TestWiFi、パスワードが password123 の場合です。
airdecap-ng -e "TestWiFi" -p "password123" capture.cap


成功すると、通常は次のファイルが生成されます。
capture-dec.cap


このファイルをWiresharkで開いて解析できます。

重要：WPA/WPA2の場合、キャプチャに有効な4-way handshakeの情報が必要です。

また、復号できるのは基本的にハンドシェイク後のデータパケットです。
aircrack-ng.com+1

4. その他のオプション
オプション	意味
-b	対象アクセスポイントのBSSIDを指定
-k	PMK（Pairwise Master Key）を指定
-w	WEPキーを16進数で指定
-l	802.11ヘッダーを削除しない
-o	出力ファイル名を指定
-c	復号に失敗したWEPパケットの出力先

BSSIDを指定する例
airdecap-ng -b F0:9F:C2:71:22:11 \
-e "TestWiFi" \
-p "password123" \
capture.cap


複数のアクセスポイントの通信が混在している場合に、対象を絞り込めます。
出力ファイル名を指定する例
airdecap-ng -e "TestWiFi" \
-p "password123" \
-o decrypted.cap \
capture.cap


5. WEPの復号
WEPの場合は、取得済みのWEPキーを指定します。
airdecap-ng -w 11A3E229084349BC25D97E2939 capture.cap


-w に指定するのは16進数形式のWEPキーです。
6. aircrack-ngとの違い
ここは試験学習でも整理しておきたいポイントです。
ツール	役割
airodump-ng	無線通信のキャプチャ
aircrack-ng	WEP/WPAの鍵解析
airdecap-ng	取得済みの鍵を使った通信の復号
aireplay-ng	無線フレームの注入・再送など
airmon-ng	モニターモードの管理


Main documentation+2
7. 試験向けの一連の流れ
8. airodump-ng
   
   対象AP・クライアント・通信を調査する
9. aircrack-ng
   
   キャプチャからパスワードを解析する
10. airdecap-ng
   
   判明したパスワードでキャプチャを復号する
11. Wireshark
   
   復号した通信内容を調査する

覚えるポイント
aircrack-ng は鍵を探す、airdecap-ng は鍵を使って通信を読む。

この違いを押さえておけば大丈夫です。

公式リファレンス：Aircrack-ng - airdecap-ng
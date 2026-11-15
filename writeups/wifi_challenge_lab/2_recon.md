---
title: 2 Recon
---
以下のフォルダで実行

```zsh
cd ~/CTF/WiFiChallengeLab-docker
pwd
```

~/CTF/WiFiChallengeLab-docker

---

# 00.What is the contents of the file /root/flag.txt on the VM?

LabのVMを起動し、実際にログインして確認する

```
flag{2162ae75cdefc5f731dfed4efa8b92743d1fb556}
```

![[Pasted image 20261115220302.png]]

---
# 01. What is the channel that the wifi-global Access Point is currently using?

wifi-globalという名前のアクセスポイントで使われているChannelは？

```zsh
sudo airodump-ng wlan60
```

![[Pasted image 20261115195622.png]]

```flag
44
```

---
# 02. What is the MAC of the wifi-IT client?

「wifi-IT」という名前のクライアントのMACアドレスを特定して回答する問題

wifi-ITのCHの特定

```zsh
sudo airodump-ng wlan60 -w ~/wifi/scan --manufacturer --wps --band abg
```

![[Pasted image 20261115195627.png]]

```zsh
sudo airodump-ng wlan60 -w ~/wifi/scanc11 --manufacturer --wps -c11
```

![[Pasted image 20261115195632.png]]

```flag
10:F9:6F:AC:53:52
```

3つは、Wi-Fiの構成を理解すると整理できます。

まず、次のように覚えてください。
- ESSID：Wi-Fiのネットワーク名
- BSSID：アクセスポイント（AP）を識別するMACアドレス
- STATION：Wi-Fiに接続している端末のMACアドレス

1. それぞれの関係

例えば、会社に「wifi-IT」というWi-Fiがあるとします。

![[Pasted image 20261115221200.png]]

つまり、ESSID（名前）→ BSSID（AP）→ STATION（接続端末）という関係です。

ただし、ESSIDとBSSIDは必ずしも1対1ではありません。同じESSIDを複数のAPが共有することもあります。
2. 今回のairodump-ngの表示との対応
今回の結果を整理すると次のとおりです。

上段：アクセスポイント一覧
```
BSSID	ESSID
F0:9F:C2:1A:CA:25	wifi-IT
```
ここから「wifi-IT」というネットワークを提供しているAPを特定します。

下段：接続端末一覧
```
BSSID	STATION
F0:9F:C2:1A:CA:25	10:F9:6F:AC:53:52
```

BSSIDが一致しているので、このSTATIONがwifi-ITに接続している端末だと判断できます。
3. 試験での調査手順
4. ESSIDを探す
   
   問題文の wifi-IT を上段から探す。
5. BSSIDを確認する
   
   対応するAPのMACアドレスを確認する。
6. STATIONを探す
   
   下段から同じBSSIDを持つ行を探す。
7. MACアドレスを回答する
   
   STATION欄のMACアドレスを回答する。

---
# 03. What is the probe of 78:C1:A7:BF:72:46?

```zsh
sudo airodump-ng wlan60 -w scan --manufacturer --wps --band abg
```

![[Pasted image 20261115195637.png]]

```flag
wifi-offices
```

---

# 04. What is the ESSID of the hidden AP (mac F0:9F:C2:6A:88
)?

辞書の作成

```zsh
cp root.bak/rockyou-top100000.txt .
```

```zsh
cat ./rockyou-top100000.txt | awk '{print "wifi-" $1}' > wifi-rockyou.txt
```

![[Pasted image 20261115195642.png]]

```zsh
sudo airmon-ng start wlan60  
```

![[Pasted image 20261115195647.png]]

```zsh
sudo iwconfig wlan60 channel 11
```

```zsh
sudo mdk4 wlan60 p -t F0:9F:C2:6A:88:26 -f wifi-rockyou.txt
```

![[Pasted image 20261115222305.png]]

```flag
wifi-free
```


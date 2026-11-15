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

![[Pasted image 20261115195654.png]]

別のターミナルから

```zsh
sudo dhclient wlan2 -v
```

![[Pasted image 20261115195701.png]]

![[Pasted image 20261115195704.png]]

admin:admin

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

![[Pasted image 20261115195735.png]]

## MACアドレスの偽装

```zsh
sudo ip link set wlan2 down
```

![[Pasted image 20261115195739.png]]

```zsh
ip link set wlan2 up
```

![[Pasted image 20261115195743.png]]

## ログインのキャプチャ

```zsh
sudo airodump-ng wlan2 -w ~/wifi/scanc6-01.cap
```

*5分ほどキャプチャしたら止める*

![[Pasted image 20261115195746.png]]

free1:Jyl1iq8UajZ1fEK

![[Pasted image 20261115195750.png]]
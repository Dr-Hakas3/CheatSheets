---
title: OPN
parent: Wi-Fi Challenge Lab
grand_parent: Red Team
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

![[Pasted image 20260606102740.png]]

別のターミナルから

```zsh
sudo dhclient wlan2 -v
```

![[Pasted image 20260606102810.png]]

![[Pasted image 20260606102840.png]]
admin:admin

---

# 06. What is the flag on the AP router of the wifi-guest network?

```zsh
sudo airodump-ng wlan60 -w ~/wifi/scanc6 --manufacturer --wps -c6
```
![[Pasted image 20260606111007.png]]

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
![[Pasted image 20260606110948.png]]

*このプロセスは止めずに以下を実行する*

別ターミナル

```zsh
sudo dhclient -v wlan2
```

![[Pasted image 20260606110926.png]]

```zsh
ip a show wlan2
```

![[Pasted image 20260606115337.png]]

## MACアドレスの偽装

```zsh
sudo ip link set wlan2 down
```

![[Pasted image 20260606134745.png]]

```zsh
ip link set wlan2 up
```

![[Pasted image 20260606115100.png]]

## ログインのキャプチャ

```zsh
sudo airodump-ng wlan2 -w ~/wifi/scanc6-01.cap
```

*5分ほどキャプチャしたら止める*

![[Pasted image 20260606135134.png]]

free1:Jyl1iq8UajZ1fEK

![[Pasted image 20260606140026.png]]
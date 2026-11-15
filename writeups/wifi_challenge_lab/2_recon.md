---
title: 2 Recon
---
以下のフォルダで実行

```zsh
cd ~/CTF/WiFiChallengeLab-docker
pwd
```

~/CTF/WiFiChallengeLab-docker

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

wifi-ITという名前のクライアントのMACアドレスを調査しこたえる問題

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
F0:9F:C2:1A:CA:25
```

---
# 03. What is the probe of 78:C1:A7:BF:72:46?

```zsh
sudo airodump-ng wlan60 -w scan --manufacturer --wps --band abg
```

![[Pasted image 20261115195637.png]]

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
sudo mdk4 wlan60 p -t F0:9F:C2:6A:88:26 -f ~/wifi-rockyou.txt
```

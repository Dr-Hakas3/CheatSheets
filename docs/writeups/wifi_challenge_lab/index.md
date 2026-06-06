# Setup

mac80211_hwsimベースの「仮想Wi-Fi環境構築〜確認」までを、最短で流れとして整理する。

```zsh
        Docker containers
     ┌──────────────────────┐
     │ AP container         │
     │ Client container     │
     └─────────┬────────────┘
               │ (netns / host network)
               ▼
     ┌──────────────────────┐
     │ mac80211_hwsim       │  ← 仮想Wi-Fi空間
     │ wlan0..wlan60        │
     └──────────────────────┘
               │
        Linux kernel only
```

① 仮想Wi-Fi NIC作成（カーネルモジュール）

mac80211_hwsim をロードして仮想NICを作る

```zsh
sudo modprobe -r mac80211_hwsim
sudo modprobe mac80211_hwsim radios=8
```
意味
-r → 一旦リセット
radios=8 → 仮想Wi-Fi 8枚生成
② 生成確認（NICができたか）
iw dev

または

```zsh
ip link show | grep wlan
```
期待結果
wlan0
wlan1
wlan2 ...
（複数出ればOK）
③ Docker環境起動（ラボ系の場合）
```zsh
docker compose up -d --build
```
④ コンテナ起動確認
```zsh
docker ps
```
重要チェック
APs → healthy
Clients → healthy
nzyme → healthy
db → healthy
⑤ 仮想Wi-Fi内部状態確認
クライアント側
docker exec -it WiFiChallengeLab-Clients bash
iw dev
AP側
docker exec -it WiFiChallengeLab-APs bash
iw dev
⑥ 接続状態確認
iw dev wlan0 link
状態
Not connected → 未接続
Connected to XX:XX → 接続済み
⑦ 通信確認（任意）
tcpdump -i any

または

ip a
⑧ 可視化（ラボ専用）

nzyme

http://localhost:22900
⑨ 全体フロー（超要約）
modprobe (hwsim)
   ↓
iw dev（NIC確認）
   ↓
docker compose up
   ↓
docker ps（healthy確認）
   ↓
iw dev / link（接続確認）
   ↓
tcpdump / nzyme（観測）
⑩ 重要ポイント（理解）
NIC作成＝カーネルモジュール
AP/Client＝Docker内部
通信＝全部カーネル内仮想空間
電波は存在しない

---

# Recon

## 01. What is the channel that the wifi-global Access Point is currently using?

```zsh
┌──(kali㉿kali)-[~/CTF/WiFiChallengeLab-docker]
└─$ sudo airodump-ng wlan60
```

![](../../assets/images/Pasted%20image%2020260606090217.png)

---
## 02. What is the MAC of the wifi-IT client?

wifi-ITのCHの特定
```zsh
sudo airodump-ng wlan60 -w ~/wifi/scan --manufacturer --wps --band abg
```

![](../../assets/images/Pasted%20image%2020260606090930.png)

```zsh
sudo airodump-ng wlan60 -w ~/wifi/scanc11 --manufacturer --wps -c11
```

![](../../assets/images/Pasted%20image%2020260606090838.png)

---
## 03. What is the probe of 78:C1:A7:BF:72:46?

```zsh
sudo airodump-ng wlan60 -w scan --manufacturer --wps --band abg
```

![](../../assets/images/Pasted%20image%2020260606091843.png)

---

## 04. What is the ESSID of the hidden AP (mac F0:9F:C2:6A:88
)?

辞書の作成

```zsh
head -n 100000 /usr/share/wordlists/rockyou.txt > ~/rockyou-top100000.txt
```

```zsh
cat /usr/share/wordlists/rockyou.txt | awk '{print "wifi-" $1}' > ~/wifi-rockyou.txt
```

```zsh
sudo airmon-ng start wlan60  
```

![](../../assets/images/Pasted%20image%2020260606092943.png)

```zsh
sudo iwconfig wlan0 channel 11
```

```zsh
sudo mdk4 wlan60 p -t F0:9F:C2:6A:88:26 -f ~/wifi-rockyou.txt
```

---

# OPN
## 5. What is the flag in the hidden AP router behind default credentials?

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
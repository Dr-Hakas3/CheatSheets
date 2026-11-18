---
title: 2 Lab Start & Stop
---
# 流れ

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

---

以下のフォルダで実行

```zsh
cd ~/CTF/WiFiChallengeLab-docker
pwd
```

~/CTF/WiFiChallengeLab-docker

## ① 仮想Wi-Fi NIC作成（カーネルモジュール）

mac80211_hwsim をロードして仮想NICを作る

```zsh
sudo modprobe -r mac80211_hwsim
sudo modprobe mac80211_hwsim radios=71
```

意味
- -r → 一旦リセット
- radios=8 → 仮想Wi-Fi 8枚生成

![[Pasted image 20261115184505.png]]

## ② 生成確認（NICができたか）

```zsh
iw dev
```

![[Pasted image 20261115184600.png]]

または

```zsh
ip link show | grep wlan
```

期待結果

```
wlan0
wlan1
wlan2 ...
（複数出ればOK）
```

![[Pasted image 20261115184622.png]]

## ③ Docker環境起動（ラボ系の場合）

```zsh
docker compose up -d --build
```

![[Pasted image 20261115184646.png]]

## ④ コンテナ起動確認

```zsh
docker ps
```

![[Pasted image 20261115184716.png]]

重要チェック

```
APs → healthy
Clients → healthy
nzyme → healthy
db → healthy
```

## ⑤ 仮想Wi-Fi内部状態確認

## クライアント側

```zsh
docker exec -it WiFiChallengeLab-Clients bash
```

```zsh
iw dev
```

## AP側

```zsh
docker exec -it WiFiChallengeLab-APs bash
```

```zsh
iw dev
```

## ⑥ 接続状態確認

```zsh
iw dev wlan0 link
```

状態

```
Not connected → 未接続
Connected to XX:XX → 接続済み
```

## ⑦ 通信確認（任意）

```zsh
tcpdump -i any
```

または

```zsh
ip a
```

## ⑧ 可視化（ラボ専用）

```zsh
nzyme
```

http://localhost:22900

## ⑨ 全体フロー（超要約）

```
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
```

## ⑩ 重要ポイント（理解）

```
NIC作成＝カーネルモジュール
AP/Client＝Docker内部
通信＝全部カーネル内仮想空間
ラボでは電波は存在しない
```

---
### **演習終了時**

WiFiChallengeLabのディレクトリで実行します。

```
docker compose stop
```

これでAP・Client・nzymeなどのコンテナが停止します。

### **演習を再開するとき**

```
docker compose start
```

### **完全に環境を終了・片付ける場合**

```
docker compose down
```

`down` はコンテナとComposeネットワークを削除します。通常の演習終了なら `stop` で十分です。

### **仮想Wi-Fiデバイスも解放したい場合**

Dockerを停止した後に実行します。

```
sudo modprobe -r mac80211_hwsim
```

次回起動時は、今回と同様に71個でロードします。

```
sudo modprobe mac80211_hwsim radios=71
docker compose start
```

**おすすめの運用**

|タイミング|操作|
|---|---|
|演習開始|`modprobe` → `docker compose start`|
|演習終了|`docker compose stop`|
|VMをシャットダウン|そのままでOK|
|環境を作り直す|`docker compose down`|

なお、`stop` だけなら仮想Wi-Fiデバイスは残ります。毎回モジュールを再ロードする必要はありません。
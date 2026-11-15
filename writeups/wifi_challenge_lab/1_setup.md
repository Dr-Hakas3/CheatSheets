---
title: 1 Setup
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

```zsh
cd ~/CTF/WiFiChallengeLab-docker
pwd
```

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

# トラブルシューティング

## トラブル例　１

- dcoker psで各VMがhealthyにならない

### **1. Dockerコンテナを停止**

WiFiChallengeLabのディレクトリで実行してください。

```
docker compose stop
```

### **2. モジュールを再ロード**

続けて以下を実行します。

```
sudo modprobe -r mac80211_hwsim
sudo modprobe mac80211_hwsim radios=71
```

### **3. 読み込み結果を確認**

```
cat /sys/module/mac80211_hwsim/parameters/radios
iw dev | grep Interface | wc -l
```

期待する結果：

- `radios`：`71`
    
- インターフェース数：`71`
    

注意

`modprobe -r` で `Module is in use` と表示された場合は、そこで止めてください。無理に削除しないでください。

以下の項目が確認できたらDockerコンテナを再起動します。

|確認項目|結果|
|---|---|
|`mac80211_hwsim` radios|71|
|`iw dev` のInterface数|71|
|状態|OK|

これでWiFiChallengeLabが想定する `wlan0`～`wlan70` の無線デバイスを用意できました。

### **次の手順**

Dockerコンテナを起動します。

```
docker compose up -d
```

起動後、状態を確認してください。

```
docker compose ps
```

まずは `APs`、`Clients`、`nzyme` が `healthy` になるか確認しましょう。

## トラブル例２

nzymeが起動しない

![[Pasted image 20261115190736.png]]

nzyme のログを確認しましょう。

### **1. nzymeのログ確認**

```
docker logs WiFiChallengeLab-nzyme --tail 100
```

### **2. ヘルスチェックの詳細確認**

```
docker inspect WiFiChallengeLab-nzyme \
  --format '{{json .State.Health}}'
```

※　**PostgreSQLのLiquibaseロックが残っていることが原因で起動できていない場合。**

ログの重要部分はここです。

```
FATAL horse.wtf.nzyme.Main - Error during database initialization and migration.

liquibase.exception.LockException:
Could not acquire change log lock.

Currently locked by 10.200.1.1
since 6/16/26, 5:14 PM
```

```zsh
docker compose stop nzyme
```

![[Pasted image 20261115191017.png]]

```zsh
docker exec -it WiFiChallengeLab-nzyme-db \
  psql -U nzyme -d nzyme
```

```zsh
SELECT id, locked, lockgranted, lockedby
FROM databasechangeloglock;
```

![[Pasted image 20261115191041.png]]

```sql
SELECT id, locked, lockgranted, lockedby
FROM databasechangeloglock;

SELECT COUNT(*) AS changeset_count
FROM databasechangelog;
```

![[Pasted image 20261115191224.png]]

### **1. Liquibaseロック解除**

現在の `nzyme=#` プロンプトで、以下を実行してください。

```
UPDATE databasechangeloglock
SET locked = false,
    lockgranted = NULL,
    lockedby = NULL
WHERE id = 1;
```

結果が `UPDATE 1` なら解除できています。

続けて確認します。

```
SELECT id, locked, lockgranted, lockedby
FROM databasechangeloglock;
```

`locked = f` になればOKです。

### **2. PostgreSQLを終了**

```
\q
```

### **3. nzymeを再起動**

Kaliのターミナルに戻ってから実行します。

```
docker compose start nzyme
```

その後、状態を確認します。

```
docker compose ps
```

![[Pasted image 20261115191459.png]]

すべてhealthyでOK

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
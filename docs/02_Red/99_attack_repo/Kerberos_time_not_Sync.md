今回の事象は典型的な「Kerberos × 時刻同期」トラブルです。構造的に整理するとこうなります。

---

# ■ 事象概要

* `impacket-getTGT` 実行時に
  **`KRB_AP_ERR_SKEW (Clock skew too great)`** 発生
* `ntpdate -q` で常に **約+28800秒（8時間）ズレ**
* 同期してもすぐ再発

---

# ■ 原因（Root Cause）

## ① RTC（ハードウェアクロック）とシステム時刻の乖離

```text
RTC → 約8時間遅れ
System Clock → 修正されても後で戻される
```

👉 **RTCが古いまま残っていたのが本丸**

---

## ② 自動同期プロセスの干渉

```text
systemd-timesyncd が常駐
```

👉 外部NTPに再同期 → DCとのズレ再発

---

## ③ VM環境特有の要因（背景）

* VMは以下のいずれかで時刻が上書きされる：

  * ホスト同期
  * RTC参照
  * NTPサービス

👉 **複数の“時刻ソース”が競合していた**

---

# ■ 発生メカニズム（因果関係）

```text
① ntpdateでDCに同期
        ↓
② RTCは古いまま
        ↓
③ systemd-timesyncd or RTC反映
        ↓
④ システム時刻が再び8時間ズレる
        ↓
⑤ Kerberos失敗（KRB_AP_ERR_SKEW）
```

---

# ■ 対策（実施内容）

## ① 自動同期の停止

```bash
sudo systemctl stop systemd-timesyncd
sudo systemctl disable systemd-timesyncd
```

---

## ② DCに手動同期

```bash
sudo ntpdate -u dc1.ping.htb
```

---

## ③ RTCの修正（最重要）

```bash
sudo hwclock --systohc
```

👉 **システム時刻 → RTCへ書き込み**

---

## ④ 検証

```bash
ntpdate -q dc1.ping.htb
```

```text
offset ≈ 0.xxx 秒
```

👉 Kerberos許容範囲内に収束

---

# ■ 結果

* 時刻ズレ：**約8時間 → 約0.02秒**
* Kerberos：**正常動作可能状態**

---

# ■ 再発防止（Best Practice）

## ✔ 攻撃前ルーチン

```bash
sudo systemctl stop systemd-timesyncd
sudo ntpdate -u <DC>
sudo hwclock --systohc
```

---

## ✔ 原則

* **Kerberos環境では「DCの時刻が正」**
* ローカルや現実時間は関係ない

---

## ✔ 注意点

* タイムゾーン変更では解決しない
* `ntpdate` だけでは不十分（RTCが残る）

---

# ■ まとめ（一行）

👉 **「時刻を直した」ではなく「時刻の“支配権”をDCに移した」が正解**

---

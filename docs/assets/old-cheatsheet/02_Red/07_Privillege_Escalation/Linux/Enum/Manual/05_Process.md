## Process
```bash
ps aux
```
- a: 自分以外のユーザーのプロセスもすべて表示
- u: ユーザー名やCPU/メモリ使用率などの詳細を表示
- x: 制御端末（TTY）を持たないプロセスも表示 

```zsh
pa -eaf
```
-e: すべてのプロセスを表示。
-a: 他のユーザーのプロセスも含めて表示（通常-eと併用）。
-f: フルフォーマット（詳細）で表示。

# pspy
## github
```
https://github.com/DominicBreuker/pspy
```

```zsh
./pspy64
```
## passphraseが取得可能な例
![651](../../../../../Assets/Images/Pasted%20image%2020260430181307.png)

# サービスフットプリントの検査
### 実行中のプロセスの動作を検査
```bash
#watchユーティリティを使ってpsコマンドを1秒ごとに実行し、 「pass」という単語が出現するたびに結果をgrep検索
watch -n 1 "ps -aux | grep pass"
```
---
# cron
```bash
ls -lah /etc/cron*

# 現在のユーザ
crontab -l

# sudo
sudo crontab -l
# sudoをつけたときとの違いを確認する
```

---
# インストールされたアプリケーションを一覧表示
```bash
dpkg -l
```
---
# Karnel_&_Module
ターゲットにロードされているドライバとカーネルモジュールのリストを収集

```bash
lsmod

# list内のモジュールについての詳細調査
/sbin/modinfo libata
```
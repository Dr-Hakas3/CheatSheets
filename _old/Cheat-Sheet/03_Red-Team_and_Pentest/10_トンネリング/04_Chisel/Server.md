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
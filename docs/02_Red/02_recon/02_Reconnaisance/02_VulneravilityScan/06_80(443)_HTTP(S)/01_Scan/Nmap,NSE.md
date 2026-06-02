## サービスの詳細情報
```bash
nmap -sV -sC -p80 192.168.0.101
```
- -sV バージョン検出 
- -sC スクリプトスキャン
  
```bash
nmap -A -p80 192.168.0.101
```
- -A OS検出、バージョン検出、スクリプトスキャン、traceroute

---

# NSE脆弱性スクリプト
NSEスクリプトは /usr/share/nmap/scripts/ディレクトリに.nseファイルタイプで保存されています。
1. Scriptのパス
```bash
cd /usr/share/nmap/scripts
cat script.db | grep "\"vuln\""
```
2. 脆弱性調査
```bash
sudo nmap -sV -p 443 --script "vuln" 192.168.50.124
```

Web サーバーの初期フィンガープリントを実行する_http-enumなどのサービス固有の Nmap NSE スクリプトを使用
```bash
sudo nmap -p80 --script=http-enum 192.168.50.20
```
# NSEスクリプトの操作
NSEの更新の例
1. 特定のCVEに関する.NSEを検索する
2. githubで見つかったファイルをダウンロード
3. 更新
```bash
sudo cp /home/kali/Downloads/http-vuln-cve-2021-41773.nse /usr/share/nmap/scripts/http-vuln-cve2021-41773.nse
sudo nmap --script-updatedb
```
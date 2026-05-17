---
title: John The Ripper
parent: Password Crack
grand_parent: Red Team
nav_order: 2
---
# Basic

 必ずsudo johnで実行する！
```zsh
unshadow /etc/passwd /etc/shadow > hash.txt
```
### パスワードハッシュの形式を自動検出してクラック

最も簡単な使い方は、ハッシュファイルを指定して、`John`に自動検出とクラックを行わせる方法です。

```bash
john hashfile.txt
```
- `hashfile.txt`: クラックしたいハッシュが記載されているファイルの名前。

### 特定のパスワードハッシュ形式を指定してクラック

ハッシュ形式がわかっている場合は、形式を指定してクラックすることができます。

```bash
john --format=sha256crypt hashfile.txt
```
- `--format=sha256crypt`: 使用するハッシュ形式を指定します。`john --list=formats` コマンドでサポートされている形式を確認できます。

### 辞書攻撃

辞書ファイルを使ってクラックする場合、以下のように実行します。

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashfile.txt
```
- `--wordlist=/usr/share/wordlists/rockyou.txt`: 使用する辞書ファイルを指定します。

### ルールベースのクラック

`John the Ripper`では、ルールを適用して辞書のパスワードを変形し、クラックすることができます。

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --rules hashfile.txt
```
- `--rules`: ルールを適用します。

# その他のコマンド

#### クラック結果の確認

クラックに成功したパスワードを確認するには、次のコマンドを実行します。
```bash
john --show hashfile.txt
```

#### 中断したクラックを再開

クラック処理を中断した場合、後で再開することができます。
```bash
john --restore
```

# 対応しているハッシュ形式の一覧を確認
```bash
john --list=formats
```

---

# Hash
```
cat thecybergeek_hash 
```

```
thecybergeek::CRAFT2:60f46e5174839f84:A42E88575DCF88DE4E3BF1F8FA75DCAC:010100000000000080BF8B4A2C85DC016BEB90CC27CFBBA60000000002000800520056003200590001001E00570049004E002D0031005A00330032004F0030003200450036004F004D0004003400570049004E002D0031005A00330032004F0030003200450036004F004D002E0052005600320059002E004C004F00430041004C000300140052005600320059002E004C004F00430041004C000500140052005600320059002E004C004F00430041004C000700080080BF8B4A2C85DC0106000400020000000800300030000000000000000000000000300000CC0138A695F108F7A308F99F4D3F33A4267464CF03A9B699EAF3B754930C64410A001000000000000000000000000000000000000900260063006900660073002F003100390032002E003100360038002E00340035002E003200310038000000000000000000 
```
# Crack
```zsh
sudo john thecybergeek_hash --wordlist=/usr/share/wordlists/rockyou.txt --rules=best64       
```
![](../../assets/images/Pasted%20image%2020260508230759.png)

---


# keepass2john
`keepass2john`は、KeePassのデータベースファイルからJohn the Ripperが使用できる形式に変換するためのツールです。これを使用すると、KeePassのデータベースのパスワードをJohn the Ripperでクラックできるようになります。

### 基本的な使い方

1. **KeePassデータベースをJohn形式に変換**

   `keepass2john`を使用して、KeePassデータベースファイルをJohn形式に変換します。

   ```bash
   keepass2john your_database.kdbx > keepass_hash.txt
   ```

   - `your_database.kdbx`: クラックしたいKeePassデータベースファイル。
   - `keepass_hash.txt`: 出力されるJohn形式のハッシュファイル。

2. **John the Ripperでクラック**

   変換したハッシュファイルをJohn the Ripperでクラックします。

   ```bash
   john keepass_hash.txt
   ```

   - `keepass_hash.txt`: 先ほど生成したJohn形式のハッシュファイル。

3. **結果を表示**

   クラックされたパスワードを表示します。

   ```bash
   john --show keepass_hash.txt
   ```

### 実際の手順

1. KeePassデータベースファイル（例: `your_database.kdbx`）が手元にあると仮定します。

2. `keepass2john`を使って、KeePassデータベースをJohn形式に変換します。

   ```bash
   keepass2john your_database.kdbx > keepass_hash.txt
   ```

3. 変換された`keepass_hash.txt`ファイルを使ってJohn the Ripperでパスワードをクラックします。

   ```bash
   john keepass_hash.txt
   ```

4. クラックされたパスワードを表示します。

   ```bash
   john --show keepass_hash.txt
   ```

### 注意点
- `keepass2john`はJohn the Ripperの一部として提供されているため、John the Ripperをインストールしていれば利用可能です。
- KeePassデータベースが暗号化されている必要があります。暗号化されていないデータベースは、パスワードクラックの対象にはなりません。

---

# ssh2john

`ssh2john`は、SSHプライベートキーからJohn the Ripperが使用できる形式に変換するためのツールです。このツールを使用することで、SSHプライベートキーをクラックするためにJohn the Ripperを使えるようになります。

### 基本的な使い方

1. **SSHプライベートキーをJohn形式に変換**
   
   まず、`ssh2john`を使ってSSHプライベートキーをJohn the Ripperで扱える形式に変換します。

   ```bash
   ssh2john id_rsa > ssh_hash.txt
   ```
   - `id_rsa`: クラック対象のSSHプライベートキー。
   - `ssh_hash.txt`: 出力されるJohn形式のハッシュファイル。

2. **John the Ripperでクラック**

   変換したハッシュファイルをJohn the Ripperでクラックします。
   ```bash
   john ssh_hash.txt
   ```
   - `ssh_hash.txt`: 先ほど生成したJohn形式のハッシュファイル。

### 実際の手順

1. まず、SSHプライベートキー（例: `id_rsa`）が手元にあると仮定します。

2. `ssh2john`を使って、SSHキーをJohn形式に変換します。
   ```bash
   ssh2john id_rsa > ssh_hash.txt
   ```

3. 変換された`ssh_hash.txt`ファイルを使ってJohn the Ripperでパスワードをクラックします。
   ```bash
   john ssh_hash.txt
   ```

4. クラックされたパスワードを表示します。
   ```bash
   john --show ssh_hash.txt
   ```

### 注意点

- `ssh2john`はJohn the Ripperに含まれるスクリプトなので、John the Ripperをインストールしていれば利用可能です。
- クラックを行うには、対象のSSHキーが暗号化されている必要があります。もしキーが暗号化されていない場合、そもそもパスワードクラックの対象にはなりません。

---

# zip2john

- パスワード付きzipファイル 解析
```bash
unzip spammer.zip 
Archive:  spammer.zip
[spammer.zip] creds.txt password: 
   skipping: creds.txt
```

```bash
zip2john spammer.zip > spammer.zip.hash
Created directory: /root/.john
ver 2.0 spammer.zip/creds.txt PKZIP Encr: cmplen=27, decmplen=15, crc=B003611D ts=ADCB cs=b003 type=0
```

```bash
john spammer.zip.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 12 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
myspace4         (spammer.zip/creds.txt)     
1g 0:00:00:00 DONE 2/3 (2024-09-15 13:00) 16.66g/s 1428Kp/s 1428Kc/s 1428KC/s MINNIE..ship4
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
myspace4
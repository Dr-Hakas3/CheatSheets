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

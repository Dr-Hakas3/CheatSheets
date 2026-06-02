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
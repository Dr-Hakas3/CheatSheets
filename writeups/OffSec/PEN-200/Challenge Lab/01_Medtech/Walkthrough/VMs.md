**Credentials|****Objectives**

**172.16.182.10**

Challenge1 - VM 1 OS Credentials:

No credentials were provided for this machine

**172.16.182.11**

Challenge1 - VM 2 OS Credentials:

No credentials were provided for this machine

**192.168.182.120**

Challenge1 - VM 3 OS Credentials:

No credentials were provided for this machine

**192.168.182.121**

Challenge1 - VM 4 OS Credentials:

No credentials were provided for this machine

**192.168.182.122**

Challenge1 - VM 5 OS Credentials:

No credentials were provided for this machine

**172.16.182.12**

Challenge1 - VM 6 OS Credentials:

No credentials were provided for this machine

**172.16.182.13**

Challenge1 - VM 7 OS Credentials:

No credentials were provided for this machine

**172.16.182.14**

Challenge1 - VM 8 OS Credentials:

No credentials were provided for this machine

**172.16.182.82**

Challenge1 - VM 9 OS Credentials:

No credentials were provided for this machine

**172.16.182.83**

Challenge1 - VM 10 OS Credentials:

貼り付け元  \<https://portal.offsec.com/courses/pen-200-44065/labs>

└─$ sudo nmap 192.168.182.120-122 --min-rate=10000

\[sudo\] password for kali:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-23 23:19 JST

Nmap scan report for 192.168.182.120

Host is up (0.12s latency).

Not shown: 998 closed tcp ports (reset)

PORT   STATE SERVICE

22/tcp open  ssh

80/tcp open  http

Nmap scan report for 192.168.182.121

Host is up (0.12s latency).

Not shown: 995 closed tcp ports (reset)

PORT     STATE SERVICE

80/tcp   open  http

135/tcp  open  msrpc

139/tcp  open  netbios-ssn

445/tcp  open  microsoft-ds

5985/tcp open  wsman

Nmap scan report for 192.168.182.122

Host is up (0.11s latency).

Not shown: 999 closed tcp ports (reset)

PORT   STATE SERVICE

22/tcp open  ssh

Nmap done: 3 IP addresses (3 hosts up) scanned in 0.93 seconds

![[VMs image.png]]

└─$ crackmapexec smb 172.16.182.10-14 -u wario -p 'Mushroom!' -d medtech.com --continue-on-success

SMB         172.16.182.11   445    FILES02          \[*\] Windows Server 2022 Build 20348 x64 (name:FILES02) (domain:medtech.com) (signing:False) (SMBv1:False)

SMB         172.16.182.10   445    DC01             \[*\] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:medtech.com) (signing:True) (SMBv1:False)

SMB         172.16.182.13   445    PROD01           \[*\] Windows Server 2022 Build 20348 x64 (name:PROD01) (domain:medtech.com) (signing:False) (SMBv1:False)

SMB         172.16.182.12   445    DEV04            \[*\] Windows Server 2022 Build 20348 x64 (name:DEV04) (domain:medtech.com) (signing:False) (SMBv1:False)

SMB         172.16.182.11   445    FILES02          \[+\] medtech.com\wario:Mushroom!

SMB         172.16.182.10   445    DC01             \[+\] medtech.com\wario:Mushroom!

SMB         172.16.182.13   445    PROD01           \[+\] medtech.com\wario:Mushroom!

SMB         172.16.182.12   445    DEV04            \[+\] medtech.com\wario:Mushroom!

┌──(kali㉿kali)-\[~/ChallengeLab/1_Medtech\]

└─$ crackmapexec smb 172.16.182.82-83 -u wario -p 'Mushroom!' -d medtech.com --continue-on-success

SMB         172.16.182.83   445    CLIENT02         \[*\] Windows 11 Build 22000 x64 (name:CLIENT02) (domain:medtech.com) (signing:False) (SMBv1:False)

SMB         172.16.182.82   445    CLIENT01         \[*\] Windows 11 Build 22000 x64 (name:CLIENT01) (domain:medtech.com) (signing:False) (SMBv1:False)

SMB         172.16.182.83   445    CLIENT02         \[+\] medtech.com\wario:Mushroom!

SMB         172.16.182.82   445    CLIENT01         \[+\] medtech.com\wario:Mushroom!

![[VMs image 1.png]]

└─$ crackmapexec winrm 172.16.182.82-83 -u wario -p 'Mushroom!' -d medtech.com --continue-on-success

HTTP        172.16.182.83   5985   172.16.182.83    \[*\] http://172.16.182.83:5985/wsman

/usr/lib/python3/dist-packages/spnego/_ntlm_raw/crypto.py:46: CryptographyDeprecationWarning: ARC4 has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.ARC4 and will be removed from this module in 48.0.0.

arc4 = algorithms.ARC4(self._key)

WINRM       172.16.182.83   5985   172.16.182.83    \[+\] medtech.com\wario:Mushroom! (Pwn3d!)

![[VMs image 2.png]]

***PROOF GUIDE***

\-------------------------------------------

***MEDTECH***

\`.120 - proof only

.121 - proof only

.122 - local and proof

.10 - proof only

.11 - local and proof

.12 - local and proof

.13 - proof only

.14 - local only

.82 - proof only

.83 - local and proof \`
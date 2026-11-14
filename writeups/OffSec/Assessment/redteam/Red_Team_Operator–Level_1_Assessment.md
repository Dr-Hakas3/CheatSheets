---
title: Red_Team_Operator–Level_1_Assessment
parent: offsec_assessment
grand_parent: Writeups
---

# 1
```zsh
ssh Freddy@192.168.228.51
```

```zsh
freddy@WINDOWS-01 C:\Users\Freddy>dir Desktop
 Volume in drive C has no label.
 Volume Serial Number is 7ADD-E6C8

 Directory of C:\Users\Freddy\Desktop

09/07/2021  02:31 PM    <DIR>          .
09/07/2021  02:31 PM    <DIR>          ..
06/25/2021  04:48 AM                 7 boring.txt
06/25/2021  04:53 AM                19 empty.txt
09/07/2021  02:16 PM             2,348 Microsoft Edge.lnk
               3 File(s)          2,374 bytes
               2 Dir(s)   5,876,297,728 bytes free
```

empty.txt

# 2
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/RedTeam_Operator/L1]
└─$ ssh offsec@192.168.228.74                                                                                         
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
offsec@192.168.228.74's password: 
Permission denied, please try again.
offsec@192.168.228.74's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-97-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 System information disabled due to load higher than 1.0


0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

offsec@nmap02:~$ curl -I http://10.13.37.33
HTTP/1.1 200 OK
Date: Tue, 02 Jun 2026 14:33:19 GMT
Server: Apache/2.4.52 (Unix)
Last-Modified: Thu, 03 Feb 2022 17:17:06 GMT
ETag: "8a-5d7204db22880"
Accept-Ranges: bytes
Content-Length: 138
Content-Type: text/html
```

# 3
```zsh
┌──(kali㉿kali)-[~/github/Dr-Hakas3]
└─$ smbclient -L //192.168.228.71 -U “” -N 

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        things          Disk      DEF100_EA
        IPC$            IPC       IPC Service (mitra server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.
smbXcli_negprot_smb1_done: No compatible protocol selected by server.
Protocol negotiation to server 192.168.228.71 (for a protocol between LANMAN1 and NT1) failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available
```

# 4
```zsh
┌──(kali㉿kali)-[~/github/Dr-Hakas3]
└─$ ssh student@192.168.228.112 -p2222
The authenticity of host '[192.168.228.112]:2222 ([192.168.228.112]:2222)' can't be established.
ED25519 key fingerprint is: SHA256:o/nQE4qImJpK9TWdq5z4Vs2RLkUGocIJUSM5rFdYgJo
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.228.112]:2222' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Welcome to the PEN-100 Assessment Kali Linux Shell.
student@192.168.228.112's password: 
┌──(student㉿35766e16ac75)-[~]
└─$ sudo su                                                                                             

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for student: 
root@35766e16ac75:/home/student# cat /root/falg.txt
cat: /root/falg.txt: No such file or directory
root@35766e16ac75:/home/student# cd /root
root@35766e16ac75:~# ls
flag.txt
root@35766e16ac75:~# cat flag.txt
OS{}

```

# 5
```zsh
┌──(kali㉿kali)-[~/github/Dr-Hakas3]
└─$ ssh student@192.168.228.112 -p2222
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Welcome to the PEN-100 Assessment Kali Linux Shell.
student@192.168.228.112's password: 
┌──(student㉿67c3deef474c)-[~]
└─$ ps aux                                                                                                                                                     
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   2424   664 ?        Ss   10:37   0:00 /bin/sh -c /root/startup.sh 99999999999 OS{b1f58b41349f3fb87c448c9fecf6211f}
root           7  0.0  0.0   3828  2712 ?        S    10:37   0:00 /bin/bash /root/startup.sh 99999999999 OS{b1f58b41349f3fb87c448c9fecf6211f}
root           9  0.0  0.1  13508  4336 ?        Ss   10:37   0:00 sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups
root          10  0.0  0.0   2336   644 ?        S    10:37   0:00 sleep 99999999999
root          11  0.0  0.2  14744  8644 ?        Ss   10:37   0:00 sshd: student [priv]
student       13  0.0  0.1  14744  4768 ?        S    10:37   0:00 sshd: student@pts/0
student       14  0.0  0.0   5984  3704 pts/0    Ss   10:37   0:00 -bash
student       21  0.0  0.0   8804  3348 pts/0    R+   10:37   0:00 ps aux
```

# 6
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/RedTeam_Operator/L1]
└─$ rdesktop 192.168.228.40 -u offsec -p lab -d demo
```

Computer 一覧
```powershell
PS C:\Windows\system32> Get-ADComputer -Filter * | Select-Object Name, OperatingSystem

Name     OperatingSystem
----     ---------------
DC01
APPSRV01
```

![](../../../assets/images/Pasted%20image%2020260602234449.png)

```powershell
PS C:\Windows\system32> (Get-ADComputer -Identity "APPSRV01").SID.Value
S-1-5-21-2661071818-1767017692-878076344-1103
```
![](../../../assets/images/Pasted%20image%2020260602234304.png)
or

```powershell
PS C:\Windows\system32> Get-ADComputer -Filter * -Properties SID | Select-Object Name, SID | Format-Table -AutoSize

Name     SID
----     ---
DC01     S-1-5-21-2661071818-1767017692-878076344-1000
APPSRV01 S-1-5-21-2661071818-1767017692-878076344-1103
```
![](../../../assets/images/Pasted%20image%2020260602234324.png)
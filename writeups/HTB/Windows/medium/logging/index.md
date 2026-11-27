---
title:
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

As is common in real life pentests, you will start the Logging box with credentials for the following account wallace.everette / Welcome2026@


---
# Reconnaissance

```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 10.129.18.76   
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-08 19:54 +0900
Nmap scan report for 10.129.18.76
Host is up (0.26s latency).
Not shown: 65506 closed tcp ports (reset)
PORT      STATE SERVICE           VERSION
53/tcp    open  domain            Simple DNS Plus
80/tcp    open  http              Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
88/tcp    open  kerberos-sec      Microsoft Windows Kerberos (server time: 2026-06-08 17:55:55Z)
135/tcp   open  msrpc             Microsoft Windows RPC
139/tcp   open  netbios-ssn       Microsoft Windows netbios-ssn
389/tcp   open  ldap
|_ssl-date: 2026-06-08T17:57:58+00:00; +7h00m00s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.logging.htb, DNS:logging.htb, DNS:logging
| Not valid before: 2026-04-24T16:40:59
|_Not valid after:  2106-04-24T16:40:59
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ldapssl?
|_ssl-date: 2026-06-08T17:57:58+00:00; +7h00m00s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.logging.htb, DNS:logging.htb, DNS:logging
| Not valid before: 2026-04-24T16:40:59
|_Not valid after:  2106-04-24T16:40:59
3268/tcp  open  ldap
|_ssl-date: 2026-06-08T17:57:59+00:00; +7h00m00s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.logging.htb, DNS:logging.htb, DNS:logging
| Not valid before: 2026-04-24T16:40:59
|_Not valid after:  2106-04-24T16:40:59
3269/tcp  open  globalcatLDAPssl?
|_ssl-date: 2026-06-08T17:57:59+00:00; +7h00m00s from scanner time.
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:DC01.logging.htb, DNS:logging.htb, DNS:logging
| Not valid before: 2026-04-24T16:40:59
|_Not valid after:  2106-04-24T16:40:59
5985/tcp  open  http              Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8530/tcp  open  http              Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Site doesn't have a title.
8531/tcp  open  unknown
| tls-alpn: 
|   h2
|_  http/1.1
| ssl-cert: Subject: 
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.logging.htb
| Not valid before: 2026-04-24T15:49:07
|_Not valid after:  2027-04-24T15:49:07
|_ssl-date: 2026-06-08T17:57:59+00:00; +7h00m00s from scanner time.
9389/tcp  open  mc-nmf            .NET Message Framing
47001/tcp open  http              Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc             Microsoft Windows RPC
49665/tcp open  msrpc             Microsoft Windows RPC
49666/tcp open  msrpc             Microsoft Windows RPC
49667/tcp open  msrpc             Microsoft Windows RPC
49673/tcp open  msrpc             Microsoft Windows RPC
49694/tcp open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
49695/tcp open  msrpc             Microsoft Windows RPC
49699/tcp open  msrpc             Microsoft Windows RPC
49715/tcp open  msrpc             Microsoft Windows RPC
49751/tcp open  msrpc             Microsoft Windows RPC
49774/tcp open  msrpc             Microsoft Windows RPC
49810/tcp open  msrpc             Microsoft Windows RPC
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.99%E=4%D=6/8%OT=53%CT=1%CU=35143%PV=Y%DS=2%DC=T%G=Y%TM=6A26A03A
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=10C%TI=I%CI=I%II=I%SS=S%TS=U
OS:)SEQ(SP=102%GCD=1%ISR=108%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=104%GCD=1%ISR=
OS:10C%TI=I%CI=I%II=I%SS=S%TS=U)SEQ(SP=FE%GCD=1%ISR=10C%TI=I%CI=I%II=I%SS=S
OS:%TS=U)SEQ(SP=FF%GCD=1%ISR=10A%TI=I%CI=I%II=I%SS=S%TS=U)OPS(O1=M552NW8NNS
OS:%O2=M552NW8NNS%O3=M552NW8%O4=M552NW8NNS%O5=M552NW8NNS%O6=M552NNS)WIN(W1=
OS:FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)ECN(R=Y%DF=Y%T=80%W=FFFF%O=
OS:M552NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)
OS:T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S
OS:+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=N)U1(
OS:R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=
OS:N%T=80%CD=Z)

Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_clock-skew: mean: 6h59m59s, deviation: 0s, median: 6h59m59s
| smb2-time: 
|   date: 2026-06-08T17:57:47
|_  start_date: N/A

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   256.84 ms 10.10.14.1
2   257.12 ms 10.129.18.76

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 217.10 seconds
```

# nxc

```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ nxc smb 10.129.18.76 -u logging.htb\\wallace.everette -p 'Welcome2026@' --shares     
SMB         10.129.18.76    445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:logging.htb) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.18.76    445    DC01             [+] logging.htb\wallace.everette:Welcome2026@ 
SMB         10.129.18.76    445    DC01             [*] Enumerated shares
SMB         10.129.18.76    445    DC01             Share           Permissions     Remark
SMB         10.129.18.76    445    DC01             -----           -----------     ------
SMB         10.129.18.76    445    DC01             ADMIN$                          Remote Admin
SMB         10.129.18.76    445    DC01             C$                              Default share
SMB         10.129.18.76    445    DC01             IPC$            READ            Remote IPC
SMB         10.129.18.76    445    DC01             Logs            READ            
SMB         10.129.18.76    445    DC01             NETLOGON        READ            Logon server share 
SMB         10.129.18.76    445    DC01             SYSVOL          READ            Logon server share 
SMB         10.129.18.76    445    DC01             WSUSTemp                        A network share used by Local Publishing from a Remote WSUS Console Instance.
        
```

```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ smbclient //logging.htb/Logs -U "logging.htb\\wallace.everette" -c "prompt OFF;recurse ON;mget *"
Password for [LOGGING.HTB\wallace.everette]:
getting file \Audit_Heartbeat.log of size 1294 as Audit_Heartbeat.log (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
getting file \IdentitySync_Trace_20260219.log of size 8488 as IdentitySync_Trace_20260219.log (8.0 KiloBytes/sec) (average 1.9 KiloBytes/sec)
getting file \Service_State.log of size 468 as Service_State.log (0.4 KiloBytes/sec) (average 1.7 KiloBytes/sec)
getting file \TaskMonitor.log of size 1170 as TaskMonitor.log (0.9 KiloBytes/sec) (average 1.6 KiloBytes/sec)
```

```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ cat IdentitySync_Trace_20260219.log
```

```zsh
[2026-02-09 03:00:03.125] [PID:4102] [Thread:04] VERBOSE - ConnectionContext Dump: { Domain: "logging.htb", Server: "DC01", SSL: "False", BindUser: "LOGGING\svc_recovery", BindPass: "Em3rg3ncyPa$$2025", Timeout: 30 }
```
LOGGING\svc_recovery
`Em3rg3ncyPa$$2025

## Kerberos Ticketの取得

	Backupを作成
```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ sudo cp /etc/krb5.conf /etc/krb5.conf.bak
```

krb5.confの作成

```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ cat /etc/krb5.conf                  
[libdefaults]
    default_realm = LOGGING.HTB
    dns_lookup_realm = false
    dns_lookup_kdc = false

[realms]
    LOGGING.HTB = {
        kdc = dc01.logging.htb
    }

[domain_realm]
    .logging.htb = LOGGING.HTB
    logging.htb = LOGGING.HTB

```

```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ kinit svc_recovery
Password for svc_recovery@LOGGING.HTB: 
kinit: Password incorrect while getting initial credentials
```

*Passwordが2026に変更されていると予想して再実行*
```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ kinit svc_recovery
Password for svc_recovery@LOGGING.HTB:
```

```zsh
┌──(kali㉿kali)-[~/CTF/HTB/Windows/Logging]
└─$ klist             
Ticket cache: FILE:/tmp/krb5cc_1000
Default principal: svc_recovery@LOGGING.HTB

Valid starting       Expires              Service principal
06/09/2026 05:35:58  06/09/2026 09:35:58  krbtgt/LOGGING.HTB@LOGGING.HTB
        renew until 06/09/2026 09:35:58
```

---

# Initial Access

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

```zsh

```

```zsh

```
---

# Privilege Escalation

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

```zsh

```

```zsh

```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh

```

</details>
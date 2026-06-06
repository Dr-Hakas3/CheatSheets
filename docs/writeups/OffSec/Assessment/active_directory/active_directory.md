---
title: Active_Directory_Level_1_Assessment
parent:
---

# 1

```zsh
xfreerdp3 /u:offsec /p:lab /d:demo /v:192.168.201.40 /dynamic-resolution
```

```powershell
PS C:\Windows\system32> Get-ADUser -Identity "john" | Select-Object DistinguishedName

DistinguishedName
-----------------
CN=John,OU=HelpDesk,OU=demoUsers,DC=demo,DC=com
```

![](../../../assets/images/Pasted%20image%2020260605042701.png)
# 2

```powershell
PS C:\Windows\system32> (Get-ADComputer -Identity "APPSRV01").SID.Value
S-1-5-21-2661071818-1767017692-878076344-1103
```

![](../../../assets/images/Pasted%20image%2020260605042636.png)

# 3

```powershell
PS C:\Windows\system32> net localgroup "Remote Desktop Users"
Alias name     Remote Desktop Users
Comment        Members in this group are granted the right to logon remotely

Members

-------------------------------------------------------------------------------
john
The command completed successfully.
```

![](../../../assets/images/Pasted%20image%2020260605043007.png)

# 4

![](../../../assets/images/Pasted%20image%2020260605050314.png)

ServerHelpDesk

# 5

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Play/MoneyBoy]
└─$ xfreerdp3 /u:student /p:lab /d:offsec /v:192.168.201.113 /dynamic-resolution
```

```powershell
PS C:\Users\Student> net group /domain

Group Accounts for \\PEN100-DC

-------------------------------------------------------------------------------
*Cloneable Domain Controllers
*DnsUpdateProxy
*Domain Admins
*Domain Computers
*Domain Controllers
*Domain Guests
*Domain Users
*Dooomain Admins
*Enterprise Admins
*Enterprise Key Admins
*Enterprise Read-only Domain Controllers
*Group Policy Creator Owners
*Key Admins
*Protected Users
*Read-only Domain Controllers
*Schema Admins
The command completed successfully.
```

![](../../../assets/images/Pasted%20image%2020260605051016.png)

Dooomain Admins

```powershell
PS C:\Users\Student> net group /domain "Dooomain Admins"
Group name     Dooomain Admins
Comment        Here is your flag: OS{}

Members

-------------------------------------------------------------------------------
Student
The command completed successfully.
```

![](../../../assets/images/Pasted%20image%2020260605050912.png)

# 6 Enum LDAP

## Enum Members

```powershell
PS C:\Users\Student> Get-ADUser -Filter * -Properties * | Select Name

Name
----
Administrator
Guest
krbtgt
Student
Ellie
Wilson
Morgan

```

![](../../../assets/images/Pasted%20image%2020260605051837.png)
## Enum Description

```powershell
PS C:\Users\Student> Get-ADUser -Filter * -Properties description |
>> Select Name,Description

Name          Description
----          -----------
Administrator Built-in account for administering the computer/domain
Guest         Built-in account for guest access to the computer/domain
krbtgt        Key Distribution Center Service Account
Student
Ellie
Wilson
Morgan        Here is your flag: OS{818674cbccb5ea81e4ca5bce7b99ff43}
```

![](../../../assets/images/Pasted%20image%2020260605051854.png)

## 全属性列挙
```powershell
Get-ADUser -Filter * -Properties * | Format-List *
```

```powershell

```
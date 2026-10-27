---
title: PsLoggedOn.exe
parent: Tools
grand_parent: Red Team
---

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

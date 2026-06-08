---
title: PsExec
parent: Active Directory
grand_parent: Red Team
---

## 前提条件
- 標的マシンに認証するユーザーがAdministratorsローカルグループに属していること
- ADMIN$共有が利用可能であること　※デフォルトで有効
- ファイルとプリンターの共有が有効になっていること　※デフォルトで有効
- Windows 10/11 のクライアントOSではデフォルトで無効化されていることが多い

## PsExecの仕組み
コマンドをリモートで実行するために、PsExec は次のタスクを実行します。
- psexesvc.exeをC:\Windowsディレクトリに書き込みます
- リモートホスト上にサービスを作成して起動します
- 要求されたプログラム/コマンドをpsexesvc.exeの子プロセスとして実行します

```powershell
.\PsExec64.exe -i  \\FILES04 -u corp\jen -p Nexus123! cmd
```
![](../../../assets/images/Pasted%20image%2020260502092934.png)

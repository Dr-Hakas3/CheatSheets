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


```bash
evil-winrm -i 192.168.236.220 -u daveadmin -p "qwertqwertqwert123\!\!"
```

## ScriptBlockCode Log Path
```text
Eventviewer\WIndows Logs\Application and Service Logs\Microsoft\Windows\PowerShell\Operational
```
この中からID4104を探す

---


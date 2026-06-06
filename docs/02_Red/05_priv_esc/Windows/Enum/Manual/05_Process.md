---
title: process
parent: Win Privilege Escalation
grand_parent: Red Team
---

# Running processes
現在実行中のアプリケーションを特定
```powershell
Get-Process

Get-Process | Select ProcessName, Path
```
---
# Installed applications
インストールされているすべてのアプリケーションを確認
- 32bit
```powershell
# Windowsレジストリ内の2つのレジストリキーを照会し、32ビットと64ビットの両方のアプリケーションを一覧表示
# 出力をselectにパイプし、引数 displaynameを指定して、アプリケーション名のみを表示
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname

# findstrとの組み合わせ
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | findstr "OS{}"
```

- 64bit
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname

# findstrとの組み合わせ
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | findstr /V "flag{"
```

---

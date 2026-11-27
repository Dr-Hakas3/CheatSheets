---
title: SQL Injection
tags: RedTeam, Web
---
## 1. 概要

SQL Injection（SQLi）は、Webアプリケーションなどが外部入力をSQL文に不適切に組み込むことで、意図しないSQL文を実行させられる脆弱性である。

攻撃者は入力値を操作することで、データベースに対する検索条件の変更、認証回避、情報取得、データ改ざんなどを引き起こす可能性がある。

### 1.1 主な影響

- 認証・認可の回避
    
- データベース内の情報漏えい
    
- データの改ざん・削除
    
- アプリケーション機能の不正利用
    
- DBMSの設定や権限によっては、ファイル操作やOSコマンド実行につながる可能性
    

### 1.2 発生原因

SQL Injectionの主な原因は、ユーザー入力とSQL構文を安全に分離できていないことである。

例えば、次のように入力値を直接連結してSQL文を生成する実装は危険である。

```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
```

入力値がSQL構文として解釈される可能性がある。

対策の基本は、プレースホルダーを利用したパラメータ化クエリである。

---

## 2. SQLの基本構造

### 2.1 SELECT文

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

|要素|役割|
|---|---|
|SELECT|取得するカラムを指定|
|FROM|対象テーブルを指定|
|WHERE|レコードの検索条件を指定|
|ORDER BY|結果の並び順を指定|
|UNION|複数のSELECT結果を結合|

### 2.2 SQL Injectionが成立する仕組み

1. アプリケーションがユーザー入力を受け取る
    
2. 入力値をSQL文に組み込む
    
3. 入力値がSQL構文として解釈される
    
4. 本来想定していないSQL処理が実行される
    

### 2.3 SQL InjectionとNoSQL Injection

SQL InjectionはSQLを使用するデータベースに対する攻撃である。

一方、NoSQL InjectionはMongoDBなどのNoSQLデータベースを利用するアプリケーションに対し、クエリ構造や演算子を不正に操作する攻撃である。

本ノートでは、NoSQL InjectionもDBMS別の関連技術として扱う。

---

## 3. 攻撃分類

### 3.1 In-band SQL Injection

攻撃者が送信したSQL文の結果を、同じ通信経路で取得する手法。

- Error-Based SQL Injection
    
- Union-Based SQL Injection
    

### 3.2 Inferential SQL Injection

直接データが返却されない場合に、アプリケーションの応答差や処理時間などから情報を推測する手法。

- Boolean-Based Blind SQL Injection
    
- Time-Based Blind SQL Injection
    

### 3.3 Out-of-band SQL Injection

通常のHTTPレスポンスとは異なる通信経路を利用して情報を取得する手法。

- DNSを利用したデータ送信
    
- HTTPなどを利用した外部通信
    

---

## 4. 攻撃の基本フロー

### 4.1 入力箇所の特定

- ログインフォーム
    
- 検索フォーム
    
- URLパラメータ
    
- Cookie
    
- HTTPヘッダー
    
- APIリクエスト
    

### 4.2 脆弱性の確認

- シングルクォートなどの入力による応答差
    
- SQLエラーの発生
    
- 条件式による応答差
    
- 処理時間の変化
    

### 4.3 DBMSの推定

エラー内容、関数、構文、レスポンスなどからDBMSを推定する。

### 4.4 攻撃可能性の検証

- カラム数の確認
    
- UNION句の成立確認
    
- データベース情報の取得可能性
    
- 権限・実行可能な機能の確認
    

### 4.5 影響範囲の確認

- 参照可能なデータ
    
- 更新・削除可能なデータ
    
- DBユーザーの権限
    
- OSやファイルシステムへの影響
    

---

## 5. DBMS別の特徴

|DBMS|主な特徴|
|---|---|
|MySQL|`information_schema`、`CONCAT()`、`VERSION()`|
|Microsoft SQL Server|`@@VERSION`、`DB_NAME()`、T-SQL|
|PostgreSQL|`version()`、`current_database()`|
|Oracle|`v$version`、`SYS_CONTEXT()`|
|NoSQL / MongoDB|JSON形式のクエリ、演算子、JavaScript関連機能|

各DBMS固有の構文・関数・制約は、個別ページで解説する。

---

## 6. 検知・対策

### 6.1 主な検知観点

- SQL構文を含む不自然なリクエスト
    
- SQLエラーの大量発生
    
- 短時間に繰り返される条件式の変更
    
- 通常と異なる応答時間
    
- DB監査ログ上の不審なクエリ
    
- WAFによるSQLi関連ルールの検知
    

### 6.2 主な対策

|対策|内容|
|---|---|
|パラメータ化クエリ|SQL構文と入力値を分離する|
|入力値検証|想定する型・形式・長さを検証する|
|最小権限|DBアカウントの権限を必要最小限にする|
|エラー制御|SQL内部情報を外部に表示しない|
|WAF|不審なリクエストを検知・遮断する|
|ログ監視|アプリケーションとDBのログを監視する|

WAFは補助的な防御であり、パラメータ化クエリなどの根本対策の代替にはならない。

---

## 7. 個別技術ページ

### 7.1 Basic

- [[Error_Based_SQLi|Error-Based SQL Injection]]
    
- [[Union_Based_SQLi|Union-Based SQL Injection]]
    
- [[Boolean_Based_SQLi|Boolean-Based SQL Injection]]
    
- [[Time_Based_SQLi|Time-Based SQL Injection]]
    
- [[Out_of_Band_SQLi|Out-of-Band SQL Injection]]
    

### 7.2 DBMS

- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/02_DBMS/MySQL|MySQL]]
    
- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/02_DBMS/MSSQL|Microsoft SQL Server]]
    
- [[02_DBMS/PostgreSQL|PostgreSQL]]
    
- [[02_DBMS/Oracle|Oracle]]
    
- [[NoSQL|NoSQL Injection]]
    

### 7.3 Advanced

- [[03_Advanced/Stacked_Queries|Stacked Queries]]
    
- [[03_Advanced/Second_Order_SQLi|Second-Order SQL Injection]]
    
- [[03_Advanced/WAF_Bypass|WAF Bypass]]
    

### 7.4 Practical

- [[04_Practical/Authentication_Bypass|Authentication Bypass]]
    
- [[04_Practical/Data_Extraction|Data Extraction]]
    
- [[04_Practical/File_Operations|File Operations]]
    

---

## 8. 参考資料

- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
    
- [OWASP - SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
    
- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection)
    
- [PortSwigger - SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
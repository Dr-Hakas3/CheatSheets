# MySQL操作
## ログイン
```bash
mysql -u root -p 'root' -h 192.168.56.16 -P 3306

# 
mysql -h 192.168.121.16 -u root -p --skip-ssl
```

## DB情報の取得
DBのバージョン
```bash
select version();
```

現在のDBユーザー
```bash
select system_user();
```

DBのリスト
```bash
show databases;
```

DBの選択
```bash
use DB_NAME;
```

Tablesの一覧（DB洗濯後）
```bash
show tables;
```
カラムの一覧
```bash
DESCRIBE users;
# 省略
DESC users;

show COLUMNS form users;
```

## テーブル内容取得
```bash
# ユーザ名leonの情報取得
SELECT * FROM users WHERE user_name= 'leon'

# ユーザ名offsecの情報（パスワード又はそのハッシュ値等）の取得
select user, authentication_string FROM mysql.user where user = 'offsec';

# userというテーブルを持つDBの検索
select table_schema, table_name from information_schema.tables where table_name like '%user%';
```

---
## OS操作
- MySQL 8.0.30以降可能

バージョン確認
```bash
select version();
```

ユーザ名
```bash
select sysexec('whoami');
```

ファイル操作
```bash
# 現在のユーザ権限の確認
select current_user();

# 現在の権限の確認
show grants for current_user();
# DB選択
use test;

# テーブルの確認
show tables;

# ファイル読み込み
LOAD DATA INFILE '/etc/passwd' INTO TABLE mytable;

# ファイルの書き込み
select 'hacked' into outfile '/tmp/test.txt';
# 結果（通常はエラー）
ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
```

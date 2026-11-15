---
title: NoSQL
tags:
  - MongoDB
---


## 1. 概要

NoSQL Injectionは、NoSQLデータベースを利用するアプリケーションにおいて、ユーザー入力がクエリやデータベース操作の構造に不適切に組み込まれることで発生する脆弱性である。

SQL Injectionと異なり、必ずしもSQL構文を利用するわけではない。

MongoDBの場合、JSON形式のクエリや演算子を利用して検索条件を構築するため、入力値がオブジェクトや演算子として解釈されることが攻撃につながる。

### 1.1 主な影響

- 認証回避
    
- 検索条件の改ざん
    
- データの不正取得
    
- データの改ざん・削除
    
- アプリケーションロジックの不正操作
    

### 1.2 主な対象

|データベース|特徴|
|---|---|
|MongoDB|JSON/BSON形式のドキュメント指向DB|
|CouchDB|HTTP APIとJSONを利用|
|Redis|Key-Value型データストア|
|Elasticsearch|JSONベースの検索・分析エンジン|

本ページではMongoDBを中心に解説する。

---

## 2. MongoDBの基本構造

### 2.1 ドキュメント構造

MongoDBはデータをドキュメントとして保存する。

例：

```json
{
  "_id": 1,
  "username": "admin",
  "password": "password123",
  "role": "administrator"
}
```

### 2.2 基本的な検索

```javascript
db.users.find({
    username: "admin"
})
```

### 2.3 クエリ演算子

MongoDBでは、検索条件に演算子を利用できる。

|演算子|意味|
|---|---|
|`$eq`|等しい|
|`$ne`|等しくない|
|`$gt`|より大きい|
|`$gte`|以上|
|`$lt`|より小さい|
|`$lte`|以下|
|`$in`|指定した配列のいずれかに一致|
|`$nin`|指定した配列のいずれにも一致しない|
|`$regex`|正規表現による検索|
|`$exists`|フィールドの存在確認|
|`$or`|OR条件|
|`$and`|AND条件|

これらの演算子自体は正規の機能である。問題は、ユーザーが意図せずクエリ構造を操作できる実装にある。

---

## 3. NoSQL Injectionの発生原理

### 3.1 脆弱な実装例

Node.jsとMongoDBを利用したログイン処理の例。

```javascript
app.post('/login', async (req, res) => {
    const user = await db.collection('users').findOne({
        username: req.body.username,
        password: req.body.password
    });

    if (user) {
        res.send('Login successful');
    } else {
        res.send('Login failed');
    }
});
```

この実装では、`req.body.username` や `req.body.password` に文字列ではなくオブジェクトが渡された場合、MongoDBのクエリ構造に影響を与える可能性がある。

### 3.2 攻撃が成立する条件

- HTTPリクエストからオブジェクト形式の入力を受け付ける
    
- 入力値を適切に型検証していない
    
- 入力値をそのままMongoDBのクエリに渡している
    
- アプリケーション側の認証ロジックが検索結果だけに依存している
    

---

## 4. 主な攻撃パターン

### 4.1 Operator Injection

MongoDBのクエリ演算子を入力値として注入する手法。

代表例：

```json
{
  "username": {
    "$ne": null
  }
}
```

`$ne` は「指定した値と等しくない」という条件を表す。

例えば、次のクエリが実行された場合、

```javascript
db.users.findOne({
    username: {
        $ne: null
    }
})
```

usernameがnullではないユーザーが検索対象になる。

ただし、これだけで必ず認証を回避できるわけではない。パスワード検証、入力処理、クエリ構造、アプリケーション側の制御に依存する。

### 4.2 Comparison Operator Injection

比較演算子を利用して検索条件を変更する。

例：

```json
{
  "password": {
    "$gt": ""
  }
}
```

空文字列より大きい値という条件を指定する例である。

### 4.3 Regex Injection

正規表現演算子を利用して検索条件を変更する。

例：

```json
{
  "username": {
    "$regex": "^admin"
  }
}
```

`^admin` はadminから始まる文字列に一致する。

### 4.4 Logical Operator Injection

論理演算子を利用して検索条件を変更する。

例：

```json
{
  "$or": [
    {
      "username": "admin"
    },
    {
      "username": "test"
    }
  ]
}
```

OR条件によって複数の検索条件を指定できる。

---

## 5. HTTPリクエストによる検証

### 5.1 通常のログインリクエスト

```http
POST /login HTTP/1.1
Host: target.local
Content-Type: application/json

{
  "username": "admin",
  "password": "password123"
}
```

### 5.2 Operator Injectionの検証例

```http
POST /login HTTP/1.1
Host: target.local
Content-Type: application/json

{
  "username": {
    "$ne": null
  },
  "password": {
    "$ne": null
  }
}
```

このリクエストは、入力値が文字列としてではなく、MongoDBの演算子を含むオブジェクトとして処理されるかを確認するための検証例である。

### 5.3 検証時の確認事項

- HTTPリクエストのContent-Type
    
- JSONとしてオブジェクトが受け付けられるか
    
- アプリケーションが入力値をどのように処理するか
    
- MongoDBに渡されるクエリの構造
    
- 認証結果やレスポンスの差異
    
- エラーメッセージやアプリケーションログ
    

---

## 6. 攻撃成立時の挙動と結果の読み方

|状況|考えられる原因|
|---|---|
|400 Bad Request|JSON形式や入力形式が不正|
|401 Unauthorized|認証に失敗|
|403 Forbidden|アクセス制御による拒否|
|500 Internal Server Error|クエリ処理や型変換時のエラー|
|通常のログイン失敗|演算子が無効化・文字列化されている可能性|
|認証成功|認証条件が意図せず変更された可能性|

HTTPステータスだけでは脆弱性の有無を確定できない。サーバー側のクエリ構造や認証処理も確認する必要がある。

---

## 7. NoSQL Injectionの検知

### 7.1 HTTPログの確認

次のような文字列や構造を含むリクエストを確認する。

- `$ne`
    
- `$gt`
    
- `$regex`
    
- `$where`
    
- `$or`
    
- `$exists`
    

ただし、これらはMongoDBの正規の演算子でもあるため、文字列の存在だけで攻撃と判断してはいけない。

### 7.2 検知観点

- 通常の文字列フィールドにオブジェクトが送信されている
    
- リクエスト内に予期しない演算子が含まれている
    
- 同一エンドポイントに対して検索条件が繰り返し変更されている
    
- 認証失敗と成功が短時間に繰り返されている
    
- MongoDBのクエリ構造に想定外の条件が含まれている
    

---

## 8. 対策

### 8.1 入力値の型検証

ユーザー名やパスワードなど、文字列であるべき入力値について、文字列以外を拒否する。

```javascript
if (
    typeof req.body.username !== 'string' ||
    typeof req.body.password !== 'string'
) {
    return res.status(400).send('Invalid input');
}
```

### 8.2 入力値のスキーマ検証

入力値の型、長さ、形式をサーバー側で検証する。

例：

- username：文字列
    
- password：文字列
    
- usernameの最大長を制限
    
- 不要なフィールドを拒否
    
- 想定外のオブジェクトや配列を拒否
    

### 8.3 クエリ構造の固定

ユーザー入力からクエリの演算子やフィールド名を自由に指定できないようにする。

```javascript
const username = req.body.username;
const password = req.body.password;

if (
    typeof username !== 'string' ||
    typeof password !== 'string'
) {
    return res.status(400).send('Invalid input');
}

const user = await db.collection('users').findOne({
    username: username
});
```

なお、パスワードをそのままDB検索条件に利用するのではなく、保存済みのパスワードハッシュを取得し、安全なパスワード検証処理で照合する設計が望ましい。

### 8.4 その他の対策

|対策|内容|
|---|---|
|入力値検証|型・形式・長さを検証|
|クエリ構造の固定|ユーザー入力による演算子指定を防止|
|最小権限|DBユーザーの権限を制限|
|エラー制御|内部エラー情報を外部に返さない|
|ログ監視|不審な演算子やクエリを監視|
|認証設計|パスワードハッシュを適切に検証|

---

## 9. SQL Injectionとの違い

|比較項目|SQL Injection|NoSQL Injection|
|---|---|---|
|主な対象|RDBMS|NoSQL DB|
|クエリ形式|SQL|JSON/BSONなど|
|攻撃対象|SQL構文|クエリ構造・演算子など|
|代表的な攻撃|UNION、Boolean、Time-Based|Operator Injection、Regex Injection|
|主な対策|パラメータ化クエリ|型検証・クエリ構造の固定|

NoSQL Injectionはデータベースごとにクエリ仕様が異なるため、MongoDBの攻撃手法をすべてのNoSQL製品に適用できるわけではない。

---

## 10. 実践演習・検証環境

検証には、次のような環境が利用できる。

- 自前のMongoDB検証環境
    
- Node.js + Express + MongoDB
    
- 意図的に脆弱な認証処理を持つローカルアプリケーション
    
- Burp SuiteによるHTTPリクエストの変更
    

検証時は、正常系と異常系の両方を用意し、入力値がどのようにクエリに反映されるかを比較する。

---

## 11. 関連ページ

- [[../index|SQL Injection]]
    
- [[MySQL|MySQL]]
    
- [[MSSQL|Microsoft SQL Server]]
    
- [[PostgreSQL|PostgreSQL]]
    
- [[Oracle|Oracle]]
    

---

## 12. 参考資料

- [PortSwigger - NoSQL Injection](https://portswigger.net/web-security/nosql-injection)
    
- [OWASP - NoSQL Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html)
    
- [MongoDB - Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/)
    
- [MongoDB - Query and Projection Operators](https://www.mongodb.com/docs/manual/reference/operator/query/)
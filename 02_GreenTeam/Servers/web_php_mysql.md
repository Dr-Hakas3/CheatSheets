
```
HTML → PHP → SQL → MySQL
```

のデータの流れを確認したうえで、

通常のSQL処理
意図的に脆弱なPHP
SQLインジェクションが成立する仕組み
Prepared Statementによる防御を同じ環境で比較できる構成がおすすめです。


# 1. 全体構成

```
[Browser]
    │
    │ HTTP
    ▼
[index.html]
    │
    │ form
    ▼
[PHP]
    │
    │ SQL
    ▼
[MySQL]
    │
    │ SELECT結果
    ▼
[PHP]
    │
    ▼
[HTMLとしてBrowserへ]
```

例えば商品検索なら、

```
ユーザー
  │
  │ name=apple
  ▼
HTMLフォーム
  │
  ▼
PHP
  │
  │ SELECT * FROM food WHERE name = 'apple'
  ▼
MySQL
  │
  │ 結果
  ▼
PHP
  │
  ▼
ブラウザ
```

という流れを実際に追えるようにします。

# 2. Ubuntuに入れるもの

学習環境なら以下で十分です。

```bash
sudo apt update

sudo apt install apache2
sudo apt install php libapache2-mod-php php-mysql
sudo apt install mysql-server
```

確認：

```
apache2 -v
php -v
mysql --version
```

```
Apache：

sudo systemctl status apache2
```

```
MySQL：

sudo systemctl status mysql
```

ブラウザから、

http://localhost/ を開いてApacheのページが表示されればOKです。

# 3. 学習用DBを作る

MySQLへ入ります。

```
sudo mysql
```

DBを作成：

```
CREATE DATABASE web_lab;
```

ユーザーも作ります。

```
CREATE USER 'webuser'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON web_lab.* TO 'webuser'@'localhost';
FLUSH PRIVILEGES;
```

DBを選択：

```
USE web_lab;
```

商品テーブル：

```
CREATE TABLE food (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INT NOT NULL
);
```

データ：

```
INSERT INTO food (name, price) VALUES
('Apple', 150),
('Banana', 120),
('Orange', 180),
('Melon', 500),
('Strawberry', 400);
```

確認：

```
SELECT * FROM food;
```

# 4. HTMLを作る

```
sudo mkdir -p /var/www/html/sql_lab
sudo nano /var/www/html/sql_lab/index.html
```

例えば、

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SQL Lab</title>
</head>
<body>

<h1>Food Search</h1>

<form action="search.php" method="GET">
    <label>商品名：</label>
    <input type="text" name="name">
    <button type="submit">検索</button>
</form>

</body>
</html>
```

ブラウザ：

http://localhost/sql_lab/

# 5. PHPからMySQLへ接続

まず、

```bash
sudo nano /var/www/html/sql_lab/search.php
```

ここではあえてSQLインジェクションを理解できるように、脆弱なコードを作ります。

```php
<?php

$pdo = new PDO(
    'mysql:host=localhost;dbname=web_lab;charset=utf8mb4',
    'webuser',
    'password123'
);

$name = $_GET['name'];

$sql = "SELECT * FROM food WHERE name = '$name'";

echo "<h2>実行SQL</h2>";
echo "<pre>" . htmlspecialchars($sql) . "</pre>";

$stmt = $pdo->query($sql);

echo "<h2>検索結果</h2>";

while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    echo "ID: " . htmlspecialchars($row['id']) . "<br>";
    echo "Name: " . htmlspecialchars($row['name']) . "<br>";
    echo "Price: " . htmlspecialchars($row['price']) . "<br>";
    echo "<hr>";
}
?>
```

ここがSQLインジェクション学習の核心です。

```sql
$sql = "SELECT * FROM food WHERE name = '$name'";
```

ユーザー入力が、そのままSQL文の一部になっています。

# 6. まず普通に動かす

ブラウザから、 http://localhost/sql_lab/index.html を開いて、Appleと入力。

PHP内部では、

```
SELECT * FROM food WHERE name = 'Apple'
```

が生成されます。

MySQLは、

```sql
SELECT
    *
FROM
    food
WHERE
    name = 'Apple'
```

として解釈します。

ここでは、

```
HTML
 ↓
GETパラメータ
 ↓
PHP $_GET
 ↓
SQL文字列
 ↓
MySQL
 ↓
結果
 ↓
PHP
 ↓
HTML
```

という流れを観察できます。

# 7. SQLインジェクションを理解する

例えば入力値が、

```
' OR '1'='1
```

だったとします。

PHPは入力値をそのまま埋め込むので、

```sql
SELECT * FROM food WHERE name = '' OR '1'='1'
```

になります。

重要なのは、ユーザー入力が単なるデータではなくSQL構文として解釈されてしまうことです。

本来

```
name = 'Apple'
```


攻撃入力

```
' OR '1'='1
```


結果

```
name = '' OR '1'='1'
```

となります。

'1'='1' は真なので、WHERE条件全体が成立します。

そのため複数の商品が返ってきます。

# 8. ここで重要なポイント

SQLインジェクションは、「危険な文字を入力した」ことそのものが本質ではありません。

本質は、

```
ユーザー入力
     ↓
SQL文の構造に混入
     ↓
DBMSがSQL構文として解釈
```

されることです。

つまり、データとSQL命令の境界が壊れています。

# 9. 次に安全なPHPを作る

同じ検索機能をPrepared Statementで作ります。

```bash
sudo nano /var/www/html/sql_lab/search_safe.php
```

```php
<?php

$pdo = new PDO(
    'mysql:host=localhost;dbname=web_lab;charset=utf8mb4',
    'webuser',
    'password123'
);

$name = $_GET['name'] ?? '';

$sql = "SELECT * FROM food WHERE name = ?";

$stmt = $pdo->prepare($sql);
$stmt->execute([$name]);

echo "<h2>検索結果</h2>";

while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    echo "ID: " . htmlspecialchars($row['id']) . "<br>";
    echo "Name: " . htmlspecialchars($row['name']) . "<br>";
    echo "Price: " . htmlspecialchars($row['price']) . "<br>";
    echo "<hr>";
}
?>
```

HTMLも、

```html
<form action="search_safe.php" method="GET">
    <input type="text" name="name">
    <button type="submit">安全な検索</button>
</form>
```

として比較できます。

# 10. 脆弱版と安全版の違い

脆弱版
```
$name = $_GET['name'];

$sql = "SELECT * FROM food WHERE name = '$name'";

$stmt = $pdo->query($sql);
```

構造としては、

```
ユーザー入力
    ↓
SQL文字列へ連結
    ↓
SQLとして解析
```

です。

Prepared Statement
```
$name = $_GET['name'];

$sql = "SELECT * FROM food WHERE name = ?";

$stmt = $pdo->prepare($sql);
$stmt->execute([$name]);
```

こちらは、

```
SQL構造
   ↓
prepare
   ↓
パラメータ
   ↓
execute
```

という分離が行われます。

したがって、入力値にSQL構文らしい文字列が含まれていても、基本的にSQL文の構造としてではなくパラメータ値として扱われます。

# 11. 最終的にはこの構成がおすすめ

```
/var/www/html/sql_lab/
│
├── index.html
│
├── search.php
│       ↑
│       │ SQL Injection学習用
│
├── search_safe.php
│       ↑
│       │ Prepared Statement
│
├── login.php
│       ↑
│       │ 認証処理の学習
│
└── login_safe.php
```
        ↑
        │ 安全な認証処理

DB：

```
web_lab
│
└── food
    ├── id
    ├── name
    └── price
```

そして学習順序を、

```
① HTMLフォーム
       ↓
② PHP $_GET / $_POST
       ↓
③ PHP → MySQL
       ↓
④ SELECT
       ↓
⑤ ユーザー入力をSQLへ連結
       ↓
⑥ SQL Injectionの成立
       ↓
⑦ Prepared Statement
       ↓
⑧ 脆弱版 vs 安全版
       ↓
⑨ ログイン処理
       ↓
⑩ 認証系SQL Injection
```

とすると、「HTML → PHP → SQL」というWebアプリの基本構造と、SQLインジェクションがなぜ起きるのかを同時に理解できます。

なお、この環境はlocalhostまたは隔離したVM内だけで実施するのが適切です。
脆弱版PHPは学習目的で意図的に脆弱にしているため、インターネット公開はしないでください。
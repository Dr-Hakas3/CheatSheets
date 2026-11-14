Burp Suiteのデフォルト設定では、通信機能によって異なります。

- Proxy：ブラウザ本来のUser-Agentを引き継ぐ
- Repeater：リクエストに含まれるUser-Agentを基本的に維持する
- Intruder：元のリクエストのUser-Agentを基本的に維持する
- Scanner：Burp Scanner固有のUser-Agentを使用する場合がある

### Chromium

![[Pasted image 20261115001818.png]]

つまり、通常のBurp Proxy経由でChromeを操作しているだけなら、サーバー側にはChromeのUser-Agentが見えます。





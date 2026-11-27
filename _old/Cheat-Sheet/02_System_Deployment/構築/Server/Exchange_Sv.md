
# Exchange Server 構築手順

## 目次
1. [システム要件](#システム要件)
2. [ダウンロードとインストール準備](#ダウンロードとインストール準備)
3. [Active Directory の準備](#active-directory-の準備)
4. [Exchange Server のインストール](#exchange-server-のインストール)
5. [Exchange Server の設定](#exchange-server-の設定)
6. [クライアントアクセスとテスト](#クライアントアクセスとテスト)
7. [セキュリティ設定と最適化](#セキュリティ設定と最適化)

---

## 1. システム要件
Exchange Serverをインストールする前に、以下のシステム要件を満たしていることを確認します。

- **OS**: Windows Server 2019/2022
- **メモリ**: 最小16GB（推奨32GB以上）
- **ディスク容量**: 最低30GB（推奨はメールボックス数に応じて増やす）
- **ネットワーク**: ドメインコントローラーとの接続が可能であること
- **Active Directory**: AD環境が必要

## 2. ダウンロードとインストール準備

### Exchange Server のダウンロード
1. [Microsoft公式サイト](https://www.microsoft.com/en-us/microsoft-365/exchange/email)からExchange Serverの評価版または購入したバージョンをダウンロードします。

### 前提条件のインストール
2. PowerShellを管理者権限で実行し、Exchangeに必要な役割や機能をインストールします。
   ```bash
   Install-WindowsFeature ADLDS, RSAT-ADDS, NET-Framework-Features, Desktop-Experience, Web-Server, Web-Mgmt-Console
   ```

3. .NET Frameworkの最新バージョンをインストールします。これは、Exchange Serverの動作に必要です。

## 3. Active Directory の準備
Exchange ServerはActive Directoryと連携するため、インストール前にADスキーマを拡張する必要があります。

1. Exchangeメディアのセットアップフォルダ内の「Setup.exe」を実行します。
2. Active Directoryを拡張するためのコマンドを実行します。
   ```bash
   Setup.exe /PrepareSchema /IAcceptExchangeServerLicenseTerms
   Setup.exe /PrepareAD /OrganizationName:"YourOrganizationName" /IAcceptExchangeServerLicenseTerms
   ```

3. ドメインの準備も同様に行います。
   ```bash
   Setup.exe /PrepareDomain /IAcceptExchangeServerLicenseTerms
   ```

## 4. Exchange Server のインストール
1. Exchange Serverのインストーラーを実行し、「Exchange管理センター」にアクセスします。
2. インストール手順に従い、役割（メールボックス、クライアントアクセスなど）を選択してインストールします。
3. インストール後、サーバーを再起動します。

## 5. Exchange Server の設定
### メールボックスデータベースの作成
1. 「Exchange管理センター」にアクセスし、メールボックスデータベースを作成します。
2. メールボックスデータベースの保存先や設定を指定します。

### 受信コネクタと送信コネクタの設定
1. **受信コネクタ**の設定で、外部からのメールを受信できるように構成します。
2. **送信コネクタ**の設定で、外部宛のメールを送信できるように構成します。

## 6. クライアントアクセスとテスト
### Outlook クライアントの設定
1. Outlookクライアントをインストールし、Exchange Serverに接続します。
2. 自動検出機能（Autodiscover）を利用して簡単に接続を設定します。
3. ExchangeサーバのサービスのIMAP4を起動し、自動起動にする
4. プロキシを使用している場合はで*.domainname.ne.jpを除外する

### Webメール（OWA）の確認
1. ブラウザから`https://[サーバーのFQDN]/owa`にアクセスし、OWA（Outlook Web Access）が動作するか確認します。

## 7. セキュリティ設定と最適化
### SSL証明書の設定
1. SSL証明書を購入または無料の証明書（Let’s Encryptなど）を利用して、Exchange Serverに適用します。
2. 証明書のインポート後、OWAやその他のクライアント接続でSSLを強制します。

### スパム対策とメールフィルタリング
1. スパムフィルタやマルウェア対策を有効にして、セキュリティを強化します。

### バックアップとメンテナンス
1. メールボックスデータベースの定期的なバックアップを設定します。
2. Exchange Serverの最適化や定期的なメンテナンスを行います。
```

これでExchange Serverの構築手順をマークダウン形式で作成しました。さらに詳細な設定や最適化に関しても各項目に追加することができます。
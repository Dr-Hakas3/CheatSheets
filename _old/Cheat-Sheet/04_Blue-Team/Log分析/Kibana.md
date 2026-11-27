
# Kibanaの使い方

## 目次

1. [Kibanaのインストール](#kibanaのインストール)
   - [Dockerを使ったインストール](#dockerを使ったインストール)
   - [直接インストール](#直接インストール)
2. [Kibanaへのアクセス](#kibanaへのアクセス)
3. [インデックスパターンの設定](#インデックスパターンの設定)
4. [データの探索](#データの探索)
   - [検索の例](#検索の例)
   - [Cobalt Strikeの通信の検索](#cobalt-strikeの通信の検索)
5. [データの可視化](#データの可視化)
6. [ダッシュボードの作成](#ダッシュボードの作成)
7. [アラートの設定](#アラートの設定)

## Kibanaのインストール

### Dockerを使ったインストール

KibanaをDockerでインストールするには、以下のコマンドを使用します。

```bash
docker run -d --name kibana -p 5601:5601 --link elasticsearch:elasticsearch docker.elastic.co/kibana/kibana:7.17.4
```

### 直接インストール

1. Kibanaの公式ウェブサイトから、対応するバージョンをダウンロードします。
   - [Kibana Downloads](https://www.elastic.co/downloads/kibana)

2. ダウンロードしたファイルを解凍し、Kibanaディレクトリに移動します。

3. Kibanaを起動します。

```bash
./bin/kibana
```

## Kibanaへのアクセス

- Kibanaが起動しているサーバーのブラウザで `http://localhost:5601` にアクセスします。

## インデックスパターンの設定

1. Kibanaのダッシュボードにログインします。
2. 左側のメニューから「Management（管理）」を選択し、「Index Patterns（インデックスパターン）」をクリックします。
3. 「Create index pattern（インデックスパターンの作成）」をクリックします。
4. データを検索するインデックス名（例: `logstash-*`）を入力し、「Next step（次のステップ）」をクリックします。
5. デフォルトのタイムフィールド（例: `@timestamp`）を選択し、「Create index pattern（インデックスパターンの作成）」をクリックします。

## データの探索

データの探索には、「Discover」機能を使用します。

### 検索の例

以下に、`Discover` 機能で使用できる検索の例を示します。

1. **全データの表示**

   ```text
   *
   ```

2. **特定のフィールドでの検索**

   ```text
   status:200
   ```

3. **複数の条件での検索**

   ```text
   status:200 AND extension:("jpg" OR "png")
   ```

4. **範囲指定での検索**

   ```text
   @timestamp:[2024-01-01 TO 2024-01-31]
   ```

5. **フルテキスト検索**

   ```text
   message:"error occurred"
   ```

6. **正規表現を使った検索**

   ```text
   url:/^\/api\/v1\/.*/
   ```

7. **フィールドの存在確認**

   ```text
   _exists_:response_time
   ```

8. **フィールドの欠如確認**

   ```text
   NOT _exists_:user_agent
   ```

9. **数値の範囲検索**

   ```text
   response_time:[100 TO 500]
   ```

10. **ソートを使った検索**

    ```text
    * | sort @timestamp desc
    ```

### Cobalt Strikeの通信の検索

Cobalt Strikeは特定のポートやプロトコルを使用して通信するため、それらのパターンを利用して検索します。以下にいくつかの検索クエリの例を示します。

1. **特定のポートでの通信**

   ```text
   destination_port:80 OR destination_port:443
   ```

2. **特定のIPアドレスへの通信**

   ```text
   destination_ip:10.0.0.1
   ```

3. **特定のプロトコルでの通信**

   ```text
   protocol:tcp
   ```

4. **特定のユーザーエージェントによる通信**

   ```text
   user_agent:"Cobalt Strike"
   ```

5. **Cobalt StrikeのBeacon通信の検索**

   ```text
   user_agent:"Beacons"
   ```

6. **特定のHTTPリクエストパターン**

   ```text
   request:"POST /api"
   ```

7. **エンコードされたペイロードの検索**

   ```text
   message:"base64"
   ```

8. **特定のデータサイズ**

   ```text
   bytes:[100 TO 1000]
   ```

9. **Cobalt StrikeのC2通信の検索**

   ```text
   request_uri:"/c2/"
   ```

10. **SSL/TLSの使用確認**

    ```text
    tls_version:1.2
    ```

## データの可視化

1. 左側メニューから「Visualize Library（可視化ライブラリ）」を選択し、「Create visualization（可視化の作成）」をクリックします。
2. 可視化のタイプを選択（例: Pie chart, Line chart, Bar chart）します。
3. インデックスパターンを選択し、可視化の設定を行います（例: 軸、メトリック、フィルターなど）。
4. 設定が完了したら、「Save（保存）」をクリックし、可視化を保存します。

## ダッシュボードの作成

1. 左側メニューから「Dashboard（ダッシュボード）」を選択し、「Create new dashboard（新しいダッシュボードの作成）」をクリックします。
2. 「Add an existing visualization（既存の可視化の追加）」をクリックし、先ほど作成した可視化を追加します。
3. レイアウトを調整し、必要に応じてフィルターや検索条件を設定します。
4. ダッシュボードを保存します。

## アラートの設定

1. 左側メニューから「Management（管理）」を選択し、「Stack Management（スタック管理）」をクリックします。
2. 「Alerts and Actions（アラートとアクション）」を選択します。
3. 「Create alert（アラートの作成）」をクリックし、アラートの条件とアクションを設定します。
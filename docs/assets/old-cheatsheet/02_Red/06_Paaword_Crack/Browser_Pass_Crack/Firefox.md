## firefox_decrypt.py
### 概要
- firefox_decrypt.py は、Mozilla Firefoxに保存されたパスワードを復号するPythonスクリプトです。このツールは、Firefoxの内部データベースファイルから暗号化されたパスワードを抽出し、それらを復号して表示します。
- python3で動作します。
#### リポジトリ
https://github.com/unode/firefox_decrypt

### 使用方法
```bash
python3 firefox_decrypt.py .mozilla/firefox/esmhp32w.default-default/
```
#### 依存関係
このスクリプトを実行するには、以下のライブラリが必要です。
- cryptography
- sqlite3
##### 依存関係のインストールは以下のコマンドで行えます。
```bash
pip install cryptography
```
#### スクリプトの基本的な流れ
- Firefoxプロファイルディレクトリの特定。
- logins.json ファイルから保存されたアカウント情報を取得。
- Firefoxが保存している暗号化されたパスワードを復号するために、key4.db データベースを使用。
- 復号されたパスワードを表示。
#### オプション
このスクリプトには一般的に引数やオプションはありませんが、以下のようにスクリプト内でプロファイルのパスなどをカスタマイズすることができます。

- firefox_profile_path:
特定のFirefoxプロファイルフォルダを指定してパスワードを復号する場合は、直接スクリプト内のプロファイルパスを変更します。
- 復号プロセス
firefox_decrypt.py は以下の手順でFirefoxの保存パスワードを復号します。
  - Firefoxプロファイルの特定:

スクリプトは、通常のプロファイルディレクトリ (~/.mozilla/firefox または %APPDATA%\Mozilla\Firefox\Profiles\) を探し、最も新しいプロファイルを選択します。
  - キーの抽出:
key4.db ファイル内のマスターパスワードのキーを取得します。
  - パスワードの復号:
logins.json から暗号化されたパスワードを取得し、抽出したキーを使用して復号します。

### 注意事項
- Firefoxが稼働している環境:

このツールを使用する際、ターゲットのFirefoxがローカルでインストールされ、かつパスワードが保存されている必要があります。
- マスターパスワード:
Firefoxでマスターパスワードが設定されている場合は、このスクリプトを使用しても復号に失敗する可能性があります。その場合、別の手法でマスターパスワードを入力する必要があります。
- 法的・倫理的な問題:
このツールは、本人の所有するシステム上のパスワードを復号するために使用することが前提です。第三者の情報を無断で取得することは違法です。
### 参考リンク
firefox_decrypt.py GitHub リポジトリ
Mozilla Firefox サポートページ
### 実行結果の例
```bash
URL: https://example.com
Username: user@example.com
Password: password123
```
このガイドに沿って、firefox_decrypt.pyを利用し、Firefoxに保存されたパスワードを安全に管理してください。

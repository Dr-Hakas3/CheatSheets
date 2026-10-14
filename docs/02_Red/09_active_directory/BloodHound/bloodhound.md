---
title: bloodhound
parent: Tools
grand_parent: Red Team
---

<details markdown="1">
<summary>Install</summary>

```zsh
./bloodhound-cli install
```
![](../../../../../../assets/images/Pasted%20image%2020260523181224.png)

# Default Password
```zsh
[+] BloodHound is ready to go!
[+] You can log in as `admin` with this password: **************************
[+] You can get your admin password by running: bloodhound-cli config get default_password
[+] You can access the BloodHound UI at: http://127.0.0.1:8080/ui/login
```
＊の行に出力される
# PATH
```zsh
echo 'export PATH=$PATH:/opt/bloodhound' >> ~/.zshrc
source ~/.zshrc
```
![](../../../../../../assets/images/Pasted%20image%2020260523181233.png)

# Password Reset
パスワードを紛失した場合は、BloodHound CLI を使用してローカルでリセットできます。
```zsh
./bloodhound-cli resetpwd
```

</details>


<details markdown="1">
<summary>Usage</summary>

```zsh
BloodHound CEを導入したあとは、日々の起動・停止、パスワードのリセットなどを bloodhound-cli コマンドで管理できる。

Docker Composeに慣れているとつい docker compose up/down を使いがちだが、私はdocker compose を直接使っていたことで設定ファイルの整合性に失敗し、初期化に失敗し復旧に苦労した。
以後は素直に bloodhound-cli を使うことにした。
```
# サービスの起動
```zsh
bloodhound-cli containers up
```

# ログイン
## URL
```zsh
http://127.0.0.1:8080/ui/login
```

## Credential
```zsh
admin
*****
```

# サービスの停止（データは維持）
```
bloodhound-cli containers stop
```

# 停止中のサービスを再開
```
bloodhound-cli containers start
```

# コンテナの削除（ボリュームは残る）
```
bloodhound-cli containers down
```

# パスワードの再発行
```
bloodhound-cli resetpwd
```

# 現在稼働中のコンテナ一覧
```
bloodhound-cli running
```

# 実際のコマンド群やヘルプ
```
bloodhound-cli help

BloodHound CLI is a command line interface for managing BloodHound and
associated containers and services. Commands are grouped by their use.

Usage:
  bloodhound-cli [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  config      Display or adjust the configuration
  containers  Manage BloodHound containers with subcommands
  help        Help about any command
  install     Builds containers and performs first-time setup of BloodHound
  logs        Fetch logs for BloodHound services
  resetpwd    Reset the admin password
  running     Print a list of running BloodHound services
  uninstall   Remove all BloodHound containers, images, and volume data
  update      Update the BloodHound container images if an update is available
  version     Displays BloodHound CLI's version information

Flags:
  -h, --help   help for bloodhound-cli

Use "bloodhound-cli [command] --help" for more information about a command.
```

このCLIは以下のようなサブコマンドを備えており、GUIが使えない環境でも一通りの操作が可能。
```
コマンド	説明
install	初回インストール（Composeファイル取得 + コンテナ構築）
containers	各種コンテナの起動/停止/再構築など
running	稼働中のサービス確認
config	各種設定ファイルの読み書き
resetpwd	adminパスワードの再発行
uninstall	コンテナ・ボリュームの削除（環境初期化）
update	イメージの更新
bloodhound-cli [command] --help で各コマンドの詳細も確認できる。
```

</details>


<details markdown="1">
<summary>SharHound</summary>

# ドメインデータを収集する
- SharpHoundはC#で記述
- Windows API関数とLDAP名前空間関数を使用
- より長期間にわたるドメインの変化を確認するために使用できるlooping（ループ処理機能）関数もサポートしている
## 準備
https://github.com/SpecterOps/SharpHound/releases
から最新のzipファイルをKaliマシンにダウンロードします 。次に、zipファイルからSharphound.ps1ファイルを抽出し、CLIENT75マシンに転送します。転送が完了したら、PowerShellウィンドウを開いてスクリプトをメモリにインポートします。

```bash
python3 -m http.server 80
```

### 接続
```bash
xfreerdp3 /u:stephanie /p:'LegmanTeamBenzoin!!' /d:corp.com /v:192.168.158.75 /dynamic-resolution
```

### ダウンロード
ブラウザからKaliにアクセスしダウンロード

### インストール
```powershell
cd .\Downloads\
powershell -ep bypass
Import-Module .\Sharphound.ps1
```

SharpHound を実行するには、まず Invoke-BloodHoundを実行する必要があります。
この段階では SharpHound のみを実行しているため、これは直感的ではありません。
Get -Helpを実行してこのコマンドの詳細を確認しましょう。
```powershell
Get-Help Invoke-BloodHound
```

### データ収集
まず、様々な収集方法を記述する-CollectionMethodから始めます 。今回は、ローカルグループポリシーを除くすべての収集方法を実行する「All」データの収集を試みます。

SharpHoundはデフォルトでJSONファイルにデータを収集し、自動的にzip圧縮します。
-ZipPasswordを使用してパスワードを設定可能。
この出力ファイルは、以下のように「corp audit」というプレフィックスを付けてデスクトップに保存します。
```powershell
Invoke-BloodHound -CollectionMethod All -OutputDirectory C:\Users\stephanie\Desktop\ -OutputPrefix "corp audit"
```

```
309 objects finished
```
合計309個のオブジェクトをスキャン

### 収集したデータの確認
```powershell
ls C:\Users\stephanie\Desktop\
```

```
-a----         8/16/2025   9:07 AM          29814 corp audit_20250816090729_BloodHound.zip
-a----         8/16/2025   9:07 AM           2110 MTk2MmZkNjItY2IyNC00MWMzLTk5YzMtM2E1ZDcwYThkMzRl.bin
```
Sharphoundはデータ収集を高速化するためにbinキャッシュファイルを作成しました。このファイルは分析には不要なので、削除しても問題ありません。

---
# BloodHoundを使用してデータを分析する
## 準備
### Neo4jの起動
```bash
sudo neo4j start
```

## 初期設定（ブラウザアクセス）
http://localhost:7474
- Username neo4j
- Password neo4j
![](../../../../../../assets/images/Pasted%20image%2020260523053035.png)
- ログイン後にパスワード変更を求められる
- データベース認証時に必要となるため記録しておく
- NewPasswordはbloodhound

## Bloodhoundの起動
bloodhoundの起動前に設定ファイル(/etc/bhapi/bhapi.json)のneo4jのsearetの部分にパスワードを反映させる

```bash
bloodhound
```
起動後自動的にブラウザが立ち上がり、ログインを求める認証ウィンドウが表示される。
- Username admin
- Password BloodHound2025!

## データのアップロード
WindowsマシンからKali Linuxマシンにzipファイルを転送する必要があります。その後、 GUI右側の「データのアップロード」機能を使用してzipファイルをアップロードするか、BloodHoundのメインウィンドウにドラッグ＆ドロップします。どちらの場合も、プログレスバーにアップロードの進行状況が表示されます。

1. 左メニューのAdministration -> UploadFileをクリック -> SharpHoundで作成したZIPファイルをドラッグ＆ドロップ
2. StatusがCompleteになったら解析へ
## 解析

## 削除
1. 左メニューのAdministration -> Database Managementをクリック -> すべてにチェックを入れDeleteをクリック
2. ポップアップにDelete this environment dataを入力しConfirmをクリック

</details>


<details markdown="1">
<summary>bloodhound-python</summary>

# bloodhound-python
```zsh
bloodhound-python -u "hrapp-service" -p 'Untimed$Runny' -d hokkaido-aerospace.com -c all --zip -ns 192.168.186.40
```
![](../../../../../../assets/images/Pasted%20image%2020260523053026.png)

</details>

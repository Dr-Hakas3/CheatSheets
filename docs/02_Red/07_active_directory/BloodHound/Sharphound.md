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


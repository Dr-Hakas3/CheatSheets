### awk
- ログ解析などに有用なコマンド
- awkはスペースでフィールドを区切る
- awk '条件 {処理}'
```bash
awk '/exe/  {print $0}'
```
exeのあるファイルを表示
```bash
awk '{print $6}' wordpress.log | sort | uniq -c
```

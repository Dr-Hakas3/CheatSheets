---
title: User
parent: Windows
grand_parent: General
nav_order: 6
---
## ユーザ関連
net_user
- ユーザの追加
```bash
net user hacker hacker123 /add
```

```bash
net localgroup Administrators hacker /add
```

```bash
net localgroup "Remote Desktop Users" hacker /ADD
```

- パスワード変更
```bash
net user hacker newpassword
```

```bash
net user /domain hacker newpassword
```


## 他者の権限でコマンド実行

# runas
```bash
runas /user:Administrator cmd
```
![](../../assets/images/Pasted%20image%2020260426141008.png)

# 認証情報を記録する
```bash
runas /user:Administrator /savecred "notepad.exe"
```
※通常は使用しない
---
## ユーザ関連

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
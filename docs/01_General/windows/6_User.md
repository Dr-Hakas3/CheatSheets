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
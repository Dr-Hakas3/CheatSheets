## 監査ポリシー
- ポリシーの確認
```bash
auditpol /get /category:*
```

- ポリシーの有効化
```bash
auditpol /set /category:"system","account logon" /success:enable /failure:enable
```

- 監査無し
```bash
auditpol /clear /y
```

- Domainサービス列挙
```bash
setspn -T ドメイン -F -Q */*
```
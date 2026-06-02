---
title: impacket-atexec
parent: Tools
grand_parent: Red Team
---

`atexec`は、Windowsのタスクスケジューラを利用してコマンドをリモート実行するツールです。ハッシュを使用して実行する場合は、以下のコマンドを使います。

```bash
atexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 <domain>/<user>@<IP> <command>
```
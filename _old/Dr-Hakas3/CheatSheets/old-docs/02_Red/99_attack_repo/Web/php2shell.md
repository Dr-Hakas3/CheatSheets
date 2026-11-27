---
title: php2shell
parent: Attack Repository
grand_parent: Red Team
nav_order: 10
---
```url
https://x.com/jedisct1/status/2112827369744437640?s=12
```

```url
https://x.com/d117z/status/2112912705426477144?s=12
```

---

#OffSec-Lab
# Target

![[Pasted image 20261027142455.png]]


```zsh
┌──(kali㉿kali)-[~/Tools/PoC]
└─$ git clone https://github.com/eness/php2shell-CVE-2026-109618-CVE-2026-109619-PoC.git
Cloning into 'php2shell-CVE-2026-109618-CVE-2026-109619-PoC'...
remote: Enumerating objects: 51, done.
remote: Counting objects: 100% (51/51), done.
remote: Compressing objects: 100% (37/37), done.
remote: Total 51 (delta 14), reused 45 (delta 9), pack-reused 0 (from 0)
Receiving objects: 100% (51/51), 220.90 KiB | 11.63 MiB/s, done.
Resolving deltas: 100% (14/14), done.
```

```zsh
gobuster dir \                                                                   
-u http://192.168.139.10 \ 
-w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
-x html,php,txt,bak,zip,old \
-t 25 \
-k \
-r \
--random-agent \
-b 403,404 \   
-o gobuster.txt
```

![[Pasted image 20261027142926.png]]
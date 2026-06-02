# redis-info
```zsh
nmap --script redis-info -sV -p 6379 192.168.120.93
```

```zsh
PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 5.0.9 (64 bits)
| redis-info: 
|   Version: 5.0.9
|   Operating System: Linux 3.10.0-1127.19.1.el7.x86_64 x86_64
|   Architecture: 64 bits
|   Process ID: 902
|   Used CPU (sys): 13.524291
|   Used CPU (user): 12.019676
|   Connected clients: 1
|   Connected slaves: 0
|   Used memory: 582.58K
|   Role: slave
|   Bind addresses: 
|     0.0.0.0
|   Client connections: 
|_    192.168.45.159
```
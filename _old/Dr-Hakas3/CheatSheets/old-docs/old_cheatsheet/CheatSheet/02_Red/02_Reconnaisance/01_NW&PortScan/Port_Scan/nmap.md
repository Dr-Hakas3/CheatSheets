# Nmap
## TCP_Scan
```zsh
nmap -Pn -p- --open 192.168.1.1 --min-rate=20000
```
- -Pn
- -p-
- --open
- --min-rate
## UDP_Scan
```bash
nmap -p- -sU 192.168.0.1
```
- -sU UDP
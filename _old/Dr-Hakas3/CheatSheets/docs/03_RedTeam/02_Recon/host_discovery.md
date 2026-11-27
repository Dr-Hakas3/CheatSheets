---
title: Host Discovery
parent: Recon
grand_parent: Red Team
nav_order: 1
---
# Host Discovery
## L2
#### arp-scan
https://whitemarkn.com/learning-ethical-hacker/arp-scan/

```bash
sudo arp-scan --interface=eth0 --localnet
```
#### --interface 
- ethxx
- tun0
- ligolo

#### netdiscover

```zsh
sudo netdiscover -r 192.168.133.0/24 -i eth0
```

---
## L3
#### nmap

```zsh
nmap -sn 192.168.10/24
```

```bash
nmap -sn 192.168.1.1-25
```

#### rustscan

```zsh
rustscan -r 1-65535 -a 10.10.11.248 -- -sV -Pn -A
```
#### zmap

```zsh
zmap -p52869 -wjp.lst -o jp
```
- /etc/zmap/blocklist.conf
*Be careful with the block list*

#### masscan

```zsh
masscan -p80,443 10.0.0.0/8 --rate=10000
```

#### bash script

```zsh
for ip in $(seq 1 254); do ping -c 1 192.168.56.$ip; done
```

#### PowerShell

##### Test-NetConnection

```powershell
Test-NetConnection -Port 445 192.168.50.151
```

##### script

```powershell
1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null
```

---

# Add hostname /etc/hosts

```bash
echo "10.10.11.249 play.crafty.htb" | sudo tee -a /etc/hosts
```
---
title: Port Scan
parent: Recon
grand_parent: Red Team
nav_order: 2
---
# Port Scan

---

# Full / Specify Port Scan
## nmap

```bash
nmap -p- --min-rate 1000 -T4 <IP>
```

```zsh
sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.201.100
```
### UDP_Scan

```bash
sudo nmap -Pn -p- -sU 192.168.0.1
```
- -sU UDP
## autorecon

```zsh
sudo autorecon 192.168.243.248
```
![](../../assets/images/Pasted%20image%2020260508200423.png)

## bash script

```zsh
for port in $(seq 21 1024); do nc -c 1 192.168.56.100 $port; done
```
## nc

```zsh
nc -nvv -w 1 -z 192.168.50.152 3388-3390
```
- -w connect 1 second
- -z No Send Data

```zsh
nc -nv -u -z -w 1 192.168.50.149 120-123
```

## powershell Script

```powershell
1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null
```

## powershell Test-NetConnection

```powershell
Test-NetConnection -Port 445 192.168.50.151
```


---

#  Service Enumeration

```bash
nmap -Pn -p <PORTS> -sC -sV -A <IP>
```

---

## Quick Triage

20 / 21 | [FTP](../03_services/ftp.md) - File transfer |
22       | [SSH](../03_services/ssh.md) - Secure login |
23       | [TELNET](../03_services/telnet.md) - Plaintext login |
25       | [SMTP](../03_services/smtp.md) - Mail service |
53       | [DNS](../03_services/dns.md) - Name resolution |
67 / 68 | [DHCP(../02_services/dhcp.md)] | 
80/443   | [HTTP/HTTPS](../03_services/http.md) - Web |
88      | [Kerberos](../03_services/kerberos.md) - AD auth |
111/2049 | [NFS](../03_services/nfs.md) - File sharing |
135      | [RPC](../03_services/rpc.md) - Windows RPC |
139/445  | [SMB](../03_services/smb.md) - File share |
161/162  | [SNMP](../03_services/snmp.md) - Info leak |
389/636  | [LDAP](../03_services/ldap.md) - Directory |
1433     | [MSSQL](../03_services/mssql.md) - DB |
3306     | [MySQL](../02_services/mysql.md) - DB |
3389     | [RDP](../03_services/rdp.md) - Remote desktop |
5985/5986| [WinRM](../03_services/winrm.md) - Remote mgmt |

---

## Port knocking
### Server side

`/etc/knockd.conf`
```ini
[options]
    logfile = /var/log/knockd.log

[openSSH]
    sequence    = 7000,8000,9000
    seq_timeout = 5
    command     = /sbin/iptables -A INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags    = syn

[closeSSH]
    sequence    = 9000,8000,7000
    seq_timeout = 5
    command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags    = syn
```
- `sequence` specifies the order in which ports are knocked on.
- `command` is the command executed if the sequence is successful. In this example, `iptables` is used to open or close port 22 (SSH).
- `seq_timeout` is the maximum time allowed for the knock sequence.

### Client side

```bash
knock 192.168.1.100 7000 8000 9000
```

or

```zsh
sudo nmap -Pn -sS -r -p 1,2,3 -n 192.168.1.100
```
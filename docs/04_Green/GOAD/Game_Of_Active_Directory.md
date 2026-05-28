---
title: GOAD
parent: Green Team
---
# Create VM

```powershell
PS G:\Virtual Machines\GOAD-main> py goad.py -t install -l GOAD-Light -p virtualbox -m vm
```

![](../../assets/images/Pasted%20image%2020260529031250.png)

```powershell
PLAY RECAP *******************************************************************************************************************************
dc01                       : ok=14   changed=6    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
dc02                       : ok=17   changed=15   unreachable=0    failed=0    skipped=6    rescued=0    ignored=0
srv02                      : ok=13   changed=10   unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

Connection to 192.168.56.3 closed.
[*] Lab successfully provisioned in 10:37:28
```

![](../../assets/images/Pasted%20image%2020260529055618.png)

```zsh
┌──(kali㉿kali)-[~/github/Dr-Hakas3/CheatSheets]
└─$ sudo arp-scan --interface=eth2 --localnet
[sudo] password for kali: 
Interface: eth2, type: EN10MB, MAC: 00:0c:29:6b:86:11, IPv4: 192.168.56.99
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
192.168.56.1    0a:00:27:00:00:13       (Unknown: locally administered)
192.168.56.3    08:00:27:5c:c5:59       PCS Systemtechnik GmbH
192.168.56.10   08:00:27:06:b1:4b       PCS Systemtechnik GmbH
192.168.56.11   08:00:27:49:ff:ac       PCS Systemtechnik GmbH
192.168.56.22   08:00:27:96:75:30       PCS Systemtechnik GmbH

5 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.10.0: 256 hosts scanned in 2.034 seconds (125.86 hosts/sec). 5 responded
```
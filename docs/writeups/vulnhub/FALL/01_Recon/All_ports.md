```zsh
sudo arp-scan --interface=eth0 --localnet
```
![](../../../../assets/images/Pasted%20image%2020260503064439.png)
*192.168.11.21*

```zsh
nmap -Pn -p- 192.168.11.21 --min-rate=5000 --open
```
![](../../../../assets/images/Pasted%20image%2020260503072310.png)
- 22/tcp   open  ssh
- 80/tcp   open  http
- 139/tcp  open  netbios-ssn
- 443/tcp  open  https
- 445/tcp  open  microsoft-ds
- 3306/tcp open  mysql
- 9090/tcp open  zeus-admin

![](../../../../assets/images/Pasted%20image%2020260503072244.png)
![](../../../../assets/images/Pasted%20image%2020260503072335.png)

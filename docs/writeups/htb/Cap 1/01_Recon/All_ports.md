```zsh
nmap -Pn -p- 10.129.49.120 -oN full_port --min-rate=5000
```
![](../../../../../../../../../assets/images/Pasted%20image%2020260503191242.png)

```zsh
nmap -Pn -p21,22,80 -sCV -A 10.129.49.120 -oN port_service --min-rate=5000
```
![](../../../../../../../../../assets/images/Pasted%20image%2020260503191317.png)
![](../../../../../../../../../assets/images/Pasted%20image%2020260503223119.png)
/data/3 -> 3.pcap
![](../../../../../../../../../assets/images/Pasted%20image%2020260503223214.png)
3pcap data exist



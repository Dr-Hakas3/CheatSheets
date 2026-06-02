# Login
## Anonymous connection (-N=no pass)
```bash
rpcclient -U “” -N <ip>
```

## Connection with user
```zsh
rpcclient -U “user” <ip>
```

## Hash Login
```zsh
rpcclient -U 'sub.poseidon\lisa' --pw-nt-hash --password='905ae9b4d957545fb7b9ea0c4333247b' 192.168.133.162
```

---
# Command
## Get information about the DC
```zsh
srvinfo
```

## Get information about objects such as groups (enum*)
```zsh
enumdomains
enumdomgroups
enumalsgroups builtin
```

## Try to get domain password policy
```zsh
getdompwinfo
```
## Try to enumerate different truste domains
```zsh
dsr_enumtrustdom
```

## Get username for a defined user ?
```zsh
getusername
```

## Query user, group etc informations
```zsh
queryuser RID
querygroupmem519
queryaliasmem builtin 0x220
```

## Query info policy
```zsh
lsaquery
```

## Convert SID to names
```zsh
lookupsids SID
```

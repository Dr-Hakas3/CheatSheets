# List shares
```zsh
smbclient -L //IP
smbclient -L <ip>
```

# Connect
```zsh
smbclient \\\\x.x.x.x\\share
smbclient -U “DOMAINNAME\Username” \\\\IP\\IPC$ password
```

# Specify username and no pass
```zsh
smbclient -U “” -N \\\\IP\\IPC$
```
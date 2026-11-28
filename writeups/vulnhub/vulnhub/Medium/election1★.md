- **Independent Challenges**
- **1 Target #1 – 192.168.110.148**
- **1.1 Initial Access –** The settings are not available

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

└─# nmap -p- --min-rate 10000 192.168.110.148

![[election1★ image.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.110.148 | **TCP**: 22,80 |

└─# nmap -p22,80 -sC -sV --min-rate=10000 192.168.110.148 -o nmap-p22,80-sc-sv.txt

![[election1★ image 1.png]]

└─# nmap -A --min-rate=10000 192.168.110.148 -o nmap-A.txt

![[election1★ image 2.png]]

Port 80

└─# whatweb http://192.168.110.148

![[election1★ image 3.png]]

偵察の結果からApacheのバージョンが2.4.29ということがわかります。

└─# feroxbuster -u http://192.168.110.148 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -g

![[election1★ image 4.png]]

Browser Access

![[election1★ image 5.png]]

![[election1★ image 6.png]]

robots.txt

![[election1★ image 7.png]]

http://192.168.110.148/election/admin/

![[election1★ image 8.png]]

**1.2** **Initial Access –** Leakage of passwords from log files due to improper website settings

I found the following files in the Directory enumeration:

http://192.168.110.148/election/admin/logs/

![[election1★ image 9.png]]

The password for the username love is listed.

![[election1★ image 10.png]]

**love****:****P@$$w0rd@123**

└─# ssh love@192.168.110.148

![[election1★ image 11.png]]

SSH login succeeded.

**Local.txt value:**cd38ac698c0d793a5236d01003f692b0

**1.3** **Privilege Escalation -**Known Elevation of Privilege Vulnerabilitieslove@election:~$ cat /etc/os-release

![[election1★ image 12.png]]

Upon investigation, this version of Ubuntu contained a privilege escalation vulnerability.

**1.4** **Post Exploitation**

![[election1★ image 13.png]]

Clone the exploit locally from github.

└─# git clone https://github.com/redhawkeye/sudo-exploit.git

![[election1★ image 14.png]]

![[election1★ image 15.png]]

![[election1★ image 16.png]]

Combine the exploit directory into a zip file.

└─# zip exploit.zip sudo-exploit/ -r

![[election1★ image 17.png]]

Start the web server on the attacker's device.

![[election1★ image 18.png]]

Download exploit on the victim machine.

![[election1★ image 19.png]]

![[election1★ image 20.png]]

Extract the downloaded file, grant permissions and run it to become the root user.

![[election1★ image 21.png]]

**Proof.txt value:**5238feefc4ffe09645d97e9ee49bc3a6
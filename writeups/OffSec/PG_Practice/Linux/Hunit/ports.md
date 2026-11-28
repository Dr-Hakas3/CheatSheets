└─$ sudo nmap -Pn -n 192.168.229.125 -p- -sC -sV --min-rate=5000 -oX hunit.xml

![[ports image 63.png]]

port12445を検出漏れしたため以下で再実行

└─$ sudo nmap -Pn -n 192.168.229.125 -p- -sC -sV -T4 -oX hunit.xml

![[ports image 64.png]]
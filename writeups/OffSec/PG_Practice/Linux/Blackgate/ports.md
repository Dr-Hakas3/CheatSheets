└─$ sudo nmap -Pn -n 192.168.145.176 -p- -sC -sV --min-rate=5000 -oX blackgate.xml

![[ports image 60.png]]

└─$ nmap --script redis-info -sV -p 6379 192.168.145.176

![[ports image 61.png]]
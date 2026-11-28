SSHのwordlistをダウンロード

wget https://github.com/pentestmonkey/yaptest/blob/master/ssh-usernames.txt

![[SSHの調査 image.png]]

普通にアクセスしてみる

ssh 192.168.15.134

![[SSHの調査 image 1.png]]

Easy as 1,2,3とKnockFriendToEnterの文字

knockしてみる

knock 192.168.15.134 1 2 3

![[SSHの調査 image 2.png]]

再度nmap

![[SSHの調査 image 3.png]]

1337が開いた
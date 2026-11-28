〇リバースシェル

・metasploitを試すがうまくいかず

・githubでLotusCMS用のPOCをダウンロード

git clone https://github.com/Hood3dRob1n/LotusCMS-Exploit.git

![[Webからの侵入 image.png]]

![[Webからの侵入 image 1.png]]

・シェルの変更

python -c 'import pty; pty.spawn("/bin/bash")'
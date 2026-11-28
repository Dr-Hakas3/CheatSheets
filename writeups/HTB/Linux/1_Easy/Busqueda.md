![[Busqueda image.png]]

OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[Busqueda image 1.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

この出版物のいかなる部分も、その全部または一部を複製、コピー、譲渡、または著作権所有者に留保するその他の権利(コピーおよびその他すべてのコピー、ネットワークまたはその他の通信手段を使用した転送または送信、遠隔学習のための放送を含む)を、情報ストレージなどのいかなる形式または手段によっても、 OffSecからの事前の書面による許可なしに、送信または検索システム。

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

![[Busqueda image 2.png]]

![[Busqueda image 3.png]]

![[Busqueda image 4.png]]

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: 22,80 |

4.1.2 初期アクセス –

ミドルウェア

![[Busqueda image 5.png]]

![[Busqueda image 6.png]]

このバージョンをGoogleで検索するとPoCが出てくる

![[Busqueda image 7.png]]

![[Busqueda image 8.png]]

![[Busqueda image 9.png]]

![[Busqueda image 10.png]]

Local.txt値:d4e125a2e2ef841fa9a314f7b5f1e488

4.1.3 特権エスカレーション -

![[Busqueda image 11.png]]

![[Busqueda image 12.png]]

![[Busqueda image 13.png]]

4.1.4 エクスプロイト後の処理

![[Busqueda image 14.png]]

Proof.txt値:9649f66ca7671f616b81a1b6ad1dc2f7

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
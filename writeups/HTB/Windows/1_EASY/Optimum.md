![[Optimum image.png]]

OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[Optimum image 1.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

4\. 自主的な課題

4.1ターゲット#1–

4.1.1 初期アクセス –

4.1.2 サービス列挙

![[Optimum image 2.png]]

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: 80 |

4.1.2 初期アクセス –

![[Optimum image 3.png]]

![[Optimum image 4.png]]

Http://FileServer 2.3

![[Optimum image 5.png]]

![[Optimum image 6.png]]

change Local IP

![[Optimum image 7.png]]

nc64.exeをウェブ直下に移動

![[Optimum image 8.png]]

ファイル名の変更

![[Optimum image 9.png]]

80番でWebサーバを起動

![[Optimum image 10.png]]

443で待ち受け

![[Optimum image 11.png]]

exploit実行

![[Optimum image 12.png]]

ターゲット上でnc.exeが実行される

![[Optimum image 13.png]]

ウェブシェルゲット

![[Optimum image 14.png]]

![[Optimum image 15.png]]

Local.txt値:0ff351bfa177bdbbb060c021d9ab2561

4.1.3 特権エスカレーション -

![[Optimum image 16.png]]

4.1.4 エクスプロイト後の処理

Proof.txt値:

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
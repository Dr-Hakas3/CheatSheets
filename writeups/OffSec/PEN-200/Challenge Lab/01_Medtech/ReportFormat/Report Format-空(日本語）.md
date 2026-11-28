OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![](assets/images/Report%20Format-%E7%A9%BA(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image.png)

Copyright © 2023 OffSec Ltd. All rights reserved.

この出版物の全部または一部の一部は、コピー、コピー、転送、または著作権所有者に留保されるその他の権利(写真複写およびその他すべてのコピー、ネットワークまたはその他の通信手段を使用した転送または送信、遠隔学習のための放送を含む)を、情報保存などのいかなる形式または手段によっても、複製、コピー、転送、またはその他の権利を著作権所有者に留保することはできません。 OffSecからの書面による事前の許可なしに、送信または検索システム。

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

[4.1 Target #1 –    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_lnxbz9)

[4.1.1 Service Enumeration    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_35nkun2)

[4.1.2 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ksv4uv)

[5. Active Directory Set    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_44sinio)

[5.1 Ajla – 21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2jxsxqh)

[5.1.1 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_z337ya)

[5.1.2 Privilege Escalation –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3j2qqm3)

[5.1.3 Post-Exploitation    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1y810tw)

[5.2 Poultry –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4i7ojhp)

[5.2.1 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2xcytpi)

[5.2.2 Post-Exploitation](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ci93xb)

[5.3 DC –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2bn6wsx)

[5.3.1 Initial Access –](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_qsh70q)

[5.3.2 Post-Exploitation](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1pxezwc)

**1. OffSec OSCP Exam Penetration Test Report**

**1.1 Introduction**

OffSec ラボおよび試験侵入テストのレポートには、OffSec コースに合格するために実施されたすべての取り組みが含まれています。このレポートには、試験全体に合格するために使用されたすべての項目が含まれている必要があり、試験のすべての側面について正確性と完全性の観点から採点されます。このレポートの目的は、学生が侵入テストの方法論を完全に理解し、OffSec認定プロフェッショナルの資格に合格するための技術的知識を持っていることを確認することです。

**1.2 Objective**

この評価の目的は、OffSec ラボおよび試験ネットワークに対して内部侵入テストを実行することです。学生は、客観的な目標へのアクセスを取得するための系統的なアプローチに従うことを任務としています。このテストでは、実際の侵入テストをシミュレートし、レポート全体を含め、最初から最後までどのように開始するかをシミュレートする必要があります。このドキュメントの後半では、このコースに合格することが期待される内容について十分な情報を提供するサンプル ページがすでに作成されています。サンプル レポートをガイドラインとして使用して、レポートをスムーズに進めます。

**1.3 Requirements**

学生は、この侵入テストレポートに完全に記入し、次のセクションを含める必要があります。

·全体的な高レベルの要約と推奨事項 (非テクニカル)

·方法論のウォークスルーと実行された手順の詳細な概要

·各検出結果には、スクリーンショット、チュートリアル、サンプル コード、該当する場合はproof.txtが含まれています。

·含まれていない追加のアイテム

**2. High-Level Summary**

John Doeは、OffSec Labsに対する内部侵入テストの実施を任されました。内部侵入テストは、内部に接続されたシステムに対する専用の攻撃です。このテストの焦点は、ハッカーと同様の攻撃を実行し、OffSecの内部ラボシステム(THINC.localドメイン)に侵入を試みることです。ジョンの全体的な目標は、ネットワークを評価し、システムを特定し、欠陥を悪用しながら、調査結果をOffSecに報告することでした。

内部侵入テストを実行したところ、OffSecのネットワークでいくつかの憂慮すべき脆弱性が特定されました。攻撃を実行する際、Johnは複数のマシンにアクセスすることができましたが、これは主に古いパッチとセキュリティ構成が不十分であったためです。 テスト中、John は複数のシステムに対する管理レベルのアクセス権を持っていました。すべてのシステムが悪用され、アクセスが許可されました。

**2.1 Recommendations**

John は、テスト中に特定された脆弱性にパッチを適用して、攻撃者が将来これらのシステムを悪用できないようにすることをお勧めします。覚えておくべきことの1つは、これらのシステムには頻繁なパッチ適用が必要であり、パッチが適用された後は、後日発見される追加の脆弱性を保護するために、定期的なパッチプログラムにとどまる必要があるということです。

**3. Methodologies**

John は、広く採用されているアプローチを使用して侵入テストを実行し、OffSec Labs と Exam の環境がどの程度安全であるかをテストするのに効果的でした。以下は、Johnがさまざまなシステムを特定して悪用した方法の内訳であり、見つかったすべての個々の脆弱性が含まれています。

**3.1 Information Gathering**

侵入テストの情報収集部分は、侵入テストの範囲を特定することに重点を置いています。この侵入テストでは、John はラボと試験のネットワークを活用する任務を負いました。具体的なIPアドレスは次のとおりです。

**Exam Network:**

**3.2 Service Enumeration**

侵入テストのサービス列挙部分は、システム上でどのサービスが動作しているかについての情報を収集することに重点を置いています。これは、システムに侵入する可能性のある攻撃ベクトルに関する詳細な情報を提供するため、攻撃者にとって価値があります。システム上でどのアプリケーションが実行されているかを理解することで、攻撃者は実際の侵入テストを実行する前に必要な情報を得ることができます。 場合によっては、一部のポートがリストされていないことがあります。

**3.3 Penetration**

評価の侵入テスト部分は、さまざまなシステムへのアクセスを取得することに重点を置いています。この侵入テスト中に、John は 50 のシステムのうち 10 に無事にアクセスすることができました。

**3.4 Maintaining Access**

システムへのアクセスを維持することは、攻撃者である私たちにとって重要であり、悪用されたシステムに戻れるようにすることは非常に貴重です。侵入テストのアクセス維持フェーズでは、集中的な攻撃(バッファオーバーフローなど)が発生したら、システムに対する管理アクセスが再び可能になることを確認することに重点を置いています。多くのエクスプロイトは一度しか悪用できない場合があり、すでにエクスプロイトを実行した後は、システムに戻ることができない可能性があります。

John は、侵害されたすべてのシステムに管理者と root レベルのアカウントを追加しました。管理/ルートアクセスに加えて、追加のアクセスを確立できるように、Metasploit meterpreter サービスがマシンにインストールされました。

**3.5 House Cleaning**

評価のハウスクリーニング部分では、侵入テストの残骸が確実に除去されます。多くの場合、ツールやユーザーアカウントの断片が組織のコンピューターに残されており、将来的にセキュリティの問題が発生する可能性があります。細心の注意を払い、侵入テストの残骸が残らないようにすることが重要です。

ラボ ネットワークと試験ネットワークの両方のトロフィーが完成した後、John はシステムにインストールされているすべてのユーザー アカウントとパスワード、および Meterpreter サービスを削除しました。OffSec は、システムからユーザー アカウントやサービスを削除する必要はありません。

- **4. Independent Challenges**
- **4.1 Target #1 –**
- **4.1.1 Initial Access –**

**Severity:**

- **4.1.1 Service Enumeration**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP**: |

We run nmap to scan the target and found a few ports open.

**4.1.2** **Initial Access –**

**Local.txt value:**

**4.1.3** **Privilege Escalation -**

**4.1.4** **Post Exploitation**

**Proof.txt value:**

- **5. Active Directory Set**

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
|  | **TCP:** |
|  | **TCP:** |
|  | **TCP:** |

- **5.1  –**
- **5.1.1 Initial Access –**

**Severity:**

- **5.1.2 Privilege Escalation –**

**Severity:**

- **5.1.3 Post-Exploitation**

**System Proof screenshot:**

- **5.2.2 Post-Exploitation**

**Local Proof Screenshot:**

- **5.3 DC –**
- **5.3.1 Initial Access –**
- **5.3.2 Post-Exploitation**

**System Proof Screenshot:**
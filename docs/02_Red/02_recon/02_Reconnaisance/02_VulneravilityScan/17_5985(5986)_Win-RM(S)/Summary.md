「Windows Remote Management (WinRM)」とは、MicrosoftによるWS-Management Protocolの実装です。
リモートのWindowsサーバーで稼働しているWinRMサービスに接続し、インタラクティブな **PowerShellセッション** を取得できることにより、さまざまなベンダーのハードウェアとオペレーティングシステムの相互運用を可能にし、
システム管理者の負担を軽減することを目指しています。  
一方で、WinRMサービスが有効な被害者のマシンでは、「Lateral Movement（横展開）」に利用可能な方法の一つになります。

MITER ATT&CKの「ATT&CK Matrix for Enterprise」では、以下のように分類されています：

- **Technique**: T1028 - Windows Remote Management
- **Tactics**: TA0008 - Lateral Movement

また、CAPEC（Common Attack Pattern Enumeration and Classification）では、「CAPEC-555: 盗まれた資格情報を使用したリモートサービス」として分類されています。
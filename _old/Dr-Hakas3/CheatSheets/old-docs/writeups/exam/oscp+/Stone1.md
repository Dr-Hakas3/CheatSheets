OSCP+/AD 攻略PDF 完全解析
対象PDF: アップロード済み演習ログPDF
---
全体構成
このPDFは以下2系統の攻略記録を含む。
Active Directory Set（AD Set）
Standalone Linux/Web
内容的にはOSCP+試験を強く意識した構成になっており、以下の技術領域を横断している。
Windows Local Privilege Escalation
Active Directory Lateral Movement
Credential Dumping
Scheduled Task Abuse
Pass-the-Hash
Service Account Abuse
SNMP Enumeration
Linux Privilege Escalation
Pivoting
Internal Network Enumeration
---
1. AD SET
---
攻撃チェーン（全体像）
```text
Initial Access
    ↓
Windows User Access
    ↓
Scheduled Task Abuse
    ↓
Local Administrator
    ↓
Mimikatz
    ↓
SAM / LSA Dump
    ↓
Credential Reuse
    ↓
Lateral Movement
    ↓
SRV22 Access
    ↓
More Credential Dumping
    ↓
Domain Credential Discovery
    ↓
Service Credential Abuse
    ↓
DC20 Access
    ↓
Domain Admin Context
```
---
章ごとの要約
---
Chapter 1 — Scheduled Task Enumeration
タスクスケジューラXMLを発見。
```xml
<Interval>PT1M</Interval>
```
1分ごとに実行されるAutomationタスク。
実行対象:
```cmd
C:\Windows\Logs\task.bat
```
バッチ内容:
```bat
net localgroup administrators r.andrews /add
```
つまり:
バッチ改変可能
SYSTEMコンテキスト実行
Local Admin追加可能
という典型的なTask Abuse。
---
Chapter 2 — Local Administrator 化
`r.andrews` を Administrators に追加。
その後:
Evil-WinRM
ipconfig
proof.txt取得
まで実施。
ここで内部セグメントを発見。
ネットワーク
Host	IP
WS26	192.168.123.206
WS26 Internal	172.16.123.206
デュアルNICにより内部ネットワーク存在を把握。
---
Chapter 3 — Mimikatz 実行
実行コマンド:
```text
privilege::debug
 token::elevate
 sekurlsa::logonpasswords
 lsadump::sam
```
目的
SYSTEM token奪取
SAM抽出
認証情報取得
取得情報
Administrator NTLM:
```text
53543e641a6f55819e487a9dc990f59b
```
重要点
`sekurlsa::logonpasswords` は失敗している。
つまり:
Credential Guard
PPL
LSASS保護
などの可能性。
しかし:
```text
lsadump::sam
```
は成功しているため、SAMダンプへ切り替えている。
OSCP+では非常に重要な判断。
---
Chapter 4 — secretsdump による追加抽出
Impacket secretsdump 使用。
回収対象
SAM
LSA
Cached Credentials
Machine Account
DPAPI Keys
発見事項
```text
OSCP.EXAM/r.andrews:$DCC2$
```
Cached domain credential存在。
Machine Account
```text
OSCP\WS26$
```
Kerberos鍵取得。
学習ポイント
secretsdumpで得られるもの:
項目	用途
SAM	Local PTH
DCC2	Offline Crack
MACHINE.ACC	Kerberos Abuse
DPAPI	Secret復号
NL$KM	Cached Credential復号
---
Chapter 5 — SRV22 横展開
別ホスト:
```text
172.16.123.202
```
へ侵入。
ここで再度Mimikatz。
---
Chapter 6 — SRV22 Credential Harvesting
ここがAD攻略の中心。
複数セッションから認証情報取得。
発見ユーザー
User	Type
a.betty	Domain User
jenkins	Local User
kali	Local User
SRV22$	Machine Account
SQLSERVERAGENT	Service
SQLTELEMETRY	Service
MSSQLSERVER	Service
---
Chapter 7 — 平文パスワード取得
最重要資格情報:
```text
a.betty : BrightSunnyDay666
```
これは:
Service Login
Interactive Session
WDigest
Kerberos
いずれかから取得された可能性。
OSCP+で頻出。
---
Chapter 8 — Service Secret Extraction
secretsdump から:
```text
_SC_Jenkins
jenkins:JenkinsAtTop888
```
Service Control Manager secret取得。
さらに:
```text
_SC_SNMPTRAP
oscp\a.betty:BrightSunnyDay666
```
サービスアカウント資格情報再利用。
---
Chapter 9 — DC20 到達
Domain Controller:
```text
172.16.123.200
```
到達後:
```text
proof.txt
```
取得。
つまりAD Set完全攻略。
---
AD Set Credential 一覧
---
Windows / Domain Credentials
User	Password / Hash	Type
r.andrews	Local Admin added	User
Administrator (WS26)	53543e641a6f55819e487a9dc990f59b	NTLM
Administrator (SRV22)	2981a2efea6228b5c3fed526cb102183	NTLM
a.betty	BrightSunnyDay666	Plaintext
jenkins	JenkinsAtTop888	Service Secret
kali	2b576acbe6bcfda7294d6bd18041b8fe	NTLM
SRV22$	a2ac6d5514cf9c91c465176f4b70ee53	Machine NTLM
WS26$	bcf1de2daf0c2e23779b9dfa250bc3d6	Machine NTLM
---
Cached Credentials
User	Hash
r.andrews	DCC2
a.betty	DCC2
---
Service Credentials
Service	Credential
_SC_Jenkins	jenkins:JenkinsAtTop888
_SC_SNMPTRAP	oscp\a.betty:BrightSunnyDay666
---
Host / IP 整理
Host	Role	IP
WS26	Initial Windows	192.168.123.206
WS26 Internal	Pivot NIC	172.16.123.206
SRV22	Internal Server	172.16.123.202
DC20	Domain Controller	172.16.123.200
Linux Host	Standalone	192.168.123.110
---
Enum → Attack 対応表（AD Set）
Enumeration	発見	Attack
Scheduled Tasks	Writable task.bat	Local Admin Add
ipconfig	Internal NIC	Pivoting
Mimikatz	NTLM Hash	Pass-the-Hash
secretsdump	DCC2	Offline Crack
secretsdump	Machine Account	Kerberos Abuse
logonpasswords	Plaintext Password	Credential Reuse
SCM Secret	Service Password	Service Abuse
Multiple Hosts	Internal Segment	Lateral Movement
---
OSCP+視点での重要ポイント（AD）
---
1. 失敗したら別手法へ切り替え
`sekurlsa::logonpasswords`
失敗後:
```text
lsadump::sam
```
へ切り替え。
OSCP+で極めて重要。
---
2. Credential Reuse が中心
攻略の本質:
```text
資格情報の再利用
```
Local Admin
NTLM
Service Secret
Domain Password
を横展開。
---
3. Service Account は超重要
以下はOSCP+頻出:
Jenkins
SQL
SNMP
Backup
Monitoring
---
4. Dual NIC を見逃さない
```text
172.16.x.x
```
内部ネットワーク発見。
Pivotingの起点。
---
5. Machine Account も重要
Machine Account:
```text
HOSTNAME$
```
Kerberos Abuseに利用可能。
---
AD攻略フロー（OSCP+向けテンプレ）
```text
Initial Access
    ↓
Local Enumeration
    ↓
Privilege Escalation
    ↓
Credential Dumping
    ↓
Hash / Password Reuse
    ↓
Internal Enumeration
    ↓
Lateral Movement
    ↓
Service Credential Discovery
    ↓
Domain User Compromise
    ↓
Domain Controller Access
```
---
2. STANDALONE
---
攻撃チェーン（Standalone）
```text
SNMP Enumeration
    ↓
Credential Disclosure
    ↓
SSH Access
    ↓
Linux Enumeration
    ↓
Kernel / Sudo PrivEsc Research
```
---
章ごとの要約
---
Chapter 1 — SNMP Enumeration
SNMP Extend機能からスクリプト情報漏洩。
発見:
```text
/etc/snmp/scripts/passwd.sh
```
さらに:
```text
jack:Not2Easy4Win8!
```
資格情報漏洩。
重要性
SNMP Extend はOSCP系で頻出。
以下を確認すべき:
```bash
snmpwalk
```
OID:
```text
1.3.6.1.4.1.8072
```
---
Chapter 2 — SSH Login
資格情報再利用でSSH成功。
```text
jack@192.168.123.110
```
local.txt取得。
---
Chapter 3 — Linux Enumeration
Linux Exploit Suggester実行。
候補:
CVE	内容
CVE-2022-32250	nftables UAF
CVE-2022-0847	DirtyPipe
CVE-2021-4034	PwnKit
CVE-2021-3156	Baron Samedit
CVE-2021-22555	Netfilter
---
Enum → Attack 対応表（Standalone）
Enumeration	発見	Attack
SNMP	Extend Script	Credential Disclosure
SNMP	Password Leak	SSH Login
SSH Access	Local User	Enumeration
Kernel Version	Vulnerable Kernel	LPE Candidate
sudo/polkit	Old Version	PwnKit / Baron Samedit
---
Standalone Credential 一覧
User	Credential
jack	Not2Easy4Win8!
---
Standalone Host 情報
Host	IP	OS
Linux Host	192.168.123.110	Ubuntu 22.04
---
OSCP+向け重要ポイント（Standalone）
---
1. SNMP を軽視しない
以下は必ず確認:
```bash
snmpwalk -c public -v2c TARGET
```
---
2. Extend MIB は危険
以下が見えたら重要:
```text
NET-SNMP-EXTEND-MIB
```
任意スクリプト情報が漏れる可能性。
---
3. Linux PrivEsc は「候補」を精査
Exploit Suggesterの結果を鵜呑みにしない。
OSCP+では:
sudo version
polkit
capabilities
SUID
cron
writable file
を優先。
---
このPDFから学ぶべきOSCP+重要テーマ
---
AD
Credential Reuse
Service Account Abuse
Lateral Movement
secretsdump
Mimikatz
Pass-the-Hash
Pivoting
Multi-homed Hosts
Internal Enumeration
---
Standalone
SNMP Enumeration
Password Disclosure
Linux Enumeration
Kernel Exploit判定
Sudo / Polkit Abuse
---
試験向け総括
このPDFはOSCP+で重要な以下の思想を強く反映している。
```text
列挙 → 認証情報取得 → 再利用 → 横展開
```
単一Exploit依存ではなく:
情報収集
認証情報再利用
サービス設定
運用ミス
を組み合わせて攻略している点が非常にOSCP+的。
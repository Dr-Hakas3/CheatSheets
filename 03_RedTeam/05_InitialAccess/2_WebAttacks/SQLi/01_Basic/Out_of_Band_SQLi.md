---
tags: [RedTeam, WebSecurity, SQLInjection]
aliases: [OOB SQLi, Out-of-Band SQL Injection]
---

# Out-of-Band SQL Injection

## 1. 概要
Out-of-Band（OOB）SQL Injectionは、通常のHTTPレスポンスとは別の通信経路を利用して、データベースから外部へ情報を送信させる手法。画面にSQL結果が表示されず、Boolean-BasedやTime-Basedの観測も難しい場合に成立する可能性がある。

## 2. 攻撃原理
DBMSや拡張機能が外部ネットワークへアクセスできる場合、その機能を悪用してDNSやHTTP等の通信を発生させる。攻撃者は管理下のDNSログ・HTTPサーバーログ等で通信の発生を観測する。

## 3. 成立条件
- SQL Injectionが成立している
- 対象DBMSに外部通信を発生させる機能がある
- DBユーザーやDBプロセスに必要な権限がある
- ネットワーク出口制御で通信が遮断されていない
- 外部側で通信を観測できる

## 4. 検証手順
1. 対象DBMS・バージョン・権限を把握する
2. DBサーバーから外部への通信可否を管理者と確認する
3. 自組織が管理するDNS名・HTTPエンドポイントを用意する
4. データを含まない無害な識別子で通信発生のみを検証する
5. DNS・プロキシ・FW・DB監査ログを突合する
6. 検証後、不要な外部通信経路を閉じる

## 5. コマンド・検証データ
OOBの具体的な呼び出し構文はDBMS、バージョン、拡張機能、権限に強く依存する。外部へ実データを送信するペイロードを汎用化せず、許可されたラボで無害な一意識別子を用いて通信の有無を確認する。

確認対象：
- DNSクエリログ
- HTTPアクセスログ
- Firewall / Proxyの通信ログ
- DBMS監査ログ
- DBサーバーのプロセス・権限

## 6. 実行結果の読み方
| 観測結果 | 解釈 |
|---|---|
| 管理下DNSに識別子の問い合わせ | DB側または関連処理からDNS通信が発生した可能性 |
| HTTPアクセスログに記録 | HTTP等の外部通信が発生した可能性 |
| DNSのみ成功、HTTPは失敗 | DNSは許可、HTTPは出口制御等で遮断されている可能性 |
| 通信記録なし | 注入不成立、機能・権限不足、出口制御、DNSキャッシュ等の可能性 |

DNS問い合わせが観測されても、必ずしもDBMSが直接発生源とは限らない。送信元IP、時刻、DBログ、プロセス情報で裏付ける。

## 7. DBMS・環境による違い
外部通信機能や必要権限はDBMSごとに異なる。拡張機能の導入状況、OS権限、ネットワーク名前解決、プロキシ設定、クラウド環境の制約も影響する。

## 8. 検知と防御
- DBサーバーからの不要な外向き通信を遮断する
- DNSを許可リゾルバへ限定し、異常な問い合わせを監視する
- DBサービスアカウントのOS権限を最小化する
- 不要な拡張機能・外部アクセス機能を無効化する
- DB監査ログ、DNSログ、FW/Proxyログを相関分析する
- パラメータ化クエリでSQL Injection自体を防ぐ

## 9. 失敗時の確認
- DBサーバーのDNS解決可否
- FW・Proxyの出口制御
- DBサービスアカウントの権限
- DBMSのバージョンと機能制限
- DNSキャッシュやログ収集遅延
- 通信発生元がDBプロセスであることを裏付ける証跡

## 10. 関連ページ
- [[Boolean_Based_SQLi|Boolean-Based SQLi]]
- [[Time_Based_SQLi|Time-Based SQLi]]
- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/02_DBMS/MySQL|MySQL]]
- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/02_DBMS/MSSQL|Microsoft SQL Server]]
- [[../02_DBMS/Oracle|Oracle]]
- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/index|SQL Injection]]

## 11. 参考資料
- https://portswigger.net/web-security/sql-injection
- https://owasp.org/www-community/attacks/SQL_Injection

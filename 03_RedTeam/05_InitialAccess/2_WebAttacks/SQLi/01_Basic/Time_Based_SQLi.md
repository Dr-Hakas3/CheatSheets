---
tags: [RedTeam, WebSecurity, SQLInjection, BlindSQLi]
aliases: [Time-Based Blind SQLi, Time-Based SQL Injection]
---

# Time-Based Blind SQL Injection

## 1. 概要
Time-Based Blind SQL Injectionは、条件に応じてデータベース側の処理時間を変化させ、その遅延を観測することで条件の真偽や情報を推測する手法。

## 2. 攻撃原理
SQL文に時間のかかる処理を条件付きで実行させる。条件が真の場合だけ遅延し、偽の場合は通常時間で応答する、といった差を測定する。

## 3. 成立条件
- SQL Injectionが成立している
- DBMS上で条件付き遅延処理が実行可能
- 応答時間の差がネットワーク・サーバー負荷の揺らぎより十分大きい
- タイムアウトや非同期処理により遅延が失われない

## 4. 検証手順
1. 通常リクエストを複数回送信し、基準応答時間を測定する
2. 許可された検証環境で遅延条件を含むテストを行う
3. TRUE/FALSE条件それぞれの応答時間を複数回測定する
4. 中央値や分布を比較し、再現性を評価する
5. 過剰なリクエストを避け、負荷影響を監視する

## 5. コマンド・検証データ
時間遅延関数はDBMSごとに異なるため、汎用構文は存在しない。検証では対象DBMSの公式ドキュメントで遅延関数・制御構文を確認し、隔離されたラボで最小回数だけ実施する。

代表的な関数・機能：
- MySQL：`SLEEP()`
- Microsoft SQL Server：`WAITFOR DELAY`
- PostgreSQL：`pg_sleep()`
- Oracle：利用可能なパッケージ・権限・バージョンに依存

## 6. 実行結果の読み方
| 観測結果 | 解釈 |
|---|---|
| 条件TRUE時のみ安定して遅延 | Time-Basedの成立を示す可能性 |
| 全リクエストが遅い | サーバー負荷やネットワーク遅延の可能性 |
| 遅延が不安定 | ノイズ、タイムアウト、並列処理等の可能性 |
| 応答時間に差がない | 注入不成立、関数制限、遅延処理の遮断等 |

単発の遅延だけで脆弱性を断定しない。ベースラインを取り、複数回の測定と統計的な比較を行う。

## 7. DBMS・環境による違い
遅延関数、実行権限、トランザクション、クエリ最適化、接続プールの挙動はDBMSや環境に依存する。各DBMSページで仕様を確認する。

## 8. 検知と防御
- パラメータ化クエリを使用する
- 不自然な遅延関数や条件付き待機処理をDB監査ログで監視する
- クエリ実行時間の異常値を監視する
- DBユーザーの権限を最小化する
- アプリケーション側に適切なタイムアウトとレート制限を設定する

## 9. 失敗時の確認
- 通常時の応答時間の分布
- ネットワーク遅延・サーバー負荷
- DB接続プールや非同期処理
- WAFやDB側の関数制限
- リクエストがDBまで到達しているか

## 10. 関連ページ
- [[Boolean_Based_SQLi|Boolean-Based SQLi]]
- [[Out_of_Band_SQLi|Out-of-Band SQLi]]
- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/02_DBMS/MySQL|MySQL]]
- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/02_DBMS/MSSQL|Microsoft SQL Server]]
- [[../02_DBMS/PostgreSQL|PostgreSQL]]
- [[03_RedTeam/05_InitialAccess/2_WebAttacks/SQLi/index|SQL Injection]]

## 11. 参考資料
- https://portswigger.net/web-security/sql-injection/blind
- https://dev.mysql.com/doc/refman/8.4/en/miscellaneous-functions.html
- https://www.postgresql.org/docs/current/functions-datetime.html

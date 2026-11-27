---
tags: [RedTeam, WebSecurity, SQLInjection]
aliases: [Error-Based SQLi, Error-Based SQL Injection]
---

# Error-Based SQL Injection

## 1. 概要
Error-Based SQL Injectionは、データベースが返すエラーメッセージや例外挙動を手掛かりに、SQL Injectionの成立やDBMSの情報を確認する手法。エラーにSQL構文、テーブル名、カラム名、型情報などが含まれる場合、内部構造の推測につながる。

## 2. 攻撃原理
アプリケーションが入力値をSQL文へ不適切に連結し、入力値がSQL構文として解釈されると、構文エラーや型変換エラーなどが発生する。DBMSやアプリケーションがエラー詳細を応答へ露出すると、その内容が情報源になる。

代表的なエラー：
- Syntax error：SQL構文の不整合
- Type conversion error：型変換の失敗
- Invalid column/table：カラム名・テーブル名の不整合
- Function/permission error：関数利用や権限に関する情報

## 3. 成立条件
- 入力値がSQL文へ安全でない方法で組み込まれている
- 入力によってDBエラーを誘発できる
- エラー内容または応答差を観測できる
- 詳細なDBエラーが外部に返る場合、情報取得の精度が高まる

## 4. 検証手順
1. 許可された検証環境で入力点を特定する
2. 通常入力時の応答を記録する
3. クォート等の構文境界を変化させ、応答差を確認する
4. エラーの種類・内容・HTTPステータス・レスポンス長を比較する
5. エラーがアプリケーションで隠蔽される場合は、Boolean-Based等の別方式を検討する

## 5. コマンド・検証データ
入力点の挙動を観察するための基本的な検証文字列（自組織の検証環境のみ）：

```sql
'
```

```sql
"
```

DBMS固有のエラー誘発構文は、対象DBMSとアプリケーションの実装に依存する。汎用ペイロードとして扱わず、検証対象のDBMSに合わせて選定する。

## 6. 実行結果の読み方
| 観測結果 | 解釈の例 |
|---|---|
| SQL syntax error | 入力がSQL構文へ影響した可能性 |
| 型変換エラー | DBまで入力が到達し、型処理に影響した可能性 |
| 一般化されたエラー | アプリケーションが詳細を隠蔽している可能性 |
| 応答に変化なし | エスケープ、パラメータ化、入力拒否などの可能性 |

エラーが発生しただけではSQLi確定ではない。再現性、入力値との因果関係、サーバー側ログやクエリを合わせて評価する。

## 7. DBMS・環境による違い
MySQL、PostgreSQL、Microsoft SQL Server、Oracleではエラー文言・型変換・関数仕様が異なる。DBMS推定では単一のエラー文字列だけに依存せず、複数の観測結果を組み合わせる。

## 8. 検知と防御
- 外部応答には一般化したエラーメッセージを返す
- 詳細な例外情報はサーバー側ログに限定する
- Prepared Statements / parameterized queriesを使用する
- DBアカウントを最小権限にする
- 同一エンドポイントでの異常なエラー率や入力パターンを監視する

## 9. 失敗時の確認
- リクエストのContent-Typeと文字コード
- アプリケーション側の入力検証・エスケープ
- DBまでリクエストが到達しているか
- WAFやミドルウェアによる遮断
- エラーがログにのみ記録され、HTTP応答では隠されていないか

## 10. 関連ページ
- [[Union_Based_SQLi|Union-Based SQLi]]
- [[Boolean_Based_SQLi|Boolean-Based SQLi]]
- [[Time_Based_SQLi|Time-Based SQLi]]
- [[03_RedTeam/04_InitialAccess/2_WebAttacks/SQLi/index|SQL Injection]]

## 11. 参考資料
- https://portswigger.net/web-security/sql-injection
- https://owasp.org/www-community/attacks/SQL_Injection

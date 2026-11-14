---
tags: [RedTeam, WebSecurity, SQLInjection]
aliases: [UNION-Based SQLi, UNION SQL Injection]
---

# Union-Based SQL Injection

## 1. 概要
Union-Based SQL Injectionは、SQLの`UNION`演算子を利用して、元のSELECT結果へ別のSELECT結果を結合し、アプリケーションの応答から追加データを観測する手法。

## 2. 攻撃原理
`UNION`は複数のSELECT結果を縦方向に結合する。結合するSELECT同士には、原則として同じ列数が必要であり、対応する列のデータ型も互換性が必要となる。

```sql
SELECT name, description FROM products
UNION
SELECT username, email FROM users;
```

上記は概念例。実際の成立可否は列数、型、権限、アプリケーションの表示処理に依存する。

## 3. 成立条件
- SQL Injectionが成立している
- 注入位置がSELECT文の構造と整合する
- UNIONを含むクエリが実行される
- 結果セットの一部がHTTP応答等に表示される
- 列数・型の条件を満たす

## 4. 検証手順
1. 入力点と元の応答を特定する
2. 列数を安全な検証方法で推定する
3. UNION結合が成立するか確認する
4. 表示される列・位置を確認する
5. 許可されたテストデータだけを使い、影響範囲を記録する

列数確認の考え方：
- `ORDER BY n`の値を段階的に変え、エラーや応答差を比較する
- `UNION SELECT`にNULLを並べ、列数・型の互換性を検証する

## 5. コマンド・検証データ
列数が3であると仮定した概念的な確認例：

```sql
UNION SELECT NULL, NULL, NULL
```

表示列の位置を確認する概念例：

```sql
UNION SELECT 'A', 'B', 'C'
```

これらは検証用の例であり、注入位置に応じたコメントや括弧の調整が必要になる場合がある。

## 6. 実行結果の読み方
| 観測結果 | 考えられる原因 |
|---|---|
| 列数不一致エラー | UNIONの列数が元のSELECTと一致しない |
| 型不一致エラー | 対応する列の型が互換でない |
| エラーなし・表示なし | 結果列が画面に出ない、またはアプリが結果を加工している |
| マーカー文字列が表示 | 対応する列が応答へ反映されている可能性 |

## 7. DBMS・環境による違い
UNIONの基本要件は共通するが、文字列・数値の型変換、NULLの扱い、文字列連結、コメント構文、メタデータ参照方法はDBMSごとに異なる。詳細は`02_DBMS/`配下を参照。

## 8. 検知と防御
- パラメータ化クエリを使用する
- 動的なテーブル名・カラム名は許可リストで制御する
- SQLエラーを外部に露出しない
- 不自然なUNION構文や繰り返しの列数探索を監視する
- DBアカウントの参照権限を必要最小限にする

## 9. 失敗時の確認
- 注入位置が文字列・数値・括弧内のどこか
- 元のSELECTの列数
- 列ごとのデータ型
- 結果が画面へ出力される設計か
- WAF、ORM、アプリケーションによる変換

## 10. 関連ページ
- [[Error_Based_SQLi|Error-Based SQLi]]
- [[Boolean_Based_SQLi|Boolean-Based SQLi]]
- [[../02_DBMS/MySQL|MySQL]]
- [[../02_DBMS/MSSQL|Microsoft SQL Server]]
- [[../index|SQL Injection]]

## 11. 参考資料
- https://portswigger.net/web-security/sql-injection/union-attacks
- https://owasp.org/www-community/attacks/SQL_Injection

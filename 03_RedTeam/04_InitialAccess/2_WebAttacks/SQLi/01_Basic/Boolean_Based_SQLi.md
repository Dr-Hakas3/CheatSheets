---
tags: [RedTeam, WebSecurity, SQLInjection, BlindSQLi]
aliases: [Boolean-Based Blind SQLi, Boolean SQL Injection]
---

# Boolean-Based Blind SQL Injection

## 1. 概要
Boolean-Based Blind SQL Injectionは、SQLの条件式が真（TRUE）か偽（FALSE）かによってアプリケーションの応答が変化することを利用し、データベース内の情報を推測する手法。SQLエラーや検索結果そのものが表示されない場合にも成立する可能性がある。

## 2. 攻撃原理
攻撃者は真偽が異なる条件を入力し、HTTPステータス、本文、レスポンス長、表示要素などの差を比較する。差が安定して観測できれば、条件を少しずつ変えて情報を推測できる。

## 3. 成立条件
- SQL Injectionが成立している
- 入力がSQLの条件式に影響する
- TRUE/FALSEで応答に観測可能な差が生じる
- 応答差がキャッシュや負荷などのノイズに埋もれない

## 4. 検証手順
1. 正常なリクエストの応答を記録する
2. 真になる条件と偽になる条件を比較する
3. 本文、長さ、ステータス、DOM要素等の差を特定する
4. 複数回実行し、差の再現性を確認する
5. 許可されたテストデータで条件推測を検証する

## 5. コマンド・検証データ
真偽条件の概念例：

```sql
AND 1=1
```

```sql
AND 1=2
```

前者は真、後者は偽となる条件式の例。実際の入力位置や元のクエリ構造に応じて構文は異なる。

## 6. 実行結果の読み方
| 観測 | 解釈 |
|---|---|
| TRUE条件で通常応答、FALSE条件で異なる応答 | 真偽に応じた差がある可能性 |
| 両方同じ応答 | 差が隠蔽されている、注入が成立していない等 |
| 実行ごとに結果が変わる | 動的コンテンツ、負荷、キャッシュ等のノイズ |
| ステータスは同じで本文長だけ異なる | 応答本文の一部が条件に依存している可能性 |

## 7. DBMS・環境による違い
真偽条件の考え方は多くのSQL DBMSで共通するが、文字列比較、照合順序、NULLの扱い、型変換などは異なる。DBMS固有の式は各DBMSページを参照。

## 8. 検知と防御
- パラメータ化クエリを使用する
- 同一パラメータに対する大量の微小な条件変更を監視する
- 応答差だけで情報を推測されないよう、エラー・応答処理を適切に設計する
- DB監査ログとWebアクセスログを相関分析する

## 9. 失敗時の確認
- 応答差が本当に入力条件に起因するか
- 動的広告・時刻・トークン等が本文差を生んでいないか
- キャッシュやロードバランサの影響
- WAFによる遮断や正規化
- 入力値がSQLクエリに到達しているか

## 10. 関連ページ
- [[Time_Based_SQLi|Time-Based SQLi]]
- [[Error_Based_SQLi|Error-Based SQLi]]
- [[Out_of_Band_SQLi|Out-of-Band SQLi]]
- [[03_RedTeam/04_InitialAccess/2_WebAttacks/SQLi/index|SQL Injection]]

## 11. 参考資料
- https://portswigger.net/web-security/sql-injection/blind
- https://owasp.org/www-community/attacks/Blind_SQL_Injection

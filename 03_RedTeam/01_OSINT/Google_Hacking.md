---
layout: default
title: Google Hacking
parent: OSINT
grand_parent: Red Team
nav_order: 3
---
## 1. 概要

Googleの検索演算子を利用して、特定の条件に合致する公開情報を検索する手法。

Google Dorksとも呼ばれる。

## 2. いつ使うか

- 特定のドメインに限定して情報を検索するとき
- 特定のファイル形式を検索するとき
- 特定の文字列を含むページを検索するとき
- 公開されている画像から関連情報を調査するとき

## 3. 前提条件

- Webブラウザ
- Google検索を利用できる環境
- 調査対象に関するキーワードやドメイン

## 4. 判定・切り分け

要追記

## 5. 手順

### 5.1 Google Dorks

旧資料に記載されていた検索演算子。

| 検索演算子 | 用途 |
|---|---|
| `filetype:` | 特定のファイル形式を検索 |
| `site:` | 特定のドメイン・サイトに限定して検索 |
| `"word"` | 指定した文字列と一致する語句を検索 |

使用例:

```text
site:example.com
filetype:pdf
"confidential"
site:example.com filetype:pdf
```

※上記の検索例は演算子の使い方を示すもの。検索結果の取得可能性は対象サイトや検索エンジンの仕様に依存する。

### 5.2 Image Search

画像を使用して類似画像や関連情報を検索する。
1. Google画像検索を開く。
2. カメラマークをクリックする。
3. 画像を貼り付ける、またはドラッグ＆ドロップする。

4. 検索結果を確認する。
6. 失敗時のチェックポイント
要追記
7. 検知される痕跡 (Blue Team)
要追記
8. 防御・対策 (Green Team)
要追記
9. 関連技術
- Domain Research
- Internet Archives
10. 演習・実践記録
要追記
11. 参考・出典
- 旧資料: google_hacking/index.md
12. 学習メモ
要追記
更新履歴
- 2026-11-13: 旧資料から初回移行

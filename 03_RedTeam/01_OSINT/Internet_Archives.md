---
layout: default
title: Internet Archives
parent: OSINT
grand_parent: Red Team
nav_order: 4
---
## 1. 概要

Webアーカイブサービスを利用して、過去に公開されていたWebページやWebサイトの情報を確認する手法。

## 2. いつ使うか

- Webサイトの過去の状態を確認するとき
- 現在は公開されていないページの情報を調査するとき
- 過去の公開情報をOSINT調査に利用するとき

## 3. 前提条件

- 調査対象のURLまたはドメイン
- 各アーカイブサービスにアクセスできる環境

## 4. 判定・切り分け

要追記

## 5. 手順

### 5.1 初期調査

以下のWebアーカイブサービスを利用する。

| サービス            | URL                        | 特徴                     |
| --------------- | -------------------------- | ---------------------- |
| Wayback Machine | https://web.archive.org/   | Webページの過去の保存状態を確認      |
| ウェブ魚拓           | https://megalodon.jp/      | Webページの保存・閲覧           |
| archive.today   | https://archive.ph/        | Webページの保存・閲覧           |
| WARP            | https://warp.da.ndl.go.jp/ | 国立国会図書館インターネット資料収集保存事業 |

### 5.2 詳細調査

要追記

### 5.3 ツールによる自動化

要追記

## 6. 失敗時のチェックポイント

要追記

## 7. 検知される痕跡 (Blue Team)

要追記

## 8. 防御・対策 (Green Team)

要追記

## 9. 関連技術

- [OSINT Methodology](OSINT_Methodology.md)
- [Domain Research](Domain_Research.md)
- [Google Hacking](Google_Hacking.md)

## 10. 演習・実践記録

要追記

## 11. 参考・出典

- [Wayback Machine](https://web.archive.org/)
- [ウェブ魚拓](https://megalodon.jp/)
- [archive.today](https://archive.ph/)
- [WARP（国立国会図書館インターネット資料収集保存事業）](https://warp.da.ndl.go.jp/)

## 12. 学習メモ

### Service Comparison Summary

| Service | Language | Web Archive | Manual Saving | Specialty |
|---|---|---|---|---|
| Wayback Machine | 要確認 | 要確認 | 要確認 | 要確認 |
| ウェブ魚拓 | 要確認 | 要確認 | 要確認 | 要確認 |
| archive.today | 要確認 | 要確認 | 要確認 | 要確認 |
| WARP | 要確認 | 要確認 | 要確認 | 要確認 |


## 更新履歴

- 2026-11-13: 旧資料から初回移行

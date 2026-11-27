```bash
NET-SNMP-EXTEND-MIB::nsExtend              ← ただの入口看板
 └── nsExtendObjects                       ← 本館（ここを歩く）
      ├── nsExtendNumEntries               ← 部屋の数
      ├── nsExtendEntry (index = 名前)
      │     ├── nsExtendCommand            ← 実行されるコマンド
      │     ├── nsExtendArgs               ← 引数
      │     ├── nsExtendInput              ← 入力データ
      │     ├── nsExtendOutput1Line        ← 出力の1行目
      │     ├── nsExtendOutputFull         ← 出力全文
      │     └── nsExtendResult             ← 実行結果（0なら成功）
      └── ...
```
つまりこういう構造の“木”
- nsExtend は 看板
- nsExtendObjects が 実データの建物
- nsExtendEntry."名前" が 個別の部屋
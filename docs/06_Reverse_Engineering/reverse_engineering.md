---
title: Reverse Engineering
nav_order: 6
has_children: true
---
# 解析の流れ

1. プログラムを動かして動きを掴む
2. gdbでmainと関数を把握
3. バッファオーバーフローの変数を探す
4. 呼び出したい箇所のアドレス取得
5. リターンアドレスのあるアドレスの場所を取得
6. ４までのByteを数える（引数のaとかで埋めてみる）
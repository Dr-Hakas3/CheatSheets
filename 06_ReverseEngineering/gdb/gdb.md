---
title: gdb
parent: Reverse Engineering
has_children: true
nav_order: 1
---

# GDBの基本的なコマンド

<details markdown="1">
<summary>GDB起動</summary>

### 起動

```bash
gdb ./program
```

### 実行中プロセスへ接続

```bash
gdb -p PID
```

</details>

<details markdown="1">
<summary>実行</summary>

### プログラム開始

```gdb
run
```

### 引数付き実行

```gdb
run arg1 arg2
```

### 再実行

```gdb
run
```

</details>

<details markdown="1">
<summary>ブレークポイント</summary>

### mainで停止

```gdb
break main
```

### 関数で停止

```gdb
break function_name
```

### 行番号で停止

```gdb
break 123
```

### ブレークポイント一覧

```gdb
info breakpoints
```

### ブレークポイント削除

```gdb
delete 1
```

### 全削除

```gdb
delete
```

</details>

<details markdown="1">
<summary>ステップ実行</summary>

### 関数内部に入る

```gdb
step
```

または

```gdb
s
```

### 関数内部に入らない

```gdb
next
```

または

```gdb
n
```

### 関数終了まで実行

```gdb
finish
```

### 次のブレークポイントまで実行

```gdb
continue
```

または

```gdb
c
```

### 命令単位で実行（REで重要）

```gdb
stepi
```

または

```gdb
si
```

### 命令単位で実行（関数に入らない）

```gdb
nexti
```

または

```gdb
ni
```

</details>

<details markdown="1">
<summary>変数確認</summary>

### 変数表示

```gdb
print variable
```

### 例

```gdb
print count
```

### 16進表示

```gdb
p/x variable
```

### アドレス表示

```gdb
p &variable
```

</details>

<details markdown="1">
<summary>レジスタ確認</summary>

### 全レジスタ表示

```gdb
info registers
```

### RIP

```gdb
p/x $rip
```

### RSP

```gdb
p/x $rsp
```

### RAX

```gdb
p/x $rax
```

</details>

<details markdown="1">
<summary>メモリ確認</summary>

### アドレス内容表示

```gdb
x ADDRESS
```

### 例

```gdb
x 0x404000
```

### 16バイトを16進表示

```gdb
x/16xb 0x404000
```

### 8個の整数表示

```gdb
x/8dw 0x404000
```

### 文字列表示

```gdb
x/s 0x404000
```

### RIP周辺の命令表示

```gdb
x/20i $rip
```

### スタック確認

```gdb
x/64xb $rsp
```

</details>

<details markdown="1">
<summary>スタック解析</summary>

### コールスタック表示

```gdb
backtrace
```

または

```gdb
bt
```

### フレーム移動

```gdb
frame 1
```

### ローカル変数表示

```gdb
info locals
```

### 引数表示

```gdb
info args
```

</details>

<details markdown="1">
<summary>アセンブリ解析</summary>

### 現在の関数を逆アセンブル

```gdb
disassemble
```

### main関数を逆アセンブル

```gdb
disassemble main
```

### Intel記法へ変更

```gdb
set disassembly-flavor intel
```

### 関数一覧

```gdb
info functions
```

### 現在実行位置確認

```gdb
x/10i $rip
```

</details>

<details markdown="1">
<summary>値の変更（デバッグ・解析用）</summary>

### 変数変更

```gdb
set variable count=100
```

### レジスタ変更

```gdb
set $rax=0
```

### メモリ書き換え

```gdb
set *(int*)0x404000=1
```

</details>

<details markdown="1">
<summary>TUIモード（画面分割）</summary>

### ソース表示

```gdb
layout src
```

### アセンブリ表示

```gdb
layout asm
```

### 分割表示

```gdb
layout split
```

### レジスタ表示

```gdb
layout regs
```

### TUI終了

```gdb
Ctrl + X → A
```

</details>

<details markdown="1">
<summary>CTF・リバースエンジニアリングでよく使う流れ</summary>

```bash
gdb ./chall

set disassembly-flavor intel

break main
run

info functions
disassemble main

info registers
x/20i $rip

x/64xb $rsp
x/s $rdi

ni
ni
si

bt
```

</details>

<details markdown="1">
<summary>最重要コマンド（まず覚える）</summary>

| コマンド | 用途 |
|----------|------|
| `run` | 実行 |
| `break` | ブレークポイント |
| `continue` | 続行 |
| `ni` | 命令単位実行 |
| `si` | 命令単位実行（関数に入る） |
| `x` | メモリ表示 |
| `info registers` | レジスタ確認 |
| `disassemble` | 逆アセンブル |
| `bt` | コールスタック確認 |

</details>
---
title: Words
parent: Reverse Engineering
nav_order: 2
---
<details markdown="1">
<summary>命令</summary>

| 命令 | 役割 | 例 |
|------|------|----|
| `mov` | データをコピーする | `mov eax, ebx` |
| `push` | スタックへ値を積む | `push eax` |
| `pop` | スタックから値を取り出す | `pop eax` |
| `lea` | アドレス計算 | `lea eax, [ebx+4]` |
| `xchg` | 値を交換 | `xchg eax, ebx` |
| `nop` | 何もしない | `nop` |

</details>

<details markdown="1">
<summary>計算</summary>

| 命令 | 役割 |
|------|------|
| `add` | 加算 |
| `sub` | 減算 |
| `inc` | +1 |
| `dec` | -1 |
| `imul` | 符号付き乗算 |
| `mul` | 符号なし乗算 |
| `idiv` | 符号付き除算 |
| `div` | 符号なし除算 |

</details>

<details markdown="1">
<summary>比較・条件分岐</summary>

| 命令 | 役割 |
|------|------|
| `cmp` | 比較 |
| `test` | AND比較 |
| `je` | 等しいならジャンプ |
| `jne` | 等しくないならジャンプ |
| `jg` | より大きい |
| `jl` | より小さい |
| `jge` | 以上 |
| `jle` | 以下 |

</details>
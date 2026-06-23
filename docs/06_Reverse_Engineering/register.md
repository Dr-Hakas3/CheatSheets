---
title: Register
parent: Reverse Engineering
nav_order: 1
---
# REで最重要レジスタ

| レジスタ | 意味 |
|----------|------|
| `RIP` | 現在実行中の命令アドレス（Instruction Pointer） |
| `RSP` | スタックの先頭（Stack Pointer） |
| `RBP` | 現在の関数の基準位置（Base Pointer） |
| `RAX` | 戻り値・演算用 |
| `RDI` | 第1引数（Linux x64） |
| `RSI` | 第2引数（Linux x64） |
| `RDX` | 第3引数 |
| `RCX` | 第4引数（Linux x64） / 第1引数（Windows x64） |
| `RFLAGS` | 比較結果や条件分岐に使用するCPUフラグ |

---

# 同じレジスタの64bit・32bit・16bit・8bit版一覧

| 64bit | 32bit | 16bit | 上位8bit | 下位8bit | 主な用途 |
|--------|--------|--------|-----------|-----------|-----------|
| `RAX` | `EAX` | `AX` | `AH` | `AL` | 戻り値・演算 |
| `RBX` | `EBX` | `BX` | `BH` | `BL` | 汎用 |
| `RCX` | `ECX` | `CX` | `CH` | `CL` | カウンタ・引数 |
| `RDX` | `EDX` | `DX` | `DH` | `DL` | 汎用・引数 |
| `RSI` | `ESI` | `SI` | - | `SIL` | ソースポインタ |
| `RDI` | `EDI` | `DI` | - | `DIL` | デスティネーションポインタ |
| `RBP` | `EBP` | `BP` | - | `BPL` | ベースポインタ |
| `RSP` | `ESP` | `SP` | - | `SPL` | スタックポインタ |
| `R8` | `R8D` | `R8W` | - | `R8B` | 汎用 |
| `R9` | `R9D` | `R9W` | - | `R9B` | 汎用 |
| `R10` | `R10D` | `R10W` | - | `R10B` | 汎用 |
| `R11` | `R11D` | `R11W` | - | `R11B` | 汎用 |
| `R12` | `R12D` | `R12W` | - | `R12B` | 汎用 |
| `R13` | `R13D` | `R13W` | - | `R13B` | 汎用 |
| `R14` | `R14D` | `R14W` | - | `R14B` | 汎用 |
| `R15` | `R15D` | `R15W` | - | `R15B` | 汎用 |
| `RIP` | `EIP` | `IP` | - | - | 命令ポインタ |
| `RFLAGS` | `EFLAGS` | `FLAGS` | - | - | CPUフラグ |

---

# GDB・IDA・Ghidraで最優先で覚えるレジスタ

| レジスタ | なぜ重要か |
|----------|------------|
| `RIP` | 次に実行される命令 |
| `RSP` | スタックの状態が分かる |
| `RBP` | ローカル変数の位置が分かる |
| `RAX` | 関数の戻り値 |
| `RDI` | 第1引数（Linux） |
| `RSI` | 第2引数（Linux） |
| `RDX` | 第3引数 |
| `RCX` | 第4引数（Linux）/第1引数（Windows） |
| `RFLAGS` | 条件分岐の判定結果 |

---

# RFLAGSでよく見るフラグ

| フラグ | 意味 |
|----------|------|
| `ZF` | Zero Flag（結果が0） |
| `CF` | Carry Flag（桁あふれ） |
| `OF` | Overflow Flag（符号付きオーバーフロー） |
| `SF` | Sign Flag（負数） |
| `PF` | Parity Flag |
| `AF` | Auxiliary Carry Flag |

```
cmp eax, 5
je success
```

この場合は `ZF=1` なら `je` が実行される。

```
test eax, eax
jne success
```

この場合は `eax != 0` のとき `jne` が実行される。
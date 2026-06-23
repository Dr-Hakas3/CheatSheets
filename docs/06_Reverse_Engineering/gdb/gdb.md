---
title: gdb
parent: Reverse Engineering
has_children: true
nav_order: 11
---
# 命令（データ転送系）

<details markdown="1">
<summary><b>一覧を表示</b></summary>

| 命令 | 役割 | 例 |
|------|------|------|
| `mov` | データをコピーする | `mov eax, ebx` |
| `push` | スタックへ値を積む | `push eax` |
| `pop` | スタックから値を取り出す | `pop eax` |
| `lea` | アドレス計算 | `lea eax, [ebx+4]` |
| `xchg` | 値を交換 | `xchg eax, ebx` |
| `nop` | 何もしない | `nop` |

</details>

---

# 計算（算術演算系）

<details markdown="1">
<summary><b>一覧を表示</b></summary>

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

---

# 比較・条件分岐

<details markdown="1">
<summary><b>一覧を表示</b></summary>

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

---

# 関数呼び出し

<details markdown="1">
<summary><b>一覧を表示</b></summary>

| 命令 | 役割 |
|------|------|
| `call` | 関数呼び出し |
| `ret` | 関数から戻る |
| `enter` | スタックフレーム作成 |
| `leave` | スタックフレーム破棄 |

</details>

---

# ジャンプ系

<details markdown="1">
<summary><b>一覧を表示</b></summary>

| 命令 | 役割 |
|------|------|
| `jmp` | 無条件ジャンプ |
| `je` | Equal |
| `jne` | Not Equal |
| `ja` | Above |
| `jb` | Below |
| `jo` | Overflow |
| `js` | Sign |

</details>

---

# ビット演算

<details markdown="1">
<summary><b>一覧を表示</b></summary>

| 命令 | 役割 |
|------|------|
| `and` | AND |
| `or` | OR |
| `xor` | XOR |
| `not` | 反転 |
| `shl` | 左シフト |
| `shr` | 右シフト |
| `sar` | 算術右シフト |
| `rol` | 左ローテート |
| `ror` | 右ローテート |

</details>

---

# リバースエンジニアリングで頻出

<details markdown="1">
<summary><b>一覧を表示</b></summary>

| 命令 | 意味 |
|------|------|
| `push rbp` | 関数開始 |
| `mov rbp, rsp` | スタックフレーム作成 |
| `sub rsp, XX` | ローカル変数確保 |
| `call` | 関数呼び出し |
| `cmp` | 条件判定 |
| `test eax, eax` | 戻り値チェック |
| `jne` | エラー分岐 |
| `xor eax, eax` | `eax = 0` |
| `lea rcx, [...]` | 引数設定 |
| `ret` | 関数終了 |

</details>

---

# GDB・IDA・Ghidraで最初に覚えるべき14個の命令

<details markdown="1">
<summary><b>一覧を表示</b></summary>

| 命令 | 用途 |
|------|------|
| `mov` | 値のコピー |
| `push` | スタック保存 |
| `pop` | スタック復元 |
| `lea` | アドレス計算 |
| `add` | 加算 |
| `sub` | 減算 |
| `cmp` | 比較 |
| `test` | フラグ確認 |
| `jmp` | 無条件ジャンプ |
| `je` | 条件ジャンプ（Equal） |
| `jne` | 条件ジャンプ（Not Equal） |
| `call` | 関数呼び出し |
| `ret` | 関数終了 |
| `xor` | 初期化（`xor eax,eax`） |

</details>

---

# 最低限覚えておくべき関数プロローグ・エピローグ

<details markdown="1">
<summary><b>一覧を表示</b></summary>

## 関数開始（プロローグ）

```asm
push rbp
mov rbp, rsp
sub rsp, 20h
```

- ベースポインタ保存
- スタックフレーム作成
- ローカル変数領域確保

## 関数終了（エピローグ）

```asm
mov rsp, rbp
pop rbp
ret
```

- スタック復元
- 呼び出し元へ戻る

</details>
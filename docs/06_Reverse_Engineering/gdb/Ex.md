---
title: Exercises001
parent: gdb
grand_parent: Reverse Engineering
---

# 足し算プログラム解析

簡易なプログラムを解析し、プログラムが処理される流れを追う
## code

```c
#include <stdio.h>
#include <stdlib.h>

// 足し算をする関数
int add(int a, int b)
{
    return a + b;
}

int main(int argc, char *argv[])
{
    // 引数の数を確認
    if (argc != 4) {
        printf("使い方: %s 数値1 数値2 出力ファイル\n", argv[0]);
        return 1;
    }

    // コマンドライン引数を整数に変換
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    // add関数を呼び出して計算
    int result = add(a, b);

    // 画面に表示
    printf("%d + %d = %d\n", a, b, result);

    // ファイルを開く
    FILE *fp = fopen(argv[3], "w");

    if (fp == NULL) {
        perror("ファイルを開けません");
        return 1;
    }

    // ファイルに書き込む
    fprintf(fp, "%d + %d = %d\n", a, b, result);

    // ファイルを閉じる
    fclose(fp);

    return 0;
}
```

## コンパイル

```bash
gcc -g -O0 test.c -o test
```

## 使い方

```bash
./test 2 3 result.txt
```

## 解析

### strace

```bash
strace ./test 2 3 result.txt
```

### gdb

#### break main

```bash
break main
run 2 3 result.txt

print argc
print argv[0]
print argv[1]
print argv[2]
print argv[3]

next
next

print a
print b
```

#### break add

```
break add
continue

info args
info frame
info registers

print &a
print &b

x/wd &a
x/wd &b

next
next

print result
print &result
x/wd &result
```


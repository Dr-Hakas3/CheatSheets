---
title: Python
---
# コーディング規約

## PEP 8

---
# if文

Pythonの if x: は、変数 x が真（True）と判定される場合に処理を実行するという意味です。

Pythonでは、if の条件に必ずしも True / False を指定する必要はありません。

1. Trueと判定される値

```
値	判定
True	True
	1	True
	-1	True
"ABC"	True
[1, 2, 3]	True
{"a": 1}	True
False	False
0	False
""（空文字）	False
[]（空リスト）	False
{}（空辞書）	False
None	False
```

2. 具体例

```python
x = "Hello"
if x:
    print("実行される")
```

x に空でない文字列が入っているため、Trueと判定されます。

一方、

```python
x = ""
if x:
    print("実行される")
```

こちらは空文字なのでFalseとなり、処理されません。

---

# コメントアウト

Pythonのコメントアウトは # を使用します。
1. 1行コメント

```python
# これはコメント
print("Hello")  # 行末にも書ける
```


2. 複数行のコメントアウト
各行の先頭に # を付けます。

```python
# print("A")
# print("B")
# print("C")
```



3. VS Code / PyCharm / Kaliなどのショートカット

```
操作	ショートカット
コメントアウト	Ctrl + /
コメント解除	Ctrl + /
```

複数行を選択して Ctrl + / を押すと、一括でコメントアウトできます。

※ Pythonには専用の複数行コメント構文はありません。''' や """ は文字列リテラルであり、コメントとは異なります。

---


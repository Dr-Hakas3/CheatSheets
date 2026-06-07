---
title: Linux Command FIle操作
parent: Linux
grand_parent: General
nav_order: 1
---
# File操作

<details markdown=1><summary>awk</summary>
- ログ解析などに有用なコマンド
- awkはスペースでフィールドを区切る
- awk '条件 {処理}'

exeのあるファイルを表示
```bash
awk '/exe/  {print $0}'
```


```bash
awk '{print $6}' wordpress.log | sort | uniq -c
```


</details>

<details markdown=1><summary>find</summary>
### find

```bash
find / -name ファイル名
```

```zsh
find /home/kevin /home/alice -name test -type f
```


</details>


<details markdown=1><summary>grep</summary>

# Recurs
```bash
grep -r hoge
```

#### AND

```bash
grep hoge | grep fuga
```

#### OR
```bash
grep -e hoge -e fuga
```

</details>


<details markdown=1><summary>tree</summary>

# treeコマンド

```bash
tree -l -L 3 /usr/share/wordlists
```

# フォルダだけ

```zsh
tree -d .
```

</details>

<details markdown="1">

<summary>sed</summary>
### sed
####標準入力からバックスラッシュを削除
```bash
echo "User\\Name" | sed 's/User\\//g'
```
このコマンドを実行すると、「UserName」が出力されます。

#### ファイル内の「User」からバックスラッシュを削除
```bash

sed 's/User\\//g' inputfile.txt > outputfile.txt
```
#### awkとの組み合わせ
```bash
 awk '{print $3}' users.txt| sed 's/User\\//g'  > username.txt
```
#### Interface名を全変更
```bash
![image](https://github.com/user-attachments/assets/2f042e29-36ba-49dd-bf95-592a8c8a0e10)
```

# wordlist + !!!
```zsh
sed 's/$/!!!/' rockyou.txt > mask_word.txt
```
![](../../../assets/images/Pasted%20image%2020260502140113.png)
# ABC123 + wordlist
```zsh
sed 's/^/ABC123/' rockyou.txt > word_mask.txt
```
![](../../../assets/images/Pasted%20image%2020260502140333.png)

# ABC123 + wordlist + !!!
```zsh
sed 's/^/ABC123/' rockyou.txt | sed 's/$/!!!/' > rockyou_hybrid.txt
```
![](../../../assets/images/Pasted%20image%2020260502140450.png)
</details>

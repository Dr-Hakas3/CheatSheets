---
title: FIle
parent: Linux
grand_parent: General
nav_order: 1
---
# File操作
<details markdown="1">
<summary>echo</summary>
hosts

```bash
echo "10.10.11.249 play.crafty.htb" | sudo tee -a /etc/hosts
```
</details>

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

```zsh
grep -rinE '(password|pword|username|user|pass|key|token|secret|admin|login|credentials|cred)' 2>/dev/null
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
![](../../assets/images/Pasted%20image%2020260502140113.png)
# ABC123 + wordlist
```zsh
sed 's/^/ABC123/' rockyou.txt > word_mask.txt
```
![](../../assets/images/Pasted%20image%2020260502140333.png)

# ABC123 + wordlist + !!!
```zsh
sed 's/^/ABC123/' rockyou.txt | sed 's/$/!!!/' > rockyou_hybrid.txt
```
![](../../assets/images/Pasted%20image%2020260502140450.png)
</details>


<details markdown="1">

<summary>vi,vim</summary>

# 置換
1. フォーマット
```bash
:%s/aaa/bbb/g
```
2. ,(カンマ)を改行に置換
```bash
:%s/,/\r/g
```

# xxd mode

```zsh
:%!xxd
```

抜けるとき

```zsh
:%!xxd -r
```
</details>

<details markdown="1">

<summary>cat</summary>
```zsh
cat -A hoge.txt
```
</details>
<details markdown="1">

<summary>cp</summary>
```bash
# cpコマンドでディレクトリ内の中身のみ、他のディレクトリにコピーする 
cp -r dir1/. dir2/
```
</details>

<details markdown="1">

<summary>ls</summary>
sのタイムスタンプを見やすくする

```bash
ls -l --time-style=long-iso
```
</details>

<details markdown="1">

<summary>df,du</summary>
## HDDの使用状況
### df
```bash
df -h
```
## 特定のディレクトリの確認
### du

```bash
du -sh /home
```
</details>

<details markdown="1">

<summary>which,type</summary>
```zsh
type pwd
```

```bash
which python3
```
</details>

<details markdown="1">

<summary>which,type</summary>
```bash
which python3
```
</details>

<details markdown="1">

<summary>zip,unzip,gunzip,7zip</summary>
# 圧縮・解凍

#### .zip

##### 圧縮

```bash
zip archive.zip file.txt
```

##### 解凍

```bash
unzip test.zip
```

</details>

#### .gz

##### 圧縮

```bash
# .gzの圧縮コマンドがありませんでしたので、必要であれば追記してください。
```

##### 解凍

```bash
gzip -d file.gz
```

#### 7zip
# 7-Zip コマンドチートシート

## 圧縮

### 単一ファイル

```bash
7z a archive.7z file.txt
```

### 複数ファイル

```bash
7z a archive.7z file1.txt file2.txt
```

### ディレクトリごと圧縮

```bash
7z a archive.7z mydir/
```

---

## 展開

### 現在のディレクトリへ展開

```bash
7z x archive.7z
```

### 別ディレクトリへ展開

```bash
7z x archive.7z -ooutput
```

> `-o` とディレクトリ名の間にスペースを入れない

---

## アーカイブ内容確認

```bash
7z l archive.7z
```

---

## 整合性チェック

```bash
7z t archive.7z
```

---

## パスワード付き圧縮

### パスワード設定

```bash
7z a archive.7z mydir -pMyPassword
```

### ファイル名も暗号化

```bash
7z a archive.7z mydir -pMyPassword -mhe=on
```

---

## ZIP形式で圧縮

```bash
7z a -tzip archive.zip mydir/
```

---

## 圧縮率指定

### 最大圧縮

```bash
7z a archive.7z mydir/ -mx=9
```

| オプション | 説明 |
|------------|------|
| `-mx=0` | 無圧縮 |
| `-mx=1` | 最速 |
| `-mx=5` | 標準 |
| `-mx=9` | 最大圧縮 |

---

## 分割圧縮

### 2GBごとに分割

```bash
7z a backup.7z bigdir/ -v2g
```

生成例:

```text
backup.7z.001
backup.7z.002
backup.7z.003
...
```

---

## Linuxでよく使う例

### ログをまとめる

```bash
7z a logs.7z *.log
```

### 日付付きバックアップ

```bash
7z a backup_$(date +%F).7z /home/kali/Documents/
```

---

## インストール確認

```bash
which 7z
```

インストールされていない場合:

```bash
sudo apt install p7zip-full
```

---

## よく使うオプション一覧

| オプション | 説明 |
|------------|------|
| `a` | 圧縮（Add） |
| `x` | 展開（フォルダ構造維持） |
| `e` | 展開（フォルダ構造無視） |
| `l` | 一覧表示 |
| `t` | テスト |
| `-oDIR` | 展開先指定 |
| `-pPASS` | パスワード指定 |
| `-mhe=on` | ファイル名暗号化 |
| `-mx=9` | 最大圧縮 |
| `-v2g` | 2GBごとに分割 |
| `-tzip` | ZIP形式で作成 |

## 覚えておくと便利な3つ

```bash
# 圧縮
7z a archive.7z dir/

# 展開
7z x archive.7z

# 中身確認
7z l archive.7z
```

</details>

<details markdown="1">

<summary>tar</summary>
### .tar
#### 圧縮
```bash
tar -zvf archive_name.tar /path/to/directory_or_files
```
#### 解凍
```bash
tar -xvf archive_name.tar.gz /path/to/directory_or_files
```
#### .tar.gz

##### 圧縮

```bash
tar -zcvf xxxx.tar.gz directory
```

##### 解凍

```bash
tar -xzvf filename.tar.gz
```

#### .tar.bz2
##### 圧縮
```bash
tar -jcvf xxxx.tar.bz2 directory
```
##### 解凍
```bash
tar -jxvf xxxx.tar.bz2
```

</details>
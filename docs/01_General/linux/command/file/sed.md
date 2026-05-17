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
![](../../../../assets/old_cheatsheet/Assets/Images/Pasted%20image%2020260502140113.png)
# ABC123 + wordlist
```zsh
sed 's/^/ABC123/' rockyou.txt > word_mask.txt
```
![](../../../../assets/old_cheatsheet/Assets/Images/Pasted%20image%2020260502140333.png)

# ABC123 + wordlist + !!!
```zsh
sed 's/^/ABC123/' rockyou.txt | sed 's/$/!!!/' > rockyou_hybrid.txt
```
![](../../../../assets/old_cheatsheet/Assets/Images/Pasted%20image%2020260502140450.png)
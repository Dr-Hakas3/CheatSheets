列挙と出力
```bash
./linpeas.sh | tee output.txt
```

重要項目
```bash
╣ Files with Interesting Permissions ╠
```

絞り込み
```bash
grep -i suid output.txt
```
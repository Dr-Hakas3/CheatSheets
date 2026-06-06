---
title: Linux Command
parent: Linux
grand_parent: General
---

<details markdown=1><summary># awk</summary>
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


<details markdown="1">
<summary>cat</summary>

```zsh

```

</details>
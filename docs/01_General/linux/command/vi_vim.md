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
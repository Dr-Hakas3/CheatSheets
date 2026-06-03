- パスワード付きzipファイル 解析
```bash
unzip spammer.zip 
Archive:  spammer.zip
[spammer.zip] creds.txt password: 
   skipping: creds.txt
```

```bash
zip2john spammer.zip > spammer.zip.hash
```

```
Created directory: /root/.john
ver 2.0 spammer.zip/creds.txt PKZIP Encr: cmplen=27, decmplen=15, crc=B003611D ts=ADCB cs=b003 type=0
```

```bash
john spammer.zip.hash
```

```
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 12 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
myspace4         (spammer.zip/creds.txt)     
1g 0:00:00:00 DONE 2/3 (2024-09-15 13:00) 16.66g/s 1428Kp/s 1428Kc/s 1428KC/s MINNIE..ship4
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
myspace4
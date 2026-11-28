〇サービス列挙

・nmap -Pn -sV -sC -A -O -p80 192.168.0.107

![[webの調査① image 7.png]]

〇ディレクトリ列挙

gobuster dir -u http://192.168.0.107 -w /usr/share/wordlists/dirb/common.txt

![[webの調査① image 8.png]]

/cache                (Status: 301) \[Size: 353\] \[--> http://192.168.0.107/cache/\]

/core                 (Status: 301) \[Size: 352\] \[--> http://192.168.0.107/core/\]

/data                 (Status: 403) \[Size: 324\]

/favicon.ico          (Status: 200) \[Size: 23126\]

/gallery              (Status: 301) \[Size: 355\] \[--> http://192.168.0.107/gallery/\]

/index.php            (Status: 200) \[Size: 1819\]

/modules              (Status: 301) \[Size: 355\] \[--> http://192.168.0.107/modules/\]

/phpmyadmin           (Status: 301) \[Size: 358\] \[--> http://192.168.0.107/phpmyadmin/\]

/style                (Status: 301) \[Size: 353\] \[--> http://192.168.0.107/style/\]

〇脆弱性調査

nikto -h 192.168.0.107

![[webの調査① image 9.png]]
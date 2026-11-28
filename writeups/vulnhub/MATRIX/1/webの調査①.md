〇サービス詳細

![[webの調査① image 10.png]]

・ディレクトリ列挙

gobuster dir -u http://192.168.0.106 -w /usr/share/wordlists/dirb/common.txt

![[webの調査① image 11.png]]

assetsがあるらしい

・dirbuster -u http://192.168.0.106

![[webの調査① image 12.png]]

情報なし

・assets内の探索

![[webの調査① image 13.png]]

情報なし

〇脆弱性調査

nikto -h 192.168.0.106

![[webの調査① image 14.png]]

情報なし
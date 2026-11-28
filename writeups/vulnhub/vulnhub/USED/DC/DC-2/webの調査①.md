〇ブラウザアクセス

![[webの調査① image.png]]

・Flagをクリック

※その他は英語以外の言語で書かれていて詳細不明

Flag

Flag 1:

Your usual wordlists probably won’t work, so instead, maybe you just need to be cewl.

More passwords is always better, but sometimes you just can’t win them all.

Log in as one to see the next flag.

If you can’t find it, log in as another.

※翻訳

通常の単語リストはおそらく機能しないので、代わりにただ黙って行動する必要があるかもしれません。  
パスワードは多いほど良いのですが、すべてを勝ち取ることができない場合もあります。  
次のフラグを確認するには、ユーザーとしてログインしてください。  
見つからない場合は、別のユーザーとしてログインしてくださ。

![[webの調査① image 1.png]]

ページのソースには特徴的なものは見つけられなかった

・ディレクトリ調査

gobuster dir -u http://dc-2 -w /usr/share/wordlists/dirb/common.txt

/wp-admin             (Status: 301) \[Size: 299\] \[--> http://dc-2/wp-admin/\]

/wp-includes          (Status: 301) \[Size: 302\] \[--> http://dc-2/wp-includes/\]

/wp-content           (Status: 301) \[Size: 301\] \[--> http://dc-2/wp-content/\]

/index.php            (Status: 301) \[Size: 0\] \[--> http://dc-2/\]

![[webの調査① image 2.png]]
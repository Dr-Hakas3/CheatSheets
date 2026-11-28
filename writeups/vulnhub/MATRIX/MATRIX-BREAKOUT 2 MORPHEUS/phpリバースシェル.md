BurpSuiteを使って、phpリバースシェルを張ることにする

・phpリバースシェルのスクリプトを準備し、Burpsuiteを立ち上げ/graffiti.phpにアクセスし、インターセプトの開始

/graffiti.php

![[phpリバースシェル image.png]]

アクセス

![[phpリバースシェル image 1.png]]

一番下のmessage=にphpリバースシェルのスクリプトを丸々貼り付けて、file＝test.phpという名前で送信する

![[phpリバースシェル image 2.png]]

その後nc -nlvp 1234で待受けた状態で、ブラウザでtest.phpにアクセス

![[phpリバースシェル image 3.png]]

待ち受け側

![[phpリバースシェル image 4.png]]

シェルゲット
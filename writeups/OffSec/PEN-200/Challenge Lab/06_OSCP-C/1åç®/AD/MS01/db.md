download

┌──(kali㉿kali)-\[~/…/ChallengeLab/OSCP_C/AD/MS01\]

└─$ file db

db: SQLite 3.x database, last written using SQLite version 3039004, file counter 6, database pages 4, 1st free page 2, free pages 1, cookie 0x7, schema 4, UTF-8, version-valid-for 6

┌──(kali㉿kali)-\[~/…/ChallengeLab/OSCP_C/AD/MS01\]

└─$ strings db

SQLite format 3

Gtablepartnerspartners

CREATE TABLE "partners" (

"id"    INTEGER NOT NULL,

"name"  TEXT NOT NULL,

"password"      TEXT NOT NULL,

"desc"  TEXT NOT NULL,

PRIMARY KEY("id" AUTOINCREMENT)

Ytablesqlite_sequencesqlite_sequence

CREATE TABLE sqlite_sequence(name,seq)

partners

bcorpe7966b31d1cad8a83f12ecec236c384c-+

acorpdf5fb539ff32f7fde5f3c05d8c8c1a6e-L

MMsupport26231162520c611ccabfb18b5ae4dff2support account for internal use+

ecorp7007296521223107d3445ea0db5a04f9-

![[db image.png]]

sqlite> .table

partners

sqlite> select * from partners;

1|ecorp|7007296521223107d3445ea0db5a04f9|-

2|support|26231162520c611ccabfb18b5ae4dff2|support account for internal use

3|bcorp|e7966b31d1cad8a83f12ecec236c384c|-

4|acorp|df5fb539ff32f7fde5f3c05d8c8c1a6e|-

![[db image 1.png]]

![[db image 2.png]]

support Freedom1
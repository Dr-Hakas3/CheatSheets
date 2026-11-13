---
title: 53 DNS
parent: Services
grand_parent: Red Team
nav_order: 53
---
# DNS
## Domain Name System

---

## Default Port

- 53

---

## Service Info

### 各種レコード
- NS : ネームサーバー レコードには、ドメインの DNS レコードをホストする権限のあるサーバーの名前が含まれます。
- A : ホスト レコードとも呼ばれる「a レコード」には、ホスト名 (www.megacorpone.com など) の IPv4 アドレスが含まれます。
- AAAA : クアッド A ホスト レコードとも呼ばれる「aaaa レコード」には、ホスト名 (www.megacorpone.com など) の IPv6 アドレスが含まれます。
- MX：メール交換レコードには、ドメインのメール処理を担当するサーバーの名前が含まれます。ドメインには複数のMXレコードを含めることができます。
- PTR : ポインタ レコードは逆引き参照ゾーンで使用され、IP アドレスに関連付けられたレコードを見つけることができます。
- CNAME : 正規名レコードは、他のホスト レコードのエイリアスを作成するために使用されます。
- TXT : テキスト レコードには任意のデータを含めることができ、ドメイン所有権の検証など、さまざまな目的に使用できます。

---
## Common security issues

- zone transfer

---

## 1. Initial Scan

```bash
nmap -sV -p 53 dns.example.com
```

```zsh
nmap --script dns-zone-transfer,dns-cache-snoop,dns-brute -p 53 dns.example.com
```
- **dns-zone-transfer**: ゾーン転送を試みて、DNSサーバーの全情報を取得します。
- **dns-cache-snoop**: DNSキャッシュに保存された情報を取得します。
- **dns-brute**: DNSサーバーに対してブルートフォース攻撃を行い、サブドメインを列挙します。

### 基本的なドメイン情報の収集

```bash
dnsrecon -d example.com
```

### サブドメインの列挙

```
dnsrecon -d megacorpone.com -D ~/list.txt -t brt
```
- -D 潜在的なサブドメイン文字列を含むファイル名を指定する
- -t 列挙の種類 (この場合はbrtブルート フォース)

```bash
dnsrecon -d megacorpone.com -t std
```
- std
### ゾーン転送のチェック

```
dnsrecon -d example.com -t axfr
```
- **-d**: 対象ドメインを指定します。
- **-t brt**: ブルートフォースによるサブドメイン列挙を実行します。
- **-t axfr**: ゾーン転送を試みます。


👉 Check:


---

## 2. Enumeration

# ドメイン情報の収集
ドメインの詳細情報を取得するためのコマンドです。

```bash
# WHOIS情報を取得
whois example.com

# DNSレコードを取得
dig example.com ANY
```

# DNSクライアント
DNSクライアントを使用してドメイン名の解決を行います。

1. **ドメイン名の解決**

```bash
nslookup example.com
```

```bash
nslookup mail.megacorptwo.com
```

2. **特定のDNSサーバーを指定して解決**

```bash
nslookup example.com 8.8.8.8
```

特定のホストに属するTXTレコードについて、特定のDNSサーバにクエリを実行

```bash
nslookup -type=TXT info.megacorptwo.com 192.168.50.151
```

3. **DNSレコードの種類を指定して取得**

```bash
 dig example.com A
 dig example.com MX
 dig example.com TXT
```

4. **逆引きDNS**

```bash
dig -x 93.184.216.34
```

広範囲のDNS列挙

```bash
dnsenum megacorpone.com
```

```bash
nmap --script dns-brute -p 53 dns.example.com
```
- **dns-brute**: サブドメインを列挙するためのNmapスクリプトです。

```bash
host www.megacorpone.com
```
- デフォルトでAレコード
### レコードの指定
```bash
host -t mx megacorpone.com
```

```bash
host -t txt megacorpone.com
```

### Bashスクリプトによるドメイン名探索
指定したIPレンジ内でアクティブなホストを見つけるためのスクリプトです。

```bash
# 指定したIPレンジ内でアクティブなホストを検索
for ip in $(seq 200 254); do host 51.222.169.$ip; done | grep -v "not found"
```

- **seq 200 254**: IPアドレスの範囲を指定します。
- **host 51.222.169.$ip**: 各IPアドレスに対してDNS情報を取得します。
- **grep -v "not found"**: DNSが見つからなかったホストを除外します。

---

## 3.  DNSゾーン転送の攻撃
```bash
dig axfr @dns.example.com example.com
```
- **axfr**: ゾーン転送をリクエストします。
- **@dns.example.com**: ゾーン転送を実行するDNSサーバーを指定します。

---

## # DNS ブルートフォース攻撃手法の自動化
1. ホスト名リストを作成する
2. ワンライナーを使用して各ホスト名の解決
```bash
for ip in $(cat list.txt); do host $ip.megacorpone.com; done
```

# 逆引き検索 を用いてこの範囲をスキャンし、 各IPのホスト名を要求
```bash
for ip in $(seq 200 254); do host 51.222.169.$ip; done | grep -v "not found"
```

---

## 5. Authenticated Actions

👉 Once connected:

```powershell
whoami
hostname
ipconfig
```

---

👉 Check privileges:

```powershell
whoami /priv
```

---

## 6. Remote Execution / Exploitation

👉 WinRM itself = execution channel

👉 If access works:
→ Direct shell obtained

---

👉 Alternative (Impacket):

```bash
impacket-wmiexec <USER>:<PASS>@<IP>
```

---

## 7. No Credentials?

👉 Try:

* Password spraying → [Password Attacks](../03_initial_access/password_attacks.md)
* Check reused creds from other services

---

## 8. Lateral Movement / Pivot

👉 Reuse credentials:

* Other hosts via WinRM
* SMB / RDP
- [ligolo](../06_pivot_tunneling/ligolo.md)
- [chisel](../06_pivot_tunneling/chisel.md)
- [ssh-tunnel](../06_pivot_tunneling/ssh_tunnel.md)

---

👉 If shell obtained:

→ [Windows Privilege Escalation](../04_privesc/windows.md)

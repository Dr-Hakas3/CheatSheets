---
title: impacket-wmiexec
parent: Tools
grand_parent: Red Team
---

wmiexec.py は 標準のツールだとファイル転送できないが、
攻撃者はよく「Base64エンコード → echo で送る → デコード」で実現する。

例：

Linux側
```
base64 myshell.exe > myshell.b64
```

Windows側（wmiexec）
```
type myshell.b64 > C:\Windows\Temp\myshell.b64
certutil -decode C:\Windows\Temp\myshell.b64 C:\Windows\Temp\myshell.exe
```

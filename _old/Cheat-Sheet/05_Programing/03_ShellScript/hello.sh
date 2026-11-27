シェルスクリプトで「Hello, World!」を表示する最も基本的なスクリプトは以下の通りです。

```bash
#!/bin/bash
echo "Hello, World!"
```
説明:
#!/bin/bash: このスクリプトがbashシェルで実行されることを指定します。シバン（#!）と呼ばれ、スクリプトの最初に記述されます。
echo "Hello, World!": echoコマンドでコンソールに「Hello, World!」を出力します。
実行方法:
スクリプトをファイルに保存します（例: hello.sh）。
実行権限を与えます:
```bash
chmod +x hello.sh
```
スクリプトを実行します:
```bash
./hello.sh
```

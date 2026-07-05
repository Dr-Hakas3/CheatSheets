---
title: Proxy Sv
parent: Servers
grand_parent: Green Team
---
```bash
sudo vim /etc/squid/squid.conf
```

```bash
sudo vim /etc/squid/squid.conf
```

```
# ① LAN許可
http_access allow localnet

# ② HTTPS CONNECT許可（これがないと403）
http_access allow CONNECT SSL_ports

# ③ 最後に全部拒否
http_access deny all
```
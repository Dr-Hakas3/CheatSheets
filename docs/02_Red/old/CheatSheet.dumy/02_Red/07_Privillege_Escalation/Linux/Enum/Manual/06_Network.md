# Interface
```bash
ip a

ifconfig
```

# Routing
```bash
route

routel
```

# Active NW
```bash
ss -anp

netstat
```

### サーバの待受けサービスの調査
```bash
netstat -ltunp
```

# ネットワーク トラフィックをキャプチャする権限があるかどうかを確認
```bash
#ループバックインターフェースに出入りするトラフィックをキャプチャ
#-Aパラメータを使用してその内容をASCII形式でダンプ
sudo tcpdump -i lo -A | grep "pass"
```
# FW
```bash
cat /etc/iptables/rules.v4
```
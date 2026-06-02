# ポートノッキングの設定例

#### `knockd` の設定例（サーバー側）

`/etc/knockd.conf` に設定を追加します。以下は簡単な設定例です。

```ini
[options]
    logfile = /var/log/knockd.log

[openSSH]
    sequence    = 7000,8000,9000
    seq_timeout = 5
    command     = /sbin/iptables -A INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags    = syn

[closeSSH]
    sequence    = 9000,8000,7000
    seq_timeout = 5
    command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
    tcpflags    = syn
```

- `sequence` は、ノックするポートの順序を指定します。
- `command` は、シーケンスが成功した際に実行されるコマンドです。この例では、`iptables` を使用してポート22（SSH）を開放または閉鎖します。
- `seq_timeout` は、ノックシーケンスの間に許可される最大時間です。

### DNSゾーン転送の攻撃
```bash
dig axfr @dns.example.com example.com
```
- **axfr**: ゾーン転送をリクエストします。
- **@dns.example.com**: ゾーン転送を実行するDNSサーバーを指定します。
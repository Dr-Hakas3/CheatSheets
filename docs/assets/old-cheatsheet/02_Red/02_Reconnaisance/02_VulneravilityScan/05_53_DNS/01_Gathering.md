# ドメイン情報の収集
ドメインの詳細情報を取得するためのコマンドです。

```bash
# WHOIS情報を取得
whois example.com

# DNSレコードを取得
dig example.com ANY
```

# DNSクライアント
DNSクライアントを使用してドメイン名の解決を行います。

1. **ドメイン名の解決**
    ```bash
    nslookup example.com
    ```

2. **特定のDNSサーバーを指定して解決**
    ```bash
    nslookup example.com 8.8.8.8
    ```

3. **DNSレコードの種類を指定して取得**
    ```bash
    dig example.com A
    dig example.com MX
    dig example.com TXT

    ```

4. **逆引きDNS**
    ```bash
    dig -x 93.184.216.34
    ```


# 基本的なドメイン情報の収集
```bash
dnsrecon -d example.com
```

# サブドメインの列挙
```
dnsrecon -d megacorpone.com -D ~/list.txt -t brt
```
- -D 潜在的なサブドメイン文字列を含むファイル名を指定する
- -t 列挙の種類 (この場合はbrtブルート フォース)

```bash
dnsrecon -d megacorpone.com -t std
```
- std
# ゾーン転送のチェック
```
dnsrecon -d example.com -t axfr
```
- **-d**: 対象ドメインを指定します。
- **-t brt**: ブルートフォースによるサブドメイン列挙を実行します。
- **-t axfr**: ゾーン転送を試みます。
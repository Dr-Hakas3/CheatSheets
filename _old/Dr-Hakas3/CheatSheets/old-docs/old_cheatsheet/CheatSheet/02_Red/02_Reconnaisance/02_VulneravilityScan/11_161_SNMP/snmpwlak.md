## ツリー全体の列挙  
- メールアドレス等が取得できる
```bash
snmpwalk -c public -v1 -t 10 192.168.50.151
```

- dc01マシン上のwindowsユーザ列挙
```bash
snmpwalk -c public -v1 192.168.50.151 1.3.6.1.4.1.77.1.2.25
```

- 現在実行中のプロセスを列挙
```bash
snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.4.2.1.2
```

- マシンにインストールされているすべてのソフトウェアを照会
```bash
snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.6.3.1.2
```

- 現在の TCP リスニング ポートをすべて一覧表示  
ローカルでのみリッスンしているポートを明らかにできる場合がある
```bash
snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.6.13.1.3
```

- オプション
   - -c コミュニティ名の指定
   - -v1 SNMPv1
   - -v2c SNMPv2c より詳細な情報取得が可能
   - -v3 SNMP3 認証と暗号化が可能

よく使用されるWindows MIBの値
- 1.3.6.1.2.1.25.1.6.0 - システムプロセス
- 1.3.6.1.2.1.25.4.2.1.2 - 実行中のプログラム
- 1.3.6.1.2.1.25.4.2.1.4 - プロセスのパス
- 1.3.6.1.2.1.25.2.3.1.4 - ストレージユニット
- 1.3.6.1.2.1.25.6.3.1.2 - ソフトウェア名
- 1.3.6.1.4.1.77.1.2.25 - ユーザーアカウント
- 1.3.6.1.2.1.6.13.1.3 - TCPローカルポート
- 1.3.6.1.2.1.6.13 - TCP接続
- 1.3.6.1.2.1.2.2.1.2 - インターフェース名の一覧
- 1.3.6.1.2.1.2 - インターフェース情報
- 1.3.6.1.2.1.1 - システム情報
- 1.3.6.1.2.1.4.21 - ルーティングテーブル

---
# Example
## ChallengeLab_Frankfurt
### Command
```zsh
snmpwalk -c public -v1 -t 10 192.168.202.156 NET-SNMP-EXTEND-MIB::nsExtendOutputFull
```

### Output
```zsh
NET-SNMP-EXTEND-MIB::nsExtendOutputFull."reset-password" = STRING: Changing password for jack.
NET-SNMP-EXTEND-MIB::nsExtendOutputFull."reset-password-cmd" = STRING: "jack:3PUKsX98BMupBiCf" | chpasswd
```
jackのパスワード漏洩
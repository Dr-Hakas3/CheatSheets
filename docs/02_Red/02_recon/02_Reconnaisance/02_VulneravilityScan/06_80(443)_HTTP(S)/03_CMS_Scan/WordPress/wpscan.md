# # インストール
```bash
wpscan --url "target" --verbose
```

# スキャン

#### デフォルト
```bash
wpscan --url "target" --verbose
```

#### サイトスキャン
```bash
wpscan --url http://example.com
```

#### ユーザ列挙
```bash
wpscan --url http://example.com --enumerate u
```

#### パスワード攻撃
```bash
wpscan --url http://example.com --passwords /path/to/passwords.txt --usernames admin
```
```bash
wpscan --url http://loly.lc/wordpress/ -U loly -P /usr/share/wordlists/rockyou.txt
```

---
# Usage

#### 脆弱なプラグイン、ユーザー、脆弱なテーマ、timthumbsの列挙
```bash
wpscan --url "target" --enumerate vp,u,vt,tt --follow-redirection --verbose --log target.log
```

#### --enumrate オプション
- u Enum user
- p Enum All plugin
- vp vulnerability plugin
- ap Active Plugin
- tt Thema
- vt Vulnerability Thema
- cb Contents Backup
- dbe Enum DB error massage
- m Enum Media FIle

```zsh
wpscan --url http://192.168.175.55/shenzi -e ap,at,u --plugins-detection aggressive -t 20
```

- --url WordPress のインストール場所を指定
- ap すべてのプラグイン
- at すべてのテーマ 
- u ユーザー を列挙
- --plugins-detection aggressive プラグインの検出をアグレッシブに設定
- -t 20 スレッドを 20設定
- Wpscan は、専門家ではない使用には十分な無料の API キーを登録できる優れたツールで、1 日あたり約 5 回のスキャンをカバーします。私はここに自分のキーを含めませんでしたが、返される情報が多すぎるため、ほとんどの Capture The Flag チャレンジにはお勧めしません。これにより、出力がノイズが多くなり、調べるのが大変になります。ただし、バグ ハンターの場合は、API キーを使用することをお勧めします。そのため、これらのタイプのチャレンジ以外で、または他に何も見つからなかった場合の 2 回目の列挙フェーズで使用することをお勧めします。現状では、調べるべきことはたくさんあります。
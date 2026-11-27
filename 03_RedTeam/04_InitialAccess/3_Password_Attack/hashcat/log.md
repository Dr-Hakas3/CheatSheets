Hashcatのログ・実行状態・解析済みハッシュは、それぞれ保存先が異なります。

## **Hashcatの主な保存先**

|ファイル・ディレクトリ|内容|
|---|---|
|`~/.local/share/hashcat/hashcat.potfile`|解析済みパスワード（Potfile）|
|`~/.cache/hashcat/`|キャッシュ|
|`hashcat.restore`|中断・再開用のセッション情報|
|`hashcat.log`|実行ログ（`--logfile` 指定時）|

## **1. 解析済みパスワードの確認**

```
hashcat -m 5500 juan.5500 --show
```

Potfileの場所を確認：

```
find ~/.local/share/hashcat -type f -name '*.potfile'
```

## **2. 実行ログを保存する方法**

次回実行時に `--logfile` を指定します。

```
hashcat -a 0 -m 5500 juan.5500 \
  ~/rockyou-top100000.txt \
  --logfile hashcat.log
```

## **3. 現在のHashcat関連ファイルを確認**

```
find ~ -maxdepth 4 \
  \( -iname '*hashcat*' -o -iname '*.potfile' \) \
  -print 2>/dev/null
```

**今回の解析結果については、まず** `hashcat.potfile` **を確認するのが適切です。**

なお、Hashcatの標準出力は、リダイレクトやログ指定をしない限り、通常はターミナルに表示されるだけです。

## 削除

目的別にコマンドを分けます。

**1. Hashcatの解析済みパスワード（Potfile）を削除**

```
rm ~/.local/share/hashcat/hashcat.potfile
```

**2. Hashcatの実行ログを削除**

```
rm -f hashcat.log
```

**3. 再開用ファイルを削除**

```
rm -f hashcat.restore
```

**4. 今回作成したハッシュファイルを削除**

```
rm -f hashcat.5500 juan.5500
```

注意：Potfileを削除すると、過去に解析済みのパスワード記録も失われます。

今回のCTFの作業記録だけ整理したいなら、まず削除対象を確認してから実行するのが安全です。
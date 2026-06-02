## ファイルの権限
```bash
ls -la /etc/shadow
-rw-r----- 1 root shadow 1751 May  2 09:31 /etc/shadow
# rw Owber(root)
# r  Group(shadow Group)
# -  Others
```
システム管理者がカスタム設定やスクリプトを使用して、/etc/fstabファイルに記載されていないドライブをマウントしている可能性があることに注意してください 。そのため、 /etc/fstabをスキャンするだけでなく、 mountを使用してマウントされたドライブに関する情報も収集することをお勧めします。

## カレントユーザーが書き込み可能なすべてのファイルを検索
```bash
find / -type f -writable 2>/dev/null
```

## カレントユーザーが書き込み可能なすべてのディレクトリを検索
```bash
find / -writable -type d 2>/dev/null
```
出力には、この Linux システムのスワップ パーティションとプライマリ ext4 ディスクが表示されます。
### 誰でも書き込み可能なファイルの調査
```bash
find / -perm -o+w -type f 2>/dev/null | grep /proc -v
```

## setuid setgid

```bash
find / -type f -perm -4000 2>/dev/null
```
- `setuid`ビット: 実行時に所有者の権限で実行されるファイル

```bash
find / -perm -u=s -type f 2>/dev/null
```
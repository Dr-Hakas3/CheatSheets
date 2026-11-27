## 基本的な静的テクニック
### ウイルス対策ソフト等でマルウェアを検知する
[Virus_Total]
### ハッシュ値の検索
- Linux
```bash
md5sum ファイル名
```
- Windows
#### コマンドプロンプト
```bash
certutil -hashfile ファイル名 md5
```
#### Powershell
```bash
Get-FileHash -Path "ファイルパス" -Algorithm SHA256
```
### 文字列の検索
```bash
strings ファイル名
```

### パック化され難読化されたマルウェア
- PEiDによるパッカーの検出

### ポータブル実行(PE)ファイル形式
- Windowsの実行ファイル
- 
# 設定

### 日本語化
- [日本語化手順](https://qiita.com/nm_suisai/items/ee7df3ba45228ebdf2aa)

### ターミナル分割

#### Terminator
- [Terminatorの使用方法](https://qiita.com/Hashibirokou/items/58cfe84975c3b3af0235)

#### tmux
- [アニメーション設定](https://qiita.com/KoyanagiHitoshi/items/318d4b8ef3b4e5b87390)
- [tmuxの使い方](https://qiita.com/shin-ch13/items/9d207a70ccc8467f7bab)
---
## 設定確認
### カーネルバージョン変更
#### 以前のバージョンのカーネルパッケージを検索します
```bash
apt search linux-image
```
#### 適切な以前のバージョンのカーネルパッケージをインストールします
```bash
apt install linux-image-version
```
#### 新しいカーネルをアンインストールします
```bash
apt purge linux-image-<new_version>
```
#### ブートローダーを更新します
```bash
update-grub
```
#### システムを再起動します
```bash
reboot
```

## 表示

### 大文字小文字変換

```bash
echo "Hello WoRLd" | tr '[:upper:][:lower:]' '[:lower:][:upper:]'
```
## Interactive

```bash
adduser uname
useradd uname
```

### UID設定

```bash
# UIDを指定してユーザを特定のグループに追加します
useradd -u UID -g group uname
```

```zsh
usermod -u 0 www-data
```
# ユーザをGroupに追加

```zsh
sudo usermod -aG root www-data
```
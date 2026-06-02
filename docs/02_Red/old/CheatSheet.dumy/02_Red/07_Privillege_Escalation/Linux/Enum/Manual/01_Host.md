# Hostname
```bash
hostname
# debian-privesc
```
# OS
```bash
cat /etc/issue

cat /etc/os-release
# バージョン（Debian 10）とリリース固有の情報（ディストリビューションのコード名（buster）を含む）を出力
```

```bash
uname -a
# Linux debian-privesc 4.19.0-21-amd64 #1 SMP Debian 4.19.249-2 (2022-06-30) x86_64 GNU/Linux
# カーネルバージョン（4.19.0）とアーキテクチャ（x86_64）を出力
```

```bash
uname -ar
```
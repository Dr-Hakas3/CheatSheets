# インストール
```bash
# 推奨
sudo apt install pipx -y
pipx install droopescan

# 非推奨
apt-get install python3-pip
python3 -m venv ~/venv-droopescan
source ~/venv-droopescan/bin/activate
pip install droopescan
deactivate
```

## Drupal
### スキャン
```bash
droopescan scan drupal -u http://192.168.0.101
```

## joomla
### ブルートフォース用ファイルのインストール
```bash
https://github.com/ajnik/joomla-bruteforce
```

### スキャン
```bash
droopescan scan joomla --url http://site
```
```bash
sudo python3 joomla-brute.py -u http://site/ -w passwords.txt -usr username
```

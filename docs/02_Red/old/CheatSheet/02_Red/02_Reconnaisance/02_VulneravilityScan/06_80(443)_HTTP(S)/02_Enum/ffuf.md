## ffuf
### ディレクトリ列挙
```bash
ffuf -c -u http://sea.htb/themes/bike/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
```
```bash
ffuf -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://example.com/FUZZ -fc 404
```
- -c 結果をカラー表示
### 拡張子の指定
```bash
ffuf -u https://example.com/FUZZ -w /path/to/wordlist.txt:W1 -w /path/to/extensions.txt:W2 -e .php,.html,.txt
```
### サブドメイン
```bash
ffuf -c -w /path/to/wordlist.txt -u http://FUZZ.example.com/ -fc 404
```
### VHost
```bash
ffuf -c -w /usr/share/seclists/Discovery/DNS/n0kovo_subdomains.txt -u "http://runner.htb" -H "Host:FUZZ.runner.htb" -fc 404
```

```bash
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.board.htb" -u http://board.htb/ -fs 15949
```
- -fs 無視する応答サイズ
# Parameter
```zsh
ffuf -u 'http://192.168.11.21/test.php?FUZZ=test' -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs 80
```
- -u URL
- -w wordlist
- -fs 

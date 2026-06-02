```zsh
for ip in $(seq 1 254); do ping -c 1 192.168.56.$ip; done
```
以下のルートを追加するだけでligoloは240.0.0.1をターゲット上の127.0.0.1に転送してくれる
```zsh
sudo ip route add 240.0.0.1/32 dev ligolo
```
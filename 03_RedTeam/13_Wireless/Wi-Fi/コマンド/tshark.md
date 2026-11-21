
## キャプチャしたファイル内のeapのドメインとユーザ名の一覧抽出

```zsh
tshark -r cap/scan_ch44-01.cap \
  -Y "eap.type == 1" \
  -T fields \
  -e frame.number \
  -e wlan.bssid \
  -e wlan.sa \
  -e eap.identity
```


![[Pasted image 20261121203148.png]]
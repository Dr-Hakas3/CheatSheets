## リンク状態の確認

```zsh
iw dev wlan3 link
```

![[Pasted image 20261118163427.png]]

# Change Channel

## 現在の設定を確認

```zsh
iw dev wlan0 info
```

![[Pasted image 20261121185712.png]]

## 変更

```zsh
sudo iw dev wlan0 set channel 44
```

## 確認

```zsh
iw dev wlan0 info
```

![[Pasted image 20261121185857.png]]

---

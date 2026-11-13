---
title: 111,2049 NSF
parent: Services
grand_parent: Red Team
nav_order: 111
---
# NFS


---

## Default Port

- 111
- 2049

---

## Service Info



---
## Common security issues



---

## 1. Initial Scan

```bash
nmap -sV --script=nfs-showmount IP
```

👉 Check:

* nfs-showmount: No NFS mounts available ?

![](../../assets/images/Pasted%20image%2020260509182104.png)

---

## 2. Enum Mount List

```zsh
showmount -e IP
```
![](../../assets/images/Pasted%20image%2020260509182727.png)

👉考えられる状況
- 実際にはエクスポートが存在しない
- NFSは起動しているが共有設定なし
- アクセス制御で showmount を拒否
- /etc/exports で特定IPのみ許可
- あなたのKaliが弾かれている
- NFSバージョン差異（特にv4）
- NFSv4はshowmountで出ないことがある
- RPCサービスは見えているが mountd が制限されている
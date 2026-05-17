リモートサーバに時刻を合わせる
```zsh
sudo ntpdate 10.129.245.130
```

もとに戻す
```zsh
sudo ntpdate ntp.nict.jp
```

---

# Example
## For Krberos

### Time Sync
```zsh
sudo ntpdate -u dc1.ping.htb
```
![](../../../assets/old-cheatsheet/Assets/Images/Pasted%20image%2020260504011057.png)
*If things don't go as shown in the figure, please refer to the [link](../../../assets/old-cheatsheet/07_Writeup/HTB/Kerberos_time_not_Sync.md)*
## Current Time
```zsh
timedatectl
```

## Set UTC
```zsh
sudo timedatectl set-timezone UTC
```

## Set UTC+0900
```zsh
sudo timedatectl set-timezone Asia/Tokyo
```


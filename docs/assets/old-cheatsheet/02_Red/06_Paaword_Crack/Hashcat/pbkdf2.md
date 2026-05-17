https://github.com/r0tn3x/pbkdf2-hashcat-converter
```zsh
git clone https://github.com/r0tn3x/pbkdf2-hashcat-converter.git
```
![](../../../Assets/Images/Pasted%20image%2020260428204555.png)

```zsh
cd pbkdf2-hashcat-converter 
```

```zsh
python3 pbkdf2-to-hashcat.py 'pbkdf2:sha256:600000$AMtzteQIG7yAbZIa$0673ad90a0b4afb19d662336f0fce3a9edd0b7b19193717be28ce4d66c887133'
sha256:600000:QU10enRlUUlHN3lBYlpJYQ==:BnOtkKC0r7GdZiM28Pzjqe3Qt7GRk3F74ozk1myIcTM=
```
![](../../../Assets/Images/Pasted%20image%2020260428204605.png)

```zsh
echo "sha256:600000:QU10enRlUUlHN3lBYlpJYQ==:BnOtkKC0r7GdZiM28Pzjqe3Qt7GRk3F74ozk1myIcTM=" > hash_final.txt
```
![](../../../Assets/Images/Pasted%20image%2020260428204616.png)

```zsh
hashcat -m 10900 hash_final.txt /usr/share/wordlists/seclists/Passwords/Common-Credentials/10k-most-common.txt   -w 3 -O
```
![](../../../Assets/Images/Pasted%20image%2020260428204630.png)
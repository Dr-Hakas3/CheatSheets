```zsh
./bloodhound-cli install
```
![](Assets/Images/Pasted%20image%2020260502084408.png)

# Default Password
```zsh
[+] BloodHound is ready to go!
[+] You can log in as `admin` with this password: **************************
[+] You can get your admin password by running: bloodhound-cli config get default_password
[+] You can access the BloodHound UI at: http://127.0.0.1:8080/ui/login
```
＊の行に出力される
# PATH
```zsh
echo 'export PATH=$PATH:/opt/bloodhound' >> ~/.zshrc
source ~/.zshrc
```
![](Assets/Images/Pasted%20image%2020260502084530.png)

# Password Reset
パスワードを紛失した場合は、BloodHound CLI を使用してローカルでリセットできます。
```zsh
./bloodhound-cli resetpwd
```
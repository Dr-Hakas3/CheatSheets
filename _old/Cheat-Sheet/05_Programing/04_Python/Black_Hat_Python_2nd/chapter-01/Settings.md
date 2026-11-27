#### 仮想環境の作成
```bash
tim@kali:~$ sudo apt-get install python3-venv
```
環境の作成
```bash
tim@kali:~$ mkdir bhp
tim@kali:~$ cd bhp
tim@kali:~/bhp$ python3 -m venv venv3
```
仮想環境の有効化
```bash
tim@kali:~/bhp$ source venv3/bin/activate
```
```bash
(venv3) tim@kali:~/bhp$ python
```
仮想環境の無効化
```bash
(venv3) tim@kali:~/bhp$ deactivate
```

#### IDEのインストール
[Download](https://code.visualstudio.com/download/)
Install
```bash
tim@kali#: apt-get install -f ./code_1.39.2-
1571154070_amd64.deb
```

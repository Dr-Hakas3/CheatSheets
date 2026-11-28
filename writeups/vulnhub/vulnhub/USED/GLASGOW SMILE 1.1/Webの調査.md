〇Webの調査

・サービスの詳細

nmap -Pn -sV -A -p80 192.168.0.113

![[Webの調査 image 56.png]]

Apache　2.4.38

・ディレクトリ

gobuster dir -u http://192.168.0.113 -w /usr/share/wordlists/dirb/common.txt

/.hta                 (Status: 403) \[Size: 278\]

/.htpasswd            (Status: 403) \[Size: 278\]

/.htaccess            (Status: 403) \[Size: 278\]

/index.html           (Status: 200) \[Size: 125\]

/joomla               (Status: 301) \[Size: 315\] \[--> http://192.168.0.113/joomla/\]

/server-status        (Status: 403) \[Size: 278\]

Progress: 4614 / 4615 (99.98%)

==🟡/joomla==

・ブラウザアクセス

![[Webの調査 image 57.png]]

**Joker**

http://192.168.0.113/joomla

Joker

**Home**

**Glasgow Smile :)**

**Details**

Written by Super User

Category: [Uncategorised](http://192.168.0.113/joomla/index.php/2-uncategorised)

Published: 14 June 2020

Hits: 34

“Comedy is subjective, Murray. Isn’t that what they say? All of you, the system that knows so much, you decide what’s right or wrong. The same way that you decide what’s funny or not. Why is everybody so upset about these guys? If it was me dying on the sidewalk, you’d walk right over me. I pass you every day and you don’t notice me!”

~~*\[Joker, in a police car, is laughing and chuckling at the chaos being spread to Gotham City\]*~~

~~***Cop 1***~~~~*: Stop laughing, you freak. This isn't funny.*~~

~~***Cop 2***~~~~*: Yeah, the whole fucking city's on fire because of you.*~~

~~***Joker***~~~~*: I know... Isn’t it beautiful?*~~

~~*\[Arthur is laughing loudly during a psychiatric examination at Arkham Asylum. He soon settles down, but still laughs\]*~~

~~***Psychiatrist***~~~~*: What's so funny?*~~

~~***Arthur***~~~~*: \[laughing and chuckling some more\] I was just thinking...just thinking of a joke.*~~

~~***Psychiatrist***~~~~*: Do you wanna tell it to me?*~~

~~***Arthur***~~~~*: \[softly whispers\] You wouldn't get it.*~~

http://192.168.0.113/joomla/robots.txt

\# If the Joomla site is installed within a folder   
\# eg www.example.com/joomla/ then the robots.txt file   
\# MUST be moved to the site root   
\# eg www.example.com/robots.txt  
\# AND the joomla folder name MUST be prefixed to all of the  
\# paths.   
\# eg the Disallow rule for the /administrator/ folder MUST   
\# be changed to read   
\# Disallow: /joomla/administrator/  
\#  
\# For more information about the robots.txt standard, see:  
\# http://www.robotstxt.org/orig.html  
\#  
\# For syntax checking, see:  
\# http://tool.motoricerca.info/robots-checker.phtml

User-agent: *  
Disallow: /administrator/  
Disallow: /bin/  
Disallow: /cache/  
Disallow: /cli/  
Disallow: /components/  
Disallow: /includes/  
Disallow: /installation/  
Disallow: /language/  
Disallow: /layouts/  
Disallow: /libraries/  
Disallow: /logs/  
Disallow: /modules/  
Disallow: /plugins/  
Disallow: /tmp/

・/administrator/

![[Webの調査 image 58.png]]

・joomlaの調査

droopescan scan joomla --url http://192.168.0.113/joomla

\[+\] Possible interesting urls found:

Detailed version information. - http://192.168.0.113/joomla/administrator/manifests/files/joomla.xml

Login page. - http://192.168.0.113/joomla/administrator/

License file. - http://192.168.0.113/joomla/LICENSE.txt

Version attribute contains approx version - http://192.168.0.113/joomla/plugins/system/cache/cache.xml

サイト内のキーワードを集める

cewl -w keywords.txt http://192.168.0.113/joomla

python3 joomla-bruteforce/joomla-brute.py -u http://192.168.0.113/joomla/ -w keywords.txt -U keywords.txt

![[Webの調査 image 59.png]]

joomla:Gotham

ID:joomla PW:Gothamでログインできる
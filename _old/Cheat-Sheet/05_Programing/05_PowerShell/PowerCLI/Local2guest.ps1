PowerCLIを使って、ホストからゲストVMにファイルをコピーするためのスクリプトの基本的な例は、Copy-VMGuestFileコマンドを使用します。このコマンドを使うためには、VMware ToolsがゲストOSにインストールされている必要があります。

例: ホストからゲストVMにファイルをコピーするPowerCLIスクリプト
```powershell
# PowerCLIに接続
Connect-VIServer -Server <vCenter-Server>

# ゲストOSにログインするための資格情報
$guestCreds = Get-Credential

# コピー元とコピー先のパス
$sourceFilePath = "C:\local\path\to\file.txt"  # ホスト側のファイルパス
$destinationFilePath = "C:\guest\path\to\file.txt"  # ゲスト側のファイルパス

# 対象のVM
$vm = Get-VM -Name "VMName"

# ホストからゲストにファイルをコピー
Copy-VMGuestFile -Source $sourceFilePath -Destination $destinationFilePath -VM $vm -GuestCredential $guestCreds -HostToGuest -Confirm:$false

# 接続を切断
Disconnect-VIServer -Server <vCenter-Server> -Confirm:$false
```
<#
スクリプトの説明:
Connect-VIServer: vCenterサーバーまたはESXiホストに接続します。<vCenter-Server>の部分には、実際のvCenterまたはESXiホストのアドレスを指定します。
Get-Credential: ゲストOSにログインするためのユーザー名とパスワードを取得します。
Copy-VMGuestFile: ホストからゲストOSにファイルをコピーします。
-Source: ホスト側のコピー元ファイルのパスを指定します。
-Destination: ゲストOS側のコピー先パスを指定します。
-VM: 対象となるVMを指定します。
-GuestCredential: ゲストOSにアクセスするための資格情報を指定します。
-HostToGuest: ホストからゲストへのコピーを指定します。
Disconnect-VIServer: スクリプトの最後にvCenterまたはESXiホストから切断します。
注意点:
ゲストOSにVMware Toolsがインストールされている必要があります。
ゲストOSのログイン資格情報が必要です。
#>

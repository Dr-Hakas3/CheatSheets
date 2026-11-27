# vCenterに接続
Connect-VIServer -Server your_vcenter_server

# フォルダ名を指定
$folderName = "YourFolderName"

# フォルダ内のすべての仮想マシンを取得
$folder = Get-Folder -Name $folderName
$vms = Get-VM -Location $folder

# 各仮想マシンの複数のスナップショットを削除
foreach ($vm in $vms) {
    $snapshots = Get-Snapshot -VM $vm
    if ($snapshots) {
        Remove-Snapshot -Snapshot $snapshots -Confirm:$false
        Write-Host "Deleted all snapshots for VM:" $vm.Name
    } else {
        Write-Host "No snapshots found for VM:" $vm.Name
    }
}

# vCenterから切断
Disconnect-VIServer -Confirm:$false
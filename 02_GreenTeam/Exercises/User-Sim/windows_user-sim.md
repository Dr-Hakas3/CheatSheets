---
title: Windows User Simulation
parent: Execises
grand_parent: Green Team
---
# Web

```powershell
$Chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"

$Sites = @(
    "https://portal.lab.local",
    "https://wiki.lab.local",
    "https://example.com"
)

while ($true) {

    Start-Sleep -Seconds (Get-Random -Minimum 30 -Maximum 181)

    $Url = Get-Random -InputObject $Sites

    $proc = Start-Process `
        -FilePath $Chrome `
        -ArgumentList $Url `
        -PassThru

    Start-Sleep -Seconds (Get-Random -Minimum 30 -Maximum 301)

    if (!$proc.HasExited) {
        $proc.CloseMainWindow() | Out-Null
        Start-Sleep 5

        if (!$proc.HasExited) {
            $proc.Kill()
        }
    }
}
```

---

# Mail

## ポイント：

- Outlookは起動済み or 自動起動OK
- PowerShellからメール生成・送信可能
- 送信済みフォルダにも残る（通常運用と同じ）

■ 基本：Outlookでメール送信（PowerShell）
# Outlook起動
```powershell
$outlook = New-Object -ComObject Outlook.Application
$mail = $outlook.CreateItem(0)

$mail.To = "user2@lab.local"
$mail.Subject = "Test mail"
$mail.Body = "Hello from PowerShell + Outlook"

$mail.Send()
```
■ ランダム送信（あなたの用途向け）

「ユーザー行動シミュレーション」用に詰めた版です。

```powershell
$Outlook = New-Object -ComObject Outlook.Application

$Recipients = @(
    "user1@lab.local",
    "user2@lab.local",
    "user3@lab.local",
    "admin@lab.local"
)

$Subjects = @(
    "Daily report",
    "Question",
    "FYI",
    "Status update",
    "Request"
)

$Bodies = @(
    "Please check this.",
    "No issues found.",
    "Attached report.",
    "Let me know.",
    "OK."
)

while ($true) {

    # ランダム待機（30～300秒）
    Start-Sleep -Seconds (Get-Random -Minimum 30 -Maximum 301)

    $mail = $Outlook.CreateItem(0)

    $to = Get-Random $Recipients
    $subject = Get-Random $Subjects
    $body = Get-Random $Bodies

    $mail.To = $to
    $mail.Subject = $subject
    $mail.Body = $body

    Write-Host "$(Get-Date) Send mail -> $to"

    $mail.Send()
}
```
■ 送信済みフォルダについて（重要）

この方式だと：

✔ 送信成功 → Outlookの「送信済みアイテム」に残る
✔ IMAP/Exchange環境ならサーバにも同期
✔ Thunderbirdより“本物の業務ログ”に近い

■ 添付ファイル付き（リアル度UP）
```powershell
$mail.Attachments.Add("C:\temp\report.txt")
```
■ Outlook起動済み前提で安定させる版

Outlookが未起動だと遅いので：

```powershell
Start-Process outlook.exe
Start-Sleep 5
```

---

# File

■ 前提（SMB共有）

例：

- ファイルサーバ：\\fileserver.lab.local\share
- ユーザー：ドメイン or ローカル認証

■ 方法①：一番シンプル（PSDriveでマウント）
# 認証情報

```powershell
$User = "lab\user1"
$Pass = ConvertTo-SecureString "password" -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential($User, $Pass)
```

# 共有をドライブとしてマウント
```powershell
New-PSDrive -Name "S" -PSProvider FileSystem `
    -Root "\\fileserver.lab.local\share" `
    -Credential $Cred `
    -Persist
■ ランダムアクセス（あなたの用途）
$Files = @(
    "a.txt",
    "b.txt",
    "c.txt",
    "report.docx"
)

while ($true) {

    # ランダム待機（ユーザー行動）
    Start-Sleep -Seconds (Get-Random -Minimum 30 -Maximum 181)

    $file = Get-Random $Files

    $path = "S:\$file"

    Write-Host "$(Get-Date) Access file: $file"

    # 読み取り（ログ生成）
    Get-Content $path | Out-Null

    # たまにコピー（ユーザー行動っぽさ）
    if ((Get-Random -Minimum 0 -Maximum 2) -eq 0) {
        Copy-Item $path -Destination "$env:TEMP\$file" -Force
    }

    # たまに一覧表示
    if ((Get-Random -Minimum 0 -Maximum 3) -eq 0) {
        Get-ChildItem "S:\" | Out-Null
    }
}
```

■ 方法②：UNC直アクセス（マウント不要）

より軽量：

```powershell
$Share = "\\fileserver.lab.local\share"
$file = "report.docx"

Get-Content "$Share\$file"
```

■ ランダム行動フル版（実用）

Web・メールと同じ思想に合わせた版です。

```powershell
$Share = "\\fileserver.lab.local\share"

$Files = @("a.txt","b.txt","c.txt","report.docx")

while ($true) {

    Start-Sleep -Seconds (Get-Random -Minimum 20 -Maximum 200)

    $action = Get-Random -Minimum 0 -Maximum 3
    $file = Get-Random $Files

    switch ($action) {

        0 {
            Write-Host "READ $file"
            Get-Content "$Share\$file" | Out-Null
        }

        1 {
            Write-Host "COPY $file"
            Copy-Item "$Share\$file" "$env:TEMP\$file" -Force
        }

        2 {
            Write-Host "LIST"
            Get-ChildItem $Share | Out-Null
        }
    }
}
```

■ よりリアルな“ユーザー行動化”

実際の人間っぽくするなら：

✔ 行動パターン追加
フォルダ移動
検索
同じファイルを何度も開く
一時ファイル生成
```powershell
if ((Get-Random -Minimum 0 -Maximum 5) -eq 0) {
    Start-Process explorer.exe $Share
}
```

■ Outlook + Web + File統合イメージ

# 行動	実装
Web閲覧	Chrome
メール送信	Outlook COM
ファイル共有	SMB + PowerShell
待機	Start-Sleep + Random
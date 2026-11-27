
# Install-ADDSForest コマンドの解説

`Install-ADDSForest` は Active Directory ドメインサービス (AD DS) フォレストを新規に作成するための PowerShell コマンドです。このコマンドには、いくつかのオプションが指定されており、具体的な内容は以下の通りです。

```powershell
Install-ADDSForest -CreateDnsDelegation:$false -DatabasePath "C:\\Windows\\NTDS" -DomainMode "7" -DomainName "cs.org" -DomainNetbiosName "cs" -ForestMode "7" -InstallDns:$true -LogPath "C:\\Windows\\NTDS" -NoRebootOnCompletion:$false -SysvolPath "C:\\Windows\\SYSVOL" -Force:$true
```

## 各パラメータの説明

- **`-CreateDnsDelegation:$false`**  
  DNS デリゲーションを作成しないように設定します。DNS デリゲーションは、フォレストの名前空間に他の DNS サーバーが管理するゾーンがある場合に使用されますが、今回はそれを作成しません。

- **`-DatabasePath "C:\\Windows\\NTDS"`**  
  Active Directory データベースファイル (`ntds.dit`) を保存するパスを指定しています。デフォルトでは `C:\Windows\NTDS` フォルダーにデータベースが保存されます。

- **`-DomainMode "7"`**  
  ドメインの機能レベルを指定します。`7` は Windows Server 2016 のドメイン機能レベルを意味します。これにより、ドメイン内で使用できる機能が Windows Server 2016 に対応したものになります。

- **`-DomainName "cs.org"`**  
  新しく作成するドメインの完全修飾ドメイン名 (FQDN) を指定します。この場合、ドメイン名は `cs.org` です。

- **`-DomainNetbiosName "cs"`**  
  NetBIOS 名を指定します。これは、レガシーなシステムで使用される短い名前で、ここでは `cs` が指定されています。

- **`-ForestMode "7"`**  
  フォレストの機能レベルを指定します。`7` は Windows Server 2016 のフォレスト機能レベルです。

- **`-InstallDns:$true`**  
  DNS サーバーをインストールするかどうかを指定します。このオプションでは、DNS サーバーをインストールする設定になっています。

- **`-LogPath "C:\\Windows\\NTDS"`**  
  Active Directory の操作ログを保存するパスを指定します。ここではデフォルトの `C:\Windows\NTDS` フォルダーが指定されています。

- **`-NoRebootOnCompletion:$false`**  
  インストールが完了した後、自動的に再起動を行うかどうかを指定します。`$false` に設定されているため、インストール後にサーバーは再起動されます。

- **`-SysvolPath "C:\\Windows\\SYSVOL"`**  
  SYSVOL フォルダーの保存パスを指定します。SYSVOL フォルダーにはドメイン内のグループポリシーやスクリプトが格納されます。

- **`-Force:$true`**  
  ユーザーの確認なしに処理を強制的に実行します。

## 全体の解説

このコマンドは、新しい AD DS フォレストを作成し、`cs.org` ドメインを設定します。DNS サーバーもインストールされ、データベースおよびログファイルは `C:\Windows\NTDS` に保存されます。また、フォレストおよびドメインの機能レベルは Windows Server 2016 に設定され、インストールが完了するとサーバーは再起動されます。

### エラー
`Install-ADDSForest` コマンドが "認識可能なコマンドではない" というエラーを返す場合、いくつかの原因が考えられます。以下は、エラーを解決するためのチェックリストです。

## 1. **AD DS モジュールがインストールされているか確認**

`Install-ADDSForest` コマンドは Active Directory ドメインサービス (AD DS) の一部なので、このモジュールがインストールされていないとエラーになります。以下の手順でモジュールをインストールできます。

### コマンドでインストール
```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

このコマンドで、AD DS と必要な管理ツールがインストールされます。

## 2. **PowerShell を管理者権限で実行**

PowerShell は管理者権限で実行する必要があります。右クリックして「管理者として実行」を選んで PowerShell を起動してください。

## 3. **必要なモジュールがインポートされているか確認**

AD DS 関連のコマンドレットが認識されない場合、モジュールが読み込まれていない可能性があります。以下のコマンドを実行して、モジュールをインポートします。

```powershell
Import-Module ADDSDeployment
```

これにより、AD DS 関連のコマンドが PowerShell で認識されるようになります。

## 4. **サーバーが Windows Server であることを確認**

`Install-ADDSForest` は Windows Server の機能です。クライアント OS（例えば Windows 10 など）ではこのコマンドを使用できないため、Windows Server 環境で実行する必要があります。

## 5. **再インストールや再起動の確認**

モジュールや機能をインストールした後、サーバーを再起動して変更が有効になる場合もあります。再起動を試みてください。

---

上記の手順を試してもエラーが解決しない場合は、エラーメッセージや環境の詳細を教えていただければ、さらに具体的なアドバイスができます。
```zsh
BloodHound CEを導入したあとは、日々の起動・停止、パスワードのリセットなどを bloodhound-cli コマンドで管理できる。

Docker Composeに慣れているとつい docker compose up/down を使いがちだが、私はdocker compose を直接使っていたことで設定ファイルの整合性に失敗し、初期化に失敗し復旧に苦労した。
以後は素直に bloodhound-cli を使うことにした。
```
# サービスの起動
```zsh
bloodhound-cli containers up
```

# ログイン
## URL
```zsh
http://127.0.0.1:8080/ui/login
```

## Credential
```zsh
admin
*****
```

# サービスの停止（データは維持）
```
bloodhound-cli containers stop
```

# 停止中のサービスを再開
```
bloodhound-cli containers start
```

# コンテナの削除（ボリュームは残る）
```
bloodhound-cli containers down
```

# パスワードの再発行
```
bloodhound-cli resetpwd
```

# 現在稼働中のコンテナ一覧
```
bloodhound-cli running
```

# 実際のコマンド群やヘルプ
```
bloodhound-cli help

BloodHound CLI is a command line interface for managing BloodHound and
associated containers and services. Commands are grouped by their use.

Usage:
  bloodhound-cli [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  config      Display or adjust the configuration
  containers  Manage BloodHound containers with subcommands
  help        Help about any command
  install     Builds containers and performs first-time setup of BloodHound
  logs        Fetch logs for BloodHound services
  resetpwd    Reset the admin password
  running     Print a list of running BloodHound services
  uninstall   Remove all BloodHound containers, images, and volume data
  update      Update the BloodHound container images if an update is available
  version     Displays BloodHound CLI's version information

Flags:
  -h, --help   help for bloodhound-cli

Use "bloodhound-cli [command] --help" for more information about a command.
```

このCLIは以下のようなサブコマンドを備えており、GUIが使えない環境でも一通りの操作が可能。
```
コマンド	説明
install	初回インストール（Composeファイル取得 + コンテナ構築）
containers	各種コンテナの起動/停止/再構築など
running	稼働中のサービス確認
config	各種設定ファイルの読み書き
resetpwd	adminパスワードの再発行
uninstall	コンテナ・ボリュームの削除（環境初期化）
update	イメージの更新
bloodhound-cli [command] --help で各コマンドの詳細も確認できる。
```
### Settings
![図9: Nessus設定の探索](https://static.offsec.com/offsec-courses/PEN-200/imgs/vulnscan/7de5af781839ba0f0012286fb6d1ec8c-vulnscan_nessusDashboardSettingsR.png)

「設定_」_タブでは、アプリケーションの設定を行うことができます。例えば、スキャン結果をメールで受け取るための[_SMTPサーバー_](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)の情報を入力できます 。「詳細設定」メニューでは、ユーザーインターフェース、スキャン、ログの動作から、セキュリティやパフォーマンス関連のオプションに至るまで、グローバル設定を行うことができます。

図9に示すように、_「About」_ メニューにはNessusの基本情報、ライセンス、残りのホスト数が表示されます。Nessusのカスタマイズと設定方法の詳細については、[Nessusのドキュメント](https://docs.tenable.com/nessus/Content/Settings.htm)を参照してください。

### Scan
- Policy  
Nessusスキャンのコンテキストで事前に定義された設定オプションのセット。  
ポリシーを保存すると、新しいスキャンのテンプレートとして使用できる。
　- _スキャンテンプレート_  
　　検出_、_脆弱性_、_コンプライアンスの_ 3つのカテゴリに分類されています 。
    - コンプライアンスカテゴリ  
    _エンタープライズ版と_モバイルデバイススキャンテンプレートでのみ利用可能。
     - __ディスカバリー_カテゴリのテンプレートは_ホストディスカバリー_のみで、稼働中のホストとそのオープンポートのリストを作成できる。
    - 脆弱_性_カテゴリ  
    重大な脆弱性または脆弱性グループ (例: [_PrintNightmare_](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) または [_Zerologon)_](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-1472)のテンプレート と、一般的なスキャン領域 (例: _Web アプリケーション テスト_または_マルウェア スキャン)_のテンプレートが含まれる。

   - 一般的な脆弱性スキャン テンプレート

　1. ベーシック_ネットワークスキャンは、_ほとんどの設定が事前に定義された状態でフルスキャンを実行します。幅広い脆弱性を検出するため、Nessus が推奨するスキャンテンプレートです。これらの設定と推奨事項をカスタマイズすることもできます。
　2. _詳細スキャンは、_事前定義された設定のないテンプレートです。脆弱性スキャンを完全にカスタマイズしたい場合や、特定のニーズがある場合に使用できます。
　3. 最後の一般的なスキャン テンプレートである_Advanced Dynamic Sc​​an_にも、事前定義された設定や推奨事項はありません。

2つのテンプレートの最大の違いは、高度な動的スキャンではプラグインを手動で選択する必要がないことです。代わりに、テンプレートでは[_動的プラグインフィルター_](https://docs.tenable.com/nessus/Content/DynamicPlugins.htm)を設定できます 。
[_Nessusプラグインは、 Nessus Attack Scripting Language_](https://en.wikipedia.org/wiki/Nessus_Attack_Scripting_Language) （NASL）で記述されたプログラムで、 脆弱性を検出するための情報とアルゴリズムを備えています。各プラグインは、異なるユースケースをカバーする[_プラグインファミリー_](https://www.tenable.com/plugins/families/about)に割り当てられています。この学習ユニットの最後のセクションでは、Advanced Dynamic Sc​​anテンプレートとプラグインを操作します。



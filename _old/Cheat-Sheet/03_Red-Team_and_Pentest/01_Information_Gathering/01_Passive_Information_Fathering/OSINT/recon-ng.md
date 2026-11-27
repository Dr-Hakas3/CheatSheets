以下に、recon-ngの詳細な使い方をMarkdown形式でまとめました。

---

# recon-ngの使い方

## 目次
1. [概要](#概要)
2. [基本的なコマンド](#基本的なコマンド)
3. [モジュールの利用方法](#モジュールの利用方法)
4. [ワークスペースの管理](#ワークスペースの管理)
5. [APIキーの設定](#apiキーの設定)
6. [実用例](#実用例)

## 概要
`recon-ng`は、OSINT（Open Source Intelligence）調査を行うためのフレームワークで、Kali Linuxなどのペネトレーションテスト環境に標準でインストールされています。モジュールベースのアプローチを採用しており、さまざまな情報収集や分析を自動化できます。

## 基本的なコマンド
recon-ngのコマンドは、他のペネトレーションテストフレームワーク（例: Metasploit）に似ています。

### 1. **起動**
```bash
recon-ng
```
- `recon-ng`を起動します。対話型のシェルに入ります。

### 2. **ヘルプの表示**
```bash
help
```
- 利用可能なコマンドのリストを表示します。

### 3. **モジュールの表示**
```bash
modules search [search_term]
```
- 利用可能なモジュールを表示します。`search_term`で絞り込みも可能です。

### 4. **モジュールのロード**
```bash
modules load [module_name]
```
- 指定したモジュールをロードします。

### 5. **オプションの設定**
```bash
options set [option_name] [value]
```
- ロードしたモジュールのオプションを設定します。

### 6. **モジュールの実行**
```bash
run
```
- ロードしたモジュールを実行します。

## モジュールの利用方法
`recon-ng`では、モジュールをロードしてオプションを設定し、調査を実行します。以下に一般的な流れを示します。

### 1. **モジュールの検索とロード**
```bash
modules search domains-hosts
modules load recon/domains-hosts/google_site_web
```
- `domains-hosts`に関連するモジュールを検索し、`google_site_web`モジュールをロードします。

### 2. **オプションの確認と設定**
```bash
options list
options set SOURCE example.com
```
- モジュールのオプションを確認し、調査対象のドメイン（例: `example.com`）を設定します。

### 3. **モジュールの実行**
```bash
run
```
- モジュールを実行し、結果を取得します。

## ワークスペースの管理
`recon-ng`では、複数の調査プロジェクトを同時に管理できるように、ワークスペースの概念が用意されています。

### 1. **ワークスペースの作成**
```bash
workspaces create example_workspace
```
- 新しいワークスペースを作成します。

### 2. **ワークスペースの切り替え**
```bash
workspaces select example_workspace
```
- 別のワークスペースに切り替えます。

### 3. **ワークスペースのリスト表示**
```bash
workspaces list
```
- すべてのワークスペースを一覧表示します。

### 4. **ワークスペースの削除**
```bash
workspaces delete example_workspace
```
- 指定したワークスペースを削除します。

## APIキーの設定
一部のモジュールは、外部サービスのAPIキーが必要です。以下の手順でAPIキーを設定します。

### 1. **APIキーの設定**
```bash
keys add shodan_api YOUR_SHODAN_API_KEY
```
- `YOUR_SHODAN_API_KEY`の部分に取得したShodan APIキーを設定します。

### 2. **設定したキーの確認**
```bash
keys list
```
- 設定済みのAPIキーを一覧表示します。

## 実用例

### 1. **Google Siteからホスト情報を収集**
```bash
recon-ng
> workspaces create site_recon
> modules load recon/domains-hosts/google_site_web
> options set SOURCE example.com
> run
```
- Google Siteから`example.com`に関連するホスト情報を収集します。

### 2. **Shodanを利用したIPアドレスの調査**
```bash
recon-ng
> workspaces create shodan_recon
> modules load recon/hosts-hosts/shodan_ip
> options set SOURCE 8.8.8.8
> run
```
- Shodanを使用して、指定したIPアドレス（例: 8.8.8.8）に関する情報を収集します。

### 3. **マルチモジュールを利用したドメインの完全調査**
```bash
recon-ng
> workspaces create full_domain_recon
> modules load recon/domains-hosts/bing_domain_web
> options set SOURCE example.com
> run
> modules load recon/contacts-hosts/whois_pocs
> options set SOURCE example.com
> run
```
- 複数のモジュールを使用して、`example.com`ドメインに関連する情報を網羅的に収集します。

---

このガイドでは、`recon-ng`の基本的な使い方から、モジュールの管理、ワークスペースの使用方法、APIキーの設定方法、そして実用的なシナリオでの使用例を紹介しました。`recon-ng`は強力で柔軟性が高いフレームワークであり、効果的なOSINT調査を実施するのに非常に役立ちます。
# 概要
Nuclei は、Webアプリケーションやネットワークのセキュリティ診断を行うための脆弱性スキャナーです。
YAMLベースのテンプレート を使用し、高速かつカスタマイズ可能なスキャンが可能です。
オープンソース であり、Red Team や Blue Team の両方 で活用されています。

特徴

✅ 高速スキャン：並列処理により、多数のターゲットを短時間でスキャン
✅ カスタム可能：YAMLテンプレートで独自のスキャンルールを作成可能
✅ 軽量＆柔軟：Go言語で実装されており、低リソースで動作
✅ CI/CD統合：DevSecOpsの一環として導入しやすい
✅ 定期的な更新：公式リポジトリで脆弱性テンプレートが頻繁に更新

# インストール

Nuclei は Linux, Windows, macOS で動作可能。

(1) Linux/macOS の場合
```bash
curl -sSfL https://raw.githubusercontent.com/projectdiscovery/nuclei/main/install.sh | sh
```

または、Go を使う場合:
```bash
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```

(2) Windows の場合

iwr -useb https://raw.githubusercontent.com/projectdiscovery/nuclei/main/install.ps1 | iex

# 基本的な使い方

(1) 脆弱性スキャン
```bash
nuclei -target http://192.168.121.16
```

# 概要
Nuclei は、Webアプリケーションやネットワークのセキュリティ診断を行うための脆弱性スキャナーです。
YAMLベースのテンプレート を使用し、高速かつカスタマイズ可能なスキャンが可能です。
オープンソース であり、Red Team や Blue Team の両方 で活用されています。

特徴

✅ 高速スキャン：並列処理により、多数のターゲットを短時間でスキャン
✅ カスタム可能：YAMLテンプレートで独自のスキャンルールを作成可能
✅ 軽量＆柔軟：Go言語で実装されており、低リソースで動作
✅ CI/CD統合：DevSecOpsの一環として導入しやすい
✅ 定期的な更新：公式リポジトリで脆弱性テンプレートが頻繁に更新

# インストール

Nuclei は Linux, Windows, macOS で動作可能。

(1) Linux/macOS の場合
```bash
curl -sSfL https://raw.githubusercontent.com/projectdiscovery/nuclei/main/install.sh | sh
```

または、Go を使う場合:
```bash
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```

(2) Windows の場合

iwr -useb https://raw.githubusercontent.com/projectdiscovery/nuclei/main/install.ps1 | iex

# 基本的な使い方

(1) 脆弱性スキャン
```bash
nuclei -target http://192.168.121.16
```
![](../../../../../Assets/Images/Pasted%20image%2020260425191911.png)
指定した URL に対して、既存の脆弱性テンプレートを適用してスキャン。

(2) 特定のカテゴリのスキャン

```zsh
nuclei -u https://example.com -t cves/
```

cves/ カテゴリのテンプレートを適用し、CVE (Common Vulnerabilities and Exposures) に関連する脆弱性をスキャン。

(3) 複数のターゲットをスキャン

```zsh
nuclei -l targets.txt
```

targets.txt にリストされた複数のホストに対してスキャンを実行。

(4) 結果をJSON形式で保存

nuclei -u https://example.com -o result.json -json

# テンプレートの仕組み

Nuclei では、YAMLベースのテンプレート を使ってスキャンを実行します。
たとえば、特定のパターンに一致するレスポンスをスキャンする簡単な例:
```yaml
id: example-detection

info:
  name: Example Vulnerability
  author: security-researcher
  severity: medium

requests:
  - method: GET
    path:
      - "{{BaseURL}}/vulnerable-endpoint"
    matchers:
      - type: word
        words:
          - "vulnerable"
```
→ 「/vulnerable-endpoint」 に “vulnerable” という単語が含まれていたら脆弱と判定

# 実用的な活用方法

✅ Webアプリの脆弱性診断 (SQLi, XSS, SSRF など)
✅ CVEスキャン (最新のCVEを定期的にチェック)
✅ CI/CDに統合し、開発段階での脆弱性検出
✅ Red Team がペネトレーションテストの一環で使用
✅ Blue Team が監視用途で使用 (攻撃の兆候を検知)

# まとめ

🔹 Nuclei は、YAMLテンプレートを使った高速で柔軟な脆弱性スキャナー
🔹 オープンソースで、最新のCVEやWebアプリの脆弱性を検出可能
🔹 カスタムテンプレートを作成すれば、独自の脆弱性スキャンも可能
🔹 Red Team / Blue Team / DevSecOps のすべてに活用できる強力なツール

次のステップ
	•	公式テンプレートを取得・更新

nuclei -update


	•	テンプレート一覧を確認

nuclei -tl


	•	カスタムテンプレートを作成して実験
	•	CI/CDに組み込んで、開発時にセキュリティスキャンを実施

指定した URL に対して、既存の脆弱性テンプレートを適用してスキャン。

(2) 特定のカテゴリのスキャン

nuclei -u https://example.com -t cves/

cves/ カテゴリのテンプレートを適用し、CVE (Common Vulnerabilities and Exposures) に関連する脆弱性をスキャン。

(3) 複数のターゲットをスキャン

nuclei -l targets.txt

targets.txt にリストされた複数のホストに対してスキャンを実行。

(4) 結果をJSON形式で保存

nuclei -u https://example.com -o result.json -json

# テンプレートの仕組み

Nuclei では、YAMLベースのテンプレート を使ってスキャンを実行します。
たとえば、特定のパターンに一致するレスポンスをスキャンする簡単な例:

id: example-detection

info:
  name: Example Vulnerability
  author: security-researcher
  severity: medium

requests:
  - method: GET
    path:
      - "{{BaseURL}}/vulnerable-endpoint"
    matchers:
      - type: word
        words:
          - "vulnerable"

→ 「/vulnerable-endpoint」 に “vulnerable” という単語が含まれていたら脆弱と判定

# 実用的な活用方法

✅ Webアプリの脆弱性診断 (SQLi, XSS, SSRF など)
✅ CVEスキャン (最新のCVEを定期的にチェック)
✅ CI/CDに統合し、開発段階での脆弱性検出
✅ Red Team がペネトレーションテストの一環で使用
✅ Blue Team が監視用途で使用 (攻撃の兆候を検知)

# まとめ

🔹 Nuclei は、YAMLテンプレートを使った高速で柔軟な脆弱性スキャナー
🔹 オープンソースで、最新のCVEやWebアプリの脆弱性を検出可能
🔹 カスタムテンプレートを作成すれば、独自の脆弱性スキャンも可能
🔹 Red Team / Blue Team / DevSecOps のすべてに活用できる強力なツール

次のステップ
	•	公式テンプレートを取得・更新

nuclei -update


	•	テンプレート一覧を確認

nuclei -tl


	•	カスタムテンプレートを作成して実験
	•	CI/CDに組み込んで、開発時にセキュリティスキャンを実施

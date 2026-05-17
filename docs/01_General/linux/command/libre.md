# Linuxでdocxやxlsxファイルを表示する方法

### 1. LibreOfficeを使用する
LibreOfficeは、Microsoft Officeファイル形式をサポートするオープンソースのオフィススイートです。

## インストール
  ```bash
  sudo apt-get install libreoffice  # Debian系ディストリビューションの場合
  sudo yum install libreoffice      # Red Hat系ディストリビューションの場合
  ```

## ファイルを開く:
```bash
libreoffice filename.docx
libreoffice filename.xlsx
```
---
# 2. WPS Officeを使用する
WPS Officeは、Microsoft Officeに近いインターフェースを持つオフィススイートです。

WPS Officeは、公式ウェブサイトからダウンロードしてインストールできます。

---
# 3. Apache OpenOfficeを使用する
Apache OpenOfficeも、Microsoft Officeファイル形式をサポートするオープンソースのオフィススイートです。

## インストール:
```bash
sudo apt-get install openoffice
```

## ファイルを開く:
```bash
openoffice filename.docx
openoffice filename.xlsx
```
---
# 4. オンラインオフィススイートを使用する
ブラウザを使用して、オンラインでファイルを表示することもできます。

Google Docs / Google Sheets:
.docxや.xlsxファイルをGoogle Driveにアップロードし、Google DocsまたはGoogle Sheetsで開くことができます。
Microsoft Office Online:
Microsoftのオンラインサービスを使用して、ブラウザで直接ファイルを開くことができます。
5. docx2txtやxlsx2csvコマンドを使用する
ターミナルで内容を確認する場合、以下のコマンドを使用してファイルをテキストやCSV形式に変換できます。

## インストール:
```bash
sudo apt-get install docx2txt
sudo apt-get install xlsx2csv
```

## 使用方法:
```bash
docx2txt filename.docx -  # ターミナルにテキストを表示
xlsx2csv filename.xlsx    # CSV形式で内容を出力
```
---
title:
---

# 情報収集
1. ファイル収集
-  Google検索で「 **site:example.com filetype:pdf」**と入力しファイルを調査する
- [_gobuster_](https://github.com/OJ/gobuster)などのツールに**-x**パラメータを指定して、ターゲットのウェブサイト上で特定のファイル拡張子を検索する
```bash
gobuster dir -u http://192.168.214.197 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x pdf,php,html,txt,zip
```

2. 対象組織の公開文書からメタデータタグを検査する
```bash
cd Downloads
exiftool -a -u example.pdf
```
注目すべきタグ
- Author 作成者
- Producer
- Create Date 
- Creator Tool Office等が記載されている
- Modify Date
---
# クライアントのフィンガープリンティング
### [_Canarytokens_](https://canarytokens.com/) 
トークンが埋め込まれたリンクを生成し、それをターゲットに送信する。ターゲットがブラウザでリンクを開くと、ブラウザ、IPアドレス、オペレーティングシステムに関する情報が取得される。  
トラッキングトークンに関するアラートを受け取る方法
1. メールアドレスを入力するか、Webhook URLを指定する
2. ドロップダウンメニューから _「Webバグ/URLトークン」_を選択し、 Webhook URLとして「https://example.com」と入力し、コメントとして「Fingerprinting 」と入力
3. _「Create my Canarytoken」_ をクリック
4. 右上の_「履歴」_をクリックし、Canarytokenリンクをクリックしたすべての訪問者と、被害者のシステムに関する情報を表示
5. Word文書またはPDFファイルにCanaryトークンを埋め込むオプションもある
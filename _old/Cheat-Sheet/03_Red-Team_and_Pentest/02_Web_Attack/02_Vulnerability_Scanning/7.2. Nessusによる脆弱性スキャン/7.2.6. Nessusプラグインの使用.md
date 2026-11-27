1. New Scanをクリック
2. Credential Validationをクリック  
認証情報を使用した基本ネットワークスキャンテンプレートとの違いは、認証情報を使用したパッチ監査スキャンではローカルセキュリティチェックのみを使用し、外部からの視点による通常の脆弱性チェックは行わないことです。認証情報を使用したパッチ監査テンプレートは、不足しているオペレーティングシステムのパッチだけでなく、[_権限昇格攻撃_](https://en.wikipedia.org/wiki/Privilege_escalation)に対して脆弱な可能性のある古いアプリケーションもスキャンします。
3. Settings
    - スキャン名の設定
    - スキャン対象のIP（ドメイン）を設定
4.  Credentials
    -  HostカテゴリでSSHを選択
    - Authenticated Methodでpasswordを選択
    - ユーザ名：パスワードを入力
    - Elevate privileges withでsudoを選択
    - root：パスワードを入力
  5. Dynamic Plugins
    複数入力できる
    1.  CVE
        - CVE番号を入力
        - Preview Plugins
        - 該当するものを選択
    2. Plugin Family
        - 該当するOSを選択
  6. Launch
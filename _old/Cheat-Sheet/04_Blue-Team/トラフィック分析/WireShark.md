### WiresharkでTLSを復号する手順
TCPの設定
まずは、TCPの設定を行います。どちらの方法で復号するにせよ、以下の手順を実施しないとうまく復号できませんので、ご注意ください。
1. Wiresharkを起動し、[Edit]menu > Preferences > Protocols > TCPを選択します。
2. "Allow subdissector to reassemble TCP stream"と"Reassemble out-of-order semgemnts"の項目をチェックします。
"Reassemble out-of-order semgements"は、Wireshark V3.0以降はデフォルトでは無効となっています。こちらを行わないとTCP上の順序不正のデータに対しての復号が行われなくなります。
サーバの秘密鍵を登録する方法で復号
1. Wiresharkを起動し、[Edit]menu > Preferences > Protocols > TLSを選択します。
2. "RSA keys list"から[Edit]ボタンをクリックし、＋ボタンで以下の項目を設定します。
項目	説明
IP address	サーバのIPアドレスを入力
Port	サーバのポート番号を入力、HTTPSの場合は通常"443"
Protocol	プロトコル名をWiresharkのダイセクタ名で入力、HTTPSの場合は"http"
Key File	秘密鍵のファイルパスを入力
Password	（秘密鍵にパスフレーズを設定している場合のみ）パスフレーズを入力
この方法は先にもお伝えした通り、限られた状況でしか復号できません。
• 鍵交換のアルゴリズムはDH系（DHEやECDH含む）ではないこと
• SSL3.0、(D)TLS1.0-1.2のみサポート
• 秘密鍵はサーバー証明書と一致、クライアント証明書や認証局 (CA) 証明書では非サポート
• キャプチャファイルにClientKeyExchangeメッセージを含むことが必要
なお、Wireshark Wikiでは、TLS画面からのRSA鍵の登録は非推奨となっており、今後は、Perences > Protocols > RSA Keysでの登録が推奨されているようです。
Wireshark Ver.3.6.8では、TLS画面からの登録で問題なく復号できました。今後設定できなくなるかもしれませんので、ご注意ください。

